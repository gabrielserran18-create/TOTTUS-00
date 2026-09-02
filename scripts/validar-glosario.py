#!/usr/bin/env python3
"""Chequeo estructural del documento maestro (glosario-retail.md).

Uso:  python3 scripts/validar-glosario.py [ruta]

Verifica lo que se puede verificar automáticamente: estructura, duplicados,
tablas, coherencia de las etiquetas de fuente y restos de edición.
No juzga el contenido — eso lo hacen las reglas de calidad de CLAUDE.md.

Sale con código 1 si hay errores, 0 si todo está bien (los avisos no rompen).
"""

import re
import sys
from pathlib import Path

DOC = Path(sys.argv[1] if len(sys.argv) > 1 else "glosario-retail.md")

errores: list[str] = []
avisos: list[str] = []


def main() -> int:
    if not DOC.exists():
        print(f"✗ No existe {DOC}")
        return 1

    texto = DOC.read_text(encoding="utf-8")
    lineas = texto.split("\n")

    fuentes = revisar_fuentes(texto, lineas)
    revisar_secciones(lineas)
    entradas = revisar_entradas(lineas)
    revisar_etiquetas(lineas, fuentes)
    revisar_tablas(lineas)
    revisar_restos(lineas)
    revisar_cierre(lineas)

    print(f"\n  {DOC}: {len(lineas)} líneas · {len(texto):,} caracteres")
    print(f"  {len(entradas)} entradas · {len(fuentes)} fuentes registradas: {', '.join(sorted(fuentes))}")

    for a in avisos:
        print(f"  ⚠  {a}")
    for e in errores:
        print(f"  ✗  {e}")

    if errores:
        print(f"\n✗ {len(errores)} error(es). Corrige antes de commitear.\n")
        return 1
    print(f"\n✓ Estructura correcta{' (' + str(len(avisos)) + ' aviso(s))' if avisos else ''}.\n")
    return 0


def revisar_fuentes(texto: str, lineas: list[str]) -> set[str]:
    """IDs declarados en la tabla de Registro de fuentes."""
    if "## Registro de fuentes" not in texto:
        errores.append("Falta la sección '## Registro de fuentes'")
        return set()
    fuentes = set(re.findall(r"\|\s*\*\*(F\d+)\*\*\s*\|", texto))
    if not fuentes:
        errores.append("El registro de fuentes no declara ningún ID (formato esperado: | **F1** | ...)")
        return set()
    nums = sorted(int(f[1:]) for f in fuentes)
    if nums != list(range(1, len(nums) + 1)):
        avisos.append(f"IDs de fuente no correlativos desde F1: {nums}")
    return fuentes


def revisar_secciones(lineas: list[str]) -> None:
    """Secciones numeradas 1..N sin saltos ni repetidos."""
    nums = [int(m.group(1)) for l in lineas if (m := re.match(r"^## (\d+)\.", l))]
    if not nums:
        errores.append("No se encontró ninguna sección numerada (formato: '## 1. Título')")
        return
    if nums != sorted(nums):
        errores.append(f"Secciones desordenadas: {nums}")
    if len(nums) != len(set(nums)):
        repes = sorted({n for n in nums if nums.count(n) > 1})
        errores.append(f"Secciones con número repetido: {repes}")
    faltan = sorted(set(range(1, max(nums) + 1)) - set(nums))
    if faltan:
        errores.append(f"Saltos en la numeración de secciones: faltan {faltan}")


def revisar_entradas(lineas: list[str]) -> list[str]:
    """Términos del glosario (línea que empieza con **Término**)."""
    entradas = [m.group(1).strip() for l in lineas if (m := re.match(r"^\*\*(.+?)\*\*", l))]
    vistos: dict[str, int] = {}
    for e in entradas:
        vistos[e] = vistos.get(e, 0) + 1
    dups = sorted(k for k, v in vistos.items() if v > 1)
    if dups:
        errores.append(f"Entradas duplicadas: {dups}")
    return entradas


def revisar_etiquetas(lineas: list[str], fuentes: set[str]) -> None:
    """Ninguna etiqueta [Fx] puede apuntar a una fuente no registrada."""
    usadas = set()
    for i, l in enumerate(lineas, 1):
        for f in re.findall(r"`\[(F\d+)\]`", l):
            usadas.add(f)
            if f not in fuentes:
                errores.append(f"línea {i}: etiqueta [{f}] sin fuente registrada")
    sin_usar = fuentes - usadas
    if sin_usar:
        avisos.append(f"Fuentes registradas sin ningún término etiquetado: {sorted(sin_usar)}")


def revisar_tablas(lineas: list[str]) -> None:
    """Cada tabla markdown necesita separador y un ancho de columnas constante."""
    bloques, actual = [], []
    for i, l in enumerate(lineas, 1):
        if l.strip().startswith("|"):
            actual.append((i, l))
        elif actual:
            bloques.append(actual)
            actual = []
    if actual:
        bloques.append(actual)

    for b in bloques:
        ini = b[0][0]
        if len(b) < 2:
            errores.append(f"línea {ini}: fila de tabla suelta (sin separador)")
            continue
        sep = set(b[1][1].replace("|", "").replace(" ", "")) <= set("-:")
        if not sep:
            errores.append(f"línea {ini}: tabla sin fila separadora |---|")
        anchos = {r[1].count("|") for r in b}
        if len(anchos) > 1:
            errores.append(f"línea {ini}: la tabla tiene filas con distinto número de columnas {sorted(anchos)}")


def revisar_restos(lineas: list[str]) -> None:
    """Placeholders y restos de edición. \\b evita cazar 'todo'/'método' en español."""
    patron = re.compile(r"\b(TBD|FIXME|XXX|lorem ipsum|\[insert)\b", re.IGNORECASE)
    for i, l in enumerate(lineas, 1):
        if patron.search(l):
            errores.append(f"línea {i}: resto de edición → {l.strip()[:70]}")


def revisar_cierre(lineas: list[str]) -> None:
    cola = "\n".join(lineas[-6:])
    if "Última actualización" not in cola:
        avisos.append("El pie no tiene la línea de 'Última actualización' — actualízala al incorporar una fuente")


if __name__ == "__main__":
    sys.exit(main())
