# Glosario de Retail — Inteligencia Comercial

Glosario vivo para el puesto de **Especialista en Inteligencia Comercial (Tottus)**.
Se construye por acumulación: cada capacitación, reunión o documento que aporte terminología se registra como **fuente** y sus términos se incorporan aquí.

**Convenciones:**
- Cada entrada indica `[F1]`, `[F2]`, … según la fuente donde apareció.
- Los términos marcados `[base]` son de uso estándar en retail y se incluyen como complemento de contexto, no provienen de una fuente registrada.
- Cuando un término tiene un significado **específico dentro de una herramienta**, se anota bajo *"En ScanView"* o similar.

---

## Registro de fuentes

| ID | Fuente | Tipo | Fecha | Nota |
|---|---|---|---|---|
| **F1** | Capacitación Comercial Scanntech — "Nueva plataforma tecnológica en retail" (Paolo Gaspar, KAM Scanntech) | Capacitación grabada, ~1h30 | Sep 2026 | 6ª sesión de la ronda al equipo comercial Tottus. Ver `scanntech-scanview-guia.md` |

---

## 1. Estructura mercadológica y surtido

**Árbol mercadológico** `[F1]`
Jerarquía con la que un retailer clasifica todo su surtido, de lo más agregado a lo más granular. En Tottus tiene 5 niveles operativos: **Negocio → Mundo → División (J) → Subdepartamento → Subclase**, y por debajo el **SKU**. Es la columna vertebral de cualquier análisis: define a qué nivel se compara, se agrega y se atribuye un resultado.
*Sinónimo:* estructura mercadológica, jerarquía de productos.

**Bandera** `[F1]`
Nivel más alto del árbol. Tottus, Precio uno, Tottus Online Agrupa la operación completa (ej. Hipermercados Tottus).

**Mundo de categoría** `[F1]`
Segundo nivel. En Tottus: **Non-Food (j18-j9-j10-j11)**, **Perecibles (J3-j4-j6-j7)**, **PGC (producto de gran consumo)** y **FLC (fiambres lacteos y congelados) (j1-j2-j5)**, **Institucional (j12) (Venta por volumne, focal en tienda que jalan venta)**.

**División (J)** `[F1]`
Tercer nivel; en Tottus se codifica como "J" + número (J1, J2, J6, J11…). Cada J agrupa un conjunto de subdepartamentos bajo una misma gestión comercial. Las divisiones de Perecibles son **J3, J4, J6 y J7**. Ejemplos citados: J5 (lácteos/FLC), J6 (Panadería y Pastelería).

**Subdepartamento** `[F1]`
Cuarto nivel. Ejemplos: dentro de J6 → Pastelería Fresca, Panadería a Granel, Pastelería Seca. Dentro de J5 → Yogur, Mantecas y Mantequillas, Leches y Cremas, Quesos.

**Clase / Subclase** `[F1]`
Niveles más finos antes del SKU. Ejemplo: Pastelería Seca → Queques → Queques Rectangulares. Es el nivel donde normalmente se toman decisiones de surtido.

**SKU** (*Stock Keeping Unit*) `[F1]`
Unidad mínima de gestión: el producto individual con su código propio. Ejemplo: "Queque Marmoleado Rectangular Tottus". Es el nivel al que se mide rotación, precio medio y presencia en tienda.

**EAN / Código de barras** `[F1]`
Identificador único del producto. En ScanView se puede pegar una **lista de EAN** para acotar todo el análisis a un conjunto específico de productos.

**Surtido** `[F1]`
Conjunto de productos que un retailer ofrece en una categoría, tienda o bandera. La *estrategia de surtido* define qué SKUs se comercializan en qué banderas o formatos (ej. tortas y pastelería repartidos entre marca Tottus en Tottus y marca propia de Precio Uno en Precio Uno).

**Cobertura de surtido** `[F1]`
Qué tan completo es el surtido propio frente al del mercado. Es una de las vistas que se habilita cuando entra la data de competencia.

**Curva ABC** `[F1]`
Clasificación de productos por su peso en la venta: A = pocos SKUs que concentran la mayor parte, B = intermedios, C = cola larga de bajo aporte. En ScanView es un criterio de ordenamiento en la Tabla de Precios.

**Producto pesable / a granel** `[F1]`
Producto que se vende por peso y no por unidad empaquetada (carnes, frutas, panadería a granel). Hoy en la plataforma no registra marca ni proveedor y aparece como **genérico** — limitación declarada, en desarrollo.

**Genérico** `[F1]`
Etiqueta que recibe un producto sin marca/proveedor identificado en la data. No confundir con "marca blanca".

**Marca propia** `[F1]`
Marca del propio retailer. En Tottus: Marca Tottus, Precio Uno. En la data de Scanntech aparece a nivel **fabricante** agrupada como "Hipermercados Tottus".

**PGC** — Productos de Gran Consumo `[F1]`
Mundo de productos de consumo masivo no perecible (abarrotes, cuidado personal, limpieza).

**FLC** — Fiambres, Lácteos y Congelados `[F1]`
Mundo que agrupa esas tres familias. Trabaja mayormente con productos unitarios (no pesables), por lo que la lectura de proveedor y marca es más limpia que en el resto de Perecibles.

**Perecibles** `[F1]`
Mundo de productos de vida útil corta: carnes y pescados, frutas y verduras, panadería y pastelería, platos preparados.

**Non-Food** `[F1]`
Mundo de productos no alimentarios.

---

## 2. Venta y volumen

**Facturación** `[F1]`
Venta registrada en dinero para un período y un corte determinado. Es la base sobre la que se calcula representatividad y variación.

**Venta en valor vs. venta en unidades** `[F1]`
Dos lecturas de la misma venta: en soles y en piezas. Divergen cuando cambia el precio o el mix. Que la venta en valor crezca y la de unidades caiga significa que se está vendiendo **más caro, no más**.

**Venta total** `[F1]`
Venta de todas las tiendas, incluidas aperturas nuevas y cierres.

**Venta Same Store** (mismas tiendas) `[F1]`
Venta considerando únicamente las tiendas que existían en ambos períodos comparados. Aísla el crecimiento **orgánico** del que viene por expansión de la red. Es el filtro correcto cuando se quiere saber si el negocio realmente mejora.

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

---

## 3. Ticket y comportamiento del shopper

**Ticket** `[base]`
Cada transacción de compra registrada en caja.

**Flujo en tienda** `[F1]`
Número de tickets generados = **tráfico**. Cuántas compras ocurrieron, no cuánta gente entró.

**Ticket medio** `[F1]`
Venta total ÷ número de tickets. Cuánto gasta en promedio un cliente por visita.

**Unidades por ticket (UPT)** `[F1]`
Unidades vendidas ÷ número de tickets. Cuántos productos se lleva el cliente por compra. Junto con el ticket medio revela si el cliente compra más cosas o cosas más caras.

**Descomposición de la venta** `[base]`
`Venta = Flujo (tickets) × Ticket medio`, y `Ticket medio = UPT × Precio medio por unidad`. Es el marco para diagnosticar de dónde viene un crecimiento o una caída.

**Misión de compra** `[F1]`
Motivo con el que el shopper entra a la tienda (reposición de despensa, compra de urgencia, ocasión especial). Un cambio de misión de compra se detecta cuando cae el tráfico pero suben ticket medio y UPT: menos visitas, pero de mayor valor.

**Shopper** `[F1]`
La persona en su rol de comprador dentro de la tienda. Se distingue del *consumidor* (quien usa el producto), porque no siempre son la misma persona ni responden a los mismos estímulos.

---

## 4. Precio

**Precio medio** `[F1]`
Precio promedio efectivamente cobrado por un SKU en el período (facturación ÷ unidades). Incorpora el efecto de promociones y descuentos, por lo que difiere del precio de lista.

**Precio moda** `[F1]`
Precio al que el producto se vende con mayor frecuencia. Es el precio con el que el cliente realmente interactúa: si el precio moda está muy por debajo del precio de lista, el producto vive en promoción.

**Precio mínimo / precio máximo** `[F1]`
Extremos del rango de precios registrados en el período. La amplitud entre ambos indica dispersión de precio (promociones agresivas, diferencias por tienda o desfase).

**Precio desfasado** `[F1]`
Producto cuyo precio quedó desalineado respecto de su categoría, su histórico o el mercado. Detectarlo es uno de los usos declarados de la Tabla de Precios.

**Price index (índice de precios)** `[F1]`
Precio propio expresado como índice frente al precio del mercado o de un competidor (100 = paridad; <100 = más barato). En Perú se activa cuando entre la data de otros retailers.

**Pricing** `[F1]`
Área/función que define la estrategia de precios. En el flujo descrito, Inteligencia Comercial detecta el desfase y lo escala a Pricing.

---

## 5. Distribución, presencia y red de tiendas

**Punto de venta (PDV)** `[F1]`
Tienda física o digital donde se registra venta. La data de ScanView considera solo puntos de venta — no almacenes ni centros de distribución.

**% PDV** `[F1]`
Porcentaje de tiendas de la red en las que un SKU **registró facturación** en el período.
⚠️ **No significa que el producto esté activo o disponible.** Un SKU puede estar activo en el 100% de tiendas y facturar solo en el 56%. La brecha es la señal de alerta: quiebre, problema de ejecución, o surtido mal asignado por bandera.

**% variación de puntos de venta** `[F1]`
Cambio en la cantidad de locales entre los dos períodos comparados. Explica variaciones de venta que no son de performance sino de expansión de red (ej. la apertura de Izaguirre).

**Quiebre (de stock / out of stock)** `[F1]`
Ausencia del producto en góndola pese a estar activo en el surtido.
En ScanView **no hay data directa de quiebre**; el `% PDV` es el proxy y debe contrastarse con la data interna de productos activos. Tampoco identifica **qué tienda** específica falló.

**Bandera** `[F1]`
Formato o marca comercial dentro del mismo grupo. En Tottus: **Tottus**, **Precio Uno**, **Ecommerce**. Filtrar mal la bandera contamina el `% PDV` y el share, porque cuenta locales donde ese surtido nunca se comercializa.

**Zona / cluster** `[F1]`
Agrupación geográfica o comercial de tiendas. En Tottus: Lima Norte, Lima Moderna, Lima Sur, Provincia, Oriente/Iquitos. Sirve tanto para lectura logística como para *cluster de mercado* (tiendas con perfil de demanda similar).

**Cajas por tienda** `[F1]`
Número de cajas registradoras. Proxy del tamaño y capacidad de la tienda (promedio Tottus ≈ 16). Permite comparar tiendas equivalentes y segmentarlas en grandes / medianas / chicas.

**Tienda estacional** `[F1]`
Tienda cuyo volumen depende fuertemente de la época del año (ej. Punta Hermosa, con pico de noviembre a marzo). Requiere planificación de surtido, personal y campañas distinta a la de una tienda promedio.

**Comercio minorista moderno vs. tradicional** `[F1]`
Moderno = cadenas de autoservicio con sistemas de caja integrados (supermercados, hipermercados, conveniencia). Tradicional = bodegas y comercio de barrio. La cobertura de mercado se reporta por separado porque conectar el canal tradicional es mucho más difícil.

---

## 6. Participación y lectura de resultados

**Share (participación)** `[F1]`
Peso de una unidad (SKU, marca, proveedor, categoría) dentro de un total definido. Siempre hay que declarar **share de qué**: share dentro de la subclase, dentro del subdepartamento, o de mercado.

**Representatividad** `[F1]`
Sinónimo de participación usado en la plataforma: cuánto pesa una división, subdepartamento o tienda dentro del total seleccionado. Es el criterio de ordenamiento más útil (por encima del alfabético) porque prioriza dónde hay dinero en juego.

**Share de mercado** `[F1]`
Participación frente al total del mercado o de la competencia. En Perú aún no disponible; se habilita al conectarse otros retailers.

**Variación (%)** `[F1]`
Crecimiento o contracción vs. el período de comparación. Convención estándar del equipo: **mes vs. mismo mes del año anterior** (YoY), porque neutraliza la estacionalidad.

**Contracción** `[F1]`
Caída de la venta (variación negativa). Usado en la plataforma como opuesto de crecimiento.

**Punto porcentual (p.p.)** `[base]`
Diferencia aritmética entre dos porcentajes. Crecer 13.3% vs. 4.6% es una diferencia de **8.7 p.p.**, no de 8.7%. Distinción importante al reportar.

**Valla** `[F1]`
Umbral de referencia contra el que se juzga un resultado: normalmente el crecimiento del nivel inmediatamente superior. Si el J6 crece 4.6%, cada subdepartamento debería crecer ≥4.6% para "pasar la valla". Es el criterio de diagnóstico central del Dashboard Categoría.

**Apalancamiento** `[F1]`
Contribución de una unidad al resultado del total. Un subdepartamento "apalanca" el crecimiento cuando crece por encima de la valla y pesa lo suficiente para mover el agregado; "apalanca la caída" en el caso inverso. Cruza siempre dos cosas: **variación** y **representatividad**.

**Período base / período de comparación** `[F1]`
El período contra el cual se mide. En ScanView se elige libremente y admite multiselección de meses, para comparar correctamente eventos estacionales móviles (ej. Semana Santa que cae en marzo un año y en abril el siguiente).

**Estacionalidad** `[F1]`
Patrón recurrente de la demanda a lo largo del año. Ejemplos citados: pescados y mariscos con pico en marzo–abril (Semana Santa), picos generalizados en diciembre, tiendas de balneario con pico de verano.

**Mes cerrado** `[F1]`
Mes cuya data ya terminó de consolidarse. La data del mes en curso llega incompleta, por lo que los análisis se hacen sobre el último mes cerrado.

---

## 7. Actores del ecosistema

**Retailer** `[F1]`
La cadena minorista. En este contexto, Tottus.

**Proveedor** `[F1]`
Empresa que abastece al retailer. En la plataforma se lista y rankea por representatividad.

**Fabricante** `[F1]`
Empresa que produce. En la práctica de la plataforma, el nivel de agregación por encima de la marca (ej. Alicorp como fabricante, con varias marcas por debajo). Se puede analizar a nivel fabricante o desmarcar el check para bajar a nivel marca.

**Marca** `[F1]`
Nivel por debajo del fabricante (ej. Marca Tottus, Gloria).

**Category management (gestión de categorías)** `[F1]`
Disciplina que gestiona una categoría como una unidad de negocio propia: surtido, precio, espacio y promoción, decidiendo con data en lugar de por SKU aislado.

**Gestor de categoría** `[F1]`
Rol responsable de una categoría o división. Es el usuario objetivo del Dashboard Categoría.

**KAM** (*Key Account Manager*) `[F1]`
Ejecutivo responsable de una cuenta clave. Paolo Gaspar es el KAM de Scanntech para la implementación en Tottus.

**Monetización de data** `[F1]`
Modelo por el cual el retailer comparte, de forma controlada, data de venta con sus proveedores a cambio de inversión comercial. El retailer define **con quién**, **por cuánto tiempo** y **qué información** se comparte.

---

## 8. Analítica y plataforma

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

## Términos por incorporar (pendientes de fuente)

Espacio de trabajo para el próximo aporte:

- [ ] Definiciones oficiales Tottus de cada J (mapeo completo J1–J11)
- [ ] Métricas de margen y rentabilidad (margen bruto, margen de contribución, GMROI)
- [ ] Terminología de trade marketing y espacio (planograma, facing, share de góndola)
- [ ] Terminología de abastecimiento (fill rate, lead time, nivel de servicio, forecast)
- [ ] Métricas de e-commerce (conversión, ticket digital, sustitución, picking)

---

*Última actualización: fuente F1 incorporada.*
