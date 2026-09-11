# 20 — Estándar de Formato · Inteligencia Comercial Tottus

> **Qué es este archivo.** La regla única de formato para **todo** entregable que Claude genere para Gabriel Serrano en el contexto Tottus: presentaciones (.pptx), dashboards (HTML, Power BI, Python) y archivos Excel (.xlsx).
>
> **Cómo se usa.** Claude debe leer este documento **antes** de construir cualquier entregable visual de Tottus y aplicarlo sin preguntar. Si una instrucción puntual del usuario contradice esta guía, gana la instrucción puntual; en todo lo demás, gana este documento.
>
> **De dónde sale.** Ingeniería inversa del archivo `Presentación Comité Comercial Tottus` (tema `Tottus`, fuente `Poppins`) usado como referencia canónica de marca.

---

## 1. Tokens de marca

### 1.1 Paleta institucional

| Token | Hex | Uso |
|---|---|---|
| `verde-tottus` | `#045F34` | **Color primario.** Títulos, cifras protagonistas, serie del año actual, acentos de tabla, encabezados |
| `verde-claro` | `#92D050` | Serie del año anterior, línea de meta, barras secundarias |
| `ambar` | `#FFC000` | Serie del año -2, alertas de atención (no de caída) |
| `verde-positivo` | `#196B24` | Texto de variación **positiva** en tablas y KPIs |
| `rojo-negativo` | `#FF0000` | Texto de variación **negativa** en tablas y KPIs |
| `rojo-alerta` | `#C00000` | Bandas, flechas y cajas de alerta; versión "seria" del rojo |
| `rojo-excel` | `#9C0006` | Texto negativo dentro de celdas Excel (par con relleno `#FFC7CE`) |
| `negro-texto` | `#000000` | Texto de datos y cuerpo de tabla |
| `gris-oscuro` | `#333333` | Texto secundario, ejes, subtítulos |
| `gris-medio` | `#B2B2B2` | Líneas divisorias, series inactivas, "sin dato" |
| `gris-verdoso` | `#CBD2CD` | Relleno de encabezados de tabla y cintillos de sección |
| `beige` | `#E3DED1` | Fondo alternativo suave (portadas, cajas de nota) |
| `blanco` | `#FFFFFF` | Fondo de slide, fondo de gráfico, texto sobre verde |
| `azul-marino` | `#002060` | Reservado: bloques de total/consolidado |

**Paleta de apoyo** (solo cuando se necesiten más de 3 series y el color no tenga carga semántica): `#4AB5C4`, `#0989B1`, `#DEB03E`, `#66AD23`.

### 1.2 Reglas duras de color

1. **El color siempre significa algo.** Si un color no comunica año, entidad o signo, va en gris.
2. **Nunca** usar rojo o verde para una serie neutra: están reservados al semáforo.
3. Fondo de slide, de gráfico y de dashboard: **blanco**. Sin degradados, sin fondos oscuros, sin sombras.
4. Máximo **3 colores con carga semántica** por visual. El resto en `gris-medio`.

---

## 2. Tipografía

| Nivel | Fuente | Tamaño PPT | Peso | Color |
|---|---|---|---|---|
| Título-insight de slide | Poppins | 18 pt | Bold | `#045F34` |
| Cifra clave dentro del título | Poppins | 18 pt | Bold | `#045F34` o semáforo |
| Subtítulo / rótulo de bloque | Poppins | 12 pt | Bold | `#333333` |
| Rótulos de KPI (Venta, Var%, Logro%) | Poppins | 11–12 pt | Regular | `#333333` |
| Valor de KPI | Poppins | 11–12 pt | Bold | `#045F34` / semáforo |
| Texto de tabla | Poppins | 8–9 pt | Regular | `#000000` |
| Encabezado de tabla | Poppins | 8 pt | Bold | `#333333` sobre `#CBD2CD` |
| Etiquetas de datos en gráfico | Poppins | 8–10 pt | Bold | color de la serie |
| Ejes y leyenda | Poppins | 9 pt | Regular | `#333333` |
| Fuente / nota al pie | Poppins | 9 pt | Regular | `#000000` |

**Regla de fuente:** `Poppins` como estándar, con **fallback a `Arial`** si no está disponible en el entorno de generación. Nunca Calibri, nunca Times, nunca la fuente por defecto del generador.

Stack CSS para dashboards y HTML:

```css
font-family: 'Poppins', 'Helvetica Neue', Arial, sans-serif;
```

**Nunca bajar de 8 pt.** Si el dato no entra en 8 pt, el problema es la cantidad de datos, no el tamaño.

---

## 3. Semáforo semántico (regla estricta)

Aplica en **PPT, Excel y dashboards**, sin excepción.

| Situación | Color del número | Signo |
|---|---|---|
| Variación positiva vs. AP / vs. meta | `#196B24` | `+` explícito |
| Variación negativa vs. AP / vs. meta | `#FF0000` (`#9C0006` en Excel) | `-` |
| Variación nula o < ±0.1 pp | `#B2B2B2` | `0.0` |
| Logro ≥ 100 % | `#196B24` | — |
| Logro < 100 % | `#FF0000` | — |

**Excepciones semánticas obligatorias** — hay métricas donde "más" es peor. En estos casos el semáforo se invierte y **debe anotarse en la nota al pie**: quiebre / OOS, merma, días de inventario, devoluciones, costo.

**Reglas de aplicación:**

- El color va en el **número**, no en el fondo de la celda, salvo en Excel donde se permite el par relleno + texto.
- Las variaciones siempre llevan signo explícito (`+13.6%`, `-0.7 pp`).
- Puntos porcentuales se escriben `pp`, nunca `%`, y se separan con espacio: `+0.5 pp`.
- Cuando una celda tiene semáforo, el resto de la fila permanece en negro. No se colorea toda la tabla.

---

## 4. Formatos numéricos

| Magnitud | Formato | Ejemplo | Código Excel |
|---|---|---|---|
| Venta en millones | `S/ #.# MM` | `S/ 72.9 MM` | `"S/ "\ #,##0.0,,\ "MM"` |
| Venta en miles | `S/ #,### M` | `S/ 1,820 M` | `"S/ "\ #,##0,\ "M"` |
| Venta absoluta | `S/ #,###` | `S/ 8,805` | `"S/ "#,##0` |
| Variación % | `+#.#%` | `+13.6%` | `+0.0%;-0.0%;0.0%` |
| Participación / share | `#.#%` | `32.6%` | `0.0%` |
| Diferencia de share | `+#.# pp` | `+0.5 pp` | `+0.0" pp";-0.0" pp"` |
| Unidades / TRX en millones | `#.# MM` | `6.7 MM` | `#,##0.0,,\ "MM"` |
| Ticket / precio | `S/ ##.#` | `S/ 76.8` | `"S/ "#,##0.0` |
| Margen % (GPE%) | `#.#%` | `16.4%` | `0.0%` |

**Reglas:**

- **Un decimal** por defecto en porcentajes y montos en MM. Dos decimales solo si la decisión depende de ellos.
- Separador de miles: coma. Separador decimal: punto. (Formato de la data fuente Tottus.)
- Escalar siempre con formato de celda, **nunca dividiendo el dato**.
- Toda cifra debe traer referencia: valor + variación vs. AP + logro vs. meta. **Ningún número solo.**

---

## 5. Presentaciones (.pptx)

### 5.1 Lienzo y grilla

- **Tamaño:** 16:9 — `13.333 in × 7.5 in` (`12192000 × 6858000` EMU). Nunca 4:3.
- **Márgenes seguros:** 0.40 in a cada lado.
- **Bandas verticales fijas:**

| Banda | Rango Y (in) | Contenido |
|---|---|---|
| Título-insight | 0.13 – 1.45 | Titular con la conclusión |
| Cuerpo | 1.55 – 6.90 | Gráficos, tablas, bloques KPI |
| Pie | 6.95 – 7.40 | Fuente, corte de información, exclusiones |

### 5.2 Anatomía obligatoria del slide

Todo slide de resultados lleva estos cuatro elementos. Si falta uno, el slide no está terminado.

1. **Título-insight.** No es un rótulo, es la conclusión. Formato:
   `<Periodo> – <Universo> : <conclusión con la cifra>`
   Ejemplo real: *"Setiembre 2026 – TSS : Crecimiento en ventas de +15.2%. Se registró un logro de 103.0%"*.
   Máximo 2 líneas, Poppins Bold 18 pt, `#045F34`, cifra clave resaltada.
2. **Visual principal** (gráfico o tabla), sin borde, sobre blanco.
3. **Bloque de KPI** a la derecha o debajo: `Venta Real` / `Var% Venta` / `Diferencia` / `Logro%`, con rótulo a la izquierda y valor en caja a la derecha.
4. **Nota al pie.** Poppins 9 pt, negro, siempre con estas tres partes:
   `Fuente: Inteligencia Comercial | Información actualizada al <fecha>. Comparación Comercial. | <exclusiones>`
   Exclusiones estándar a declarar cuando apliquen: *No incluye J12. J99. JSJ. · No se considera Venta Institucional (910. 936. J12).*

### 5.3 Bloques KPI

- Rótulo: Poppins 11–12 pt regular, `#333333`, alineado a la izquierda.
- Valor: caja de ~1.3 × 0.5 in, Poppins 11–12 pt **Bold**.
- Orden canónico de arriba hacia abajo: **Venta Real → Var% Venta → Diferencia → Logro%**.
- La `Diferencia` siempre en MM con signo (`+8.7 MM`).
- Cuando exista proyección de cierre, va como bloque aparte rotulado *"Proyectado cierre de mes"*.

### 5.4 Tablas en PPT

- Encabezado: relleno `#CBD2CD`, texto Poppins Bold 8 pt `#333333`, centrado.
- Cuerpo: Poppins 8 pt, `#000000`, fondo blanco. **Sin banding de colores.**
- Alto de fila: 0.24 – 0.33 in. Primera columna (descripción) alineada a la izquierda; el resto centrado.
- Bordes: solo línea horizontal fina `#B2B2B2` entre filas. Sin bordes verticales.
- Columnas de variación aplican semáforo por celda.
- Máximo **15 filas de datos** por tabla. Si hay más, se corta en Top 15 y se declara en el título.
- Jerarquía de encabezado a dos niveles cuando haya agrupación (`Total Mercado` / `Comp` / `TT + PU`), con celdas combinadas en la fila superior.

### 5.5 Gráficos en PPT

**Paleta por serie temporal — es fija:**

| Serie | Color |
|---|---|
| Año actual (2026) | `#045F34` |
| Año anterior (2025) | `#92D050` |
| Año -2 (2024) | `#FFC000` |
| Meta / presupuesto | `#92D050` en línea punteada |
| Mercado / competencia | `#B2B2B2` |

**Reglas duras:**

- **Sin líneas de grilla.** Ninguna, ni horizontal ni vertical.
- **Sin borde** alrededor del área de gráfico, sin sombra, sin 3D, sin efectos.
- **Etiquetas de datos activadas** en la serie principal: Poppins Bold 8–10 pt, color de la serie.
- Cuando hay etiquetas de datos, se **elimina el eje de valores**. No se muestran ambos.
- Leyenda: abajo (`legendPos = b`), Poppins 9 pt. Se omite si solo hay una serie o si las series están rotuladas directamente sobre la línea.
- Tipo por intención: **línea** para tendencia y evolución semanal · **barra vertical** para comparación entre periodos · **barra horizontal** para ranking de categorías o tiendas · **combinado barra+línea** para venta vs. share/logro. Nunca pie, nunca dona, nunca área apilada.
- Orden: en rankings, siempre descendente por magnitud.

### 5.6 Portada y estructura del mazo

- **Portada:** fondo blanco o `#E3DED1`, logo Tottus, título del comité, semana/periodo (`Comité Comercial S35-2026`) y fecha en formato `06 de Setiembre, 2026`.
- **Orden narrativo estándar del comité:** Consolidado TSS → Tottus → Precio Uno → Online → Mercado y share → Divisiones → Zonas y tiendas → Categorías → Conclusiones.
- Nomenclatura de archivo: `AAAAMMDD Presentación <Nombre> Tottus.pptx`.

---

## 6. Excel (.xlsx)

### 6.1 Estructura del libro

- Primera hoja: **`Resumen`** — KPIs y conclusión. El detalle nunca es la primera hoja.
- Hojas de detalle después. Hoja de data cruda al final, nombrada `_data` y oculta o claramente marcada.
- Nombres de hoja sin espacios raros, máx. 20 caracteres, sin fechas en el nombre si el libro es recurrente.

### 6.2 Formato de celdas

| Elemento | Regla |
|---|---|
| Encabezado de tabla | Relleno `#045F34`, texto blanco Poppins Bold 10 pt, centrado, **fila congelada** |
| Encabezado de segundo nivel | Relleno `#CBD2CD`, texto `#333333` Bold 9 pt |
| Datos | Poppins 10 pt, `#000000`, alineación: texto a la izquierda, números a la derecha |
| Fila de total | Bold, borde superior fino `#045F34`, sin relleno |
| Variación positiva | Texto `#196B24` |
| Variación negativa | Texto `#9C0006`, relleno `#FFC7CE` permitido |
| Neutro | Texto `#B2B2B2` |

### 6.3 Reglas de construcción

1. **Congelar paneles** siempre (fila de encabezado + columna de descripción).
2. **Autofiltro** en la fila de encabezado de toda tabla de detalle.
3. **Ancho de columna ajustado** al contenido; nada de `#####`.
4. Formato numérico por **formato de celda**, jamás como texto.
5. Fórmulas visibles y auditables: nada de valores pegados donde debería haber cálculo. Si se pegan valores, se declara en una celda de nota.
6. Formato condicional: solo semáforo de 2 colores sobre variaciones. **Sin escalas de color de 3 tonos, sin barras de datos, sin íconos.**
7. Celda `A1` de cada hoja: título de la hoja en Poppins Bold 12 pt `#045F34`. Debajo, una línea de contexto: fuente, corte de data y exclusiones.
8. Sin líneas de cuadrícula visibles en hojas de presentación (`Vista > Líneas de cuadrícula = off`).

---

## 7. Dashboards HTML

- **Fondo blanco**, contenedor máximo `1280px`, padding lateral mínimo `16px`, responsive hasta `400px`.
- Tipografía: el stack Poppins/Arial de §2. Tamaño base `14px`.
- **Estructura fija:** título + subtítulo con corte de data → fila de tarjetas KPI → filtros → gráficos → tabla de detalle → nota de fuente.
- **Tarjetas KPI:** fondo blanco, borde `1px solid #E3DED1`, radio `8px`, sin sombra pesada. Rótulo en `#333333` 12 px, valor en `#045F34` 28 px bold, variación debajo con semáforo 13 px.
- **Gráficos:** misma paleta por serie de §5.5, sin gridlines, etiquetas de datos activas, tooltip con el formato numérico de §4.
- **Tablas:** encabezado `#CBD2CD`, filas con separador `#E3DED1`, hover `#F5F7F5`, semáforo por celda de variación, `overflow-x: auto` en pantallas angostas.
- Todo el HTML **autocontenido**: CSS y JS en línea, sin dependencias externas más allá de un CDN permitido.
- Nada de modo oscuro salvo pedido explícito; si se activa, `#045F34` se aclara a `#3D9B6E` para mantener contraste AA.

### 7.1 Tema de Power BI

Guardar como `tottus-ic-theme.json` e importar desde *Vista → Temas → Buscar temas*.

```json
{
  "name": "Tottus Inteligencia Comercial",
  "dataColors": ["#045F34", "#92D050", "#FFC000", "#4AB5C4", "#0989B1", "#DEB03E", "#66AD23", "#B2B2B2"],
  "background": "#FFFFFF",
  "foreground": "#333333",
  "tableAccent": "#045F34",
  "good": "#196B24",
  "neutral": "#B2B2B2",
  "bad": "#FF0000",
  "maximum": "#045F34",
  "center": "#B2B2B2",
  "minimum": "#FF0000",
  "textClasses": {
    "title":    { "fontFace": "Poppins", "fontSize": 14, "color": "#045F34" },
    "header":   { "fontFace": "Poppins", "fontSize": 11, "color": "#333333" },
    "label":    { "fontFace": "Poppins", "fontSize": 9,  "color": "#333333" },
    "callout":  { "fontFace": "Poppins", "fontSize": 28, "color": "#045F34" }
  },
  "visualStyles": {
    "*": {
      "*": {
        "background":  [{ "show": true, "color": { "solid": { "color": "#FFFFFF" } }, "transparency": 0 }],
        "border":      [{ "show": false }],
        "dropShadow":  [{ "show": false }],
        "visualHeader":[{ "show": false }],
        "title":       [{ "show": true, "fontColor": { "solid": { "color": "#045F34" } }, "fontFamily": "Poppins", "fontSize": 12, "alignment": "left" }]
      }
    },
    "lineChart": {
      "*": {
        "valueAxis":    [{ "show": false, "gridlineShow": false }],
        "categoryAxis": [{ "show": true, "gridlineShow": false, "fontFamily": "Poppins", "fontSize": 9, "labelColor": { "solid": { "color": "#333333" } } }],
        "labels":       [{ "show": true, "fontFamily": "Poppins", "fontSize": 9, "labelPrecision": 1 }],
        "legend":       [{ "show": true, "position": "Bottom", "fontFamily": "Poppins", "fontSize": 9 }]
      }
    },
    "columnChart": {
      "*": {
        "valueAxis":    [{ "show": false, "gridlineShow": false }],
        "categoryAxis": [{ "show": true, "gridlineShow": false, "fontFamily": "Poppins", "fontSize": 9 }],
        "labels":       [{ "show": true, "fontFamily": "Poppins", "fontSize": 9, "labelPrecision": 1 }]
      }
    },
    "card": {
      "*": {
        "labels":        [{ "fontFamily": "Poppins", "fontSize": 28, "color": { "solid": { "color": "#045F34" } } }],
        "categoryLabels":[{ "fontFamily": "Poppins", "fontSize": 11, "color": { "solid": { "color": "#333333" } } }]
      }
    },
    "tableEx": {
      "*": {
        "columnHeaders": [{ "fontFamily": "Poppins", "fontSize": 9, "backColor": { "solid": { "color": "#CBD2CD" } }, "fontColor": { "solid": { "color": "#333333" } }, "bold": true }],
        "values":        [{ "fontFamily": "Poppins", "fontSize": 9, "fontColorPrimary": { "solid": { "color": "#000000" } }, "backColorPrimary": { "solid": { "color": "#FFFFFF" } }, "backColorSecondary": { "solid": { "color": "#FFFFFF" } } }],
        "grid":          [{ "gridVertical": false, "gridHorizontal": true, "gridHorizontalColor": { "solid": { "color": "#E3DED1" } }, "outlineColor": { "solid": { "color": "#FFFFFF" } } }]
      }
    }
  }
}
```

**Reglas de layout Power BI:** lienzo 16:9 `1280×720`, fondo blanco, KPI cards en la fila superior, filtros/segmentadores agrupados a la izquierda o en el panel de filtros, una idea por página, nota de fuente y corte de data en el pie de cada página.

### 7.2 Estilo para gráficos en Python

```python
import matplotlib as mpl
import matplotlib.pyplot as plt

TOTTUS = {
    "verde":     "#045F34",
    "verde_cl":  "#92D050",
    "ambar":     "#FFC000",
    "positivo":  "#196B24",
    "negativo":  "#FF0000",
    "gris":      "#B2B2B2",
    "gris_osc":  "#333333",
    "header":    "#CBD2CD",
}

mpl.rcParams.update({
    "font.family":        ["Poppins", "DejaVu Sans", "Arial"],
    "font.size":          9,
    "figure.facecolor":   "white",
    "axes.facecolor":     "white",
    "axes.edgecolor":     "#B2B2B2",
    "axes.labelcolor":    "#333333",
    "axes.grid":          False,          # sin gridlines, siempre
    "axes.spines.top":    False,
    "axes.spines.right":  False,
    "axes.spines.left":   False,          # se elimina el eje Y si hay data labels
    "axes.titlesize":     12,
    "axes.titleweight":   "bold",
    "axes.titlecolor":    "#045F34",
    "axes.titlelocation": "left",
    "xtick.color":        "#333333",
    "ytick.color":        "#333333",
    "xtick.bottom":       True,
    "ytick.left":         False,
    "legend.frameon":     False,
    "legend.fontsize":    9,
    "axes.prop_cycle":    mpl.cycler(color=[TOTTUS["verde"], TOTTUS["verde_cl"],
                                            TOTTUS["ambar"], TOTTUS["gris"]]),
    "savefig.dpi":        200,
    "savefig.bbox":       "tight",
    "savefig.facecolor":  "white",
})

def color_var(x):
    """Semáforo semántico para variaciones."""
    if abs(x) < 0.001:
        return TOTTUS["gris"]
    return TOTTUS["positivo"] if x > 0 else TOTTUS["negativo"]
```

Exportar siempre en PNG a 200 dpi mínimo, fondo blanco, con `bbox_inches="tight"`. Para Plotly: `template="plotly_white"`, `showgrid=False` en ambos ejes, misma secuencia de colores.

---

## 8. Lenguaje y nomenclatura

- Español, tono ejecutivo, sin adjetivos de relleno. La conclusión va primero.
- Abreviaturas estándar: **TSS** (Tottus + Precio Uno, piso + online), **SSS** (same store sales), **TT** (Tottus), **PU** (Precio Uno), **Comp** (competencia), **AP/AA** (año pasado / año anterior), **GPE** (ganancia bruta), **TRX** (transacciones), **Tkt** (ticket), **SOV** (share of value), **MS** (market share), **YTD**, **MM** (millones), **M** (miles), **pp** (puntos porcentuales).
- Divisiones por código: `J01 – PGC Comestible`, `J02 …`. Siempre código + nombre en la primera mención del slide.
- Periodos: `Semana 35` o `S35`, `Setiembre 2026`, `YTD'26`.
- Meses en español con mayúscula inicial: `Setiembre` (no "Septiembre" — se respeta la nomenclatura interna).

---

## 9. Checklist de QA — antes de entregar

Aplicar a todo entregable, sin excepción:

- [ ] ¿El título dice la conclusión, no el tema?
- [ ] ¿Toda cifra tiene referencia (variación y/o logro)?
- [ ] ¿El semáforo es correcto y está invertido donde corresponde (quiebre, merma, días de inventario)?
- [ ] ¿Los decimales son consistentes (1 decimal por defecto)?
- [ ] ¿Las series temporales usan la paleta fija por año?
- [ ] ¿No hay gridlines, bordes, sombras ni 3D?
- [ ] ¿Está la nota al pie con fuente, fecha de corte y exclusiones (J12, J99, JSJ, venta institucional)?
- [ ] ¿La tipografía es Poppins en todo el documento?
- [ ] ¿Ningún texto baja de 8 pt?
- [ ] ¿Los totales cuadran con la suma del detalle?
- [ ] ¿El nombre del archivo sigue la nomenclatura `AAAAMMDD <Nombre>`?

---

## 10. Anti-patrones — nunca hacer esto

| ✗ No | ✓ Sí |
|---|---|
| Título tipo "Ventas Setiembre" | "Setiembre 2026 – TSS: crecimiento de +15.2%, logro de 103.0%" |
| Gráficos de torta o dona | Barra horizontal ordenada |
| Gridlines + etiquetas de datos | Etiquetas de datos, sin eje ni grilla |
| Toda la tabla pintada de colores | Semáforo solo en las columnas de variación |
| Fondo oscuro o degradado | Blanco |
| 8 series en un gráfico | 3 series con carga semántica + resto en gris |
| Un número sin comparación | Valor + Var% vs. AP + Logro% |
| Mezclar Calibri, Arial y Poppins | Poppins (fallback Arial) en todo |
| Slide sin fuente ni fecha de corte | Nota al pie completa siempre |
| Escalar dividiendo el dato entre 1,000,000 | Formato de celda `#,##0.0,,\ "MM"` |

---

*Estándar derivado del Comité Comercial S35-2026. Actualizar este archivo cuando cambie la plantilla oficial de marca; todo entregable generado después de esa fecha debe seguir la versión vigente.*
