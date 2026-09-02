# Scanntech / ScanView — Guía de la plataforma para Tottus

> **Fuente:** Capacitación Comercial Scanntech — "Nueva plataforma tecnológica en retail"
> **Expositor:** Paolo Gaspar (KAM Scanntech) · **Anfitriones Tottus:** Gabriel Serrano, Jamile Martins (Comercial), equipo BI
> **Duración:** ~1h30 · **Sesión:** 6ª y última de la ronda de capacitaciones al equipo comercial
> **Fecha de referencia de la data mostrada:** cierres hasta Julio 2026 (Agosto 2026 aún en procesamiento)

---

## 1. Qué es Scanntech y cómo funciona el modelo

**Modelo de negocio (3 pasos):**

1. **Ingesta.** Tottus envía su data transaccional (ventas punto a punto, todo lo que genera el sistema a partir de las ventas) vía **API**.
2. **Procesamiento y devolución.** Scanntech procesa esa data y la devuelve convertida en **insights**: KPIs y drivers del negocio ya calculados, listos para leer, sin tener que descargar-cruzar-calcular.
3. **Monetización.** Scanntech comparte data con **proveedores/fabricantes**. El retailer decide **con qué proveedores** comparte, **por qué período** y **qué información puntual**. Eso trae inversión del proveedor hacia la cadena y permite promociones más optimizadas y colaboración comercial.

**Cifras que presentó Scanntech (estudio Brasil):**

| Actor | Sin Scanntech | Con Scanntech |
|---|---|---|
| Redes / retailers | +4.6% | hasta +13.3% (≈ 8.7 p.p. de diferencia) |
| Proveedores (poca apertura, <10 cadenas) | +10.6% | — |
| Proveedores (mayor apertura de cadenas) | — | +13.9% a +19% |

**Cobertura:**
- +450 proveedores en Latinoamérica (Coca-Cola, AB InBev, etc.).
- Brasil: **90%** de las cadenas del comercio minorista **moderno** conectadas; **80%** del mercado total (moderno + tradicional). Cadenas: Pão de Açúcar, Carrefour, Assaí, Oxxo, Día, Americanas, Atacadão. Digitales: Mercado Libre, Amazon, entre otros.
- **Perú: Tottus es la primera conexión del país y el primer supermercado en incorporar Scanntech.**

**Roadmap declarado (~6 meses):** conexión de otros retailers peruanos (se mencionaron Cencosud y Supermercados Peruanos). Al conectarse, se habilitan las vistas de **mercado**: share vs. competencia, **price index** real, y cobertura de surtido comparada.

**Portafolio:** Scanntech tiene **6 soluciones disponibles** para Tottus. La capacitación cubre **una**: **ScanView** (también referida como *Cambio Retail*).

---

## 2. Ruta de acceso

```
Scanntech → Perú → Desarrollo → Red Tottus → "Tottus Dashboard Grupos 9.1"
```

- Los usuarios del equipo comercial ya están creados.
- Soporte presencial: Paolo Gaspar en oficinas Tottus **martes y jueves, 9:00–18:00**; también por WhatsApp/correo para agendar revisiones por categoría o capacitar equipos completos.

---

## 3. Mapa de la aplicación: 5 hojas (dashboards)

| # | Hoja | Pregunta que responde | Granularidad temporal | Nivel de análisis |
|---|---|---|---|---|
| 1 | **Dashboard Categoría** | ¿Cómo performa mi surtido dentro del árbol mercadológico? | Mes cerrado | Mundo → División → Subdepartamento → Clase → Subclase → SKU |
| 2 | **Dashboard Negociación** | ¿Cómo performan mis proveedores y marcas dentro de mis categorías? | Mes cerrado | Fabricante → Marca → Jerarquía → SKU |
| 3 | **Tabla de Precios** | ¿Cómo se comporta el precio de mis productos? | **Semanal** | SKU |
| 4 | **Dashboard Ejecutivo** | ¿Cómo va la compañía a nivel macro? | Mes cerrado + histórico | Compañía / Bandera |
| 5 | **Dashboard Operacional** | ¿Cómo performa cada tienda? | Mes cerrado + histórico | Tienda |

> **Lógica de uso recomendada por el expositor:** empezar por el **Ejecutivo** (saber dónde está parada la compañía) → bajar a **Categoría** (¿mi categoría crece a la par del negocio?) → **Negociación** (¿qué proveedor apalanca o frena?) → **Precios** y **Operacional** para accionar.

---

## 4. Panel de filtros (transversal a casi todas las hojas)

Casi todos los filtros se repiten hoja a hoja. Conocerlos una vez sirve para las cinco.

| Filtro | Opciones / detalle |
|---|---|
| **Tipo de venta** | Venta total · Venta **Same Store** (mismas tiendas) |
| **Ponderación** | Ventas totales · Ventas **no ponderadas** |
| **Métrica** | **Valor** (soles) · **Unidades** |
| **Fechas de comparación** | Períodos personalizados · último mes cerrado · mes vs. mismo mes del año anterior (comparación estándar del equipo). Permite **multiselección de meses** para estacionalidades móviles (ej. Semana Santa/Pascua que cambia de mes entre años) |
| **Estructura mercadológica** | Árbol de **5 niveles**, fijado al árbol interno de Tottus: **Bandera → Mundo de categoría → División (J) → Subdepartamento → Subclase**. Mundos: Non-Food (J18, J9, J10, J11), Perecibles (J3, J4, J6, J7), PGC y FLC (J1, J2, J5), Institucional (J12). Ver el glosario para el mapeo completo |
| **Fabricante / Proveedor** | Búsqueda y selección (ej. Alicorp). Se desmarca el check para pasar a nivel marca |
| **Marca** | Búsqueda y selección (ej. Marca Tottus) |
| **Códigos de barras** | Se pega una **lista de EAN** y toda la data se acota a esos SKUs |
| **Ordenar por** | Alfabético · **Representatividad** (participación en el negocio) — filtro "orden por grupo" |
| **Bandera** | **Tottus · Precio Uno · Ecommerce** (o total) |
| **Zonas** | Logística y cluster de mercado: Lima (Lima Norte, Lima Moderna, Lima Sur…), Provincia, Oriente/Iquitos |
| **Top fabricantes** | Solo en Negociación: top N proveedores (por defecto 10) |
| **Mercado** | Aún no disponible en Perú; se habilita cuando entren más retailers |

⚠️ **Advertencia operativa señalada en la sesión:** si el surtido está repartido por bandera (ej. tortas y pastelería van con marca Tottus en Tottus y con su propia marca en Precio Uno), hay que **quitar el filtro de bandera que no corresponde**, o el `% PDV` sale sucio porque cuenta locales donde ese SKU nunca se comercializa.

**Funciones transversales:**
- **Guardar vista personalizada** (botón inferior central) → se le pone nombre (ej. "Revisión Carnes y Pescados", "Revisión Ecommerce") y opcionalmente **"Establecer como valor predeterminado"**, para que el dashboard abra siempre con esa configuración. Se puede volver a la **vista original** (configuración de fábrica) en cualquier momento.
- **Descarga a Excel** vía **tabulación cruzada** en todas las hojas.
- **Botón de retroceso** (inferior izquierdo) para subir de nivel en la jerarquía sin rehacer filtros.

---

## 5. Contenido hoja por hoja

### 5.1 Dashboard Categoría

**Para qué sirve:** ver el performance del surtido bajando por el árbol mercadológico hasta el SKU, comparando contra un período base.

**Qué se ve en la tabla principal (por nivel de jerarquía):**
- **Facturación** del período seleccionado.
- **% de representatividad / participación** del nivel sobre el total seleccionado.
- **% de variación** vs. el período de comparación (crecimiento o contracción).

**Drill-down por clic:** División (J) → Subdepartamento → Clase → Subclase → **botón de detalle SKU**.

**Vista SKU (columnas):**
| Columna | Qué es |
|---|---|
| Share / participación | Peso del SKU dentro de su subclase |
| Rotación unitaria | Unidades vendidas en el período |
| % var. rotación por tienda | Variación de la rotación vs. período base |
| Precio medio | Precio promedio de venta del SKU |
| Var. precio medio | Cuánto subió/bajó el precio vs. período base |
| **% PDV** (puntos de venta) | % de tiendas donde el SKU **registró facturación** |
| % var. de puntos de venta | Cambio en el número de locales (aperturas/cierres) |
| Share del proveedor | Participación del proveedor dentro de la subclase |

**Gráfica lateral derecha:** evolutivo histórico de **venta media por tienda** del nivel de jerarquía seleccionado. Sirve para leer tendencia y **estacionalidad** (ej. pescados y mariscos con pico en marzo–abril por Semana Santa; picos de diciembre).

**Caso de uso demostrado (Perecibles, J6 Panadería y Pastelería):**
1. Perecibles (J3, J4, J6, J7) creció **+18.8%** en Julio 2026 vs. Julio 2025, apalancado por Carnes y Pescados (+27.6%).
2. J6 Panadería y Pastelería creció solo **+4.6%**, por debajo del mundo.
3. Dentro de J6: Pastelería Fresca +6.7% y Panadería a Granel +7.1% (por encima de la valla del J), pero **Pastelería Seca** se queda ~1.8 p.p. corta.
4. Dentro de Pastelería Seca: **Queques** lidera representatividad pero se contrae -2%; **Queques Rectangulares** -8.6%.
5. A nivel proveedor/marca: marca propia (Hipermercados Tottus) -7% como fabricante, -11.5% como marca → es quien apalanca la caída.
6. A nivel SKU: Queque Marmoleado Rectangular Tottus, 15.77% de share de la subclase, ~3,174 unidades, precio medio S/ 8.76 (+0.7%), **% PDV 96%**.

**Cálculo de venta perdida (ejercicio en Excel mostrado en vivo):**

```
Venta perdida ≈ Rotación unitaria × Precio medio × (100% − % PDV)
```

En el ejemplo, llevar los top SKUs de la subclase al 100% de PDV representaba **~S/ 11,000** adicionales en el mes.

---

### 5.2 Dashboard Negociación

**Para qué sirve:** ver el performance de **proveedores y marcas** dentro de la estructura mercadológica. Es la hoja para preparar negociaciones.

**Qué se ve:**
- **Ranking de fabricantes/proveedores** por representatividad dentro de las divisiones seleccionadas. Con el filtro **top 10** se ve que esos 10 concentran ~**60% del negocio**.
- Selección de un proveedor → **su performance en cada J / subdepartamento / clase / subclase**.
- **Share del proveedor** en el subdepartamento y su **variación vs. período anterior** (ej. Gloria en Mantecas y Mantequillas: 54.7% → 54.3%).
- **Variación de ventas** del proveedor por nivel (ej. Gloria: Yogur +2.5%, Mantecas y Mantequilla -6.2%, Leches y Cremas plano, Quesos +3.4%).
- **Histórico de venta media por tienda** del proveedor en ese subdepartamento → tendencia y estacionalidad (ej. pico de diciembre).
- **Ranking de productos del proveedor** con rotación unitaria, precio unitario promedio y amplitud de surtido dentro del subdepartamento.

**Filtros:** los mismos de Categoría **más el filtro de fabricantes**.

**Cuando llegue la data de mercado:** además del ranking de proveedores interno, se verá el **ranking de proveedores de la competencia** → insumo para decidir a qué proveedores adoptar o a cuáles dar facilidades para que crezcan en Tottus y no solo en la competencia.

---

### 5.3 Tabla de Precios

**Diferencial clave:** las hojas de Categoría y Negociación entregan **venta mensual cerrada**; esta hoja trabaja con comportamiento **semanal**.

**Qué se ve por SKU:**
- Proveedor, marca y ubicación en el árbol mercadológico.
- **Precio mínimo**, **precio medio**, **precio moda** (el precio con el que el producto se vende habitualmente / con el que el cliente prefiere interactuar) y **precio máximo**.
- **Curva ABC** como criterio de ordenamiento.
- **Rotación unitaria** y **% PDV**.

**Ejemplo mostrado:** "Pan Pancitos del Sur Cabanossi y Queso 6 unidades" → mínimo S/ 21.20, medio S/ 26.04, moda S/ 25.35, máximo S/ 26.50. Un producto como "Jugo Ecofresh Natural Naranja" mantuvo S/ 14.90 estable.

**Uso:** detectar productos con precio desfasado o dispersión alta, y llevar el hallazgo a la mesa con el **equipo de pricing** para definir estrategia de precio.

---

### 5.4 Dashboard Ejecutivo

**Para qué sirve:** foto macro de la compañía y su histórico. El expositor insistió en que el gestor de categoría lo mire **antes** de juzgar su categoría: sirve para saber si una contracción propia está respaldada por una contracción del negocio.

**Qué se ve:**
- **Venta total** en soles y en unidades, con variación vs. **mes anterior** y vs. **mismo mes del año anterior** (ej. compañía -1.8% vs. mes anterior pero +4.3% vs. año anterior).
- Apertura por **bandera** (Tottus / Precio Uno / Ecommerce) con la contribución de cada una al crecimiento o la contracción (ej. Precio Uno -6.9%, Ecommerce +1.3% empujando).
- **KPIs de compañía:**
  - **Flujo en tienda** (número de tickets / tráfico)
  - **Ticket medio** (venta media por ticket)
  - **Unidades por ticket**
  - **Venta media**
  - **Price index** (índice de precios comparado con el mercado — se activa con la data de mercado)
- **Gráfico evolutivo de venta media por tienda** del negocio (rango mostrado: septiembre 2024 – agosto 2026).
- Variación mes a mes vs. mismo mes del año anterior (ej. Agosto +5.6%, Julio +11.4%, Junio +7.6%).

**Lectura de negocio demostrada:** entró menos gente (menos tickets) pero el **ticket medio creció +7.5%** y las **unidades por ticket ~+7%** → la misión de compra del shopper cambió hacia productos de mayor valor. Precio Uno triplica el crecimiento de unidades por ticket (+17%) y Ecommerce empuja el ticket medio (+14%).

---

### 5.5 Dashboard Operacional

**Para qué sirve:** bajar el performance a nivel **tienda**.

**Qué se ve:**
- **Listado completo de tiendas catalogadas por bandera** (cuáles son Tottus, cuáles Precio Uno, cuáles Ecommerce). Solo puntos de venta — no incluye almacenes ni centros que no venden.
- **Cantidad de cajas por tienda** (promedio ~15.9–16), como proxy del tamaño de la tienda. Universo: ~103–105 tiendas.
- **Mapa de calor de aperturas/cierres** en el tiempo: mientras más oscuro, más tiendas activas (agosto 2026 fue el mes con mayor número de tiendas).
- **Cuadro "Performance por tienda del grupo":**
  - Variación de ventas en **valor** y **unidades** del período seleccionado
  - **Importancia para el grupo** (representatividad de la tienda en el negocio)
  - **Cantidad de tickets** (tráfico)
  - **Venta media por ticket del grupo**
  - **Unidades por ticket**
- **Ordenamiento** por representatividad o por **tamaño** (tiendas grandes / medianas / chicas / Ecommerce).
- **Histórico por tienda** de venta media, ticket medio, flujo en tienda y unidades por ticket.

**Casos de lectura demostrados:**
- **Trujillo 1** — tienda más representativa (1.37% del negocio), 228,000 tickets, ticket medio S/ 88, ~7 unidades por ticket, +3% vs. agosto 2025.
- **Megaplaza** — vende ~60,000 tickets más que Trujillo 1, pero con ticket medio de S/ 66.4 y 5 unidades por ticket, y cae -4.8%. Más tráfico no equivale a más venta: Trujillo 1 es más eficiente por ticket.
- **Punta Hermosa** — tienda **estacional** marcada: pico en noviembre–marzo (verano/balnearios del sur). Insumo para decidir si vale la pena no cerrarla temporalmente, y para planificar surtido y campañas por estacionalidad de tienda.

---

## 6. Limitaciones y pendientes declarados en la sesión

| Tema | Estado |
|---|---|
| **Quiebres (out of stock)** | **No hay data directa de quiebre.** El `% PDV` es el proxy: dice en qué % de tiendas el SKU **facturó**, no si estaba activo. Tampoco indica **en qué tienda específica** no hubo venta. Hay que contrastar con la data interna de productos activos |
| **Productos pesables / a granel** | Hoy no registran marca ni proveedor; aparecen como **genéricos**. Scanntech declaró que está en desarrollo |
| **Marca propia** | Aparece agrupada como fabricante **"Hipermercados Tottus"** |
| **Data de mercado / competencia** | No disponible en Perú todavía. Llega cuando se conecten otros retailers (~6 meses). Habilita share de mercado, price index y cobertura de surtido comparada |
| **Cierre de mes** | La data del mes en curso llega incompleta. En la sesión se trabajó con Julio 2026 porque Agosto seguía procesándose |
| **Envío automático por correo** | **No disponible.** La alternativa ofrecida es la **vista personalizada guardada** como predeterminada, para entrar y tener la configuración lista |

---

## 7. Cómo usar esto desde Inteligencia Comercial

Rutina sugerida a partir de lo mostrado:

1. **Ejecutivo** → contexto: ¿la compañía crece o se contrae? ¿por bandera? ¿el driver fue tráfico, ticket medio o unidades por ticket?
2. **Categoría** → ¿mi mundo/división crece por encima o por debajo de la compañía? Bajar hasta encontrar el subdepartamento/subclase que rompe la valla.
3. **SKU** → identificar los que caen en rotación y los que tienen `% PDV < 100%`. Cuantificar la **venta perdida** con la fórmula de la sección 5.1.
4. **Negociación** → atribuir: ¿la caída es de un proveedor o marca concreta? ¿su share cae? Llevar el dato numérico a la negociación.
5. **Tabla de Precios** → verificar si hay dispersión o desfase de precio detrás de la caída de rotación. Escalar a pricing.
6. **Operacional** → ¿es un problema transversal o de un cluster de tiendas / estacionalidad?
7. Guardar cada análisis recurrente como **vista personalizada** con nombre.

---

*Documento elaborado a partir de la transcripción de la capacitación. Los números citados son los ejemplos usados en vivo durante la demo, no cifras oficiales de cierre.*
