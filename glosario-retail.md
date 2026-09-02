# Glosario de Retail — Inteligencia Comercial

Glosario vivo para el puesto de **Especialista en Inteligencia Comercial (Tottus)**.
Se construye por acumulación: cada capacitación, reunión o documento que aporte terminología se registra como **fuente** y sus términos se incorporan aquí.

**Convenciones:**
- Cada entrada indica `[F1]`, `[F2]`, … según la fuente donde apareció. Si un término aparece en varias, se listan todas.
- Los términos marcados `[base]` son de uso estándar en retail y se incluyen como complemento de contexto, no provienen de una fuente registrada.
- Los términos marcados `⚠️ por confirmar` aparecieron en una fuente sin definición explícita; el significado anotado es una lectura del contexto y **debe validarse con el área dueña** antes de usarse en un entregable.
- Cuando un término tiene un significado **específico dentro de una herramienta**, se anota bajo *"En ScanView"* o similar.

---

## Registro de fuentes

| ID | Fuente | Tipo | Fecha | Nota |
|---|---|---|---|---|
| **F1** | Capacitación Comercial Scanntech — "Nueva plataforma tecnológica en retail" (Paolo Gaspar, KAM Scanntech) | Capacitación grabada, ~1h30 | Sep 2026 | 6ª sesión de la ronda al equipo comercial Tottus. Ver `scanntech-scanview-guia.md` |
| **F2** | *Impulso+: Análisis y Estrategia de HS* | Presentación de trabajo, 110 slides | Oct–Nov 2025 | Acumulado de 5 sesiones de diseño de la política promocional de Hardsell. Portada fechada Oct-2025; el contenido llega al 13-Nov. Incluye anexo regional (PE/CL) |
| **F3** | *Chapa Tu Yapa II — Julio* | Presentación de resultados, 9 slides | Jul 2026 | Cierre de la 2ª edición de la campaña en Precio Uno (29-Jun al 15-Jul 2026) |
| **F4** | *Comité Comercial S36-2026* | Comité de ventas, 60 págs | 01-Set-2026 | Cierre Agosto 2026. Bloques: Planificación Comercial, Logística, Marketing, Loyalty, plan de acción Colchones, y pre-read (competitividad, ruta crítica, CDA) |

---

## 1. Estructura mercadológica y surtido

**Árbol mercadológico** `[F1]`
Jerarquía con la que un retailer clasifica todo su surtido, de lo más agregado a lo más granular. En Tottus tiene 5 niveles operativos: **Negocio → Mundo → División (J) → Subdepartamento → Subclase**, y por debajo el **SKU**. Es la columna vertebral de cualquier análisis: define a qué nivel se compara, se agrega y se atribuye un resultado.
*Sinónimo:* estructura mercadológica, jerarquía de productos.

**Negocio** `[F1]`
Nivel más alto del árbol. Agrupa la operación completa (ej. Hipermercados Tottus).

**Mundo** `[F1]`
Segundo nivel. En Tottus: **Non-Food**, **Perecibles**, **PGC**, **FLC**.

**División (J)** `[F1]` `[F3]` `[F4]`
Tercer nivel; en Tottus se codifica como "J" + número. Cada J agrupa un conjunto de subdepartamentos bajo una misma gestión comercial.
Agrupaciones de reporte observadas en el Comité `[F4]`:
- **Food PGC/FLC:** J01, J02, J05
- **Perecibles:** J03, J04, J06, J07
- **Non-Food:** J08, J09, J10, J11
- **Excluidos de la lectura comercial estándar:** **J12**, **J99**, **JSJ** (ver *Venta institucional*)

Referencias sueltas de categoría por J recogidas de F4 y F2: J01 (abarrotes, aceites, galletas, bebidas alcohólicas, confitería, desayunos), J02 (belleza, limpieza), J05 (lácteos/FLC), J06 (panadería y pastelería), J08 (vestuario), J09 (dormitorio, colchones), J11 (electromenor).
⚠️ El mapeo oficial y completo J01–J12 sigue pendiente de fuente.

**Subdepartamento** `[F1]`
Cuarto nivel. Ejemplos: dentro de J6 → Pastelería Fresca, Panadería a Granel, Pastelería Seca. Dentro de J5 → Yogur, Mantecas y Mantequillas, Leches y Cremas, Quesos.

**Clase / Subclase** `[F1]`
Niveles más finos antes del SKU. Ejemplo: Pastelería Seca → Queques → Queques Rectangulares. Es el nivel donde normalmente se toman decisiones de surtido.
La clase se codifica concatenando la jerarquía: `J09050104 – COLCHONES` `[F4]`.

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

**Estado de producto** `[F2]`
Ciclo de vida del SKU en el maestro: **Activo → Inactivo → Descontinuado → Purgado**. Es uno de los cinco ejes de calidad de una selección promocional: F2 detectó que ~22% de los SKUs de un HS no estaban en estado Activo.

**Producto pesable / a granel** `[F1]`
Producto que se vende por peso y no por unidad empaquetada (carnes, frutas, panadería a granel). Hoy en la plataforma no registra marca ni proveedor y aparece como **genérico** — limitación declarada, en desarrollo.

**Genérico** `[F1]`
Etiqueta que recibe un producto sin marca/proveedor identificado en la data. No confundir con "marca blanca".

**Marca propia / MMPP** `[F1]` `[F2]` `[F4]`
Marca del propio retailer. En Tottus: **Marca Tottus**, **Precio Uno**. En la data de Scanntech aparece a nivel **fabricante** agrupada como "Hipermercados Tottus". En los decks internos se abrevia **MMPP** y se reporta como corte propio (ej. "¿cuántos SKUs de MMPP tenemos en arriendo?" `[F2]`; "Especial MMPP 03/09–16/09" `[F4]`).

**PGC** — Productos de Gran Consumo `[F1]`
Mundo de productos de consumo masivo no perecible (abarrotes, cuidado personal, limpieza).

**FLC** — Fiambres, Lácteos y Congelados `[F1]`
Mundo que agrupa esas tres familias. Trabaja mayormente con productos unitarios (no pesables), por lo que la lectura de proveedor y marca es más limpia que en el resto de Perecibles.

**Perecibles** `[F1]`
Mundo de productos de vida útil corta: carnes y pescados, frutas y verduras, panadería y pastelería, platos preparados.
**Ultra Perecibles** `[F4]`: corte más estricto dentro de Perecibles, reportado por separado en el indicador de quiebre.

**Non-Food** `[F1]`
Mundo de productos no alimentarios.

---

## 2. Venta y volumen

**Facturación** `[F1]`
Venta registrada en dinero para un período y un corte determinado. Es la base sobre la que se calcula representatividad y variación.

**Venta SI** (sin impuestos) `[F4]`
Venta neta de IGV. Es la base sobre la que se reporta la venta en el Comité y sobre la que se calcula el GPE.
⚠️ **Trampa habitual:** el ticket promedio y el precio medio suelen venir **con** impuesto. Multiplicar `TRX × Ticket Promedio` no reproduce la Venta SI del mismo slide. Declarar siempre la base.

**Venta institucional** `[F4]`
Venta a clientes institucionales (no shopper de tienda). Se **excluye** de la lectura comercial estándar junto con las divisiones **910, 936 y J12**.

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

**Clientes identificados** `[F3]`
Transacciones en las que el cliente se identificó (típicamente con tarjeta de fidelidad). Es el universo sobre el que se puede hacer análisis de comportamiento individual y de recurrencia.

**Universo de análisis** `[F3]`
Recorte explícito de tickets sobre el que corre un estudio. Ejemplo de F3: "tickets mayores o iguales a S/40", "tickets con Yapa", "tickets ≥ S/40 y con productos de campaña". Declararlo es obligatorio: cambiar el universo cambia todos los resultados.

---

## 4. Precio

**Precio medio** `[F1]` `[F3]` `[F4]`
Precio promedio efectivamente cobrado por un SKU en el período (facturación ÷ unidades). Incorpora el efecto de promociones y descuentos, por lo que difiere del precio de lista.

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

**Punto precio** `[F2]`
Precio cerrado y comunicable (ej. S/9.90) que se fija como mecánica, en oposición a un porcentaje de descuento.

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

**L&A** `[F4]`
Fuente externa de data de mercado usada para el reporte de crecimiento y share del Comité.
⚠️ *por confirmar:* razón social completa del proveedor.

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
Ganancia bruta de explotación: el margen bruto del negocio, en soles (**GPE MM**) y como porcentaje de la venta (**GPE%**). Es el indicador de margen estándar de los reportes de Tottus.
Referencia F4 (Agosto 2026, Tottus): GPE S/62.0 MM sobre venta S/369.0 MM = **16.8%**, +0.8 p.p. vs AP.

**GM%** (*Gross Margin*) `[F4]`
Margen bruto porcentual, usado en los reportes de categoría de Non-Food. Se reporta **GM% Act** (actual) contra **GM% AP** (año pasado).

**Contribución (Contri)** `[F4]`
Margen después de descontar los costos directos atribuibles a la categoría. Se reporta contra **Plan Contri** y contra **Contri AP**.
⚠️ **Trampa:** cuando el Contri AP es negativo, el "Contri AP%" calculado sobre esa base no es interpretable. Y logros de contribución de tres dígitos (654%, 388%) no indican desempeño sino un plan mal puesto.

**Cash margin** `[F2]`
Margen en soles (no en porcentaje) que genera una promoción. Junto con el volumen incremental, es uno de los dos criterios con que F2 define si una promoción fue **efectiva**.

**Rentabilidad promocional** `[F2]`
Definida en F2 como **`GPE + Sellout`**: el margen bruto más el ingreso por acuerdos comerciales asociados a la promoción.
Referencia F2 (Ago-2025, J01/J02/J05): **16.6%** de las combinaciones SKU-promoción tenían rentabilidad negativa.

**Rebate / Sellout** `[F2]`
Ingreso que el proveedor paga al retailer, vinculado a la venta efectiva del producto en promoción. En el proyecto regional se trabajó la "disponibilización de rebate sell out por SKU" para poder calcular rentabilidad promocional a nivel producto.

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

**Táctico (TC)** `[F2]` `[F4]`
Campaña de menor escala y ciclo propio, numerada en paralelo al HS (T35, T36, T37, T38, T39). Tiene sus propios capacities, más reducidos que los del HS.

**Campaña conceptual / Especial** `[F2]` `[F4]`
Campaña temática que se monta sobre o en paralelo al calendario regular (ej. *Especial MMPP*, *Especial Bucal*, *Especial Limpieza*, *Feria Abarrotera*). Queda **fuera** de los máximos de cambio definidos en la política de HS, y por eso es la excepción que hay que gobernar aparte.

**Campaña Core** `[F2]`
Campaña estructural del calendario comercial. Es una de las cuatro fuentes de cartelería junto con Especiales, Mecánicas y Top Deals.

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

**Llamado** `[F2]`
Unidad de comunicación promocional: el mensaje de oferta que se comunica al cliente. Un llamado puede agrupar varios SKUs (**llamado multiproducto**) o uno solo (**llamado monoproducto**).
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

**Vigencia** `[F2]` `[F4]`
Período durante el cual una oferta está activa. El ciclo base del HS es catorcenal.

**Golpe A / Golpe B** `[F2]`
Los dos cambios de precio dentro de un mismo HS: **Golpe A** es la semana con cambio fuerte (~75% de los SKUs cambian de fleje), **Golpe B** la segunda (~7%). En promedio semanal, el **40%** de los SKUs presentaba cambio de fleje respecto del HS anterior.
La política propuesta en F2 elimina los golpes semanales.

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

**Arriendo** `[F2]`
Espacio de exhibición en tienda que el proveedor paga para destacar su producto. Es una fuente de **recaudación** además de una palanca de venta.
Referencia F2: **11,272 arriendos** en la cadena, promedio **194 por tienda**; rango de 25 (Próceres) a 487 (Trujillo 1). El **90.3%** de los SKUs de un HS tenía presencia en algún tipo de arriendo.

**Arriendos prioritarios (MV, R y C)** `[F2]`
Los arriendos de mayor visibilidad: **MV**, **Rumas** y **Cabeceras**. ~6,065 arriendos, ~105 por tienda, 28.5% de los SKUs.
⚠️ *por confirmar:* la expansión de la sigla **MV** no aparece en F2.
**Hallazgo de F2:** los arriendos prioritarios tenían **menos promocionalidad** (65% vs 79% del HS) y **mayor efectividad** (60.6% vs 55.4%). El espacio rinde más que el descuento.

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

**Peso Mercado vs. Peso TT** `[F4]`
Participación de una plaza en el mercado total frente a su participación en la venta de Tottus. La brecha mide **sobre o sub-exposición**.
⚠️ Ejemplo F4: Arequipa pesa 3.5% del mercado y 7.3% de Tottus (2.1x sobre-indexado); Lima 64.5% vs 60.1% (sub-indexada). Un problema en una plaza sobre-indexada golpea más de lo que su tamaño de mercado sugiere.

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

**Share de mercado** `[F1]` `[F4]`
Participación frente al total del mercado o de la competencia. En ScanView aún no disponible; se habilita al conectarse otros retailers. En el Comité se reporta con fuente externa (L&A) `[F4]`.

**Dif Share (p.p.)** `[F4]`
Ganancia o pérdida de participación de mercado en puntos porcentuales. Se calcula comparando el crecimiento propio contra el del mercado: crecer por debajo del mercado = perder share aunque la venta suba.
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

Hitos de la ruta crítica de **HS** `[F4]`: Checklist Confirmación (−52), Briefing Comercial (−27), Carga Apuestas (−27), Alerta mercadería (−21), Compra mercadería (−21/−16), Validación precios (−10), Cumplimiento de mercadería (−3). Responsables: Trade Marketing, Planificación Promocional, Comercial y Planning.

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

### Competitividad de precio — S34 2026 `[F4]`

IPC físico SKVI Food: **U6S 98.5% / US 98.0%**. Distribución de la venta SKVI: 48% con IPC <99% · 15% entre 99–100% · 21% >100% · **16% >105%**.

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

---

## Términos por incorporar (pendientes de fuente)

Espacio de trabajo para el próximo aporte:

- [ ] Definiciones oficiales Tottus de cada J (mapeo completo J01–J12, más J99 y JSJ)
- [ ] Expansión confirmada de siglas: **MV** (arriendo prioritario), **FQ** (quiebre), **MDV** y **RT** (POP), **Fcom**, **KVC**, **H-E-L** (semaforización IPC), **LW** (logística de proveedor), **L&A** (fuente de mercado)
- [ ] Definición formal de **Básico 1 / Básico 2** y de **surtido troncal**
- [ ] Criterio de selección de **Focals**
- [ ] Métricas de rentabilidad complementarias: margen de contribución formal, GMROI
- [ ] Terminología de espacio: planograma, facing, share de góndola
- [ ] Métricas de e-commerce: conversión, ticket digital, sustitución, picking, peso objetivo de web
- [ ] Metodología **A&M** de medición de quiebre — definición y alcance
- [ ] Definición operativa de **capacity operativo** de tienda (declarada "en definición" en F2)
- [ ] Umbrales oficiales de la matriz de efectividad (qué separa Estrella de Bajo Impacto)

---

*Última actualización: fuentes F1–F4 incorporadas. F2 (Estrategia HS), F3 (Chapa Tu Yapa II) y F4 (Comité Comercial S36) aportaron las secciones 5 a 13, los anexos A y B, y enriquecieron las secciones 1 a 4 y 9 a 11.*
