# TOTTUS-00

Base de conocimientos de **Inteligencia Comercial — Tottus (Perú)**.

Repositorio vivo: se alimenta de capacitaciones, comités, presentaciones de campaña y documentos internos. Cada aporte se **integra en un único documento maestro** en lugar de acumular archivos sueltos.

## Documento maestro

📘 **[`glosario-retail.md`](glosario-retail.md)** — glosario de terminología de retail y de Tottus.

- 17 secciones temáticas: surtido y lanzamientos, venta, ticket, precio, margen, promociones, ejecución en tienda, abastecimiento, red de tiendas, lectura de resultados, calendario, loyalty, procesos, actores, analítica, el manual operativo de ScanView y los entregables recurrentes del puesto.
- **Anexo A** — cifras de referencia, cada bloque con su corte temporal.
- **Anexo B** — trampas de lectura: errores metodológicos frecuentes al interpretar los reportes.
- **Anexo C** — casos de referencia: episodios concretos de marca propia que ilustran un patrón (o su excepción).
- Cada término indica de qué fuente proviene (`[F1]`, `[F2]`, …), registradas en la tabla que encabeza el documento.

## La única excepción: `PENDIENTES.md`

⏱ **[`PENDIENTES.md`](PENDIENTES.md)** — rastreador de tareas de esta semana, con fechas y nombres. No es conocimiento de referencia: se **reemplaza en cada ciclo**, no acumula versiones. El "por qué" de cada pendiente vive en el glosario; este archivo solo trackea el "qué falta y para cuándo".

## Cómo se alimenta

Se sube el documento nuevo (PPT, PDF, Excel, notas, grabación) y se pide incorporarlo. El procedimiento completo — registrar la fuente, extraer terminología, etiquetarla y validar — está en **[`CLAUDE.md`](CLAUDE.md)**, que Claude Code lee automáticamente al abrir el repo.

## Verificar el documento

```bash
python3 scripts/validar-glosario.py
```

Comprueba numeración de secciones, entradas duplicadas, tablas, etiquetas de fuente huérfanas y restos de edición. Se ejecuta solo sobre `glosario-retail.md`; `PENDIENTES.md` no sigue esa estructura.

## Estructura

```
TOTTUS-00/
├── CLAUDE.md                  instrucciones de mantenimiento (para IAs)
├── README.md                  este archivo
├── glosario-retail.md         ⭐ documento maestro
├── PENDIENTES.md              ⏱ rastreador de tareas, se reemplaza cada ciclo
└── scripts/
    └── validar-glosario.py    chequeo estructural del documento maestro
```
