# GPS - Entregable 6: Control Económico y Diseño Contable de Software (PANVIZ)
**Curso:** Gestión de Proyectos de Software — Semana 11  
**Universidad:** Universidad Nacional de San Agustín de Arequipa (UNSA) — Escuela Profesional de Ingeniería de Sistemas (EPIS)  
**Fecha de Entrega:** 16 de noviembre de 2026  
**Caso de Estudio:** Andes Software — Implementación de PANVIZ en Salud Pública  

---

## Integrantes del Equipo de Trabajo (4 Integrantes)
1. **Chambilla Perca, Ricardo Mauricio** — Especialista Contable y Modelado Operacional
2. **Gutiérrez Ccama, Juan Diego** — Especialista en Reportes Financieros y Conciliación
3. **Mollo Chuquicaña, Dolly Yadhira** — Analista de Liquidez, Ratios y Proyecciones de Tesorería
4. **Suclle Suca, Michael Benjamin** — Coordinador General del Proyecto y Auditor Gerencial

---

## Estructura de Entregables del Proyecto

### 1. Documentación e Informes Escritos
* 📄 **[`INFORME_ENTREGABLE_6.md`](INFORME_ENTREGABLE_6.md)**  
  Informe técnico exhaustivo en formato Markdown. Contiene:
  * Solución completa del **Control de Lectura 43** (Slide 43 de `gps5_3_econ.pptx`).
  * Síntesis crítica de la lectura obligatoria (Guim-Bustos et al., 2023, pp. 152–154) en 288 palabras.
  * Catálogo de 14 cuentas codificadas PCGE y sustento normativo (NIIF 15, NIC 16, Devengo).
  * Libro Diario (OP01–OP11), Libro Mayor y Balance de Comprobación de sumas y saldos.
  * Los cuatro estados financieros básicos: Situación Financiera, Resultados, Cambios en el Patrimonio y Flujo de Efectivo Directo (NIC 7).
  * Matriz de Conciliación Integral Calc vs. GnuCash con diferencia neta de S/ 0.00.
  * Ratios financieros (Margen Neto: 8.33%, Razón Corriente: 2.33, Cobertura Inmediata: 1.89).
  * Presupuesto de caja quincenal y modelado de estrés a 45 días ("La trampa de liquidez" y riesgo de déficit de -S/ 2,500).
  * Tres decisiones gerenciales estratégicas con responsable, plazo e impacto en salud pública.
  * Matriz de revisión cruzada entre los 4 integrantes y referencias bibliográficas en formato APA 7ma edición.

* 📕 **[`INFORME_ENTREGABLE_6.pdf`](INFORME_ENTREGABLE_6.pdf)**  
  Versión compilada formal en PDF de 7 páginas (1 página de portada + 6 páginas de contenido técnico), cumpliendo con el límite reglamentario de 5 a 7 páginas.

---

### 2. Presentación Interactiva en HTML (`ppt con html`)
* 🖥️ **[`presentation.html`](presentation.html)** (también disponible como **[`index.html`](index.html)**)  
  Presentación interactiva desarrollada en HTML5, CSS moderno y JavaScript puro (100% autónoma, funciona sin conexión a internet).
  * **Características:**
    * Navegación por teclado con flechas `[←]` `[→]`, `Espacio`, `Re Pág` / `Av Pág`, `Inicio` / `Fin`.
    * Botón de Pantalla Completa (o tecla `F`).
    * Barra de progreso superior y contador de diapositivas.
    * Guión de orador con notas y cronómetro integrado (tecla `N`).
    * Tarjetas de datos contrastadas, tablas financieras y métricas destacadas.
    * Compatible con impresión directa a PDF (`@media print`).
  * **Estructura de las 7 Diapositivas:**
    1. *Portada:* Caso PANVIZ / Andes Software, salud pública y equipo de 4 integrantes.
    2. *Control de Lectura 43:* Las 3 preguntas resueltas del PPTX y fundamentos de software.
    3. *Catálogo y Teneduría:* Partida doble y asientos OP01–OP11 (Sumas S/ 119,000.00).
    4. *Situación Financiera:* Equilibrio patrimonial (Activo S/ 64,500 = Pasivo S/ 22,500 + Patrimonio S/ 42,000).
    5. *Resultados vs. Flujo de Efectivo:* Contraste entre la Utilidad Neta (S/ 2,000) y el Saldo en Bancos (S/ 44,500).
    6. *Presupuesto y Estrés:* Superávit a 15 días (S/ 21,000) vs. Déficit inminente a 45 días (-S/ 2,500 en días 35–44).
    7. *Decisiones Estratégicas:* Factoring Hito 1, Aceleración Hito 2 y Optimización Cloud / SLA 99.9%.

---

### 3. Modelos Contables y Libros de Cálculo
* 📊 **[`PANVIZ_Control_Economico.xlsx`](PANVIZ_Control_Economico.xlsx)**  
  Libro de cálculo compatible con LibreOffice Calc y Microsoft Excel. Contiene 11 hojas enlazadas con fórmulas dinámicas (`SUMAR.SI`, `MAX`, `IF`):
  1. `Cuentas`: Catálogo contable clasificado.
  2. `Diario`: Registro de operaciones OP01 a OP11 y control de balance.
  3. `Mayor`: Mayorización por cuentas T con fórmulas automáticas.
  4. `Comprobación`: Balance de comprobación de sumas y saldos.
  5. `Situación financiera`: Balance general cuadrado al sol.
  6. `Resultados`: Estado de resultados por función.
  7. `Patrimonio`: Estado de cambios en el patrimonio neto.
  8. `Flujo`: Flujo de efectivo directo (NIC 7).
  9. `Caja 15 días`: Presupuesto quincenal, ratios financieros y simulación de estrés a 45 días.
  10. `Conciliación GnuCash`: Matriz de conciliación cuenta por cuenta (diferencias S/ 0.00).
  11. `Participación`: Matriz formal con los 4 integrantes y revisión cruzada.

* 💼 **[`PANVIZ.gnucash`](PANVIZ.gnucash)**  
  Archivo contable nativo en formato GnuCash XML v2.0 (moneda PEN). Configura el árbol completo de cuentas y las 11 operaciones registradas mediante transacciones divididas (*split transactions*).

---

### 4. Reportes Oficiales y Capturas de GnuCash
* 📑 **[`Reporte_GnuCash_Balance_General.pdf`](Reporte_GnuCash_Balance_General.pdf)** — Reporte oficial de Balance General emitido desde GnuCash.
* 📑 **[`Reporte_GnuCash_Perdidas_y_Ganancias.pdf`](Reporte_GnuCash_Perdidas_y_Ganancias.pdf)** — Reporte oficial de Estado de Resultados emitido desde GnuCash.
* 🖼️ **`capturas/`**:
  * [`captura_1_catalogo_cuentas_gnucash.png`](capturas/captura_1_catalogo_cuentas_gnucash.png) — Catálogo y saldos en GnuCash.
  * [`captura_2_transaccion_compuesta_gnucash.png`](capturas/captura_2_transaccion_compuesta_gnucash.png) — Asiento compuesto OP02 con transacciones divididas.
  * [`captura_3_balance_general_gnucash.png`](capturas/captura_3_balance_general_gnucash.png) — Reporte de Balance General.
  * [`captura_4_estado_resultados_gnucash.png`](capturas/captura_4_estado_resultados_gnucash.png) — Reporte de Pérdidas y Ganancias.

---

### 5. Documentos Fuente y Material Bibliográfico
* 📘 **[`gps5_3_econ.pptx`](gps5_3_econ.pptx)** — Presentación académica del curso (Semana 11, diapositivas 43 y 45).
* 📕 **[`trab_53.pdf`](trab_53.pdf)** — Guía de trabajo parcial de control económico de PANVIZ.
* 📗 **[`guim_bustos_2023.pdf`](guim_bustos_2023.pdf)** — Artículo científico de Guim-Bustos et al. (2023) descargado desde Dialnet.
