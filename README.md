# TOTTUS-00

Base de conocimientos de **Inteligencia Comercial — Tottus (Perú)**.

Repositorio vivo: se alimenta de capacitaciones, comités, presentaciones de campaña y documentos internos. Cada aporte se **integra en un único documento maestro** en lugar de acumular archivos sueltos.

## Documento maestro

📘 **[`glosario-retail.md`](glosario-retail.md)** — glosario de terminología de retail y de Tottus.

- 16 secciones temáticas: surtido, venta, ticket, precio, margen, promociones, ejecución en tienda, abastecimiento, red de tiendas, lectura de resultados, calendario, loyalty, procesos, actores, analítica y el manual operativo de ScanView.
- **Anexo A** — cifras de referencia, cada bloque con su corte temporal.
- **Anexo B** — trampas de lectura: errores metodológicos frecuentes al interpretar los reportes.
- Cada término indica de qué fuente proviene (`[F1]`, `[F2]`, …), registradas en la tabla que encabeza el documento.

## Cómo se alimenta

Se sube el documento nuevo (PPT, PDF, Excel, notas) y se pide incorporarlo. El procedimiento completo — registrar la fuente, extraer terminología, etiquetarla y validar — está en **[`CLAUDE.md`](CLAUDE.md)**, que Claude Code lee automáticamente al abrir el repo.

## Verificar el documento

```bash
python3 scripts/validar-glosario.py
```

Comprueba numeración de secciones, entradas duplicadas, tablas, etiquetas de fuente huérfanas y restos de edición.

## Estructura

```
TOTTUS-00/
├── CLAUDE.md                  instrucciones de mantenimiento (para IAs)
├── README.md                  este archivo
├── glosario-retail.md         ⭐ documento maestro
└── scripts/
    └── validar-glosario.py    chequeo estructural
```
