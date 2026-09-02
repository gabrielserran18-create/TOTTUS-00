# CLAUDE.md — Instrucciones del repositorio

> Este archivo lo lee automáticamente Claude Code al abrir el repo. Si eres una IA trabajando aquí, **léelo entero antes de tocar nada**.

---

## 1. Qué es este repositorio

Base de conocimientos personal de **Gabriel Serrano**, Especialista en **Inteligencia Comercial en Tottus (Perú)**.

Se alimenta de forma incremental: capacitaciones, comités, presentaciones de campaña y documentos internos que van llegando. Cada aporte se procesa y se **integra en el documento maestro** — no se acumulan archivos sueltos.

```
TOTTUS-00/
├── CLAUDE.md                  ← este archivo (instrucciones para IAs)
├── README.md                  ← orientación rápida para humanos
├── glosario-retail.md         ← ⭐ DOCUMENTO MAESTRO
└── scripts/
    └── validar-glosario.py    ← chequeo estructural del documento maestro
```

**`glosario-retail.md` es el único documento de contenido.** Todo lo que se aprenda de una fuente nueva entra ahí. No crear documentos paralelos salvo que el usuario lo pida explícitamente.

---

## 2. Cómo está construido el documento maestro

### Registro de fuentes
Encabeza el documento. Cada fuente tiene un ID (`F1`, `F2`, …) con su nombre, tipo, fecha y una nota. **Toda fuente nueva se registra ahí antes de incorporar sus términos.**

Fuentes actuales:

| ID | Fuente | Fecha |
|---|---|---|
| F1 | Capacitación Scanntech — plataforma ScanView | Sep 2026 |
| F2 | *Impulso+: Análisis y Estrategia de HS* | Oct–Nov 2025 |
| F3 | *Chapa Tu Yapa II — Julio* | Jul 2026 |
| F4 | *Comité Comercial S36-2026* | Set 2026 |
| F5 | Correcciones directas de Gabriel Serrano (fuente continua) | desde Set 2026 |

**`[F5]` tiene prioridad sobre F1–F4.** Cuando el usuario corrige algo extraído de un documento, gana su corrección: él conoce la operación, los documentos tienen erratas. Aplicar el cambio, etiquetarlo `[F5]` y — si el documento decía otra cosa — dejar constancia de la discrepancia en vez de borrarla (ver regla 8).

### Convenciones de marcado

| Marca | Significado |
|---|---|
| `` `[F2]` `` | El término apareció en esa fuente. Si aparece en varias, se listan todas: `` `[F1]` `[F4]` `` |
| `` `[base]` `` | Término estándar de retail, incluido como contexto. No proviene de una fuente registrada |
| `⚠️ por confirmar` | La sigla o el término apareció **sin definirse**. Lo anotado es lectura del contexto y debe validarse con el área dueña |
| `⚠️ **Trampa:**` / `⚠️` | Advertencia metodológica: un error de lectura frecuente sobre ese término |
| `*Sinónimo:*` | Nombres alternativos, incluidos los encabezados antiguos de entradas que se fusionaron |

### Estructura

- **Secciones 1–15**, numeradas y temáticas (surtido, venta, ticket, precio, margen, promociones, ejecución, abastecimiento, tiendas, resultados, calendario, loyalty, procesos, actores, analítica).
- **Anexo A — Cifras de referencia:** valores puntuales, **cada bloque con su corte temporal explícito**.
- **Anexo B — Trampas de lectura:** checklist de errores metodológicos detectados en las fuentes.
- **Términos por incorporar:** lista viva de lo que falta.

---

## 3. Protocolo para incorporar una fuente nueva

Cuando el usuario suba un PPT, PDF, Excel, grabación o documento:

**1. Leer la fuente completa.** No parcialmente. Para PPTX usar la skill `pptx` (`markitdown` para el texto); para PDF, `pypdfium2` extrae texto y renderiza páginas — **renderizar las páginas con gráficos**, porque las tablas y los mensajes clave suelen estar en imágenes que el extractor de texto no captura.

**2. Registrarla** en la tabla de fuentes con el siguiente ID libre (`F5`, `F6`, …), su tipo, fecha y una nota que la identifique.

**3. Extraer terminología, no resúmenes.** Lo que entra al glosario son *términos con su definición*, no las conclusiones del documento. Un hallazgo puntual entra solo si sirve como **referencia** (va al Anexo A, con fecha) o como **advertencia metodológica** (va al Anexo B o como `⚠️` dentro del término).

**4. Colocar cada término en su sección temática.** Si un tema nuevo no cabe en ninguna, crear sección al final de las numeradas y renumerar el resto solo si hace falta.

**5. Etiquetar todo** con el ID de la fuente. Si el término ya existía, **añadir** la etiqueta nueva y enriquecer la definición — no reescribirla desde cero.

**6. Actualizar** la lista de *Términos por incorporar* (marcar lo resuelto, añadir lo nuevo que quedó abierto) y la línea de *Última actualización* al pie.

**7. Validar y commitear** (ver §5 y §6).

---

## 4. Reglas de calidad — no negociables

Estas reglas existen porque el valor de esta base depende de que se pueda confiar en ella sin volver a la fuente.

1. **Nunca inventar la expansión de una sigla.** Si la fuente no la define, se marca `⚠️ por confirmar` con la lectura de contexto y se añade a *Términos por incorporar*. Un vacío señalizado es correcto; una definición plausible pero falsa se propaga y contamina.

2. **Nunca borrar una entrada existente.** Si se fusiona con otra (ej. `Venta Same Store` → `SSS — Same Store Sales`), el nombre anterior queda como `*Sinónimo:*` para que siga siendo buscable.

3. **Toda cifra lleva su corte temporal y su fuente.** "Ep 55.4%" sin más es inútil en seis meses. Correcto: "Referencia F2 (Set-2025): Ep 55.4%".

4. **Declarar siempre la base de una métrica compuesta.** Efectividad por SKU ≠ por llamado. Promo share vs Total PU ≠ vs Total Food. Venta SI ≠ venta con IGV. Si la fuente no la declara, decirlo.

5. **Distinguir dato de interpretación.** La definición del término es dato. Una lectura propia va marcada con `⚠️` y redactada como advertencia, no como hecho de la fuente.

6. **Español de Perú, terminología de Tottus.** Usar el término que usa la casa (GPE, no "margen bruto"; fleje, no "etiqueta"; llamado, no "oferta"). El equivalente genérico va como sinónimo.

7. **No inflar.** Si una fuente no aporta terminología nueva, se registra y se dice que no aportó. Repetir con otras palabras lo que ya está no es alimentar la base.

8. **Conservar la discrepancia, no taparla.** Cuando el usuario corrige algo que un documento decía distinto, se aplica su versión **y** se anota la forma que usan los reportes. Quien lea un comité viejo tiene que poder reconocer el término. Ejemplo vivo: la sigla de Same Store es `SSM` según el usuario y `SSS` en los reportes revisados — el glosario registra ambas.

---

## 5. Validación antes de commitear

```bash
python3 scripts/validar-glosario.py
```

Comprueba: numeración de secciones sin saltos, entradas duplicadas, integridad de tablas markdown, etiquetas de fuente huérfanas (un `[Fx]` sin fuente registrada), placeholders olvidados y cierre del archivo. **Sale con código ≠ 0 si algo falla.**

Cuando el usuario pregunte "¿está bien el archivo?", correr esto y reportar el resultado.

---

## 6. Git

Esta es una base de conocimientos personal, no un proyecto de código con revisores. **El flujo normal es commitear directo a `main` y pushear** — sin rama ni PR.

- Commit en español, explicando **qué fuente se incorporó y qué secciones cambiaron**.
- Validar (§5) antes de cada commit. Ese es el control de calidad; sustituye a la revisión.
- Rama + PR solo si el usuario lo pide, o para un cambio grande que quiera revisar antes de consolidar.
- Nunca mergear ni aprobar un PR: esa decisión es del usuario.

---

## 7. Cómo responder al usuario

- **En español.** Es su idioma de trabajo.
- Cuando pida "insights" o "revisa esto", quiere **análisis sustantivo** — qué dice realmente la data y qué contradicciones tiene el documento — no un resumen ni un entregable formateado. Verificar la aritmética de las tablas antes de afirmar que algo está mal.
- Si pide explícitamente que no haya entregable, la respuesta va en el terminal, sin artifact ni archivo.
- Ser directo con los errores encontrados y separar lo verificado de lo que necesita confirmarse mirando el slide original.
