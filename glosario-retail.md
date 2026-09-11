# Glosario de Retail — Inteligencia Comercial

Glosario vivo para el puesto de **Especialista en Inteligencia Comercial (Tottus)**.
Se construye por acumulación: cada capacitación, reunión o documento que aporte terminología se registra como **fuente** y sus términos se incorporan aquí.

> **Para mantener este documento** (incorporar una fuente nueva, convenciones de marcado, reglas de calidad y validación): ver [`CLAUDE.md`](CLAUDE.md). Antes de commitear, correr `python3 scripts/validar-glosario.py`.

**Convenciones:**
- Cada entrada indica `[F1]`, `[F2]`, … según la fuente donde apareció. Si un término aparece en varias, se listan todas.
- Los términos marcados `[base]` son de uso estándar en retail y se incluyen como complemento de contexto, no provienen de una fuente registrada.
- Los términos marcados `⚠️ por confirmar` aparecieron en una fuente sin definición explícita; el significado anotado es una lectura del contexto y **debe validarse con el área dueña** antes de usarse en un entregable.
- `[F5]` marca una **corrección directa del usuario**. Prevalece sobre lo extraído de las fuentes documentales cuando hay conflicto.
- Cuando un término tiene un significado **específico dentro de una herramienta**, se anota bajo *"En ScanView"* o similar.

---

## Registro de fuentes

| ID | Fuente | Tipo | Fecha | Nota |
|---|---|---|---|---|
| **F1** | Capacitación Comercial Scanntech — "Nueva plataforma tecnológica en retail" (Paolo Gaspar, KAM Scanntech) | Capacitación grabada, ~1h30 | Sep 2026 | 6ª sesión de la ronda al equipo comercial Tottus. Su contenido operativo está consolidado en la sección 16 |
| **F2** | *Impulso+: Análisis y Estrategia de HS* | Presentación de trabajo, 110 slides | Oct–Nov 2025 | Acumulado de 5 sesiones de diseño de la política promocional de Hardsell. Portada fechada Oct-2025; el contenido llega al 13-Nov. Incluye anexo regional (PE/CL) |
| **F3** | *Chapa Tu Yapa II — Julio* | Presentación de resultados, 9 slides | Jul 2026 | Cierre de la 2ª edición de la campaña en Precio Uno (29-Jun al 15-Jul 2026) |
| **F4** | *Comité Comercial S36-2026* | Comité de ventas, 60 págs | 01-Set-2026 | Cierre Agosto 2026. Bloques: Planificación Comercial, Logística, Marketing, Loyalty, plan de acción Colchones, y pre-read (competitividad, ruta crítica, CDA) |
| **F5** | Correcciones y precisiones de Gabriel Serrano | Conocimiento del puesto — fuente continua | Desde Set 2026 | Correcciones directas del usuario sobre lo extraído de las fuentes documentales: árbol mercadológico de 6 niveles, mapeo de mundos a divisiones J, notación de las divisiones. **Tiene prioridad sobre F1–F4 cuando hay conflicto** |
| **F6** | Traspaso de Mirella Gómez Montufar | Grabación de traspaso + conocimiento operativo heredado | Set 2026 | Predecesora del puesto, de vacaciones. Cubre personas del área, archivos fuente, carpetas compartidas y el procedimiento heredado de los dos entregables recurrentes |
| **F7** | `Data_Resultados (Categorías) Marcas Propias.xlsx` + 6 láminas de `Presentación MMPP - Sep'26.pptx` | Bases de datos + deck mensual | Bases Ene–Jul 2026, deck Ene–Ago 2026 | El bloque más grande de esta ronda: titular de marca propia por división, share y contribución de lanzamientos, efecto panetón, economía del margen (GPE vs GP) y cinco casos (huevos frescos, higiene personal, panetón, Xplend, papas fritas) |
| **F8** | `LANZAMIENTOS_2024_2025.xlsx`, `Lanzamientos_Dic_Ene_Feb.xlsx`, `Lanzamientos_MMPP_31_08.xlsx` + deck `Lanzamientos MMPP - 2026` (77 láminas) | Bases + deck de lanzamientos | 2024 a 31-Ago-2026 | Histórico, ejecución del trimestre y pipeline vigente (167 SKU, 56 proyectos) de lanzamientos de marca propia |
| **F9** | *Estrategia de MMPP - Directorio* | Deck regional, origen Chile, 66 láminas | s/f | Marco "one-pager de resultado de lanzamiento" (ejemplo observado: Craanch, dic-2025). Complementa, no reemplaza, el marco de Etapas propio de Tottus |
| **F10** | Consolidados de campaña HS18-A, HS18-B, T36 adelantado y T36 clásico | 4 archivos, detalle SKU × llamado | Set 2026 | HS18-A: 8,770 filas, 117 columnas, 6,340 SKU, 2,646 llamados. Es el nivel de detalle más fino revisado sobre una campaña real |
| **F11** | `RUTA CRITICA 2025.xlsx`, hoja `HS CONCEPTUAL` | Cronograma de campaña | 2025 | ⚠️ Antecede al rediseño de F2 — sus hitos y plazos no coinciden con los de la ruta crítica que reporta el Comité S36-2026 (F4); ver *Ruta Crítica*, sección 13 |
| **F12** | Plantillas de los entregables recurrentes: `Especial de Marcas Propias - HS##.pptx` y `Boletín MKT [Mes] - Campañas Especiales.xlsx` | Plantillas + procedimiento | Vigentes Set 2026 | Las dos piezas que produce Inteligencia Comercial cada campaña / cada mes |
| **F13** | *Campañas Core '25.xlsx* | Histórico de campañas core | 2025 | Las cinco campañas estacionales del año, calendario y mapeo de categorías campañeras |
| **F14** | *Campaña Navideña.xlsx* | Detalle de Navidad | 2025 | Venta por categoría y por marca dentro de la campaña navideña de 2025 |
| **F15** | *Market Share PE* — dashboard de participación de mercado | Reporte semanal, capturas de pantalla | S35 2026 (24–30 ago) | `[F5]` Confirmado: es el reporte de la fuente **L&A** (ver *L&A*, sección 4, y *Share de mercado*, sección 10): Tottus/Precio Uno vs. Resto Mercado, por canal, bandera, mundo, categoría y geografía. Primera fuente de mercado externo revisada con este nivel de detalle |
| **F16** | Grabación de capacitación de Gabriel Serrano — panorama de proveedores de data de mercado y fórmula de Market Share | Transcripción automática de audio (VTT), ~20 min | Set 2026 | ⚠️ Transcripción con errores de reconocimiento frecuentes en nombres propios (empresas y personas) — marcados individualmente donde la lectura no es segura. Cubre Kantar, Nielsen, GfK y otros proveedores, sus metodologías, las herramientas Discover/Radar y la fórmula de Market Share |
| **F17** | Grabación de capacitación de Gabriel Serrano — recorrido en vivo de la plataforma de mercado y metodología de revisión de categoría | Transcripción automática de audio (VTT), ~50 min | Set 2026 | ⚠️ Misma advertencia que F16: transcripción automática con errores frecuentes en nombres propios. Sesión práctica: diagnóstico de una caída (aceite vegetal soya) drill-down por el árbol mercadológico, la metodología Nuevo/Existe/Deslistado de surtido vs. competencia, la lógica de negocio por mundo (Abarrotes/Perecibles/No Food) y el framework en diseño para la revisión profunda de categoría |
| **F18** | Reunión de Gabriel Serrano con Carla Teresa Flores Otoya (Planificación Promocional) — ruta crítica del Táctico 37 y Excel operativo | Transcripción automática de audio (VTT), ~13 min | 10-Set-2026 | ⚠️ Transcripción automática, con el mismo tipo de ruido que F16/F17. Recorrido de la fuente dueña del proceso (Planificación Promocional) sobre el Excel de ruta crítica, la relación Táctico↔HS, los golpes de Táctico, el sistema Mi Portal/SPF y mecánicas de campaña |

---

## 1. Estructura mercadológica y surtido

**Árbol mercadológico** `[F1]` `[F5]`
Jerarquía con la que se clasifica todo el surtido, de lo más agregado a lo más granular. En Tottus tiene **6 niveles**:

> **Mundo → División (J) → Departamento → Subdepartamento → Clase → Subclase**, y por debajo el **SKU**.

Es la columna vertebral de cualquier análisis: define a qué nivel se compara, se agrega y se atribuye un resultado.
*Sinónimo:* estructura mercadológica, jerarquía de productos.

**Negocio** `[F1]`
La operación completa (ej. Hipermercados Tottus). Está por encima del árbol mercadológico, no es uno de sus niveles.

**Mundo** `[F1]` `[F5]`
Nivel 1, el más alto del árbol. Mapeo a divisiones:

| Mundo | Divisiones |
|---|---|
| **PGC** (Productos de Gran Consumo) y **FLC** (Fiambres, Lácteos y Congelados) | J1, J2, J5 |
| **Perecibles** | J3, J4, J6, J7 |
| **Non-Food** | J8, J9, J10, J11 |
| **Institucional** | J12 — venta por volumen; focos en tienda que jalan venta |

*Sinónimo:* mundo de categoría.

**División (J)** `[F1]` `[F3]` `[F4]` `[F5]`
Nivel 2; se codifica como "J" + número (J1, J2, … J12). Cada J agrupa un conjunto de departamentos bajo una misma gestión comercial.
Agrupaciones de reporte observadas en el Comité `[F4]`:
- **Food PGC/FLC:** J1, J2, J5
- **Perecibles:** J3, J4, J6, J7
- **Non-Food:** J8, J9, J10, J11
- **Excluidos de la lectura comercial estándar:** **J12**, **J99**, **JSJ** (ver *Venta institucional*)

Referencias sueltas de categoría por J recogidas de F4 y F2: J1 (abarrotes, aceites, galletas, bebidas alcohólicas, confitería, desayunos), J2 (belleza, limpieza), J5 (lácteos/FLC), J6 (panadería y pastelería), J8 (vestuario), J9 (dormitorio, colchones), J11 (electromenor).
⚠️ **Notación:** la forma canónica es **sin cero a la izquierda** (J1, J8). Los reportes del Comité y los códigos de clase la escriben rellenada a dos dígitos (`J01`, `J08`); son la misma división.
⚠️ El mapeo oficial y completo J1–J12 sigue pendiente de fuente.

**Departamento** `[F5]`
Nivel 3, entre la División y el Subdepartamento.
⚠️ *por confirmar:* ejemplos concretos por división — no aparecen en las fuentes documentales registradas.

**Subdepartamento** `[F1]`
Nivel 4. Ejemplos: dentro de J6 → Pastelería Fresca, Panadería a Granel, Pastelería Seca. Dentro de J5 → Yogur, Mantecas y Mantequillas, Leches y Cremas, Quesos.

**Clase** `[F1]` `[F4]` `[F5]`
Nivel 5. Ejemplo: dentro de Pastelería Seca → Queques.
Se codifica concatenando la jerarquía: `J09050104 – COLCHONES` `[F4]`.

**Subclase** `[F1]` `[F5]`
Nivel 6, el más fino antes del SKU. Ejemplo: Queques → Queques Rectangulares. Es el nivel donde normalmente se toman decisiones de surtido.

**SKU** (*Stock Keeping Unit*) `[F1]`
Unidad mínima de gestión: el producto individual con su código propio. Ejemplo: "Queque Marmoleado Rectangular Tottus". Es el nivel al que se mide rotación, precio medio y presencia en tienda.

**EAN / Código de barras** `[F1]`
Identificador único del producto. En ScanView se puede pegar una **lista de EAN** para acotar todo el análisis a un conjunto específico de productos.

**Surtido** `[F1]`
Conjunto de productos que un retailer ofrece en una categoría, tienda o bandera. La *estrategia de surtido* define qué SKUs se comercializan en qué banderas o formatos.

**% Surtido** `[F2]`
En la lectura promocional: porcentaje de los SKUs de una selección que están presentes en **todas** las tiendas de la red. Es el indicador que revela si una promoción se puede ejecutar a nivel nacional o solo en parte de la cadena.
Referencia F2: solo el **35–36%** del surtido de un HS tenía presencia en todas las tiendas, frente al **75.4%** de lo comunicado en medios.

**Surtido troncal** `[F2]`
Núcleo de surtido común a toda la red, sobre el que se apoya la propuesta permanente. Referencia F2: **35.0%** de los productos en HS formaban parte del troncal.

**Básico 1 / Básico 2 (B1, B2)** `[F2]`
Niveles de agrupación de surtido usados para definir el alcance de una promoción. En la política de HS se acordó definir el surtido promocional "con básico 1 y básico 2" en lugar de SKU por SKU.
⚠️ *por confirmar:* la definición exacta de cada nivel no está en F2.

**Cobertura de surtido** `[F1]`
Qué tan completo es el surtido propio frente al del mercado. Es una de las vistas que se habilita cuando entra la data de competencia.

**Curva ABC** `[F1]` `[F2]`
Clasificación de productos por su peso en la venta: A = pocos SKUs que concentran la mayor parte, B = intermedios, C = cola larga de bajo aporte. En ScanView es un criterio de ordenamiento en la Tabla de Precios. En F2 es uno de los cinco ejes con los que se perfila la calidad de una selección promocional.

**KVI** (*Key Value Item*) `[F2]` `[F4]`
Producto sensible al precio: aquel cuyo precio el cliente reconoce y usa para formarse una imagen de precio de la cadena. Escala usada en Tottus:
- **SKVI** — *Super KVI*. Máxima sensibilidad; es el grupo sobre el que se hace relevo físico de precios de competencia con prioridad.
- **KVI** — sensibilidad media.
- **NKVI** — *No KVI*. Baja sensibilidad; el cliente no ancla su percepción de precio en ellos.

Referencia F2: **65.2%** del surtido promocional de HS era NKVI y solo **7%** SKVI, frente a **44.3%** de SKVI en lo comunicado en medios.
*Nota:* en F2 también aparece la sigla **KVC** junto a KVI en el flujo de pricing, sin definirse. ⚠️ por confirmar.

**Rol de categoría** `[F2]`
Función estratégica que se le asigna a una categoría dentro del negocio. Roles usados en Tottus: **Destino**, **Tráfico**, **Imagen**, **Complementaria** (abreviada "Complem."). Define cuánto se debe invertir en precio y espacio en esa categoría.
Referencia F2: los focos de Categorías de Destino en Tottus son las de consumo de familias jóvenes con hijos pequeños y las principales de Perecibles, como fidelizador.

⚠️ **Trampa: la columna "Categoría" de los consolidados de campaña no es un nivel del árbol mercadológico** `[F18]`. Confirmado por Planificación Promocional: es una **nomenclatura o nombre comercial**, distinta de la jerarquía formal (Mundo → **División (J)** → Departamento → Subdepartamento → Clase → Subclase, ver *Árbol mercadológico*, sección 1). La División (J1, J2, J5…) sí es un nivel de la jerarquía; "Categoría" en esos archivos no lo es — no cruzar una por la otra.

**Estado de producto** `[F2]`
Ciclo de vida del SKU en el maestro: **Activo → Inactivo → Descontinuado → Purgado**. Es uno de los cinco ejes de calidad de una selección promocional: F2 detectó que ~22% de los SKUs de un HS no estaban en estado Activo.

**Nuevo / Existe / Deslistado (surtido vs. competencia)** `[F17]`
Metodología distinta de *Estado de producto* (arriba): no clasifica el ciclo de vida interno del SKU, sino su **comportamiento de venta frente a una ventana histórica**, y se aplica igual a Tottus/bandera propia y a la competencia — es la base para detectar oportunidades de surtido. Definición usada en la fuente, con ventana desde enero 2025 hasta las últimas 4 semanas del corte vigente:
- **Nuevo** — no vendió en su historia (antes de la ventana) pero **sí** vendió en las últimas 4 semanas.
- **Existe** — vendió en las últimas 4 semanas **y** tiene historia de venta previa.
- **Deslistado** — tiene historia de venta previa pero **no** vendió en las últimas 4 semanas.
- Si nadie (ni Tottus ni la competencia) lo vendió nunca, no entra al análisis.

Lectura de oportunidad: un producto que la competencia tiene como **nuevo** o **existente fuerte** y Tottus no tiene es una oportunidad de incorporar surtido. Al revés, revisar **por qué** se deslistó algo propio es igual de válido — puede ser una oportunidad perdida si el producto venía creciendo antes de salir.
⚠️ **Limitaciones declaradas:** (1) hoy solo se aplica a **marca fabricante** (marca de proveedor) — la marca propia queda fuera porque "tiene otra forma de trabajo", pendiente de extender. (2) Funciona bien en categorías con código de barras estable (abarrotes); es más difícil en categorías donde el producto cambia de diseño o empaque con frecuencia (ej. prendas de vestir) porque el identificador no es estable en el tiempo — mismo problema declarado para No Food (ver *Lógica de negocio por mundo*, sección 1).

**Matriz de surtido en mix (vs. competencia, por bandera)** `[F17]` `[F5]`
Matriz en desarrollo (trabajada con **Daniela Montoya**, Planificación Promocional — sección 14 — y con soporte de Williams para llevarla a un dashboard). Corrección del usuario sobre el alcance: no es solo la lectura Nuevo/Existe/Deslistado abierta por bandera — es una matriz más amplia que **cruza distintos KPIs** (Nuevo/Existe/Deslistado es uno de los insumos, no el único) para **comparar mercado/competencia contra el surtido propio de Tottus** y, con ese cruce, **clasificar los productos**. Hoy es manual (se rearma desde cero cada semana con la data actualizada); el objetivo declarado es automatizarla.
⚠️ *por confirmar:* el set completo de KPIs que cruza la matriz — la fuente aún no lo detalla.

**Producto pesable / a granel** `[F1]`
Producto que se vende por peso y no por unidad empaquetada (carnes, frutas, panadería a granel). Hoy en la plataforma no registra marca ni proveedor y aparece como **genérico** — limitación declarada, en desarrollo.

**Genérico** `[F1]`
Etiqueta que recibe un producto sin marca/proveedor identificado en la data. No confundir con "marca blanca".

**Marca propia / MMPP** `[F1]` `[F2]` `[F4]` `[F7]`
Marca del propio retailer. En Tottus: **Marca Tottus** (con sub-marcas **Bebé, Kids, Life, Orígenes, Premium, Soft, Xplend**), **Precio Uno** y **Murana**. En la data de Scanntech aparece a nivel **fabricante** agrupada como "Hipermercados Tottus". En los decks internos se abrevia **MMPP** y se reporta como corte propio (ej. "¿cuántos SKUs de MMPP tenemos en arriendo?" `[F2]`; "Especial MMPP 03/09–16/09" `[F4]`).

*Filtro correcto* `[F7]`: por **prefijo** (`TOTTUS*`, `PRECIO UNO`, `MURANA`), no por lista cerrada de tres marcas — una lista cerrada no captura las sub-marcas. La forma más robusta es no filtrar por marca sino usar el campo `FLAG_MMPP` de la base de venta, que ya viene resuelto.

⚠️ **Trampa — `FRESH`** `[F10]`: entre 19 y 31 SKU de gaseosas (el conteo varía según el corte revisado) cuya `Descripcion` dice "COLA AMARILLA FRESH **TOTTUS** 500ML" pero cuyo campo `Marca` dice solo `FRESH` (proveedor: Inversiones y Representaciones La Fábrica). Ningún filtro por marca ni por prefijo lo captura. ⚠️ *por confirmar* si es marca propia.

El deck mensual y el Especial MMPP miden hoy solo las divisiones **J1, J2 y J5** — el mundo **PGC y FLC** completo (ver *Mundo*, arriba). Hay SKU de MMPP participando también en **J6 y J7** (Panadería, Comidas Preparadas) que ese universo no mide: en la campaña HS18-A eran 65 de 693 SKU MMPP en campaña `[F10]`.
`[F5]` **Aclaración del usuario: esto es el alcance de ese entregable puntual, no un límite oficial de dónde existe marca propia.** Marca propia puede tener presencia en **cualquier división** — el corte J1/J2/J5 de los decks de F7/F8 fue probablemente un análisis aislado, no una regla del negocio. Al reportar cobertura de MMPP en otra categoría (fuera de J1/J2/J5), no asumir que "no aplica" solo porque los entregables recurrentes no la miden.

**MMTT** `[F7]`
Marcas Terceras: la contraparte de MMPP, marca de proveedor. Es el corte contra el que se mide participación y margen de la marca propia — ver *GPE / GPE%* y *Rebate / Sellout*, sección 5.

### Lanzamientos de marca propia

**Proyecto** `[F8]`
La unidad de gestión real de un lanzamiento de marca propia: agrupa los SKU que salen y se miden juntos (ej. "Mejora Detergente Líquido Tottus Xplend – Botella" agrupa 4 SKU). Analizar por SKU suelto rompe esa unidad. Pipeline vigente (corte 31-Ago-2026): 56 proyectos, 167 SKU.

**Tipo de SKU (lanzamiento)** `[F8]`
`NUEVO` · `REEMPLAZO FÓRMULA` · `REEMPLAZO OTROS`. El resumen operativo los colapsa en **Nuevos** y **Reformulación**. En el pipeline vigente: 78 Nuevo, 55 Reemplazo Fórmula, 34 Reemplazo Otros, sobre 167 SKU.
⚠️ *por confirmar:* qué distingue exactamente Reemplazo Fórmula de Reemplazo Otros.

**Cump. Branding** `[F8]`
`SI / (SI + NO)` sobre el campo `Diseño es nuevo Tottus`, **excluyendo `NO APLICA` del denominador**.
⚠️ **Trampa:** del bloque de Productos Nuevos (34 SKU), 15 caen en `NO APLICA` y salen del cálculo. El 89.5% de cumplimiento reportado se calcula sobre 19 SKU, no sobre 34. Declarar siempre la base — el mismo tipo de trampa que la de *Efectividad promocional*, sección 6.

**Etapas Pre-Lanzamiento / Lanzamiento / Post** `[F8]`
Plantilla propia de Tottus para medir el share de un producto nuevo, partiendo la serie alrededor de la fecha de entrada: **Pre-Lanzamiento** (línea base, antes de que entre el producto) → **Lanzamiento** (ventana de entrada) → **Post** (share estabilizado). Cada etapa lleva su par **SOV TSS** / **SOV SSS**.
Resuelve el problema de comparabilidad de un producto nuevo: **comparar contra el año anterior no dice nada cuando el producto no existía; comparar la categoría contra sí misma antes y después, sí.**
⚠️ *por confirmar:* cuántas semanas definen cada etapa y si el criterio es fijo o varía por categoría.

**One-pager de resultado de lanzamiento** `[F9]`
Marco de medición del Directorio regional (Chile), complementario al de Etapas. Combina titulares (crecimiento, share con variación en p.p.), serie de ventas, **ejecución en punto de venta** (% surtido activo por bandera, % con POP de lanzamiento, quiebre, share of shelf vs. líder), rentabilidad (precio y margen vs. referencia interna) y el bloque de clientes.

**Migración vs. Nuevo real** `[F9]`
Dentro del bloque de clientes del one-pager: separa al comprador que solo cambió de SKU (**migración**) del que representa demanda incremental (**nuevo real**). Es el corte que responde si el lanzamiento sumó o solo movió al comprador existente. Ejemplo observado (Craanch, dic-2025): migración 41% vs. nuevo real 4%.
⚠️ Sin data de ejecución en punto de venta, el análisis de un lanzamiento queda cojo: un producto que no llegó a góndola no es un lanzamiento que falló comercialmente.

**PGC** — Productos de Gran Consumo `[F1]`
Mundo de productos de consumo masivo no perecible (abarrotes, cuidado personal, limpieza).

**FLC** — Fiambres, Lácteos y Congelados `[F1]`
Mundo que agrupa esas tres familias. Trabaja mayormente con productos unitarios (no pesables), por lo que la lectura de proveedor y marca es más limpia que en el resto de Perecibles.

**Perecibles** `[F1]`
Mundo de productos de vida útil corta: carnes y pescados, frutas y verduras, panadería y pastelería, platos preparados.
**Ultra Perecibles** `[F4]`: corte más estricto dentro de Perecibles, reportado por separado en el indicador de quiebre.

**Non-Food** `[F1]`
Mundo de productos no alimentarios.

**Lógica de negocio por mundo (Abarrotes / Perecibles / No Food)** `[F17]`
Cada uno de los tres grandes negocios de un supermercado tiene una economía distinta — no se gestionan igual:
- **Abarrotes** (J1, ver *División*, arriba) — "se gana al centavito": el margen unitario es bajo y el crecimiento se logra por **volumen/rotación**, no por margen.
- **Perecibles** — impactado por **merma** (se pudre si no rota), **estacionalidad** (fruta según temporada — ej. mandarina/naranja, papa blanca vs. papa rosada según época) y por **tránsito de mercadería** (importación sujeta a clima: una tormenta que retrasa un barco impacta directamente la disponibilidad). El margen varía por subcategoría — frutas y verduras, por ejemplo, se reporta con margen mayor y ganan también por venta al mayoreo, ayudando a la **frecuencia de visita** del cliente.
- **No Food** — complementario a los otros dos: aporta más a la **imagen** de la cadena que al margen directo. Particularidad sistémica señalada en la fuente: buena parte de la mercadería sale primero para otras unidades del grupo (Falabella, Sodimac) y llega después a Tottus; hoy se maneja en la plataforma como **pesable/genérico** (ver *Producto pesable / a granel*, arriba) porque el producto cambia de diseño o empaque con frecuencia y no tiene un identificador estable — es más difícil de medir que abarrotes, donde el código de barras es estable.

⚠️ **Condiciones de pago a proveedor** (mencionadas en la fuente, sin cifra oficial): varían por categoría — perecibles ~30–45 días, otras hasta 60–90 días — y son parte de la negociación comercial: un proveedor puede ceder mejor precio o más promoción a cambio de un pago más rápido (liquidez). *Por confirmar contra la política oficial de Finanzas antes de citarlo en un entregable.*

---

## 2. Venta y volumen

**Facturación** `[F1]`
Venta registrada en dinero para un período y un corte determinado. Es la base sobre la que se calcula representatividad y variación.

**Venta SI** (sin impuestos) `[F4]`
Venta neta de IGV. Es la base sobre la que se reporta la venta en el Comité y sobre la que se calcula el GPE.
⚠️ **Trampa habitual:** el ticket promedio y el precio medio suelen venir **con** impuesto. Multiplicar `TRX × Ticket Promedio` no reproduce la Venta SI del mismo slide. Declarar siempre la base.
Reincidencia observada `[F12]`: en la plantilla del Especial MMPP, `TRX × Ticket Promedio` da 70.6 contra los 81.7 que muestra la lámina — mismo desfase, otro documento. Confirmar y declarar al pie cada vez.

**Venta institucional** `[F4]`
Venta a clientes institucionales (no shopper de tienda). Se **excluye** de la lectura comercial estándar junto con las divisiones **910, 936 y J12**.
*Código* `[F10]`: **910** = venta institucional propiamente dicha; **936** = Repsol. Ambos se filtran por el campo `TIPO_VENTA`.

**Venta en valor vs. venta en unidades** `[F1]`
Dos lecturas de la misma venta: en soles y en piezas. Divergen cuando cambia el precio o el mix. Que la venta en valor crezca y la de unidades caiga significa que se está vendiendo **más caro, no más**.

**Venta UND / Venta Q** `[F3]` `[F4]`
Venta expresada en unidades (piezas). "Q" por *quantity*. Es el contrapeso obligatorio de la venta en soles cuando hay agresividad de precio.

**Venta total** `[F1]`
Venta de todas las tiendas, incluidas aperturas nuevas y cierres.

**SSS** — *Same Store Sales* `[F1]` `[F3]` `[F4]`
Venta considerando únicamente las tiendas que existían en ambos períodos comparados. Aísla el crecimiento **orgánico** del que viene por expansión de la red. En F4 se reporta además como **"solo piso"**, es decir excluyendo el canal online.
*Sinónimo:* Venta Same Store, venta mismas tiendas.

**TSS** — *Total Store Sales* `[F3]` `[F4]`
Venta total de la operación: **piso + online**, sin el filtro de mismas tiendas.
⚠️ **SSS y TSS pueden contar historias opuestas.** En el Comité S36, en la semana 34 Tottus ganaba 1.2 p.p. de share en SSS y perdía 0.5 p.p. en TSS — la diferencia apunta al canal online. Nunca leer una sin la otra.

**Venta ponderada / no ponderada** `[F1]`
Filtro de ScanView que define si la venta se ajusta por algún factor de peso (ej. días operativos, tamaño de tienda) o se toma en bruto.

**Venta media** `[F1]`
Venta promedio de una unidad de análisis en un período. Según el contexto: venta media por tienda o venta media por ticket.

**Venta media por tienda** `[F1]`
Facturación total dividida entre el número de tiendas. Es la métrica del gráfico evolutivo de ScanView: neutraliza el efecto de aperturas y cierres, por lo que muestra tendencia real y estacionalidad.

**Rotación unitaria** `[F1]`
Unidades vendidas de un SKU en el período. Mide velocidad de salida del producto, independiente del precio.

**Rotación por tienda** `[F1]`
Rotación unitaria promedio por punto de venta. Permite comparar SKUs y tiendas de tamaños distintos.

**Venta perdida** `[F1]`
Facturación que se dejó de capturar por no tener el producto vendiendo en toda la red. Aproximación mostrada en la capacitación:
> `Venta perdida ≈ Rotación unitaria × Precio medio × (100% − % PDV)`

**Venta reciente alta** `[F4]`
Motivo de quiebre: la demanda real superó de forma abrupta a la proyectada, dejando el sistema de reposición corto. Se corrige con **limpieza de demanda**.

---

## 3. Ticket y comportamiento del shopper

**Ticket** `[base]`
Cada transacción de compra registrada en caja.

**TRX (transacciones)** `[F3]` `[F4]`
Cantidad de tickets del período. Es la métrica de **tráfico** en los reportes internos.

**Flujo en tienda** `[F1]`
Número de tickets generados = **tráfico**. Cuántas compras ocurrieron, no cuánta gente entró.

**Ticket medio / Ticket promedio** `[F1]` `[F3]` `[F4]`
Venta total ÷ número de tickets. Cuánto gasta en promedio un cliente por visita.

**Unidades por ticket (UPT) / UND x TRX** `[F1]` `[F3]` `[F4]`
Unidades vendidas ÷ número de tickets. Cuántos productos se lleva el cliente por compra. Junto con el ticket medio revela si el cliente compra más cosas o cosas más caras.

**Descomposición de la venta** `[base]`
`Venta = Flujo (tickets) × Ticket medio`, y `Ticket medio = UPT × Precio medio por unidad`. Es el marco para diagnosticar de dónde viene un crecimiento o una caída.
Aplicación práctica `[F3]` `[F4]`: en campañas promocionales, verificar siempre **cuál de los tres factores** movió el resultado antes de escribir el titular. En CDA II (F4) la venta creció +5.3% con ticket −2.0% y UPT −1.0%: todo el incremental fue tráfico.

**Misión de compra** `[F1]`
Motivo con el que el shopper entra a la tienda (reposición de despensa, compra de urgencia, ocasión especial). Un cambio de misión de compra se detecta cuando cae el tráfico pero suben ticket medio y UPT: menos visitas, pero de mayor valor.

**Shopper** `[F1]`
La persona en su rol de comprador dentro de la tienda. Se distingue del *consumidor* (quien usa el producto), porque no siempre son la misma persona ni responden a los mismos estímulos.

**Transacción vs. cliente (agregabilidad)** `[F17]`
Distinción operativa al sumar cifras entre tiendas o banderas: las **transacciones (TRX)** se pueden sumar libremente entre tiendas o banderas (ej. sumar las transacciones de una tienda con las de Megaplaza) siempre que la data esté abierta por tienda. Los **clientes únicos no**: el mismo cliente puede transar en dos tiendas o dos banderas distintas y sumar sus transacciones por separado no lo duplica, pero sumar el conteo de "clientes" sí lo haría — un cliente que compró en dos banderas cuenta una vez en cada una, no dos veces en el total. Antes de sumar cualquier cifra de clientes entre unidades, declarar si se está deduplicando.

**Clientes identificados** `[F3]`
Transacciones en las que el cliente se identificó (típicamente con tarjeta de fidelidad). Es el universo sobre el que se puede hacer análisis de comportamiento individual y de recurrencia.

**Universo de análisis** `[F3]`
Recorte explícito de tickets sobre el que corre un estudio. Ejemplo de F3: "tickets mayores o iguales a S/40", "tickets con Yapa", "tickets ≥ S/40 y con productos de campaña". Declararlo es obligatorio: cambiar el universo cambia todos los resultados.

---

## 4. Precio

**Precio medio** `[F1]` `[F3]` `[F4]` `[F17]`
Precio promedio efectivamente cobrado por un SKU en el período (facturación ÷ unidades). Incorpora el efecto de promociones y descuentos, por lo que difiere del precio de lista.
⚠️ **Dos causas distintas de que suba, y hay que distinguirlas antes de diagnosticar `[F17]`:**
1. **Subida real de precio** — el índice de precio propio es mayor que el de la competencia y que el del año pasado (ver *Price index / IPC*, abajo).
2. **Cambio de mix** — sin que haya subido el precio unitario de ningún producto, las compras del cliente se desplazan hacia productos de distinto **gramaje/tamaño** o **tier de precio** (ver abajo). Aplica en cualquier categoría donde convivan presentaciones o tiers distintos.
Confundir ambas lleva a leer "estamos más caros" cuando en realidad el cliente cambió lo que compra.

**Tier de precio (Low cost / Mainstream / Premium)** `[F17]` `[F5]`
Segmentación de los SKU de una categoría por nivel de precio, usada para explicar cambios de mix (ver *Precio medio*, arriba): si el año pasado la promoción empujaba lo **low cost** y este año empuja **mainstream** o **premium** (o viceversa), el precio medio se mueve sin que cambie el precio de ningún SKU individual. La fuente menciona incorporar esta apertura, junto con **misión de compra** y **quiebre**, como dimensiones nuevas de análisis.
Confirmado por el usuario: son los tres tiers correctos, **especialmente útiles en Abarrotes** (J1) — no necesariamente la apertura más relevante en todos los mundos por igual.

**Precio moda** `[F1]`
Precio al que el producto se vende con mayor frecuencia. Es el precio con el que el cliente realmente interactúa: si el precio moda está muy por debajo del precio de lista, el producto vive en promoción.

**Moda U3S** `[F2]`
Precio moda de las **últimas 3 semanas** de la competencia. Es el input de la regla de competitividad de Tottus (ver *IPC 98%*).

**Precio mínimo / precio máximo** `[F1]`
Extremos del rango de precios registrados en el período. La amplitud entre ambos indica dispersión de precio (promociones agresivas, diferencias por tienda o desfase).

**Precio desfasado** `[F1]`
Producto cuyo precio quedó desalineado respecto de su categoría, su histórico o el mercado. Detectarlo es uno de los usos declarados de la Tabla de Precios.

**Precio regular / precio de lista** `[F2]`
Precio cargado en el sistema en la creación del SKU. Es la referencia teórica, no necesariamente la que el cliente ve.

**Precio vigente** `[F2]`
Precio efectivamente activo en tienda en un momento dado, incluyendo el precio base de mecánicas (ej. la base de un "20% dcto") y el punto precio.

**Precio de campaña (boletín)** `[F2]`
Precio comunicado en la campaña (cartelería, medios, boletín).

**Precio percibido** `[F2]`
Precio medio calculado con la venta real de los **últimos 3 meses**. Es el precio que el cliente ha estado pagando de hecho, y por lo tanto el ancla real de su percepción.

**%Descuento teórico vs. %descuento percibido** `[F2]`
Dos formas de medir la profundidad de una promoción:
- **Teórico** = Precio Campaña vs. Precio Regular.
- **Percibido** = Precio Campaña vs. Precio Percibido.

Pueden divergir brutalmente. Ejemplo de F2: un cereal con −7.7% de descuento teórico tenía −49.7% percibido; un detergente con −20.8% teórico tenía solo −8.8% percibido. **El descuento percibido es el que mueve al cliente.**

**Punto precio** `[F2]` `[F18]`
Precio cerrado y comunicable (ej. S/9.90) que se fija como mecánica, en oposición a un porcentaje de descuento. Ejemplo dado por Planificación Promocional: una Cusqueña a "S/22.90 / S/21.90 con CMR" — el precio directo que se comunica en tienda sin más cálculo.

**Preciazo** `[F4]`
Precio de ataque comunicado como el más agresivo de la oferta. Aparece como columna de comparación competitiva.

**Price index / IPC (índice de precio de competencia)** `[F1]` `[F2]` `[F4]`
Precio propio expresado como índice frente al del competidor (100 = paridad; <100 = Tottus más barato).
Regla de competitividad vigente en Tottus `[F2]` `[F4]`: **techo del 98% sobre la moda de las últimas 3 semanas** ("IPC 98% – moda U3S").
En F4 se reporta como **IPC físico** por clasificación SKVI, abierto en **DDS** y **FDS**, con seguimiento semanal Nielsen Pricetrack contra Plaza Vea.
⚠️ **Un IPC promedio esconde la dispersión.** En el Comité S36 el IPC agregado era 98.0 pero el 37% de la venta SKVI estaba por encima de 100 (16% por encima de 105). El promedio no es una política de precio.

**DDS / FDS** `[F4]`
Cortes de la semana para el relevo de precios: **DDS** = días de semana (lun–jue), **FDS** = fin de semana (vie–dom). Los precios de competencia y el IPC se leen por separado en cada corte porque las dinámicas promocionales difieren.

**Relevo de precios** `[F2]` `[F4]`
Toma de precios de la competencia. Modalidades:
- **Relevo físico** — visita a tienda del competidor. Prioridad SKVI, típicamente en FDS.
- **Relevo digital / scrapping** — captura automatizada de precios web. En Tottus se apoya en **Netrivals** para KVI + NKVI.

**Nielsen Pricetrack** `[F4]`
Fuente externa de seguimiento de precios de competencia usada para el IPC físico.

**L&A** `[F4]` `[F5]`
Fuente externa de data de mercado usada para el reporte de crecimiento y share del Comité. Confirmado por el usuario: es la misma fuente detrás de *Market Share PE* (F15, ver sección 10) — mismo proveedor, dos nombres para el mismo reporte.
⚠️ *por confirmar:* razón social completa del proveedor (el nombre "L&A" sigue siendo una sigla, no una razón social).

**Congelamiento de precios** `[F4]`
Decisión de mantener precios fijos durante un período. Aparece anotado sobre la serie de IPC ("CONGELAMOS PRECIOS PVEA"), lo que rompe la comparabilidad de la serie a partir de ese punto.

**EDLP vs. High & Low** `[F2]`
Las dos estrategias de precio de referencia en retail:
- **EDLP** (*Every Day Low Price*) — precio bajo permanente, poca promoción.
- **High & Low** — precio regular más alto con promociones frecuentes y profundas.

Tottus es descrita en F2 como *"empresa con pasado EDLP ahora en estrategia High & Low"*, con el desafío de posicionarse como **price maker** y mejorar su **imagen de precio**.
⚠️ **Implicación analítica:** un SKU que aparece en el 95% de las campañas no está en promoción, está en precio base. Es EDLP disfrazado de High&Low y contamina la lectura de efectividad.

**Pricing** `[F1]` `[F2]`
Área/función que define la estrategia de precios. En el flujo descrito, Inteligencia Comercial detecta el desfase y lo escala a Pricing. En el proceso de HS `[F2]`, Pricing valida la propuesta comercial y **reacciona semanalmente**, con pase automático de cambios de SKVI los lunes hasta la 1 p.m.

**Blocker** `[F2]` `[F4]`
Precio o condición que impide que una apuesta salga como estaba definida y obliga a corregirla antes del cierre (típicamente por competitividad o por conflicto con otra mecánica vigente). "Mejora de precios (Blockers)" es un paso formal del flujo de pricing.

---

## 5. Margen y rentabilidad

**GPE / GPE%** `[F3]` `[F4]`
Ganancia bruta de explotación: el margen bruto del negocio, **antes de aportes comerciales**, en soles (**GPE MM**) y como porcentaje de la venta (**GPE%**). Es el indicador de margen estándar de los reportes de Tottus. Verificado F7: `GPE = VENTA_SI − COSTO_VENTA`.
Referencia F4 (Agosto 2026, Tottus): GPE S/62.0 MM sobre venta S/369.0 MM = **16.8%**, +0.8 p.p. vs AP.

**GP%** `[F7]`
Margen porcentual **después** de aportes comerciales y de merma — a diferencia del GPE%, que es antes. Se calcula desde la columna `PROFIT` (ver abajo).
Referencia F7 (Ene–Jul 2026, `BD_Profit`): Marca Propia GPE 16.5% → **GP% 15.7%** (−0.8 p.p.); Marca Proveedor (MMTT) GPE 9.4% → **GP% 27.9%** (+18.5 p.p.). La marca propia gana el margen frontal y lo pierde todo al pasar a GP% — ver *Rebate / Sellout*.

**PROFIT** `[F7]` `[F5]`
Columna de `BD_Profit` que alimenta el GP%. Convive con `COSTO_RECIBO` y `MERMA_CONOCIDA`.
Confirmado por el usuario: **PROFIT es, en esencia, el margen — no existe una fórmula más granular o documentada más allá de eso.** No hay un desglose oficial que perseguir. La observación de que MMPP cae 0.8 p.p. de GPE% a GP% sin recibir rebates (ver *GP%*, arriba) sigue siendo real, pero no se puede atribuir a un componente específico de `PROFIT` porque ese nivel de detalle no existe — queda como una diferencia observada, no como una ecuación por resolver.

**GM%** (*Gross Margin*) `[F4]`
Margen bruto porcentual, usado en los reportes de categoría de Non-Food. Se reporta **GM% Act** (actual) contra **GM% AP** (año pasado).

**Contribución (Contri)** `[F4]`
Margen después de descontar los costos directos atribuibles a la categoría. Se reporta contra **Plan Contri** y contra **Contri AP**.
⚠️ **Trampa:** cuando el Contri AP es negativo, el "Contri AP%" calculado sobre esa base no es interpretable. Y logros de contribución de tres dígitos (654%, 388%) no indican desempeño sino un plan mal puesto.

**Cash margin** `[F2]`
Margen en soles (no en porcentaje) que genera una promoción. Junto con el volumen incremental, es uno de los dos criterios con que F2 define si una promoción fue **efectiva**.

**Rentabilidad promocional** `[F2]`
Definida en F2 como **`GPE + Sellout`**: el margen bruto más el ingreso por acuerdos comerciales asociados a la promoción.
Referencia F2 (Ago-2025, J1/J2/J5): **16.6%** de las combinaciones SKU-promoción tenían rentabilidad negativa.

**Rebate / Sellout** `[F2]` `[F7]`
Ingreso que el proveedor paga al retailer, vinculado a la venta efectiva del producto en promoción. En el proyecto regional se trabajó la "disponibilización de rebate sell out por SKU" para poder calcular rentabilidad promocional a nivel producto.
**La marca propia no lo recibe** `[F7]`: es el origen estructural de la brecha entre su GPE% y su GP% (ver *GP%*, arriba) — no es una brecha de negociación, es estructural al modelo.
`[F5]` El usuario confirma que **no existe una cifra ni una regla formal** de cuánto aporte comercial se deja de cobrar por cada punto de share ganado con marca propia — lo que aparecía como pregunta abierta era probablemente parte de un insight puntual, no una métrica que se calcule de forma recurrente. No perseguir esta cifra como si tuviera una respuesta pendiente de encontrar.

**Fondos promocionales** `[F2]`
Inversión aportada por el proveedor para financiar una promoción. En la política de HS se contrapone a los **arriendos** como dos formas distintas de monetizar el espacio y la comunicación.

**Elasticidad** `[F2]`
Sensibilidad de la demanda al precio. Clasificada en **alta / baja**. Cruzada con la clasificación KVI, define la matriz de decisión promocional:

| | Alta elasticidad | Baja elasticidad |
|---|---|---|
| **SKVI** | Importante | Media |
| **KVI** | Importante | Media |
| **NKVI** | Media | **Quick Win** → parar de promocionar |

Referencia F2: la cuadrícula "NKVI + baja elasticidad + rentabilidad negativa" era el quick win identificado.

**Efecto halo** `[F2]`
Venta adicional de otros productos generada por la presencia de una promoción. Es el argumento que puede justificar mantener una promo con rentabilidad directa negativa — y por eso debe medirse, no asumirse.

**Curva A/B/C/D de promociones** `[F2]`
Clasificación de las promociones por efectividad: A (mejores) a D, más una categoría de **no efectivas**. Es el output del modelo de efectividad promocional del proyecto regional.

**Margen de contribución / GMROI** `[base]`
Pendiente de fuente oficial Tottus. Ver *Términos por incorporar*.

---

## 6. Promociones y campañas

### 6.1 Vehículos de campaña

**HS — Hardsell (Hardseller)** `[F2]` `[F4]`
El vehículo promocional principal de Tottus: una campaña de vigencia **catorcenal** que agrupa toda la oferta del período. Se numera correlativamente (HS17, HS18, HS19, HS20, HS21) y puede abrirse en subperíodos (HS19A / HS19B).
Escala de referencia `[F2]` (Set-2025): ~**5,700 SKUs**, ~**2,493 llamados**, ~**773 cartelerías** por HS.

**Táctico (TC)** `[F2]` `[F4]` `[F18]`
Campaña de menor escala y ciclo propio, numerada en paralelo al HS (T35, T36, T37, T38, T39). Tiene sus propios capacities, más reducidos que los del HS. Es una campaña **sin arriendos**, de menor duración — ver *Clasificación de campañas: con/sin arriendos*, abajo.
**Relación con el HS** `[F18]`, según Planificación Promocional: un HS (14 días) convive siempre con **dos Tácticos consecutivos**, uno por semana (ej. HS18 convive con T36 y T37; HS19 va acompañado de T38 y T39). Pero **no hay relación 1:1 de producto**: Hardsell y Táctico "viven a la par" en el calendario, pero el surtido no es el mismo — un Táctico puede tener productos nuevos que no están en el Hardsell de esa quincena.
**Variante Perecibles** `[F18]`: además del ciclo Golpe A/Golpe B (ver abajo), existe un Táctico específico para **Perecibles** (divisiones J3, J4, J6 y J7 — Ultra Frescos incluido) que corre **lunes a miércoles**, en un ciclo distinto al de las demás categorías.

**Flash** `[F18]`
Campaña puntual estructurada como un Táctico (sin arriendos, corta), activada de forma ad-hoc para un evento específico — ejemplo dado: un partido importante de fútbol, con apuestas en categorías asociadas a la ocasión (carbón, cerveza, carnes).

**Clasificación de campañas: con / sin arriendos** `[F18]`
Principio general de Planificación Promocional para agrupar los vehículos de campaña: son **campañas con arriendos** (HS — ver *Vigencia*, abajo) o **campañas sin arriendos y de menor duración** (Táctico, Flash). Es el eje que explica por qué HS tiene su propio capacity de cartelería (sección 7) y los otros vehículos no.

**Campaña conceptual / Especial** `[F2]` `[F4]` `[F18]`
Campaña temática que se monta sobre o en paralelo al calendario regular (ej. *Especial MMPP*, *Especial Bucal*, *Especial Limpieza*, *Feria Abarrotera*). Queda **fuera** de los máximos de cambio definidos en la política de HS, y por eso es la excepción que hay que gobernar aparte.
*Sinónimo:* **"Hardsell conceptual"** `[F18]` — término usado por Planificación Promocional para el mismo tipo de campaña cuando se monta sobre un HS: no es una campaña regular, tiene toda una comunicación propia detrás.

**Campaña Core** `[F2]` `[F13]`
Campaña estructural del calendario comercial. Es una de las cuatro fuentes de cartelería junto con Especiales, Mecánicas y Top Deals. Las cinco campañas core del año `[F13]`, con su ventana 2025:

| Campaña | Qué es | Ventana 2025 | Días |
|---|---|---|---|
| **DDM** | Día de la Madre | 24 abr – 07 may | 14 |
| **FFPP** | Fiestas Patrias | 17 jul – 30 jul | 14 |
| **DDN** | Día del Niño | 31 jul – 24 ago | 25 |
| **ANIVERSARIO** | Aniversario Tottus | 09 oct – 05 nov | 28 |
| **NAVIDAD** | Navidad | 20 nov – 24 dic | 35 |

Resultados 2025 (venta sin impuesto): Aniversario S/304.0 MM (+4.1%, 45.4% del total core) · Navidad S/186.2 MM (**+10.2%**, 27.8%) · DDM S/67.1 MM (+3.9%) · DDN S/63.4 MM (+6.8%) · FFPP S/48.8 MM (**−1.8%**, la única que cayó, ventana más corta y compitiendo con el arranque de DDN al día siguiente). Total core: S/669.5 MM, **+5.5%**.
**Benchmark para cualquier campaña core nueva:** +5.5% promedio 2025, rango de −1.8% a +10.2%. Las ventanas van de 14 a 35 días: normalizar por días o declarar que no se hace.

**Categoría campañera / `CAMPAÑERO`** `[F13]` `[F14]`
No toda la venta de la ventana de una campaña cuenta como venta de esa campaña: cada una define su propio conjunto de categorías participantes, y **cada una lo hace a un nivel de jerarquía distinto**.

| Campaña | Nivel de definición | Nº de reglas |
|---|---|---|
| DDM | División, Subdepartamento, Clase | 14 |
| FFPP | División, Departamento, Subdepartamento, Clase, Subclase | 18 |
| DDN | Departamento | 1 |
| NAVIDAD | Subclase | 230 |
| **ANIVERSARIO** | **ninguna** | — |

⚠️ **Aniversario no filtra categorías: participa toda la tienda.** Verificado recalculando desde la base: su cifra coincide con la venta total de la ventana a bandera Tottus y canal piso, mientras las otras cuatro quedan muy por debajo de su total de ventana. Decir "Aniversario es más grande que Navidad" sin esta aclaración es incorrecto: no es que venda más, **es que mide más**. Navidad define 230 subclases una por una — la definición más trabajada y la más frágil; cada subclase nueva que nadie agrega subestima la campaña.

El campo binario **`CAMPAÑERO`** (la categoría es de la campaña / es del resto) habilita la lectura "campañeros vs. resto", replicable a cualquier campaña: responde si creció a costa del resto de la tienda. Ejemplo Navidad `[F14]`: venta campañera S/204.7 MM sobre venta de ventana S/738.5 MM = **27.7%** de lo vendido esos días fue de categorías navideñas; dentro de esa venta campañera, **Panetón es el 48.8%** (ver Anexo C, caso Panetón, para la lectura por marca).

⚠️ **Navidad tiene dos definiciones de ventana conviviendo, sin reconciliar.** El archivo core (F13) la define 20 nov – 24 dic, solo bandera Tottus, canal piso de venta. El archivo de Navidad (F14) la define 26 nov – 24 dic, con Tottus, Precio Uno y Online. Declarar siempre cuál se usa antes de citar una cifra de Navidad.

**CDA** `[F4]`
Campaña comercial de Tottus con ediciones numeradas en el año (CDA I en marzo, CDA II en agosto de 2026). Se monta sobre un HS: en F4 aparece como "HS17 + CDA II".

**Chapa Tu Yapa (CTY)** `[F3]`
Campaña de **Precio Uno** con ediciones numeradas (CTY I en abril, CTY II del 29-Jun al 15-Jul de 2026). Su mecánica gira en torno a la **Yapa**.

**Yapa** `[F3]`
El producto o beneficio adicional que el cliente obtiene al cumplir la condición de la campaña Chapa Tu Yapa. Métrica asociada: **# Yapas promedio por ticket** (2.4 en CTY II).

**Boletín** `[F2]`
Pieza de comunicación de la oferta de campaña. En la política propuesta, el "boletín de arriendos chicos" tendría vigencia de 2 meses, desacoplándose del ciclo catorcenal del HS.

### 6.2 Unidades de la oferta

**Apuesta** `[F2]` `[F4]`
Cada oferta individual cargada en una campaña. "Carga de apuestas" es el primer hito de la ruta crítica.

**Llamado** `[F2]` `[F18]`
Unidad de comunicación promocional: el mensaje de oferta que se comunica al cliente. Un llamado puede agrupar varios SKUs (**llamado multiproducto**) o uno solo (**llamado monoproducto**).
⚠️ **Confirmado por Planificación Promocional:** el llamado (o "llamado de apuesta") es la nomenclatura comercial de cómo se comunica la promoción en tienda — **no es el nombre del SKU**. Ejemplo de multiproducto: el llamado "Yogures Gloria 1.6kg" agrupa 6 SKU (fresa, durazno, vainilla, lúcuma, guanana, etc.) bajo un mismo cartel.
⚠️ Es la unidad que consume **capacity de cartelería**, no el SKU. Referencia F2: ~5,700 SKUs generaban ~2,493 llamados.

**Deal** `[F2]` `[F4]`
Combinación SKU-promoción. Es la unidad sobre la que se mide rentabilidad promocional y efectividad.

**Best Deals / Top Deals** `[F2]`
Ofertas destacadas definidas comercialmente. Fueron el principal driver del crecimiento de cartelería: de +464 carteles entre Ene y Set-2025, **Top Deals aportó +293 (63%)** y Campañas Especiales +143 (31%).

**Mecánica** `[F2]`
Estructura de la oferta (ej. "20% dcto", "lleva 3 paga 2", "por compras superiores a S/30 llévate X a S/9.90"). Es una de las cuatro fuentes de cartelería.

**SKU Condición / SKU Beneficio** `[F2]`
En una mecánica condicionada: el producto que el cliente debe comprar (**condición**) y el que obtiene con el beneficio (**beneficio**).
⚠️ **Error frecuente documentado en F2:** repetir el SKU beneficio también en el campo de condición hace que el sistema aplique el precio beneficio como precio unitario sin exigir la condición.

**Cruce promocional** `[F2]` `[F4]`
Conflicto entre dos promociones vigentes sobre el mismo SKU o la misma canasta, que produce un precio no deseado en caja. Es una de las dos grandes fuentes de incidencia junto con los blockers.

**Prohibición** `[F2]`
Restricción sobre qué productos o categorías pueden participar en una promoción (ej. el caso Rones citado en F2).

**Blacklist** `[F2]`
Lista de exclusión propuesta en la política: llamados monoproducto no efectivos que no pueden volver a participar. Criterio acordado: productos con **menos de 5% de efectividad** no pueden participar en llamados monoproducto.

### 6.3 Medición de la promoción

**Efectividad promocional (Ep)** `[F2]`
Porcentaje de SKUs (o de llamados) de una campaña que generaron cash margin y/o volumen incremental. Es el KPI central de la política de HS.
⚠️ **Declarar siempre la base.** La Ep por **SKU** y la Ep por **llamado** dan resultados muy distintos: en F2 conviven Ep de 55.4% (SKU, universo HS) y 76.7% (llamado, arriendos prioritarios) sin que la diferencia esté señalizada.
Referencias F2 (2025): Ep universo HS **55.4%**; arriendos prioritarios **60.6%**; "internas" **52.2%**.

**Promocionalidad** `[F2]`
Porcentaje de los SKUs de una campaña que efectivamente tienen un **precio promocional** cargado (a diferencia de estar solo comunicados o exhibidos).
Referencia F2: **~79%** del HS tenía precio promocional; el **~21% restante participaba sin descuento**.
⚠️ **Hallazgo contraintuitivo de F2:** la efectividad de los SKUs *con* precio promocional (56.2%) era solo ~3 p.p. mayor que la de los SKUs *sin* precio promocional (53.2%) — y entre enero y abril los *sin* precio eran más efectivos. Cuestiona el valor marginal del descuento.

**Promo Share** `[F3]` `[F4]`
Participación de la venta de los productos de campaña sobre la venta total del universo comparable.
Referencias: CTY II **9.6%** vs Total Precio Uno `[F3]`; HS17+CDA II **44.6%** vs venta total Food de Tottus `[F4]`.
⚠️ Declarar siempre el denominador: "vs Total PU" y "vs Total Food" no son comparables entre sí.

**Matriz de efectividad (campaña vs. regular)** `[F3]`
Clasificación de los SKUs participantes según su desempeño en campaña frente a su comportamiento regular:

| Cuadrante | Lectura |
|---|---|
| **Estrella** | Rendimiento por encima del promedio de la campaña |
| **Bajo Impacto** | Por debajo del promedio |
| **Tráfico TRX** | Aportó transacciones aunque no venta |
| **Sin Engage** | No movió nada |
| **Sin Comparable** | No tiene referencia regular para medirlo |

Referencia CTY II: 34 Estrella / 20 Tráfico TRX / 27 Sin Engage / 3 Bajo Impacto / 10 Sin Comparable (94 SKUs).
⚠️ El "Sin Engage" es el cuadrante que se suele omitir del titular y es el que sostiene la decisión de depuración de surtido.
También vista, en versión más temprana y con otro nombre, en una lámina de HS17+CDA II `[F10]`: "Matriz de Efectividad — Campaña vs AP", eje **Var% de Transacciones (TRX)**, con solo 3 de sus cuadrantes nombrados (**Estrellas**, **Baja Efectividad**, **Venta sin Engagement**) y el cuarto sin definir. Estaba **en construcción**. Probablemente la misma matriz de arriba en un estado anterior — pedirla terminada.

**Descomposición Mantiene / Nuevo / Salieron / No Promo** `[F4]`
Método para saber si una campaña generó incremental real, comparando el estado promocional de cada SKU contra el año anterior:

| Grupo | Definición |
|---|---|
| **Mantiene** | Promo '26 – Promo '25 |
| **Nuevo** | Promo '26 – No Promo '25 |
| **Salieron** | No Promo '26 – Promo '25 |
| **No Promo** | No Promo '26 – No Promo '25 |

⚠️ **Es la vista más honesta de una campaña.** En CDA II el +S/4.4 MM se descompuso en: Nuevo +9.4M, Mantiene −0.2M, Salieron −3.8M, No Promo −1.0M. El surtido que se mantuvo en promo no aportó nada y el que salió cayó −39%: no hay incremental, hay rotación de SKUs.

**Repetición de surtido promocional** `[F2]`
Cuántas vigencias de campaña repite un mismo SKU. Referencia F2: **1,692 SKUs** aparecieron en más del **95%** de los HS del año, sobre 10,217 SKUs únicos (~17% del catálogo promocional permanentemente en promoción).

**Venta incremental** `[F2]`
Venta adicional atribuible a la promoción, por encima de lo que el producto habría vendido en condiciones regulares. Es lo que la comparación contra el **periodo regular** intenta aislar.

### 6.4 Vigencias y política de cambios

**Vigencia** `[F2]` `[F4]` `[F10]`
Período durante el cual una oferta está activa. El ciclo base del HS es catorcenal, partido en **Salida A** (días 1–7) y **Salida B** (días 8–14).
En el consolidado, la vigencia se codifica en el campo **`Tipo (14, A, B)`**: `14` corre las dos semanas completas, `A` solo la primera, `B` solo la segunda.
`[F5]` El usuario confirma que el vacío en `Tipo` (5,181 de 8,770 filas en HS18-A) **no tiene una definición específica que buscar** — no vale la pena tratarlo como una regla oculta por descubrir.
⚠️ **El archivo "B" no es "la campaña de la semana 2":** es el incremento sobre el A (en HS18, 21 filas / 2 llamados). Los deals `Tipo=14` ya corren las dos semanas y viven en el archivo A. El universo de la Salida B es A + B, no B solo.

**Golpe A / Golpe B** `[F2]` `[F18]`
⚠️ **El significado depende del vehículo — no confundir los dos usos:**
- **En HS** `[F2]`: los dos cambios de precio dentro de un mismo HS. **Golpe A** es la semana con cambio fuerte (~75% de los SKUs cambian de fleje), **Golpe B** la segunda (~7%). En promedio semanal, el **40%** de los SKUs presentaba cambio de fleje respecto del HS anterior. La política propuesta en F2 elimina los golpes semanales.
- **En Táctico** `[F18]`: los dos sub-períodos de 2 días dentro del mismo Táctico. **Golpe A** = jueves y viernes, **Golpe B** = sábado y domingo. Ejemplo (Táctico 37): Golpe A corre 10–11 set, Golpe B corre 12–13 set. Es la unidad que se sube al Excel de ruta crítica por separado (el archivo de Golpe B llega aparte del de Golpe A, mismas columnas y lógica).

**Máximo de cambios** `[F2]`
Tope de SKUs cuyo precio puede cambiar por ciclo, definido para no exceder el capacity de tienda. Propuestas evaluadas en F2: máximos de 500, 600, 1,000 y 1,100 SKUs según el grupo.
Objetivo declarado: pasar de ~5,700 flejes por HS a ~1,700, **acotando los cambios de precio en tienda ~65–70% al mes**.

**Smart HS** `[F2]`
Herramienta/plataforma en desarrollo para gestionar el armado del HS con información integrada de efectividad, competitividad y elasticidad. Salida prevista: 1Q Dic (HS3).

**Bitácora de llamados** `[F2]`
Registro histórico de los llamados usados, con su efectividad, para no repetir mecánicas que no funcionan.

---

## 7. Ejecución en tienda y trade marketing

**Cartelería** `[F2]` `[F4]`
Material gráfico que comunica la oferta en el piso de venta. Es el recurso escaso que limita cuántos llamados puede soportar una campaña.
⚠️ **Hallazgo estructural de F2:** entre Ene y Set-2025 los SKUs promocionados crecieron +53%, los llamados +68% y la **demanda de cartelería +150%**. Cada eslabón creció más rápido que el anterior — la campaña no creció por surtido sino por fragmentación. Y el **80% de las quejas de clientes por "error" de precio provienen de cambios de cartelería no ejecutados**.

**Fleje** `[F2]`
Etiqueta de precio en góndola. Es la unidad de cambio de precio en tienda: cambiar el precio de un SKU = cambiar un fleje.

**Capacity** `[F2]`
Capacidad máxima de la operación para absorber cambios en un ciclo. Se declara en tres dimensiones:

| | Operaciones | Visual | Sistémico |
|---|---|---|---|
| **HS** | 1,100 flejes / 400 cartelería | 303 cartelería | 4,000 entrada / 2,000 salida |
| **TC** | 600 flejes / 170 cartelería | 85 cartelería | 4,000 entrada / 2,000 salida |

⚠️ En Set-2025 se emitían **773 cartelerías** contra un capacity visual de **400**: la operación corría al ~193% de capacidad. Esa brecha es la causa raíz de la no ejecución en piso.

**Implementación de cartelería** `[F4]`
Seguimiento del porcentaje de cartelería que efectivamente llegó al piso, abierto en tres estados:
- **Implementado**
- **Sin Stock** — no se implementó porque el producto no estaba
- **No Implementado** — falla de ejecución

Referencia F4 (T31–T35): implementación estancada en **~84%**, con "Sin Stock" entre 10% y 16%.
⚠️ La causa dominante de no-implementación no es ejecución, es **quiebre**. Conecta directamente con el bloque de Logística del mismo comité.

**Arriendo** `[F2]` `[F10]`
Espacio de exhibición en tienda que el proveedor paga para destacar su producto. Es una fuente de **recaudación** además de una palanca de venta.
Referencia F2: **11,272 arriendos** en la cadena, promedio **194 por tienda**; rango de 25 (Próceres) a 487 (Trujillo 1). El **90.3%** de los SKUs de un HS tenía presencia en algún tipo de arriendo.
**Los arriendos se comprometen a través de varias campañas** `[F10]`, no dentro de una sola: el campo `Nombre de arriendo` del consolidado trae textos como "COMPENSADO CABECERAS PORTUGAL DESDE HS15 HASTA HS20". Un análisis de rentabilidad de espacio no puede mirar una sola campaña.

**Arriendos prioritarios (MV, R y C)** `[F2]` `[F10]`
Los arriendos de mayor visibilidad: **MV**, **Rumas** y **Cabeceras**. ~6,065 arriendos, ~105 por tienda, 28.5% de los SKUs.
⚠️ *por confirmar:* la expansión de la sigla **MV** no aparece en F2.
**Hallazgo de F2:** los arriendos prioritarios tenían **menos promocionalidad** (65% vs 79% del HS) y **mayor efectividad** (60.6% vs 55.4%). El espacio rinde más que el descuento.
**Probable equivalencia con los códigos de espacio del consolidado** `[F10]`: el consolidado trae 62 columnas, una por tienda, con códigos (`C`, `R`, `RC`, `CM`, `CSL`, `CMY`, `RL`, `HC1`, `AL2`, `CPC`, `CSF`, `CME`) en vez de sí/no. `C` y `R` calzan con **Cabeceras** y **Rumas** de esta entrada — el resto del diccionario sigue sin confirmar. Solo 3,913 de 8,770 filas de HS18-A tenían espacio asignado en alguna tienda. Habilita medir efectividad de deal controlando por exhibición física: un llamado con cabecera en 40 tiendas y otro sin espacio hoy se evalúan con la misma vara.

**Arriendos chicos** `[F2]`
Arriendos de menor visibilidad: gancheras, laterales y similares.

**"Internas"** `[F2]`
Promociones **sin arriendo**: producto en góndola con precio promocional pero sin espacio pagado ni exhibición destacada. ~54% de los SKUs del HS, con la efectividad más baja de todos los grupos (**52.2%**) y el menor % de surtido (27%).

**Composición de un HS** `[F2]`
Marco de referencia para leer cualquier campaña de Hardsell:

| Grupo | SKUs | Ep | Llamados | % Surtido |
|---|---|---|---|---|
| **Universo HS** | ~5,700 | 55.4% | ~2,493 | 36% |
| Arriendos prioritarios (MV, R, C) | ~1,700 | 60.6% | ~812 | 53% |
| Arriendos chicos | ~1,000 | 59.1% | ~428 | — |
| "Internas" (sin arriendo) | ~3,000 | 52.2% | ~2,000 | 27% |

*Datos F2, base Set-2025. Los grupos se solapan parcialmente; los % no suman 100.*

**Material POP** `[F4]`
Conjunto de piezas de comunicación en el punto de venta desplegadas en campaña. Vocabulario recogido de F4: **MDV**, **ruma / faster display**, **RT**, **banner triple / simple**, **cubresensores**, **floorgraphics**, **marcador de endoses**, **cubreruma**, **cabecera**, **banner carrito**, **perifoneo**.
⚠️ *por confirmar:* expansión de **MDV** y **RT**.

**OOH** (*Out Of Home*) `[F4]`
Publicidad exterior (pantallas, vía pública) como parte del despliegue de medios de una campaña.

**Encarte** `[F4]`
Pieza impresa de oferta distribuida fuera de la tienda.

**Error comercial** `[F4]` `[F2]`
Porcentaje de solicitudes de precio o promoción mal cargadas que llegan a producir un precio incorrecto en tienda.
Referencia F4 (Set): 99.2% programación / 98.2% ejecución / **0.9% error comercial**.
⚠️ Con ~5,700 flejes por HS, un 1.8% de error son ~103 flejes mal por campaña. El porcentaje tranquiliza; el volumen absoluto es el que genera las quejas.

---

## 8. Abastecimiento y quiebre

**Quiebre (de stock / out of stock)** `[F1]` `[F2]` `[F3]` `[F4]`
Ausencia del producto en góndola pese a estar activo en el surtido.
En ScanView **no hay data directa de quiebre**; el `% PDV` es el proxy y debe contrastarse con la data interna de productos activos `[F1]`.
En los reportes internos sí se mide directamente, con **metodología A&M** `[F3]`.

**FQ** `[F4]`
Indicador de quiebre reportado por categoría en el bloque de Logística (ej. "Papel Higiénico FQ 7.8% (−2 ppt)").
⚠️ *por confirmar:* expansión de la sigla (probablemente *Factor / Frecuencia de Quiebre*).

**Fill Rate (FR)** `[F4]`
Porcentaje del pedido que el proveedor efectivamente despacha. Es la causa raíz más citada del quiebre en el Comité (ej. "Motivo FR bajo 37%; KCC FR 70%").

**OH** (*On Hand*) `[F4]`
Stock disponible registrado en sistema. Un **OH negativo** indica desajuste entre sistema y físico, y obliga a un **sinceramiento de stock**.

**Limpieza de demanda** `[F4]`
Ajuste del histórico de demanda para que un pico atípico (típicamente promocional) no distorsione la proyección de reposición.

**Sinceramiento de stock** `[F4]`
Corrección del inventario en sistema para que refleje el físico real.

**Quiebre Pareto** `[F4]`
Quiebre medido solo sobre los SKUs que concentran la mayor parte de la venta, en lugar de sobre todo el surtido.

**Lead Time (LT)** `[F4]`
Días entre el pedido y la disponibilidad. En F4 se compara como atributo competitivo en la entrega de colchones.

**CDF / CP** `[F4]`
Centro de distribución / centro de producción. Aparecen como origen del despacho en el diagnóstico de quiebre de Perecibles.

**Bloqueante sistémico** `[F2]`
Restricción del sistema que impide ejecutar la definición comercial tal como fue diseñada.

---

## 9. Distribución, presencia y red de tiendas

**Punto de venta (PDV)** `[F1]`
Tienda física o digital donde se registra venta. La data de ScanView considera solo puntos de venta — no almacenes ni centros de distribución.

**% PDV** `[F1]`
Porcentaje de tiendas de la red en las que un SKU **registró facturación** en el período.
⚠️ **No significa que el producto esté activo o disponible.** Un SKU puede estar activo en el 100% de tiendas y facturar solo en el 56%. La brecha es la señal de alerta: quiebre, problema de ejecución, o surtido mal asignado por bandera.

**% variación de puntos de venta** `[F1]`
Cambio en la cantidad de locales entre los dos períodos comparados. Explica variaciones de venta que no son de performance sino de expansión de red (ej. la apertura de Izaguirre).
`[F5]` **Izaguirre es una tienda de pruebas** — el usuario confirma que este tipo de tiendas piloto se descarta de los análisis por convención, lo que explica su exclusión del Especial MMPP (`[F12]`, ver sección 17). No es una exclusión sin justificar: es la regla general para tiendas de prueba.
`[F18]` Consistente con lo anterior: Planificación Promocional confirma que Izaguirre tiene su **propia campaña específica** — un vehículo dedicado, aparte de HS/Táctico/Flash — lo que refuerza que se trata de una tienda con tratamiento especial en todo el proceso comercial, no solo en el reporting.

**Bandera / Formato** `[F1]` `[F4]`
Formato o marca comercial dentro del mismo grupo. En Tottus: **Tottus**, **Precio Uno / Hiperbodega (HB)**, **Ecommerce**. Filtrar mal la bandera contamina el `% PDV` y el share, porque cuenta locales donde ese surtido nunca se comercializa.
En F4 los formatos de reporte incluyen además **App + Web**, **Fcom** y **Tienda Internet (912)**.
⚠️ *por confirmar:* expansión de **Fcom**.

**Zona / cluster** `[F1]` `[F3]` `[F4]`
Agrupación geográfica o comercial de tiendas.
- Zonas comerciales Tottus `[F1]`: Lima Norte, Lima Moderna, Lima Sur, Provincia, Oriente/Iquitos.
- Zonas de seguimiento operativo `[F4]`: **A, B, C, D, E** (usadas en cartelería y en el KPI de canjes).
- Clusters de Precio Uno `[F3]`: **P**, **M**, **G** y **Oriente** (agrupación por tamaño/perfil de tienda).
- Regiones de reporte `[F3]`: Lima, Norte, Sur, Oriente, Iquitos.

**Peso Mercado vs. Peso TT** `[F4]` `[F15]`
Participación de una plaza en el mercado total frente a su participación en la venta de Tottus. La brecha mide **sobre o sub-exposición**.
⚠️ Ejemplo F4: Arequipa pesa 3.5% del mercado y 7.3% de Tottus (2.1x sobre-indexado); Lima 64.5% vs 60.1% (sub-indexada). Un problema en una plaza sobre-indexada golpea más de lo que su tamaño de mercado sugiere.

⚠️ **Lima difiere entre fuentes.** F15 (S35 2026, piso de venta) muestra Lima con **53.8%** de peso en Resto Mercado contra **71.4%** de peso en Tottus — sobre-indexada, lo opuesto a la lectura de F4 arriba.
`[F5]` El usuario indica darle más peso a **F4** cuando las dos fuentes no coinciden — es la lectura de referencia por defecto ante esta discrepancia, aunque la causa exacta (bases distintas o semanas con composición real distinta) sigue sin aislarse.

Referencia F15 (S35 2026, piso de venta): **Lima Norte** es la plaza con mayor ganancia semanal de share (+2.7 p.p., +3.4 p.p. YTD); **Lima Moderna** la de mayor pérdida (−1.3 p.p. semanal). En provincias, Arequipa y Trujillo concentran el mayor peso de Tottus fuera de Lima. **Resto Provincias** muestra un salto raro entre su share semanal (65.7%) y su YTD (36.1%) en la misma fila — revisar antes de citarlo, probablemente base semanal chica.

**Cajas por tienda** `[F1]`
Número de cajas registradoras. Proxy del tamaño y capacidad de la tienda (promedio Tottus ≈ 16). Permite comparar tiendas equivalentes y segmentarlas en grandes / medianas / chicas.

**Tienda estacional** `[F1]`
Tienda cuyo volumen depende fuertemente de la época del año (ej. Punta Hermosa, con pico de noviembre a marzo). Requiere planificación de surtido, personal y campañas distinta a la de una tienda promedio.

**Comercio minorista moderno vs. tradicional** `[F1]`
Moderno = cadenas de autoservicio con sistemas de caja integrados (supermercados, hipermercados, conveniencia). Tradicional = bodegas y comercio de barrio. La cobertura de mercado se reporta por separado porque conectar el canal tradicional es mucho más difícil.

---

## 10. Participación y lectura de resultados

**Share (participación)** `[F1]`
Peso de una unidad (SKU, marca, proveedor, categoría) dentro de un total definido. Siempre hay que declarar **share de qué**: share dentro de la subclase, dentro del subdepartamento, o de mercado.

**Representatividad** `[F1]`
Sinónimo de participación usado en la plataforma: cuánto pesa una división, subdepartamento o tienda dentro del total seleccionado. Es el criterio de ordenamiento más útil (por encima del alfabético) porque prioriza dónde hay dinero en juego.

**Share de mercado / Mshare** `[F1]` `[F4]` `[F15]`
Participación frente al total del mercado o de la competencia. En ScanView aún no disponible; se habilita al conectarse otros retailers. En el Comité se reporta con fuente externa (L&A) `[F4]`. **`Mshare`** es la abreviatura usada en el reporte semanal *Market Share PE* (F15), sobre todo en el bloque de Ecommerce.
El reporte *Market Share PE* abre esta lectura por **canal** (Piso de Venta / E-Commerce), **bandera** (Tottus / Precio Uno), **mundo** (PGC / Perecibles / Non Food), **categoría** y **geografía**, siempre con el mismo par TSS/SSS — ver Anexo A para el detalle S35 2026.
⚠️ **La taxonomía de categorías de este reporte no es la de las divisiones J internas.** Usa nombres de mercado (Comestibles, Cuidado del Hogar, Carnes y Pescados…) que no calzan uno a uno con J1–J12. No cruzar por nombre sin mapear primero.

⚠️ **Trampa señalada en `[F16]` — qué es "mercado":** un error de lectura frecuente es asumir que mercado = competencia + Tottus, dejando fuera a Precio Uno. La fórmula correcta:
> `Mercado = Grupo Tottus (Tottus + Precio Uno) + Competencia`
> `Market Share (de un jugador) = ese jugador / Mercado`

Así se puede leer indistintamente la participación de Tottus, de Precio Uno o de cualquier competidor, siempre sobre el mismo denominador. La fuente insiste en anotarla sin ambigüedad porque genera dudas recurrentes al equipo nuevo. Hoy la apertura completa (participación de cada competidor por separado, no solo la de Grupo Tottus) no está disponible en el **Excel semanal** que recibe el puesto — ver *Excel semanal*, sección 15 — y es parte de lo que se busca resolver migrando a la plataforma nueva.
⚠️ Confirmado en una segunda sesión `[F17]`: la plataforma con estas aperturas (por bandera, por formato, por zona) es casi seguro la misma que alimenta *Market Share PE* (F15) — **no es ScanView**, que en Perú todavía no tiene el filtro de Mercado habilitado (ver *Mercado*, sección 16.4).

**Chequeo de coherencia Supermarket vs. Excel propio** `[F17]`
Prueba de sanidad recomendada al usar la plataforma de mercado: si se filtra **solo Supermarket** (sin Precio Uno), la cifra de Tottus debería cuadrar con el Excel interno propio. Si se agrega Precio Uno al filtro, puede haber una pequeña diferencia por definición de universo, pero el filtro de solo Supermarket es el que debería conciliar de forma más directa. Es la forma de detectar un filtro mal puesto antes de presentar un número.

**Apertura zonal del mercado (Norte / Sur)** `[F17]`
Recomendación explícita: no quedarse solo con la lectura de mercado a nivel compañía — abrir también por **zona geográfica**. Un share que se ve estable o "muy pegado" al agregado puede estar escondiendo un problema concentrado en una zona (ej. una categoría cayendo fuerte en el Norte y compensada por el Sur). Es la misma lógica de *Apalancamiento* (arriba) aplicada a geografía en vez de a jerarquía de producto — cruza siempre con el campo de geografía de *Market Share PE* (F15).

**Resto Mercado / Resto M.** `[F15]`
El complemento de Tottus dentro del mercado total: mercado menos Tottus (TT+PU). Es el término que usa el reporte *Market Share PE* para lo que en la sección 10 ya se llama simplemente "el mercado" en *Dif Share*, abajo — mismo concepto, otro nombre.

**Dif Share (p.p.)** `[F4]` `[F15]`
Ganancia o pérdida de participación de mercado en puntos porcentuales. Se calcula comparando el crecimiento propio contra el del mercado (o **Resto Mercado**, arriba): crecer por debajo del mercado = perder share aunque la venta suba.
Ejemplo F4 (Chiclayo): mercado +11.3%, Tottus +7.3% → **−0.8 p.p.**; Precio Uno +14.1% → **+0.4 p.p.**

**#Sem Caída** `[F4]`
Número de semanas consecutivas en que una plaza viene perdiendo share. Convierte un indicador semanal en una señal estructural.
Referencia F4 (S34): Ica 25, Trujillo 22, Cajamarca 17, Piura 16, Chiclayo 15, Chimbote 14, Huancayo 11, **Lima 10**.

**Variación (%)** `[F1]`
Crecimiento o contracción vs. el período de comparación. Convención estándar del equipo: **mes vs. mismo mes del año anterior** (YoY), porque neutraliza la estacionalidad.

**AP** (Año Pasado) `[F3]` `[F4]`
El período equivalente del año anterior. Es la base de comparación por defecto en todos los reportes internos.

**Contracción** `[F1]`
Caída de la venta (variación negativa). Usado en la plataforma como opuesto de crecimiento.

**Punto porcentual (p.p. / ppt)** `[base]`
Diferencia aritmética entre dos porcentajes. Crecer 13.3% vs. 4.6% es una diferencia de **8.7 p.p.**, no de 8.7%. Distinción importante al reportar.

**Plan / Logro%** `[F4]`
**Plan** = objetivo presupuestado del período. **Logro%** = venta real ÷ plan.
⚠️ **Logro y crecimiento pueden apuntar en direcciones opuestas.** En F4, Colchones cerró julio con Logro 106.75% y crecimiento **−4.98%**: se sobrecumplió un plan puesto por debajo del año anterior. Cuando eso pasa dos meses seguidos, el problema es el plan.

**Valla** `[F1]`
Umbral de referencia contra el que se juzga un resultado: normalmente el crecimiento del nivel inmediatamente superior. Si el J6 crece 4.6%, cada subdepartamento debería crecer ≥4.6% para "pasar la valla". Es el criterio de diagnóstico central del Dashboard Categoría.
Extensión natural `[F4]`: para el negocio completo, la valla es el **crecimiento del mercado**.

**Apalancamiento** `[F1]`
Contribución de una unidad al resultado del total. Un subdepartamento "apalanca" el crecimiento cuando crece por encima de la valla y pesa lo suficiente para mover el agregado; "apalanca la caída" en el caso inverso. Cruza siempre dos cosas: **variación** y **representatividad**.

**Focals** `[F4]`
Conjunto de categorías o iniciativas bajo foco explícito del período, con seguimiento de aporte propio (ej. "Los Focals aportan −0.6 MM vs AP").
⚠️ *por confirmar:* definición formal del criterio de selección.

**Cumplimiento en subdepartamentos / tiendas** `[F4]`
Lectura de dispersión: cuántas unidades del total cumplieron su meta (ej. "Food: 31/48, oportunidad de S/5.5 MM"). Complementa el agregado, que puede estar bien mientras la mitad de las unidades falla.

**Oportunidad (S/)** `[F4]`
Soles que faltaron para que las unidades incumplidas alcanzaran su meta. Es la forma estándar de dimensionar una brecha en el Comité.

---

## 11. Bases de comparación y calendario

> Sección crítica: **la mayoría de las inconsistencias detectadas en los decks revisados vienen de mezclar bases.** Declarar siempre las cuatro dimensiones: universo de divisiones, formato (SSS/TSS), calendario (comercial/gregoriano) y período de comparación.

**Comparación Comercial vs. Comparación Gregoriana** `[F3]` `[F4]`
- **Gregoriano** — mes calendario (1 al 31).
- **Comercial** — semanas comerciales alineadas por día de la semana, de forma que un sábado se compare contra un sábado.

Dan cifras distintas para el mismo mes. En el Comité S36 conviven ambas en la misma página (el gráfico en comercial, los cuadros en gregoriano), y por eso Tottus aparece con cifras ligeramente distintas según el bloque.

**Período regular** `[F3]` `[F4]`
Base de comparación no promocional que se usa para aislar el incremental de una campaña. Se define como **mediana diaria** de un rango sin campañas.
⚠️ En las fuentes revisadas conviven **al menos tres definiciones** ("01-Ene a 25-Mar 2026", "01-Ene a 30-Jun 2026", "Enero'26 a Junio'26"). Fijar una y declararla en cada slide.

**Mes cerrado** `[F1]`
Mes cuya data ya terminó de consolidarse. La data del mes en curso llega incompleta, por lo que los análisis se hacen sobre el último mes cerrado.

**Proyectado cierre de mes** `[F4]`
Estimación del cierre a partir del avance parcial. Se reporta junto al real y **debe ir siempre etiquetado**: en el KPI de canjes de F4 el "+13%" era una proyección presentada al lado del avance real.

**YTD** (*Year To Date*) `[F4]`
Acumulado del año hasta la fecha.
⚠️ El acumulado puede invertir la señal del período reciente: en Colchones, Ene-Ago daba +3% y Jun-Jul **−4%**. En un comité de seguimiento, el corte reciente manda.

**Período base / período de comparación** `[F1]`
El período contra el cual se mide. En ScanView se elige libremente y admite multiselección de meses, para comparar correctamente eventos estacionales móviles (ej. Semana Santa que cae en marzo un año y en abril el siguiente).

**Estacionalidad** `[F1]`
Patrón recurrente de la demanda a lo largo del año. Ejemplos citados: pescados y mariscos con pico en marzo–abril (Semana Santa), picos generalizados en diciembre, tiendas de balneario con pico de verano.

**Numeración de semana (SXX)** `[F4]`
Semana comercial del año. Es la unidad de seguimiento del Comité (S36-2026 = semana 36) y de todos los reportes de mercado.

---

## 12. Loyalty y clientes

**Loyalty** `[F4]`
Área y programa de fidelización. Sus KPIs de seguimiento: canjes físicos, canjeadores, cumplimiento por zona y tienda, top de productos canjeados.

**Canje** `[F4]`
Operación en la que el cliente cambia puntos por producto.

**Canjeador** `[F4]`
Cliente que realizó al menos un canje en el período. Se distingue de **nuevo canjeador** (primera vez) y de **cliente adquirido**.

**Costo CMR Puntos** `[F4]`
Costo con el que un SKU entra al catálogo de canje: costo del producto más el margen negociado. De ahí se deriva el **puntaje** que se le asigna al cliente y el **costo por punto**.
> Cadena de la palanca comercial: *Comercial negocia mejor costo → baja el Costo CMR Puntos → Loyalty asigna menor puntaje → canje más atractivo, sin subir el costo del programa.*

**CMR** `[F4]`
Tarjeta del grupo (Banco Falabella). Se reporta como canal con su propia variación y participación (~24.3% de participación YTD-2026).

**ON** `[F4]`
Canal online, reportado junto a CMR en los KPIs adicionales del Comité (~6.0% de participación YTD-2026).

**Canje profundizado** `[F4]`
Campaña de canje ejecutada de forma coordinada por cinco áreas (Comercial, Banco, Marketing, Operaciones, Trade+Visual) en lugar del canje regular pasivo. Caso Chile: x74 canjes y x96 canjeadores frente al canje regular.
⚠️ En ese mismo caso, **"clientes adquiridos" pasó de 4% a 4% (0 p.p.)**: multiplica el canje entre clientes existentes, no adquiere clientes nuevos.

---

## 13. Procesos y gobernanza comercial

**Ruta Crítica** `[F2]` `[F4]`
Secuencia de hitos con responsable y fecha límite que debe cumplirse para que una campaña salga a tiempo. Se mide por campaña y se reporta como **hitos cumplidos / incumplimientos críticos / observaciones menores**.

Hitos de la ruta crítica de **Táctico** `[F4]`, con días de anticipación:

| # | Hito | Días | Responsable |
|---|---|---|---|
| 1 | Carga de apuestas | −19 | Analista Comercial |
| 2 | Selección de medios | −17 | Gerente de Línea |
| 3 | Compra de mercadería | −15 | Planning |
| 4 | Validación de precios | −10 | Analista Comercial |
| 5 | Cumplimiento de mercadería | −3 | Planning |

⚠️ **Tercera versión de la ruta crítica del Táctico, sin reconciliar con la tabla anterior** `[F18]`. Planificación Promocional (dueña del proceso) describe la ruta crítica del Táctico contada desde el **día cero = inicio de vigencia**, hacia atrás, arrancando en **−40 días** (con hitos intermedios en −1, −9, −15…) — no en −19 como muestra la tabla del Comité arriba. Aplica la misma regla que para HS (ver más abajo): **el vigente es siempre el calendario más reciente**, y esta versión viene directo del área dueña del proceso el 10-Set-2026, por lo que probablemente sea la más confiable de las tres. Pendiente conseguir el desglose completo de hitos intermedios de Planificación Promocional.

Hitos de la ruta crítica de **HS** `[F4]`: Checklist Confirmación (−52), Briefing Comercial (−27), Carga Apuestas (−27), Alerta mercadería (−21), Compra mercadería (−21/−16), Validación precios (−10), Cumplimiento de mercadería (−3). Responsables: Trade Marketing, Planificación Promocional, Comercial y Planning.

⚠️ **Versión más granular y con otros plazos, sin reconciliar** `[F11]`. `RUTA CRITICA 2025.xlsx` (hoja `HS CONCEPTUAL`) trae 13 hitos con día en rojo cuando hay corrimiento por feriado o facturación: Confirmación y definición (−52) · Briefing comercial + plantilla arriendos (**−50**) · Convocatoria CO+AL (−45) · Deadline postulaciones CO+AL, Comercial→Trade (−41) y Trade→Planificación (−38) · 1er envío plantilla arriendos + apuestas Salida A (−34) · Confirmación espacios en medios (−31) · Envío primer reporte de arriendos (−29) · Selección de medios/rumas/MV/cabecera/QR (−27) · Definición de espacios comerciales (−24) · Envío consolidado preliminar (−22) · Carga de selección de medios (−20) · Alerta de quiebres o sobre stock (−17) · **fecha máxima de cambios por alertas y excepciones (−16)**.
El "Briefing Comercial" difiere en **23 días** entre esta fuente (−50) y la del Comité (−27, arriba).
`[F5]` **Regla confirmada por el usuario: el vigente siempre es el calendario más reciente.** Entre F11 (`RUTA CRITICA 2025.xlsx`, 2025) y F4 (Comité S36-2026), el que manda es **F4** — no hace falta reconciliar ambos como si compitieran; F11 queda como referencia histórica del proceso anterior a "Impulso+" (F2).
**Lo que sí es estable en ambas versiones:** la campaña se cierra comercialmente entre 16 y 10 días antes de salir. Un hallazgo post-campaña ya no cambia nada de esa edición — alimenta el ciclo de la siguiente.

**Retro Gantt** `[F2]`
Planificación hacia atrás desde la fecha de salida de la campaña, que fija cuándo debe ocurrir cada hito. Es el instrumento sobre el que se monta la ruta crítica.
En el proyecto regional `[F2]` el objetivo era incorporar la **efectividad promocional** como input formal del Retro Gantt.

**Planificación Promocional** `[F2]` `[F4]`
Área responsable de consolidar las apuestas, validar la definición comercial y evitar errores de precio y cruces.

**Planning** `[F2]` `[F4]`
Área responsable de la compra y el aseguramiento de mercadería para la campaña.

**Trade Marketing** `[F4]`
Área responsable del checklist de confirmación y de la bajada de la campaña al piso de venta.

**Visual** `[F2]`
Área responsable de la producción de cartelería. Su capacity (400 llamados en HS) es la restricción dura del volumen de comunicación de una campaña.

**Plantilla de carga promocional** `[F2]`
Formato con el que Comercial ingresa las apuestas. El proyecto regional trabajaba en una nueva plantilla con información de **efectividad, competitividad y elasticidad** incorporada, más su automatización.

**Rebote de plantillas** `[F2]`
Devolución de una plantilla mal cargada para corrección. Reducirlo es uno de los beneficios declarados de Smart HS.

**Homologación de procesos** `[F2]`
Alineamiento del proceso promocional entre países del grupo (PE / CL).

### Revisión profunda de categoría — framework en diseño `[F17]`

⚠️ **En diseño al momento de la fuente — no es todavía un entregable formalizado.** Metodología que Gabriel está armando para revisar una categoría a fondo (piloto observado: Galletas), pensada para escalar de **una categoría cada dos semanas** a **una por semana**, y eventualmente automatizarse.

**Estructura declarada, dos láminas por categoría:**
1. **Lámina de framework/metodología** — un esquema en semáforo (positivo/negativo) por variable de diagnóstico, que permite ubicar de un vistazo dónde está el foco antes de entrar al detalle.
2. **Lámina de mercado** — vista transversal por marca/fabricante-proveedor (no solo por categoría), con el comportamiento de las **últimas 3 semanas** y cuántas semanas consecutivas lleva cayendo el share de esa marca. Se apoya en las vistas satélite de **surtido** (qué productos, y si el espacio de góndola de esa categoría aumentó o disminuyó) y de **clientes** (a cargo del equipo de Clientes, sección 14).

**Recomendaciones metodológicas explícitas:**
- Abrir siempre por **zona geográfica** (Norte/Sur), no solo a nivel compañía — ver *Apertura zonal del mercado*, sección 10.
- Cruzar cada arista con **comercial** y con **operaciones**: un hallazgo puede ser transversal a toda la red (tema comercial) o concentrado en una zona/tienda (tema operativo) — no asumir cuál es sin revisar ambas.
- Herramienta personal sugerida: un Excel propio donde solo se pega la data actualizada cada semana y los indicadores/histórico se recalculan solos, en vez de rearmar el análisis desde cero en cada corte.

**Flujo de aprobación declarado — levantamiento con las áreas dueñas del dato:**
1. **Definir la categoría** a revisar (piloto observado: Galletas).
2. **Levantamiento por área**, cada una entrega su arista por separado (Inteligencia Comercial consolida, no arma cada pieza desde cero):
   - **Inventarios** (Alan, sección 14) — disponibilidad y quiebre.
   - **Catman** (Isabel Aliaga, sección 14) — surtido, mix y espacio de góndola (qué productos, si el espacio subió o bajó).
   - **Promociones** (Mire, sección 14) — mecánica y calendario promocional vigente.
   - **Carga / Data** (Hans para carga, Daniel para soporte de data, sección 14) — armado de la base que alimenta el análisis.
   - **Clientes** (Marisabel, sección 14) — comportamiento del shopper de esa categoría.
3. **Consolidación** por Inteligencia Comercial: se arma el framework y la lámina de mercado con lo que entregó cada área, cuidando que **todo tenga coherencia narrativa** — si un bloque no calza con el resto, se explica, no se esconde.
4. **Revisión de Yami** (líder del área, sección 14) — primera pasada rápida.
5. **Validación con Comercial** — gerente de categorías/Planificación Comercial y Hugo (sección 14).
6. **Presentación en el Comité Comercial.**

⚠️ **Pricing no aparece en este levantamiento** — la relación confirmada en otra parte de esta sección es reactiva: Inteligencia Comercial detecta un desfase de precio y **lo escala a Pricing** (ver arriba, *Pricing*), un flujo distinto al ciclo fijo de revisión por categoría. *Por confirmar* si en la práctica también participa del levantamiento.
⚠️ *por confirmar:* nombre final de este entregable y si termina viviendo en la sección 17 (Entregables del puesto) una vez formalizado.

---

## 14. Actores del ecosistema

**Retailer** `[F1]`
La cadena minorista. En este contexto, Tottus.

**Proveedor** `[F1]`
Empresa que abastece al retailer. En la plataforma se lista y rankea por representatividad.

**Fabricante** `[F1]`
Empresa que produce. En la práctica de la plataforma, el nivel de agregación por encima de la marca (ej. Alicorp como fabricante, con varias marcas por debajo). Se puede analizar a nivel fabricante o desmarcar el check para bajar a nivel marca.

**Marca** `[F1]`
Nivel por debajo del fabricante (ej. Marca Tottus, Gloria).

**Competidor de referencia** `[F4]`
En el seguimiento de precios, **Plaza Vea** es el competidor contra el que se calcula el IPC físico. En categorías Non-Food el set competitivo se amplía a **Falabella, Sodimac y Plaza Vea**.

**Category management (gestión de categorías)** `[F1]`
Disciplina que gestiona una categoría como una unidad de negocio propia: surtido, precio, espacio y promoción, decidiendo con data en lugar de por SKU aislado.

**Gestor de categoría** `[F1]`
Rol responsable de una categoría o división. Es el usuario objetivo del Dashboard Categoría.

**KAM** (*Key Account Manager*) `[F1]`
Ejecutivo responsable de una cuenta clave. Paolo Gaspar es el KAM de Scanntech para la implementación en Tottus.

**Monetización de data** `[F1]`
Modelo por el cual el retailer comparte, de forma controlada, data de venta con sus proveedores a cambio de inversión comercial. El retailer define **con quién**, **por cuánto tiempo** y **qué información** se comparte.

### Proveedores de data de mercado `[F16]`

Panorama de los proveedores externos que miden el mercado retail, con quién los conecta el puesto y cómo cobran. Se dividen en dos lógicas de captura muy distintas — confundirlas al comparar cifras entre proveedores es el error más común señalado en la fuente:
- **Panel de hogares** — el proveedor recluta hogares "representativos" y registra lo que compran, sin depender de que el retailer entregue nada (Kantar).
- **Auditoría de punto de venta / venta del propio retailer** — el número viene de las cadenas, vía scanner o entrega directa (Nielsen, GfK, y los proveedores con modelo de monetización de data).

⚠️ Varios nombres de proveedores y de personas en esta subsección vienen de una transcripción automática de audio con errores de reconocimiento frecuentes en nombres propios — se marcan individualmente donde la lectura es insegura, y no deben usarse en un entregable sin confirmar contra el área.

**Kantar** `[F16]`
Proveedor de data de mercado con metodología de **panel de hogares**. Entró **recientemente** al mercado peruano frente a otros proveedores con más historia local (ver *Lock*, abajo).
⚠️ **Trampa señalada en la fuente:** Kantar es fuerte en Lima; en provincia su número "no conversa" tanto con la venta real de Tottus. A nivel Tottus general sí es representativo, pero sigue siendo **muestra muestral** — tomar con pinzas cualquier cifra abierta a un nivel muy granular (la fuente menciona un caso donde el ticket promedio que reportaba Kantar no cuadraba con el propio).
`[F5]` **Corrección del usuario: el contacto "Paolo" no es de Kantar.** Paolo Gaspar es el KAM de **Scanntech** (`[F1]`, ver *KAM* arriba) — la transcripción atribuyó mal el nombre a Kantar. El contacto real de Kantar queda sin identificar.

**Kantar Panel / Numerator** `[F16]`
Producto de panel de hogares de Kantar. La fuente señala que **"hoy día ha cambiado [a] Numerator"** — Kantar Worldpanel operaría/reportaría hoy bajo la marca **Numerator**. ⚠️ *por confirmar:* alcance exacto del cambio (solo de marca, o de operador).

**Kantar Insights** `[F16]`
El otro producto de Kantar mencionado en la fuente, **basado en encuestas** en vez del panel de compras: preguntas directas a hogares, no registro de transacciones.

**Nielsen** `[F16]`
Proveedor de **auditoría de punto de venta**, con metodología similar a *Lock* (abajo): mide supermercado, mercado moderno y también mercado tradicional — cobertura más amplia que el panel de Kantar. Muchos años operando en Perú.
Nielsen y GfK se mencionan conjuntamente para categorías especializadas (colchones, TV, audio, video) en canales especializados (tiendas tipo La Curacao/Mall, Samsung) que Nielsen no cubre por sí solo.
Contacto: **Mauricio**, quien lidera la cuenta; trabaja con un analista de soporte que **rota con frecuencia**.
Es la misma casa Nielsen de *Nielsen Pricetrack* (sección 4).

**GfK** `[F16]`
Proveedor de auditoría de punto de venta especializado en categorías de electro/hogar (colchones, TV, audio, video) y canales especializados que Nielsen no cubre por sí solo. Aparece también nombrado como "Pro GFK" sin que se aclare si es un producto distinto. ⚠️ *por confirmar.*
Contactos: **Helen** (apellido no confirmado) y **Jacob**.

**Lock** ⚠️ *nombre por confirmar* `[F16]` `[F5]`
Nombre de proveedor tal como quedó en la transcripción automática — la lectura fonética es insegura. Según el audio: trabaja "muy similar" a Nielsen (auditoría de punto de venta) y tiene **muchos años de historia en el mercado peruano** (más que Kantar, entrante reciente). Contacto mencionado, también con lectura insegura ("Swan", posiblemente "Juan").
Confirmado por el usuario: **es un proveedor de información de terceros** (no Nielsen, Kantar o GfK bajo otro nombre) y **es distinto de L&A** (sección 4, `[F4]`) — no fusionar ni usar uno para inferir el otro. Su nombre real y el de su contacto siguen sin identificar.

**"Escatec" y "Scarpe" = Scanntech** `[F16]` `[F5]`
Confirmado por el usuario: tanto "Escatec" como "Scarpe" son transcripciones defectuosas de **Scanntech** (escritura correcta) — no son dos proveedores adicionales, son el mismo Scanntech ya documentado (`[F1]`, ver *KAM* y *Monetización de data*, arriba, y la sección 16 completa), mencionado dos veces en la grabación con lecturas distintas del reconocimiento de voz. La descripción de "Scarpe" (una herramienta que pone en el centro al fabricante/proveedor y al retailer para que negocien con esa data de por medio, con un fee mínimo) es probablemente uno de los otros servicios de Scanntech además de ScanView — Scanntech tiene 6 soluciones y Tottus usa hoy solo una (ver 16.1).
Se conservan ambas variantes transcritas como referencia, siguiendo la regla de no borrar una discrepancia (§8 de CLAUDE.md): si en el futuro aparece "Escatec" o "Scarpe" en esta u otra grabación, es Scanntech.

**Personas del área** `[F6]` `[F16]`
Contactos operativos del puesto y para qué se les busca:

| Quién | Rol | Para qué |
|---|---|---|
| **Mirella Gómez Montufar** | Predecesora, de vacaciones | Traspaso; dueña de las carpetas compartidas heredadas |
| **Dani (Daniel)** `[F6]` `[F16]` `[F17]` `[F5]` | Miembro del equipo de Gabriel. Provee las bases de venta, ajusta el Excel semanal de mercado y da soporte de Data en la revisión de categoría | Insumo de los dos entregables recurrentes (sección 17), del Excel semanal (sección 15) y de la revisión de categoría (sección 13) |
| **"Dani" (Planificación Promocional)** ⚠️ *posible homónimo, no confirmado* `[F18]` | Carla Flores la nombra como parte de **su propio equipo** — sube los archivos de Táctico (ej. T37) al Excel de ruta crítica | ⚠️ **Discrepancia sin resolver:** el usuario confirmó que "Dani" es Daniel, de su propio equipo (fila de arriba, `[F5]`). Esta fuente nombra a un "Dani" distinto, del equipo de Carla. Probablemente sea un homónimo (persona distinta con el mismo apodo) y no el mismo Daniel — confirmar antes de asumir cualquiera de las dos opciones |
| **Denisse** | Arma el Boletín de Marketing | Destinataria del bloque de resultados de campañas |
| **Daniela Montoya / Carla Flores** (Carla Teresa Flores Otoya) `[F18]` | Planificación Promocional | Tácticos (T##) y las preguntas abiertas del consolidado (sección 6). `[F17]` `[F5]` También trabaja con Gabriel en la *Matriz de surtido en mix* (sección 1). `[F18]` Es quien explicó la ruta crítica del Táctico 37 y el Excel operativo del área |
| **María Alejandra Balarezo** | Responsable de lanzamientos | Contexto de lanzamientos y relanzamientos (caso Xplend, Anexo C) |
| **Yami** (Yamile) | Lidera el área | Priorización y validación de criterios. `[F17]` `[F5]` "Yani" (F17) es la misma persona — variante del nombre |
| **Finanzas / Control de Gestión** | — | Que las cifras cuadren antes de presentar |
| **Joan** `[F16]` | Envía el Excel semanal de mercado (cerrado, sin tiendas nuevas) | Fuente del corte que alimenta *Share de mercado* mientras se migra a la plataforma nueva (ver sección 15) |
| **Isabel Aliaga** `[F17]` | Category Management (Catman) | Cruzar hallazgos de surtido/mix con Catman antes de presentarlos |
| **Marisabel** `[F17]` | Lidera el equipo de Clientes | Vista de cliente dentro de la revisión profunda de categoría (sección 13) |
| **Williams** `[F17]` | Soporte para llevar la *Matriz de surtido en mix* (sección 1) a un dashboard | — |
| **Hugo** `[F17]` ⚠️ *por confirmar* | Gerente de línea comercial que valida la revisión de categoría antes del Comité Comercial (rol leído del contexto, no confirmado) | — |
| **Hans** `[F17]` ⚠️ *por confirmar* | Contacto para temas de "carga" (rol impreciso) | — |
| **Mire** `[F17]` ⚠️ *por confirmar* | Contacto para promociones (rol impreciso) | — |
| **Alan** `[F17]` ⚠️ *por confirmar* | Contacto de inventarios | — |
| **Daniela Aste** `[F5]` | Brand Manager — valida el objetivo de campaña del boletín | Boletín de Marketing (sección 17). Confirmado: es una persona **distinta** de Dani/Daniel (arriba) |

---

## 15. Analítica y plataforma

**Insight** `[F1]`
Hallazgo accionable derivado de la data — no el dato en sí. En el modelo de Scanntech, el output que se devuelve al retailer después de procesar sus ventas.

**KPI** (*Key Performance Indicator*) `[F1]`
Indicador clave de desempeño. Los del negocio en este contexto: flujo en tienda, ticket medio, unidades por ticket, venta media, price index.

**Driver** `[F1]`
Variable que explica el movimiento de un resultado. Diagnosticar por drivers = descomponer la venta hasta encontrar qué la movió (tráfico, ticket, precio, distribución).

**API** `[F1]`
Interfaz por la que Tottus envía su data transaccional a Scanntech de forma automática y continua.

**Dashboard** `[F1]`
Cada una de las hojas de la herramienta. En ScanView para Tottus: Categoría, Negociación, Tabla de Precios, Ejecutivo y Operacional.

**Explorador de Complementariedad de Productos** `[F4]`
Herramienta interna de asociación de productos, con tres niveles de análisis (Clase / Subcategoría / Producto). Métricas propias:
- **Clase origen (antecedente)** — el producto o clase desde el que se analiza.
- **Clase destino (consecuente)** — lo que el cliente tiende a llevar junto.
- **Intersección (items)** — volumen de tickets en que ambos coinciden.
- **Ratio complemento (%)** — fuerza de la relación.

Matriz de decisión: alta afinidad + alto volumen → **Prioridad Comercial** (impulsar cross-sell y bundles); alta afinidad + bajo volumen → **Oportunidad de Crecimiento** (mejorar disponibilidad, surtido y exhibición); baja afinidad + alto volumen → **Revisión Comercial**; baja afinidad + bajo volumen → **Baja Prioridad**.
⚠️ Ordenar la tabla solo por *ratio complemento* entierra los pares de mayor volumen de co-ocurrencia, que son los que más soles mueven. Leer siempre las dos columnas juntas.

**Tabulación cruzada** `[F1]`
Formato de exportación de la plataforma que permite bajar cualquier tabla a Excel para seguir trabajándola.

**Vista personalizada** `[F1]`
Configuración de filtros guardada con un nombre, que puede fijarse como **valor predeterminado** para que el dashboard abra siempre así. Es la alternativa al envío automático de reportes por correo, que la plataforma no ofrece.

**Vista original** `[F1]`
Configuración de fábrica del dashboard, a la que siempre se puede volver.

**Drill-down** `[base]`
Navegación de lo agregado a lo detallado dentro de una jerarquía, haciendo clic nivel por nivel. Es el modo de uso central del Dashboard Categoría.

**Vista macro vs. vista micro** `[F1]`
Macro = compañía / mundo / división. Micro = subclase / SKU / tienda. La recomendación explícita de la capacitación es no analizar la propia categoría sin haber mirado antes la macro: una caída propia puede estar respaldada por una contracción del negocio.

**Discover** `[F16]`
Plataforma donde Nielsen y *Lock* (sección 14, ⚠️ nombre por confirmar) cargan su data de auditoría de punto de venta en modo autoservicio, en lugar de entregarla en bruto — Nielsen ya tiene toda su información migrada ahí.
⚠️ *por confirmar:* si Tottus tiene acceso hoy a Discover, o si sigue dependiendo del **Excel semanal** (abajo) mientras otros retailers ya lo usan — la fuente lo deja ambiguo ("nosotros somos los que nos estamos quedando en el Excel").

**Radar / Active** `[F16]`
Herramienta mencionada junto a Discover para seguimiento de la evolución, con data semanal cerrada (semana 34, semana 35, semana 36…) y apertura diaria más reciente. En la fuente el nombre queda ambiguo entre "Radar" y "Active" — pueden ser la misma herramienta o herramientas emparentadas.
⚠️ *por confirmar:* nombre exacto y si Tottus tiene acceso ("este no lo tenemos, fíjate si lo tenemos").

**Excel semanal (mercado)** `[F16]`
Archivo que recibe hoy el puesto con el corte de mercado, en lugar de acceso directo a Discover. Llega **cerrado, sin tiendas nuevas** — lo manda **Joan** (sección 14); hay un ajuste puntual pendiente a cargo de **Daniel** (sección 14, rol sin confirmar).
A diferencia de la plataforma nueva, **no tiene apertura completa de mercado**: no permite ver la participación de cada competidor por separado (solo la de Grupo Tottus, ver *Share de mercado*, sección 10), ni filtrar por formato (ver abajo). Migrar de este Excel a la plataforma nueva es tarea declarada pendiente ("hay que evangelizar las próximas semanas").

**Filtro por formato (cluster / discounter / cash & carry)** `[F16]`
En la plataforma nueva, el mercado puede abrirse por **cluster**, por **discounter** y por **cash & carry**, además de por supermercado — aperturas que el *Excel semanal* (arriba) todavía no ofrece.

**Mi Portal** `[F18]`
Sistema de Planificación Promocional donde se cargan y gestionan las promociones — incluye la carga de precios. Genera un **número de solicitud** propio por cada proceso.
⚠️ **No confundir número de solicitud con SPF** (ver abajo): son dos códigos distintos para la misma promoción, de dos sistemas distintos.

**SPF** `[F6]` `[F18]`
Código relacionado a la promoción que aparece en la data de GCP. Lo genera el equipo de **Precios / Ejecución Promocional** una vez que Mi Portal envía la promoción a programar — es un código de ejecución, no el número de solicitud de Mi Portal.

**Archivos y herramientas del área** `[F6]`
Plataforma: GCP · BigQuery · Looker Studio · Databricks. Herramientas de uso frecuente: Huaycos, CRONO, CYBERS, SPF, Medios, Cronogramas, Google Cloud Console, Enterprise Data Platform, Sharepoint Salesrun.
Carpeta adicional identificada `[F18]`: Planificación Promocional mantiene su propia carpeta en **Teams**, donde archiva todos los consolidados y Excels ya enviados a Operaciones/tiendas — fuente directa de los archivos de ruta crítica de Táctico y HS.
Archivos fuente citados en este documento: `Data_Resultados (Categorías) Marcas Propias.xlsx` (F7), `Data_Resultados Marcas Propias.xlsx` / bases de lanzamiento (F8), `RUTA CRITICA 2025.xlsx` (F11), `Campañas Core '25.xlsx` (F13), `Campaña Navideña.xlsx` (F14), consolidados `CONSOLIDADO_FINAL_AREAS_HS##-A/B.xlsx` (F10).
⚠️ Las carpetas compartidas heredadas de Mirella son enlaces de invitado sobre su OneDrive personal — pedir copia propia o mover a ubicación de equipo antes de que caduquen a mitad de campaña.

---

## 16. ScanView — manual operativo `[F1]`

Todo lo procedimental de la plataforma. El resto del glosario define los términos; esta sección dice **dónde hacer clic y en qué orden**.

### 16.1 El modelo Scanntech

Tres pasos: **(1) Ingesta** — Tottus envía su data transaccional por API. **(2) Procesamiento** — Scanntech la devuelve convertida en KPIs y drivers ya calculados. **(3) Monetización** — Scanntech comparte data con proveedores; **Tottus decide con quién, por cuánto tiempo y qué información**, y eso trae inversión del proveedor a la cadena.

Tottus es la **primera conexión de Perú** y el primer supermercado del país en incorporar Scanntech. El roadmap declarado (~6 meses desde Set-2026) es conectar otros retailers peruanos; al ocurrir se habilitan las vistas de **mercado**: share vs. competencia, price index real y cobertura de surtido comparada.

Scanntech tiene **6 soluciones**; Tottus usa hoy una: **ScanView** (también llamada *Cambio Retail*).

### 16.2 Acceso y soporte

```
Scanntech → Perú → Desarrollo → Red Tottus → "Tottus Dashboard Grupos 9.1"
```

Los usuarios del equipo comercial ya están creados. Soporte presencial del KAM en oficinas Tottus **martes y jueves, 9:00–18:00**; también por WhatsApp o correo para agendar revisiones por categoría.

### 16.3 Las 5 hojas

| # | Hoja | Pregunta que responde | Granularidad | Nivel |
|---|---|---|---|---|
| 1 | **Categoría** | ¿Cómo performa mi surtido dentro del árbol? | Mes cerrado | Mundo → División → Subdepartamento → Clase → Subclase → SKU |
| 2 | **Negociación** | ¿Cómo performan mis proveedores y marcas? | Mes cerrado | Fabricante → Marca → Jerarquía → SKU |
| 3 | **Tabla de Precios** | ¿Cómo se comporta el precio? | **Semanal** | SKU |
| 4 | **Ejecutivo** | ¿Cómo va la compañía a nivel macro? | Mes cerrado + histórico | Compañía / Bandera |
| 5 | **Operacional** | ¿Cómo performa cada tienda? | Mes cerrado + histórico | Tienda |

### 16.4 Panel de filtros

Casi todos se repiten hoja a hoja.

| Filtro | Opciones |
|---|---|
| **Tipo de venta** | Venta total · Venta Same Store |
| **Ponderación** | Ventas totales · no ponderadas |
| **Métrica** | Valor (soles) · Unidades |
| **Fechas** | Personalizado · último mes cerrado · mes vs. mismo mes AP. Admite **multiselección de meses** para estacionalidades móviles (Semana Santa) |
| **Estructura mercadológica** | El árbol interno de Tottus (ver sección 1) |
| **Fabricante / Proveedor** | Búsqueda y selección. Se **desmarca el check** para bajar a nivel marca |
| **Marca** | Búsqueda y selección |
| **Códigos de barras** | Se pega una lista de **EAN** y toda la data se acota a esos SKUs |
| **Ordenar por** | Alfabético · **Representatividad** |
| **Bandera** | Tottus · Precio Uno · Ecommerce (o total) |
| **Zonas** | Lima (Norte, Moderna, Sur) · Provincia · Oriente/Iquitos |
| **Top fabricantes** | Solo en Negociación; por defecto top 10 |
| **Mercado** | Aún no disponible en Perú |

⚠️ **Trampa:** si el surtido está repartido por bandera (ej. pastelería va con marca Tottus en Tottus y con marca propia en Precio Uno), hay que **quitar el filtro de la bandera que no corresponde** o el `% PDV` sale sucio: cuenta locales donde ese SKU nunca se comercializó.

**Funciones transversales:** guardar **vista personalizada** con nombre y fijarla como predeterminada · volver a la **vista original** · descarga a Excel por **tabulación cruzada** · botón de retroceso para subir de nivel sin rehacer filtros.

### 16.5 Qué se ve en cada hoja

**Categoría.** Por nivel de jerarquía: facturación, % de representatividad y % de variación vs. período base. Drill-down por clic hasta el botón de detalle SKU. La **vista SKU** trae: share dentro de su subclase, rotación unitaria, % var. de rotación por tienda, precio medio y su variación, **% PDV**, % var. de puntos de venta y share del proveedor. La gráfica lateral muestra el evolutivo de **venta media por tienda** del nivel seleccionado — es donde se lee tendencia y estacionalidad.

**Negociación.** Ranking de fabricantes por representatividad dentro de las divisiones seleccionadas (el top 10 concentra ~60% del negocio). Al seleccionar un proveedor: su performance por J / subdepartamento / clase / subclase, su **share y la variación de ese share**, su histórico de venta media por tienda y el ranking de sus productos. Es la hoja para preparar una negociación con datos.

**Tabla de Precios.** La única con corte **semanal**. Por SKU: proveedor, marca, ubicación en el árbol, **precio mínimo / medio / moda / máximo**, curva ABC como ordenamiento, rotación unitaria y % PDV. Sirve para detectar dispersión o desfase de precio y escalarlo a Pricing.

**Ejecutivo.** Venta total en soles y unidades, con variación vs. mes anterior y vs. AP; apertura por bandera con la contribución de cada una; KPIs de compañía (flujo en tienda, ticket medio, unidades por ticket, venta media, price index); evolutivo de venta media por tienda.
⚠️ Probablemente la misma hoja que una segunda fuente `[F17]` nombra **"Reporte Transaccional"**: describe el mismo set de variaciones (venta SI, GPE diferencial, unidades, precio medio, unidades por transacción, ticket promedio, transaccional), cargado a **cierre de mes** (a diferencia de otras vistas con corte diario), abierto por Tottus + Precio Uno. *Por confirmar* si es un nombre alternativo de Ejecutivo o una vista distinta.

**Operacional.** Listado de tiendas catalogadas por bandera — solo puntos de venta, sin almacenes ni centros que no venden. Cajas por tienda como proxy de tamaño, mapa de calor de aperturas y cierres, y el cuadro de performance por tienda (variación en valor y unidades, importancia para el grupo, tickets, venta media por ticket, unidades por ticket). Ordenable por representatividad o por tamaño.

### 16.6 Rutina de trabajo recomendada

1. **Ejecutivo** → contexto: ¿la compañía crece o se contrae? ¿por bandera? ¿el driver fue tráfico, ticket o unidades por ticket?
2. **Categoría** → ¿mi mundo/división pasa la valla de la compañía? Bajar hasta el subdepartamento o subclase que la rompe.
3. **SKU** → los que caen en rotación y los que tienen `% PDV < 100%`. Cuantificar la **venta perdida**.
4. **Negociación** → atribuir: ¿la caída es de un proveedor o marca concreta? ¿su share cae? Llevar el número a la mesa.
5. **Tabla de Precios** → ¿hay dispersión o desfase detrás de la caída de rotación? Escalar a Pricing.
6. **Operacional** → ¿es transversal o de un cluster de tiendas / estacionalidad?
7. Guardar cada análisis recurrente como **vista personalizada** con nombre.

### 16.7 Limitaciones declaradas

| Tema | Estado |
|---|---|
| **Quiebres** | **No hay data directa.** El `% PDV` es el proxy: dice dónde el SKU facturó, no si estaba activo, ni en qué tienda falló. Contrastar con la data interna de productos activos |
| **Pesables / a granel** | Sin marca ni proveedor; aparecen como **genéricos**. En desarrollo |
| **Marca propia** | Agrupada como fabricante "Hipermercados Tottus" |
| **Data de mercado** | No disponible en Perú hasta que se conecten otros retailers |
| **Mes en curso** | Llega incompleta: analizar sobre el último **mes cerrado** |
| **Envío automático por correo** | **No existe.** La alternativa es la vista personalizada guardada como predeterminada |

---

## 17. Entregables del puesto `[F6]` `[F12]`

Los dos entregables recurrentes que produce Inteligencia Comercial. En ambos, la base de venta la entrega **Dani** (ver sección 14); el trabajo propio es estructurar, calcular, interpretar y redactar.

**Especial de Marcas Propias** `[F12]`
Lámina de resultados de marca propia, copiada como **imagen** al chat del equipo comercial. Cadencia: **tres cortes por campaña**, dos los lunes y el cierre el jueves posterior al fin de la ventana.
Filtro declarado en la plantilla: **Tottus + Online, sin Izaguirre**, corte **SSS**, fechas según el corte. Pie de página fijo: *"Considera las Banderas de Tottus y Online | Total Tottus de J1 a J11 | Total Food de J1 a J7 | Campaña Especial MMPP abarca solo los productos participantes."*

Los seis cortes de la lámina, de lo general a lo estratégico:

| # | Corte | Definición |
|---|---|---|
| 1 | Total Tottus (Food + Non-Food) | J1 a J11 |
| 2 | Total Food | J1 a J7 |
| 3 | Total MMPP Food | Marca propia de J1, J2, J5 |
| 4 | Campaña "Especial MMPP" | SKU de marca propia que participan en el HS y los tácticos de la ventana |
| 5 | Resto MMPP Food | Marca propia que no está en campaña |
| 6 | Otras Marcas Food | Terceros de J1, J2, J5 |

⚠️ **El corte 5 es el que da la lectura de valor.** Si "Campaña MMPP" crece y "Resto MMPP" no, el crecimiento es atribuible al impulso promocional, no a una tendencia de la marca.
⚠️ **El corte 6 solo es comparable dentro de las mismas divisiones.** Comparar MMPP contra el total de marcas de proveedor de toda la cadena es comparar peras con manzanas.

Cinco métricas por corte, con variación vs. mismos días AP: Venta Soles (abierta en Piso y Online), Venta UND, TRX, Ticket Promedio, UND × TRX.

Segunda lámina de la plantilla: el **Cheat Sheet** — el cronograma de la campaña en formato calendario de 14 días, con la mecánica que corre cada día. Mantenerlo actualizado corte a corte es lo que evita que el tercer envío compare contra una ventana distinta del primero.

⚠️ **Errores conocidos de la plantilla:** el Cheat Sheet arrastra el número de campaña de la edición anterior si no se actualiza a mano · el desfase del ticket promedio ya documentado en *Venta SI* (sección 2) también aparece aquí · la exclusión de Izaguirre es la convención estándar para tiendas de prueba, no un error (ver *% variación de puntos de venta*, sección 9) · el corte de MMPP en J1/J2/J5 es el universo de este entregable puntual — no un límite oficial de dónde existe marca propia (ver *Marca propia / MMPP*, sección 1).

**Boletín de Marketing — bloque de campañas** `[F12]`
Resumen mensual de acciones promocionales con foco en cuánto incremental generó cada campaña. Denisse arma el boletín; Inteligencia Comercial aporta el bloque de resultados. **El entregable es un correo con bullets**, no un Excel ni una presentación — sube al CEO.

Universo por campaña, hoja `Detalle Deals` de la plantilla `Boletín MKT [Mes] - Campañas Especiales.xlsx` (ejemplo agosto):

| Campaña | Vigencia | Cómo se define el universo | Días |
|---|---|---|---|
| Especial Café | 20 ago – 02 set | Por código de clase (`J01010702`) | 14 |
| Especial Belleza | 20 ago – 02 set | Por lista de SKU asociados a cada deal | 14 |
| Multimarca | 23 ago – 30 ago | Por códigos de división, J1 a J6 completas | 8 |

⚠️ **Las tres no son comparables entre sí.** Multimarca abarca seis divisiones completas — su "venta de campaña" es casi la venta de la tienda —, mientras Café y Belleza tienen surtido acotado; y las vigencias difieren, 14 días contra 8. La plantilla lo advierte en la fila `Nota surtido`; conviene subir esa advertencia al cuerpo del correo.

Once filas de KPI por campaña, siempre vs. mismos días AP: Venta SI, Var% vs AP, Dif. AP, UND, Var% UND, TRX, Var% TRX, Dif. TRX, Ticket Promedio, Var% Ticket, UND × TRX.
⚠️ Las tres bases del boletín (`BD_Compacta`, `BD_División`, `BD_Marca`) traen **`GPE`** y la hoja de KPIs no lo usa. El boletín va al CEO y no dice cuánto margen dejó la campaña — agregar la fila no cuesta nada porque el dato ya está (ver *GP%*, sección 5).

Estructura del correo: **Objetivo de la campaña** (validar con la brand manager) → **Resultados resaltantes** → **Impacto en el negocio**. Nivel de desagregación esperado: no basta el total por campaña — ejemplo real, *"el flujo de clientes creció en Multimarca, pero al abrir por división la J5 fue la que más aportó"*.

---

## Anexo A — Cifras de referencia

Valores puntuales recogidos de las fuentes. **Sirven como orden de magnitud, no como dato vigente**: cada uno lleva su corte temporal.

### Escala del negocio — Agosto 2026 `[F4]`

| Métrica | Total (TT+PU+Online) | Tottus |
|---|---|---|
| Venta | S/485.8 MM (+9.2%) | S/369.0 MM (+7.8%) |
| Logro% | 101.0% | ~101.9% |
| GPE | — | S/62.0 MM (16.8%, +0.8 p.p.) |
| TRX | — | 5.6 MM (+8.8%) |
| Ticket promedio | — | S/77.0 (−0.9%) |
| Unid/Trx | — | 6.3 (−1.2%) |

Crecimiento por canal: Tottus +7.8% · Precio Uno +11.7% · Online +20.3%.

### Mercado — Semana 34, 2026 `[F4]`

| | 2025 | YTD26 | S34 |
|---|---|---|---|
| **TSS** Mercado | 5.8% | 8.8% | 12.6% |
| **TSS** Tottus | 4.5% | 10.5% | 12.1% |
| **SSS** Mercado | 2.3% | 6.8% | 9.5% |
| **SSS** Tottus | 3.7% | 8.6% | 10.7% |

### Escala promocional del HS — Set 2025 `[F2]`

| | Valor | Capacity |
|---|---|---|
| SKUs por HS | ~5,700 | — |
| Llamados por HS | ~2,493 | — |
| Cartelería por HS | ~773 | **400** (visual) |
| Flejes por HS | ~5,700 | **1,100** (operaciones) |
| Efectividad promocional | 55.4% | — |
| Promocionalidad | ~79% | — |
| Arriendos en la cadena | 11,272 (194/tienda) | — |

Crecimiento Ene→Set 2025: SKUs **+53%** · Llamados **+68%** · Cartelería **+150%**.

### Red de tiendas y concentración — Jul 2026 `[F1]`

| Métrica | Valor |
|---|---|
| Tiendas en la red | ~103–105 puntos de venta |
| Cajas por tienda (promedio) | ~16 |
| Concentración de proveedores | El **top 10 concentra ~60%** del negocio |
| Tienda más representativa | Trujillo 1 — 1.37% del negocio, ~228 K tickets, ticket medio ~S/88 |

⚠️ Más tráfico no es más venta: Megaplaza hacía ~60 K tickets más que Trujillo 1 con ticket medio de S/66.4 y caía −4.8%.

### Competitividad de precio — S34 2026 `[F4]`

IPC físico SKVI Food: **U6S 98.5% / US 98.0%**. Distribución de la venta SKVI: 48% con IPC <99% · 15% entre 99–100% · 21% >100% · **16% >105%**.

### Lanzamientos MMPP — rendimiento y cruce con campaña — Ago 2026 `[F7]` `[F8]` `[F10]`

| Indicador | Con panetón | Sin panetón |
|---|---|---|
| Share Venta SI de MMPP | 14.2% (−2.1 p.p.) | 13.7% (−2.0 p.p.) |
| Share en Precio Uno | **23.5% (+0.5 p.p.)** | 23.0% (+0.6 p.p.) |
| Share en Tottus | 11.8% (−2.8 p.p.) | 11.2% (−2.7 p.p.) |
| Lanzamientos últimos 2 años / Total MMPP | 15.3% | 16.0% |
| — en Online | **10.5%** | 10.5% |
| — en Piso (Tottus) | 15.3% | 16.3% |

⚠️ **Precio Uno es la única bandera que gana share de marca propia** (+0.5 p.p.) mientras Tottus cae (−2.8 p.p.): la caída de MMPP a nivel compañía es un fenómeno de la bandera Tottus, no del formato de descuento — abrir siempre por bandera antes de concluir a nivel total.
⚠️ **Los lanzamientos rinden ~5 p.p. menos en Online que en piso**, y es el único indicador que no mejora al quitar panetón. Sin explicación confirmada.

Cruce lanzamientos × campaña, HS18-A `[F8]` `[F10]`: de los 693 SKU de marca propia en campaña, **170 (24.5%) son lanzamientos recientes** — 101 lanzados en 2026, 69 en 2024–2025 (incluye 17 SKU de Xplend). **Uno de cada cuatro SKU de marca propia en campaña es un lanzamiento reciente:** el hard sell no es solo palanca de volumen, es vehículo de soporte de lanzamientos. Separar "MMPP lanzamiento reciente" de "MMPP portafolio establecido" en el reporte de campaña responde si la promoción empuja lo nuevo o defiende lo viejo.

### Market Share PE — Semana 35, 2026 (24–30 ago) `[F15]`

**Piso de venta, Negocio (Tottus + Precio Uno) vs. Resto Mercado:**

| | TSS | SSS |
|---|---|---|
| Crecimiento semanal | +1.3% (−3.7 p.p. vs Resto Mercado) | −0.3% (−3.1 p.p. vs Resto Mercado) |
| Share semanal | 32.1% (−0.8 p.p. vs AP) | 32.2% (−0.7 p.p. vs AP) |
| Crecimiento YTD | +9.9% (+3.2 p.p. vs Resto Mercado, que creció +6.7%) | +8.5% (+2.8 p.p. vs Resto Mercado, que creció +5.7%) |
| Share YTD | 32.8% (+0.6 p.p. vs AP) | 32.9% (+0.6 p.p. vs AP) |

Por bandera (TSS semanal): **Tottus** +0.4% vs AP (−4.6 p.p. vs Resto Mercado) · **Precio Uno** +5.1% vs AP (+0.1 p.p. vs Resto Mercado) — la misma lectura que en marca propia (Anexo A, arriba): **Precio Uno gana terreno frente al mercado; Tottus lo pierde.**

**E-Commerce:** Mshare 26.2% (−2.0 p.p. vs AP), creciendo +17% (−12.3 p.p. vs Resto Mercado). Abierto en Tottus Internet (8.6%, −0.9 p.p.) y Tottus App (17.6%, −1.1 p.p.). Por mundo: Food 25.7% share (+10% crecimiento, −5.3 p.p. vs Resto Mercado) · Non Food 27.1% share (+29.2% crecimiento, −31.2 p.p. vs Resto Mercado — la brecha más grande de todo el reporte).

**Por mundo (piso de venta, TSS), semanal → YTD:**

| Mundo | Peso en Tottus | Share semanal | vs AP | Share YTD | vs AP |
|---|---|---|---|---|---|
| PGC | 49.4% | 31.2% | −1.5 p.p. | 31.8% | +0.6 p.p. |
| Perecibles | 22.7% | 26.8% | +0.4 p.p. | 26.6% | +0.9 p.p. |
| Non Food | 27.9% | 40.5% | −0.2 p.p. | 41.6% | +0.7 p.p. |

⚠️ Consistente con la caída de PGC arriba: PGC es el único mundo que cae vs AP tanto semanal como (menos) en YTD, y el que más pesa en el negocio (49.4%) — es el que más explica la caída de share total.

**Categorías destacadas (piso de venta, semanal, vs AP en p.p.):** suben con fuerza *Cepillos Dentales* (+7.3 p.p.), *Cremas y Lociones* (+5.3 p.p.), *Azúcar* (+3.7 p.p.), *Yogurt* (+1.6 p.p.), *Línea Blanca* (+3.4 p.p.). Caen con fuerza *Whisky* (−24.4 p.p.), *Aceites Vegetales* (−12.1 p.p.), *Carnes Otras Aves* (−30.8 p.p.), *Decoración del Hogar* (−12.1 p.p.), *Gaseosas* (−4.1 p.p.).

⚠️ **La taxonomía de este reporte no es la de las divisiones J** (ver *Share de mercado / Mshare*, sección 10) — antes de cruzar una de estas categorías con una división J propia, mapear a mano.

---

## Anexo B — Trampas de lectura conocidas

Errores recurrentes detectados al revisar F2, F3 y F4. Checklist antes de firmar un análisis o un slide.

1. **Declarar la base de toda métrica compuesta.** Efectividad por SKU ≠ por llamado. Promo share vs Total PU ≠ vs Total Food. Venta SI ≠ venta con IGV: `TRX × Ticket` no reproduce la venta neta.
2. **No mezclar SSS y TSS, ni comercial y gregoriano, en la misma lectura** sin señalarlo. Pueden dar conclusiones opuestas sobre el mismo mes.
3. **Fijar una sola definición de "período regular"** y repetirla en cada slide que la use.
4. **Etiquetar lo proyectado.** Un dato de cierre estimado al lado de uno real, sin etiqueta, se lee como real.
5. **Verificar el driver antes de escribir el titular.** Si el ticket y las unidades por ticket caen, el crecimiento fue tráfico — no se puede titular "ticket más alto".
6. **Comparar contra el período regular, no solo contra AP.** Una campaña puede crecer vs. el año pasado y aun así vender menos y con menos margen que una quincena normal.
7. **Descomponer el incremental en Mantiene / Nuevo / Salieron / No Promo** antes de declarar que una campaña funcionó.
8. **Cruzar Logro% con crecimiento.** Si divergen dos períodos seguidos, el diagnóstico es sobre el plan, no sobre la categoría.
9. **Los porcentajes de tres dígitos delatan un plan mal puesto**, no un desempeño extraordinario. Y un % calculado sobre una base negativa no es interpretable.
10. **Un promedio de índice esconde la dispersión.** IPC 98.0 puede convivir con un tercio de la venta por encima de la competencia.
11. **Revisar que las filas sumen 100%** en tablas de composición, y que los subtotales sumen al total (piso + online = venta total).
12. **Rojo/verde debe seguir el desempeño, no el formato ni la categoría.** Una barra roja que crece al doble del mercado se lee como problema.
13. **Rankear por cumplimiento premia metas bajas.** Un ranking de tiendas por %meta ordena la calidad de las metas, no el desempeño. Mostrar el volumen al lado.
14. **Nombrar bien la categoría en crisis.** Antes de titular sobre una categoría, abrir por clase: en el caso Colchones, colchones crecía +10% y lo que caía −21% era Juego de Dormitorio.
15. **Purgar notas al pie heredadas.** Las fuentes revisadas arrastraban notas de campañas anteriores ("Lucas I", "AP Jarana", fechas de otra edición) que invalidan la metodología declarada.
16. **Vigilar el efecto base.** Un crecimiento de +11,735% sobre una base de S/5,988 no es un crecimiento; es un arranque.
17. **"Medir más" no es "vender más".** Una campaña sin filtro de categoría (Aniversario) siempre se ve más grande que una con surtido acotado (Navidad, Café, Belleza) aunque el negocio real sea comparable — declarar el universo antes de comparar el tamaño de dos campañas.
18. **Ejecutar el surtido completo no garantiza recuperar el share.** Un relanzamiento puede completar todas sus tandas de SKU y aun así no volver al nivel de participación previo — ver Anexo C, caso Xplend.
19. **No dar por perdida una categoría de identidad de marca sin revisar ejecución.** La marca propia puede ganar incluso en categorías de tradición y regalo si precio, exhibición masiva y confianza en la marca del retailer se alinean — ver Anexo C, caso Panetón.
20. **Una tabla de SKU por segmentación puede sumar más que el total de SKU únicos.** Si un mismo SKU vive en más de un llamado o más de una segmentación dentro de la campaña, la suma por categoría no es el universo — usar el total de SKU únicos declarado aparte, nunca la suma de la tabla abierta.

---

## Anexo C — Casos de referencia `[F7]`

Cinco casos de marca propia que conviene tener en la cabeza. Vienen de láminas del deck, no de recálculo propio: se marcan 🟡 salvo donde se indique lo contrario.

### Huevos Frescos — dominancia con margen negativo 🟡
MMPP tiene **69.8%** de la categoría, la participación más alta de todo el portafolio, con **GP% de −5.7%**. El tercero se queda con 30.2% a **37.7%** de GP%. Y MMPP cae −16.1% mientras el tercero crece +29.8%. Tottus domina la categoría con marca propia y pierde dinero haciéndolo — el caso más extremo del portafolio, sin lámina propia en el deck.

### Higiene Personal — la rentabilidad donde no hay presencia 🟡
Único subdepartamento donde MMPP **gana** en GP%: 46.0% contra 36.6% del tercero. Y es donde menos presencia tiene: 6.6% de la categoría, cayendo −18.8%. La categoría donde la marca propia es más rentable es donde menos está — es una oportunidad, no un problema.

### Panetón — el contraejemplo a la tesis estructural ✅
Navidad 2025, categoría Panetón (48.8% de toda la campaña navideña — ver *Categoría campañera*, sección 6):

| Marca | Venta '25 | %Pp | Var% vs AP |
|---|---|---|---|
| **TOTTUS** | S/66.1 MM | **66.1%** | **+20.5%** |
| Donofrio | S/9.8 MM | 9.8% | +18.5% |
| **PRECIO UNO** | S/7.3 MM | 7.3% | **−8.7%** |
| Blanca Flor | S/3.8 MM | 3.8% | +52.5% |
| Gloria | S/3.7 MM | 3.7% | +20.6% |

Marca propia tiene el **73.4%** de panetón (Tottus + Precio Uno), y Tottus crece por encima de Donofrio. Hipótesis: categoría estacional de compra múltiple donde el precio pesa, el retailer controla la exhibición masiva (rumas) y la marca del retailer transfiere confianza en un producto de calidad verificable — si es la explicación correcta, es replicable a otras categorías.
⚠️ **Punto ciego:** Precio Uno es la única marca de la tabla que cae, −8.7%. Canibalización de Tottus o problema de surtido en Hiperbodega, sin resolver. Llega a tiempo para Navidad '26.

### Xplend — un relanzamiento que perdió share 🟡
Detergentes y Suavizante Tottus, semanas 9 a 34 de 2026. La venta semanal sube de 7 a un pico de 180 según entran las tandas de SKU (polvo → líquido botella floral → líquido Ultra → suavizante floral → polvo 8kg → doypacks): la sustitución de portafolio funcionó. **El share no:** estable en 12–13% en 2025, arrancó en 7–8% en 2026 y después de 26 semanas y ocho tandas de SKU sigue en 9–11%. Nunca recuperó el nivel previo. Ver Anexo B #18.

### Papas Fritas — quiebre estructural sin recuperación 🟡
Caída de ~10 p.p. de share MMPP en la semana 15 que nunca se recuperó, mientras el perímetro MMPP+Proveedor se mantuvo estable: el proveedor absorbió la pérdida de MMPP por sustitución dentro de la misma góndola.

**La tesis y sus límites:** la marca propia funciona en categorías commodity de bajo riesgo percibido (arroz, aceite, leche, enlatados) y sufre en categorías de alta identidad de marca — con **Panetón como contraejemplo directo**. Antes de declarar una categoría estructuralmente inadecuada para marca propia, diagnosticar disponibilidad, ejecución en tienda y propuesta de valor: Xplend demuestra que se puede perder share con el surtido completo ejecutado.

---

## Términos por incorporar (pendientes de fuente)

Espacio de trabajo para el próximo aporte:

- [ ] Definiciones oficiales Tottus de cada J (mapeo completo J1–J12, más J99 y JSJ)
- [ ] Ejemplos de **Departamento** (nivel 3) por división — el nivel está confirmado, faltan casos concretos
- [ ] Expansión confirmada de siglas: **MV** (arriendo prioritario), **FQ** (quiebre), **MDV** y **RT** (POP), **Fcom**, **KVC**, **H-E-L** (semaforización IPC), **LW** (logística de proveedor) — origen no identificado por el usuario; confirmar contra quien mantenga cada documento fuente (F2/F4), no es conocimiento que dependa de Gabriel
- [ ] Definición formal de **Básico 1 / Básico 2** y de **surtido troncal**
- [ ] Criterio de selección de **Focals**
- [ ] Métricas de rentabilidad complementarias: margen de contribución formal, GMROI
- [ ] Terminología de espacio: planograma, facing, share de góndola
- [ ] Métricas de e-commerce: conversión, ticket digital, sustitución, picking, peso objetivo de web
- [ ] Metodología **A&M** de medición de quiebre — definición y alcance
- [ ] Definición operativa de **capacity operativo** de tienda (declarada "en definición" en F2)
- [ ] Umbrales oficiales de la matriz de efectividad (qué separa Estrella de Bajo Impacto)
- [ ] Conteo exacto de SKU de `FRESH` y si hay lista maestra oficial de marca propia que lo resuelva
- [ ] Diccionario completo de códigos de espacio en tienda del consolidado (`RC`, `CM`, `CSL`, `CMY`, `RL`, `HC1`, `AL2`, `CPC`, `CSF`, `CME` — `C` y `R` ya se identifican como Cabecera y Ruma)
- [ ] Qué distingue `REEMPLAZO FÓRMULA` de `REEMPLAZO OTROS` en lanzamientos, y quién es dueño del pipeline
- [ ] Cuántas semanas definen cada etapa Pre-Lanzamiento / Lanzamiento / Post
- [ ] Por qué los lanzamientos rinden ~5 p.p. menos en Online que en piso
- [ ] Diccionario de nombres: mapeo entre la taxonomía de categorías de *Market Share PE* (Comestibles, Cuidado del Hogar…) y las divisiones J internas
- [ ] Nombre real del proveedor transcrito como **"Lock"** (sección 14) y de su contacto ("Swan"/"Juan") — confirmado que es un proveedor de terceros distinto de L&A; sigue sin identidad real
- [ ] Apellidos de **Helen** y **Jacob**, contactos de GfK (sección 14)
- [ ] Alcance exacto del paso de Kantar Panel a **Numerator** (sección 14)
- [ ] Si Tottus tiene acceso hoy a **Discover** y a **Radar/Active** (sección 15), o si sigue dependiendo del Excel semanal
- [ ] Set completo de KPIs que cruza la **Matriz de surtido en mix** (sección 1) — confirmado su alcance general, falta el detalle
- [ ] Confirmar condiciones de pago a proveedor por categoría (sección 1) contra la política oficial de Finanzas
- [ ] Roles exactos de **Hugo**, **Hans**, **Mire** y **Alan** (sección 14) — leídos del contexto, no confirmados
- [ ] Si "Reporte Transaccional" (sección 16, hoja Ejecutivo) es un nombre alternativo de esa hoja o una vista distinta
- [ ] Nombre y alcance final del framework de "revisión profunda de categoría" (sección 13) una vez formalizado — y si migra a la sección 17
- [ ] Si el "Dani" del equipo de Planificación Promocional (sección 14, `[F18]`) es un homónimo distinto de Daniel (equipo de Gabriel) o la misma persona — discrepancia sin resolver entre F5 y F18
- [ ] Desglose completo de hitos intermedios de la ruta crítica de Táctico según Planificación Promocional (sección 13, `[F18]`) — hoy solo se tiene el rango −40 a día 0

---

*Última actualización: fuentes F1–F15 incorporadas. F2 (Estrategia HS), F3 (Chapa Tu Yapa II) y F4 (Comité Comercial S36) aportaron las secciones 5 a 13, los anexos A y B, y enriquecieron las secciones 1 a 4 y 9 a 11. F5 (correcciones del usuario) corrigió el árbol mercadológico a 6 niveles, con Departamento y Clase como niveles propios, y la notación de las divisiones sin cero a la izquierda. La sección 16 consolida el manual operativo de ScanView. F6–F14 (traspaso de Mirella, bases y deck de marca propia, bases y deck de lanzamientos, deck regional de lanzamientos, consolidados de campaña HS18+T36, ruta crítica 2025, plantillas de los dos entregables, y los archivos de Campañas Core y Navideña) enriquecieron la sección 1 (marca propia y lanzamientos), la sección 5 (GP% y PROFIT), la sección 6 (vigencias, arriendos, campañas core y Navidad), la sección 13 (segunda versión de la ruta crítica) y las secciones 14 y 15 (personas, archivos y herramientas); aportaron la sección 17 (entregables del puesto) y el Anexo C (cinco casos de marca propia). F15 (*Market Share PE*, S35 2026) aportó el primer detalle de mercado externo con este nivel de apertura: enriqueció "Share de mercado" y "Peso Mercado vs. Peso TT" (sección 9-10) y sumó un bloque nuevo al Anexo A. F16 (grabación de capacitación, transcripción automática con ruido en nombres propios) sumó la subsección "Proveedores de data de mercado" en la sección 14 (Kantar, Nielsen, GfK y otros, varios marcados por confirmar), las herramientas Discover/Radar/Excel semanal en la sección 15, y precisó la fórmula de Market Share (Grupo Tottus = Tottus + Precio Uno) en la sección 10. F17 (segunda grabación, mismo tipo de fuente) aportó la metodología Nuevo/Existe/Deslistado y la Matriz de surtido en mix (sección 1), la distinción de agregabilidad transacción vs. cliente (sección 3), las dos causas de variación del precio medio y los tiers de precio (sección 4), la lógica de negocio por mundo Abarrotes/Perecibles/No Food (sección 1), el chequeo de coherencia Supermarket-vs-Excel y la apertura zonal del mercado (sección 10), el framework en diseño de revisión profunda de categoría (sección 13), varios contactos nuevos (sección 14) y una nota de correspondencia con la hoja Ejecutivo de ScanView (sección 16). Segunda ronda de correcciones directas del usuario (`[F5]`) sobre F16/F17 y sobre fuentes previas: "Escatec" y "Scarpe" son ambas Scanntech mal transcrito (se fusionaron); "Lock" es un proveedor de terceros distinto de L&A, con nombre real aún sin identificar; el contacto "Paolo" es de Scanntech, no de Kantar; los tiers de precio quedaron confirmados, especialmente útiles en Abarrotes; la Matriz de surtido en mix cruza varios KPIs (no solo Nuevo/Existe/Deslistado) comparando mercado/competencia contra el surtido propio; Daniela/Yani quedaron identificadas como Daniela Montoya y Yami (Yamile); "Dani" es Daniel, del equipo de Gabriel, y es una persona distinta de Daniela Aste (Brand Manager, antes mal escrita "Astep"); `PROFIT` (sección 5) se confirma que es simplemente el margen, sin fórmula más granular; el vacío en `Tipo` (sección 6) y el aporte comercial por punto de share de MMPP (sección 5) no tienen una regla oficial que perseguir; Izaguirre (sección 9) es una tienda de pruebas, excluida por convención; marca propia puede existir en cualquier división, no solo J1/J2/J5 (sección 1); el calendario de Ruta Crítica vigente es siempre el más reciente (F4 sobre F11, sección 13); *Market Share PE* (F15) se confirma como el reporte de L&A (sección 4); y ante una discrepancia de Lima entre F4 y F15, se le da más peso a F4 (sección 9-10). F18 (reunión con Carla Teresa Flores Otoya, Planificación Promocional, 10-Set-2026) aportó la relación Táctico↔HS y la variante Perecibles del Táctico (sección 6.1), el vehículo Flash y el principio de campañas con/sin arriendos (sección 6.1), la desambiguación de Golpe A/Golpe B según vehículo (sección 6.4), ejemplos concretos de Llamado y Punto precio (sección 6.2), la trampa de la columna "Categoría" (nombre comercial, no jerarquía) en la sección 1, el sistema Mi Portal/SPF y la carpeta de Teams del área (sección 15), una tercera versión sin reconciliar de la ruta crítica del Táctico (sección 13), y una discrepancia sin resolver sobre si "Dani" es una sola persona o dos homónimos (sección 14). El rastreador de pendientes con fecha vive aparte, en `PENDIENTES.md` — no es contenido de glosario y se reemplaza en cada ciclo.*
