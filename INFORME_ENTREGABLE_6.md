# UNIVERSIDAD NACIONAL DE SAN AGUSTÍN DE AREQUIPA
## FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS
### ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS

---

# INFORME TÉCNICO - ENTREGABLE 6: CONTROL ECONÓMICO Y DISEÑO CONTABLE DE PROYECTO DE SOFTWARE
## Caso de Estudio: Plataforma de Vigilancia Epidemiológica en Salud Pública (PANVIZ) – Andes Software

* **Asignatura:** Gestión de Proyectos de Software
* **Semestre Académico:** 2026-B (Semana 11)
* **Fecha de Entrega:** 16 de noviembre de 2026
* **Herramientas Obligatorias:** LibreOffice Calc (`PANVIZ_Control_Economico.xlsx`) y GnuCash (`PANVIZ.gnucash`)

---

### Integrantes del Equipo de Trabajo:
1. **Chambilla Perca, Ricardo Mauricio**
   * *Rol Asignado:* Especialista Contable y Modelado Operacional
   * *Responsabilidad:* Catálogo de Cuentas, Libro Diario (OP01–OP11), Libro Mayor y Balance de Comprobación
   * *Revisión Cruzada:* Revisa la Síntesis Crítica y el Control de Lectura 43 de Suclle Suca
2. **Gutiérrez Ccama, Juan Diego**
   * *Rol Asignado:* Especialista en Reportes Financieros y Conciliación
   * *Responsabilidad:* Elaboración de los 4 Estados Financieros (ESF, EERR, EFE, Patrimonio) y Conciliación Integral Calc vs. GnuCash
   * *Revisión Cruzada:* Revisa los registros y balance de comprobación de Chambilla Perca
3. **Mollo Chuquicaña, Dolly Yadhira**
   * *Rol Asignado:* Analista de Liquidez, Ratios y Proyecciones de Tesorería
   * *Responsabilidad:* Indicadores Financieros, Presupuesto de Caja a 15 y 45 días, Simulación de Estrés Financiero y Decisiones Estratégicas
   * *Revisión Cruzada:* Revisa los Estados Financieros y Conciliación de Gutiérrez Ccama
4. **Suclle Suca, Michael Benjamin**
   * *Rol Asignado:* Coordinador General del Proyecto y Auditoría Gerencial de Software
   * *Responsabilidad:* Coordinación general, resolución del Control de Lectura 43 (Slide 43 PPTX), Síntesis Crítica de Guim-Bustos et al. (2023) e integración gerencial
   * *Revisión Cruzada:* Revisa el Presupuesto de Caja y Decisiones Estratégicas de Mollo Chuquicaña

---

## ÍNDICE DE CONTENIDOS
1. [Sección I: Control de Lectura 43 (Slide 43 PPTX)](#sección-i-control-de-lectura-43-slide-43-pptx)
2. [Sección II: Síntesis Crítica de la Lectura Obligatoria (Guim-Bustos et al., 2023)](#sección-ii-síntesis-crítica-de-la-lectura-obligatoria-guim-bustos-et-al-2023)
3. [Sección III: Caso de Estudio PANVIZ y Criterios Contables](#sección-iii-caso-de-estudio-panviz-y-criterios-contables)
4. [Sección IV: Registro de Operaciones (Libro Diario, Mayor y Comprobación)](#sección-iv-registro-de-operaciones-libro-diario-mayor-y-comprobación)
5. [Sección V: Los Cuatro Estados Financieros al Cierre del Mes](#sección-v-los-cuatro-estados-financieros-al-cierre-del-mes)
6. [Sección VI: Conciliación Integral Hoja de Cálculo vs. GnuCash](#sección-vi-conciliación-integral-hoja-de-cálculo-vs-gnucash)
7. [Sección VII: Indicadores Financieros y Diagnóstico de Salud Económica](#sección-vii-indicadores-financieros-y-diagnóstico-de-salud-económica)
8. [Sección VIII: Presupuesto de Caja Quincenal y la "Trampa de Liquidez" a 45 Días](#sección-viii-presupuesto-de-caja-quincenal-y-la-trampa-de-liquidez-a-45-días)
9. [Sección IX: Tres Decisiones Gerenciales Estratégicas y Continuidad Sanitaria](#sección-ix-tres-decisiones-gerenciales-estratégicas-y-continuidad-sanitaria)
10. [Sección X: Matriz de Responsabilidades y Revisión Cruzada](#sección-x-matriz-de-responsabilidades-y-revisión-cruzada)
11. [Sección XI: Conclusiones y Referencias Bibliográficas](#sección-xi-conclusiones-y-referencias-bibliográficas)

---

## SECCIÓN I: CONTROL DE LECTURA 43 (SLIDE 43 PPTX)

Conforme a lo instruido en la **Diapositiva 43** de la presentación académica (`gps5_3_econ.pptx`), a continuación se resuelve detalladamente el cuestionario basado en el artículo científico de Guim-Bustos et al. (2023):

### 1. ¿Cuál es el propósito de los estados financieros según el fragmento y por qué registrar operaciones contables resulta insuficiente si la gerencia no analiza e interpreta esa información?
* **Propósito Fundamental:** Según Guim-Bustos et al. (2023, pp. 152–154), los estados financieros constituyen representaciones estructuradas, comprensibles y sistemáticas de la situación financiera, el desempeño económico y los flujos de efectivo de una organización. Su propósito esencial no es puramente tributario o de archivo legal, sino proporcionar información relevante, fidedigna y oportuna que ilumine el proceso gerencial, reduzca la incertidumbre y sirva como soporte objetivo para la toma de decisiones operativas, tácticas y de inversión.
* **Insuficiencia del Mero Registro:** Limitarse a la teneduría de libros (registro de débitos y créditos) es insuficiente porque los datos aislados no constituyen diagnóstico. El registro contable es una compilación histórica pasiva; sin un análisis horizontal, vertical y de ratios (liquidez, solvencia, rentabilidad), la gerencia permanece ciega frente a fenómenos críticos como el ciclo de conversión del efectivo, la carga de costos fijos o el riesgo de insolvencia técnica. Como señalan los autores, una contabilidad sin interpretación gerencial impide la previsión estratégica, transformando los informes en documentos estériles que no alertan sobre la necesidad de financiamiento o desvíos presupuestarios antes de que se produzca una crisis irreversible.

### 2. El texto menciona activos, pasivos, capital contable, ingresos, costos y gastos. Elija tres componentes y describa la implementación de cada uno en una empresa que desarrolla software.
Para una empresa de base tecnológica como *Andes Software*, la implementación de tres de estos componentes se traduce en:
1. **Activos (Equipos de Procesamiento y Entorno Tecnológico):**
   * *Implementación:* Comprende la infraestructura tecnológica tangible e intangible de la empresa. En software, incluye servidores locales, estaciones de trabajo de alto rendimiento para desarrolladores, laptops especializadas y licencias de software perpetuas. Bajo la **NIC 16**, los equipos de cómputo se reconocen como activos fijos a su costo de adquisición, depreciándose a lo largo de su vida útil. Aportan valor al habilitar la capacidad instalada para diseñar, compilar, testear y desplegar sistemas informáticos.
2. **Pasivos (Anticipos de Clientes e Ingresos Diferidos):**
   * *Implementación:* En contratos de software por hitos, es habitual recibir cobros adelantados de los clientes antes de la liberación formal del código o del pase a producción. De acuerdo con la **NIIF 15**, estos fondos no son ganancias inmediatas, sino obligaciones de desempeño no satisfechas (pasivo corriente diferido). La empresa mantiene una deuda operativa de servicio que solo se descargará contra ingresos cuando el cliente emita el acta de conformidad del módulo correspondiente.
3. **Costos del Servicio (Remuneraciones de Desarrollo y Cloud Computing):**
   * *Implementación:* Representa los recursos directamente consumidos para crear el producto entregable. Agrupa los sueldos y cargas laborales del equipo técnico (arquitectos de software, desarrolladores frontend/backend, ingenieros QA) y los servicios de cómputo en la nube (AWS, Azure o Google Cloud) consumidos durante los sprints de desarrollo. A diferencia de los gastos generales, estos costos se vinculan biunívocamente al contrato del software y determinan la utilidad bruta del proyecto.

### 3. Una empresa de software informa ganancias, pero tiene dificultades para pagar las remuneraciones del equipo. De los tres estados financieros mencionados en la lectura, ¿cuáles revisaría para evaluar las ganancias y la disponibilidad de efectivo? Justifique su elección y proponga una decisión para proteger la continuidad del proyecto.
* **Estados Financieros a Evaluar:**
  * Para evaluar las ganancias: Se debe revisar el **Estado de Resultados (o Estado de Pérdidas y Ganancias)**.
  * Para evaluar la disponibilidad de efectivo: Se debe revisar el **Estado de Flujos de Efectivo** (contrastado analíticamente con las cuentas de Efectivo y Clientes del **Estado de Situación Financiera**).
* **Justificación Técnica:**
  * El Estado de Resultados se rige bajo el **principio de devengo**: un ingreso por venta de software se reconoce íntegramente en el momento en que se entrega el hito y el cliente lo aprueba, independientemente de cuándo se cobre. Así, si una empresa factura S/ 100,000 con costos de S/ 60,000, reportará una ganancia contable excelente de S/ 40,000.
  * Sin embargo, si el cliente pacta pagar a 60 o 90 días, ese dinero figura en el Estado de Situación Financiera como una Cuenta por Cobrar Comercial (activo exigible), pero no como dinero en el banco. Por su parte, los desarrolladores exigen sus salarios en efectivo a fin de mes.
  * El Estado de Flujos de Efectivo desglosa las entradas y salidas reales de dinero. Si el flujo de actividades de operación es negativo debido a una acumulación masiva de cuentas por cobrar no líquidas, la empresa sufrirá una asfixia de tesorería (*paradoja contable de quebrar con utilidades*).
* **Decisión Gerencial para Proteger la Continuidad del Proyecto:**
  * *Acción Inmediata:* Acudir de inmediato al mecanismo de **Factoring Financiero** o negociar una **Adenda de Pronto Pago con Descuento por Pronto Desembolso** sobre las facturas pendientes de cobro con el cliente. Cediendo un porcentaje menor (tasa de descuento financiero del 2% al 3%), la empresa transforma de inmediato sus cuentas por cobrar en efectivo líquido disponible en cuenta corriente, cubriendo prioritariamente la nómina salarial de los programadores y asegurando el uptime de la nube, lo cual evita la paralización del servicio de salud y la fuga del talento clave.

---

## SECCIÓN II: SÍNTESIS CRÍTICA DE LA LECTURA OBLIGATORIA (GUIM-BUSTOS ET AL., 2023)

> **Referencia:** Guim-Bustos, P., Martillo-Mieles, O., Guerrero-Cortez, V. y Carrillo-Pérez, F. (2023). Los estados financieros y las tomas de decisiones empresariales. *593 Digital Publisher CEIT*, 8(2), 149–160. https://doi.org/10.33386/593dp.2023.2.1679  
> **Páginas Consultadas:** 152–154  
> **Extensión de la Síntesis:** 288 palabras (rango estricto exigido: 250–350 palabras)

Los estados financieros constituyen el compendio estructurado de la realidad económica, patrimonial y financiera de una entidad, cuyo propósito central trasciende la obligación legal o tributaria para erigirse en el fundamento analítico de la toma de decisiones gerenciales. En las páginas examinadas (152–154), los autores demuestran que registrar transacciones mediante partida doble es meramente instrumental; si la gerencia no analiza los saldos mediante indicadores ni interpreta la interacción entre devengo y liquidez, la organización opera en la incertidumbre. La dirección estratégica exige comprender el comportamiento del balance general, las pérdidas y ganancias, y el flujo de caja para evaluar solvencia, anticipar insolvencias y respaldar decisiones de inversión o endeudamiento con evidencia contable verificable.

De este análisis se desprenden dos ideas aplicables directamente al control económico de PANVIZ:

1. **La autonomía analítica del flujo de caja frente al resultado contable:** Reconocer ingresos por hitos aprobados produce utilidades en el estado de resultados, pero no garantiza solvencia inmediata si los plazos de cobranza exceden las obligaciones laborales quincenales. Para PANVIZ, el control debe basarse en un presupuesto de caja proyectado que evite la asfixia de tesorería por retrasos del sector público.
2. **La categorización rigurosa de las obligaciones de desempeño como pasivo corriente:** Los fondos recibidos de forma anticipada antes de prestar el servicio tecnológico no deben registrarse como ingresos ganados, sino como un pasivo diferido. Esto asegura que la gerencia visualice con precisión las obligaciones técnicas comprometidas y salvaguarde los recursos requeridos para completar los módulos sanitarios pendientes sin comprometer la continuidad operativa del sistema.

En conclusión, la contabilidad en proyectos de software no es un ejercicio pasivo, sino un mecanismo de navegación directiva que vincula registros técnicos con la supervivencia del servicio.

---

## SECCIÓN III: CASO DE ESTUDIO PANVIZ Y CRITERIOS CONTABLES

### 3.1. Contexto Operativo y Delimitación Académica
*Andes Software* inicia sus actividades económicas teniendo como único contrato la construcción y despliegue del sistema **PANVIZ**, una plataforma orientada a la ingesta agregada de datos epidemiológicos y generación de tableros de control para la vigilancia sanitaria del sector público.
* **Hito 1 (Mes 1):** Carga y visualización de indicadores sanitarios (completado, entregado y aceptado).
* **Hito 2 (Mes 2):** Módulo de alertas tempranas y generación automatizada de reportes.
* **Delimitación del Ejercicio:** Todas las operaciones están denominadas en Soles peruanos (PEN, S/). No existen saldos iniciales (creación de empresa). Por delimitación académica expresa, se omite el Impuesto General a las Ventas (IGV), el Impuesto a la Renta (IR) y la depreciación de equipos.

### 3.2. Catálogo Mínimo de Cuentas (14 Cuentas Codificadas PCGE)
A continuación se presenta el catálogo contable diseñado para gobernar las transacciones de Andes Software, alineado al Plan Contable General Empresarial (PCGE) y a las Normas Internacionales de Información Financiera (NIIF):

| Código | Denominación de la Cuenta | Elemento | Naturaleza | Estado Financiero | Sustento Normativo y Criterio de Uso |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1041** | Cuentas Corrientes Bancarias | Activo | Deudora | Situación Financiera | Fondos líquidos disponibles depositados en la entidad bancaria. |
| **1212** | Facturas por Cobrar Comerciales - Clientes | Activo | Deudora | Situación Financiera | Derecho exigible por Hito 1 aceptado con promesa de cobro a 45 días. |
| **3361** | Equipos para Procesamiento de Información | Activo | Deudora | Situación Financiera | Hardware de computación adquirido con vida útil prolongada (NIC 16). |
| **4111** | Remuneraciones por Pagar | Pasivo | Acreedora | Situación Financiera | Obligación devengada con el personal administrativo al cierre del mes. |
| **4212** | Proveedores por Pagar | Pasivo | Acreedora | Situación Financiera | Saldo de deuda comercial pendiente con el proveedor de hardware. |
| **4511** | Préstamos Bancarios a Corto Plazo | Pasivo | Acreedora | Situación Financiera | Deuda financiera recibida para capital de trabajo con vencimiento a 6 meses. |
| **4699** | Anticipos de Clientes (Ingresos Diferidos) | Pasivo | Acreedora | Situación Financiera | Cobro recibido por Hito 2; obligación de desempeño pendiente (NIIF 15). |
| **5011** | Capital Social Aportado | Patrimonio | Acreedora | Situación Financiera | Aporte dinerario constitutivo realizado por los socios accionistas. |
| **5911** | Utilidad Neta del Ejercicio | Patrimonio | Acreedora | Situación Financiera | Ganancia neta final generada por las operaciones del primer mes. |
| **7041** | Ingresos por Desarrollo de Software | Ingreso | Acreedora | Estado de Resultados | Ingreso ganado por la entrega conforme del Hito 1 independiente. |
| **6941** | Costo del Servicio - Remuneraciones Desarrollo | Costo | Deudora | Estado de Resultados | Mano de obra directa devengada y pagada al equipo de desarrollo. |
| **6942** | Costo del Servicio - Servicios de Nube | Costo | Deudora | Estado de Resultados | Consumo mensual directo de infraestructura cloud computing para PANVIZ. |
| **9411** | Gastos Administrativos - Operativos Pagados | Gasto | Deudora | Estado de Resultados | Servicios generales y gastos administrativos desembolsados en el mes. |
| **9412** | Gastos Administrativos - Sueldos Devengados | Gasto | Deudora | Estado de Resultados | Gasto administrativo laboral devengado en el mes pero impago al cierre. |
| **9711** | Gastos Financieros - Intereses Bancarios | Gasto | Deudora | Estado de Resultados | Costo del servicio financiero devengado por el préstamo bancario recibido. |

### 3.3. Justificaciones Técnicas y Tratamiento Normativo

1. **Tratamiento del Anticipo de S/ 9,000 (Operación OP04 - NIIF 15):**  
   Bajo la **NIIF 15** (*Ingresos de Actividades Ordinarias Procedentes de Contratos con Clientes*), los ingresos se reconocen cuando (o a medida que) la entidad satisface una obligación de desempeño mediante la transferencia del control de los bienes o servicios comprometidos. En la OP04, la entidad de salud entrega S/ 9,000 por un módulo que se construirá y desplegará en el mes siguiente. Al cierre del periodo no se ha ejecutado ninguna actividad de dicho módulo; en consecuencia, no existe transferencia de control. Registrar esta entrada como ingreso distorsionaría la utilidad del periodo haciéndola parecer mayor. Debe reconocerse un débito en *Bancos (1041)* y un crédito en *Anticipos de Clientes (4699)*, figurando como un pasivo corriente exigible.

2. **Tratamiento de la Adquisición de Equipos Informáticos por S/ 12,000 (Operación OP02 - NIC 16):**  
   Bajo la **NIC 16** (*Propiedad, Planta y Equipo*), un bien tangible se reconoce como activo si es probable que genere beneficios económicos futuros para la empresa y su costo puede medirse con fiabilidad. Las estaciones de cómputo y servidores adquiridos son recursos productivos que prestarán servicio a lo largo de múltiples periodos de desarrollo y no se extinguen en un único ciclo mensual. Por tanto, es técnicamente incorrecto registrarlos como gasto del mes; deben activarse íntegramente en la cuenta *Equipos para Procesamiento de Información (3361)* por S/ 12,000.00, reconociendo la salida de bancos por S/ 8,000.00 y la cuenta por pagar comercial por S/ 4,000.00.

3. **Tratamiento de los Costos de Desarrollo (OP05 y OP06) vs. Intangibles:**  
   En consonancia con las instrucciones del caso y las directrices de la **NIC 38** (*Activos Intangibles*), los desembolsos de remuneraciones de programadores (S/ 15,000.00) y servidores en la nube (S/ 2,000.00) incurridos para la ejecución directa del hito de software vendido se imputan como *Costo del Servicio PANVIZ (Cuentas 6941 y 6942)* en el Estado de Resultados. No se capitalizan como intangibles dado que el desarrollo no es para venta de propiedad intelectual retenida por la empresa, sino un servicio por encargo transferido a la entidad de salud pública.

4. **Principio de Devengo en Gastos Administrativos (Operación OP10):**  
   De acuerdo con el Marco Conceptual de las NIIF, las transacciones y demás sucesos se reconocen cuando ocurren (y no cuando se cobra o se paga el efectivo). Al cierre del mes se devengaron S/ 1,500.00 de salarios administrativos. Aunque queden pendientes de pago, el consumo del trabajo administrativo ya ocurrió en noviembre, por lo que debe registrarse el gasto en la cuenta *9412 Gastos Administrativos - Sueldos Devengados* con abono a la cuenta de pasivo *4111 Remuneraciones por Pagar*.

---

## SECCIÓN IV: REGISTRO DE OPERACIONES (LIBRO DIARIO, MAYOR Y COMPROBACIÓN)

### 4.1. Libro Diario General (Operaciones OP01 a OP11)
A continuación se detalla el registro cronológico del primer mes de Andes Software:

| ID | Fecha | Cód. | Denominación de la Cuenta Contable | Glosa y Sustento Operacional | Debe (S/) | Haber (S/) |
| :---: | :---: | :---: | :--- | :--- | :---: | :---: |
| **OP01** | 02/11/2026 | 1041<br>5011 | Cuentas Corrientes Bancarias<br>Capital Social Aportado | Por el aporte inicial en efectivo de los socios accionistas depositado en la cuenta corriente bancaria de la empresa. | 40,000.00<br>- | -<br>40,000.00 |
| **OP02** | 04/11/2026 | 3361<br>1041<br>4212 | Equipos para Procesamiento de Inf.<br>Cuentas Corrientes Bancarias<br>Proveedores por Pagar | Por la compra de hardware de desarrollo por S/ 12,000: pago de S/ 8,000 con cheque/transferencia y saldo de S/ 4,000 a crédito. | 12,000.00<br>-<br>- | -<br>8,000.00<br>4,000.00 |
| **OP03** | 06/11/2026 | 1041<br>4511 | Cuentas Corrientes Bancarias<br>Préstamos Bancarios Corto Plazo | Por el desembolso íntegro del préstamo bancario recibido para capital de trabajo con vencimiento a 6 meses. | 10,000.00<br>- | -<br>10,000.00 |
| **OP04** | 09/11/2026 | 1041<br>4699 | Cuentas Corrientes Bancarias<br>Anticipos de Clientes (Diferidos) | Por la recepción del anticipo en efectivo de la entidad de salud pública para el módulo del próximo mes (NIIF 15). | 9,000.00<br>- | -<br>9,000.00 |
| **OP05** | 13/11/2026 | 6941<br>1041 | Costo Servicio - Remuneraciones Dev.<br>Cuentas Corrientes Bancarias | Por el pago desde bancos de las planillas salariales del equipo técnico de desarrollo de software correspondientes al mes. | 15,000.00<br>- | -<br>15,000.00 |
| **OP06** | 16/11/2026 | 6942<br>1041 | Costo Servicio - Servicios de Nube<br>Cuentas Corrientes Bancarias | Por la recepción y cancelación inmediata desde bancos de las facturas de servidores cloud consumidos en el mes. | 2,000.00<br>- | -<br>2,000.00 |
| **OP07** | 19/11/2026 | 9411<br>1041 | Gastos Admin. - Operativos Generales<br>Cuentas Corrientes Bancarias | Por la cancelación de gastos operativos administrativos del mes mediante transferencia bancaria. | 3,000.00<br>- | -<br>3,000.00 |
| **OP08** | 23/11/2026 | 1041<br>1212<br>7041 | Cuentas Corrientes Bancarias<br>Clientes - Facturas por Cobrar<br>Ingresos por Desarrollo de Software | Por la entrega y aceptación formal del primer hito independiente: reconocimiento de S/ 24,000 (cobro S/ 16,000 y saldo S/ 8,000 a 45 d). | 16,000.00<br>8,000.00<br>- | -<br>-<br>24,000.00 |
| **OP09** | 25/11/2026 | 4212<br>1041 | Proveedores por Pagar<br>Cuentas Corrientes Bancarias | Por la amortización parcial de la deuda con el proveedor de equipos informáticos mediante transferencia desde bancos. | 2,000.00<br>- | -<br>2,000.00 |
| **OP10** | 28/11/2026 | 9412<br>4111 | Gastos Admin. - Sueldos Devengados<br>Remuneraciones por Pagar | Por el reconocimiento del devengo de las remuneraciones administrativas del mes pendientes de pago al cierre. | 1,500.00<br>- | -<br>1,500.00 |
| **OP11** | 30/11/2026 | 9711<br>1041 | Gastos Financieros - Intereses<br>Cuentas Corrientes Bancarias | Por la cancelación de los intereses bancarios devengados correspondientes al préstamo financiero (sin amortizar capital). | 500.00<br>- | -<br>500.00 |
| **TOTAL** | | | **TOTALES LIBRO DIARIO GENERAL** | **CONTROL DE PARTIDA DOBLE: DEBE - HABER = 0.00** | **S/ 119,000.00** | **S/ 119,000.00** |

### 4.2. Libro Mayor General (Cuentas T y Movimientos)
A partir del Libro Diario, se efectuó la mayorización con fórmulas automáticas `SUMAR.SI`, obteniendo la totalidad de cargos, abonos y saldos de cierre:

* **1041 Cuentas Corrientes Bancarias (Activo):**
  * *Debe (Cargos):* S/ 40,000.00 (OP01) + S/ 10,000.00 (OP03) + S/ 9,000.00 (OP04) + S/ 16,000.00 (OP08) = **S/ 75,000.00**
  * *Haber (Abonos):* S/ 8,000.00 (OP02) + S/ 15,000.00 (OP05) + S/ 2,000.00 (OP06) + S/ 3,000.00 (OP07) + S/ 2,000.00 (OP09) + S/ 500.00 (OP11) = **S/ 30,500.00**
  * *Saldo Deudor:* S/ 75,000.00 - S/ 30,500.00 = **S/ 44,500.00**
* **1212 Facturas por Cobrar Comerciales - Clientes (Activo):**
  * *Debe:* S/ 8,000.00 (OP08) | *Haber:* S/ 0.00 | *Saldo Deudor:* **S/ 8,000.00**
* **3361 Equipos para Procesamiento de Información (Activo):**
  * *Debe:* S/ 12,000.00 (OP02) | *Haber:* S/ 0.00 | *Saldo Deudor:* **S/ 12,000.00**
* **4111 Remuneraciones por Pagar (Pasivo):**
  * *Debe:* S/ 0.00 | *Haber:* S/ 1,500.00 (OP10) | *Saldo Acreedor:* **S/ 1,500.00**
* **4212 Proveedores por Pagar (Pasivo):**
  * *Debe:* S/ 2,000.00 (OP09) | *Haber:* S/ 4,000.00 (OP02) | *Saldo Acreedor:* **S/ 2,000.00**
* **4511 Préstamos Bancarios a Corto Plazo (Pasivo):**
  * *Debe:* S/ 0.00 | *Haber:* S/ 10,000.00 (OP03) | *Saldo Acreedor:* **S/ 10,000.00**
* **4699 Anticipos de Clientes - Ingresos Diferidos (Pasivo):**
  * *Debe:* S/ 0.00 | *Haber:* S/ 9,000.00 (OP04) | *Saldo Acreedor:* **S/ 9,000.00**
* **5011 Capital Social Aportado (Patrimonio):**
  * *Debe:* S/ 0.00 | *Haber:* S/ 40,000.00 (OP01) | *Saldo Acreedor:* **S/ 40,000.00**
* **7041 Ingresos por Desarrollo de Software (Ingreso):**
  * *Debe:* S/ 0.00 | *Haber:* S/ 24,000.00 (OP08) | *Saldo Acreedor:* **S/ 24,000.00**
* **6941 Costo del Servicio - Remuneraciones de Desarrollo (Costo):**
  * *Debe:* S/ 15,000.00 (OP05) | *Haber:* S/ 0.00 | *Saldo Deudor:* **S/ 15,000.00**
* **6942 Costo del Servicio - Servicios de Nube (Costo):**
  * *Debe:* S/ 2,000.00 (OP06) | *Haber:* S/ 0.00 | *Saldo Deudor:* **S/ 2,000.00**
* **9411 Gastos Administrativos - Operativos Generales (Gasto):**
  * *Debe:* S/ 3,000.00 (OP07) | *Haber:* S/ 0.00 | *Saldo Deudor:* **S/ 3,000.00**
* **9412 Gastos Administrativos - Sueldos Devengados (Gasto):**
  * *Debe:* S/ 1,500.00 (OP10) | *Haber:* S/ 0.00 | *Saldo Deudor:* **S/ 1,500.00**
* **9711 Gastos Financieros - Intereses Bancarios (Gasto):**
  * *Debe:* S/ 500.00 (OP11) | *Haber:* S/ 0.00 | *Saldo Deudor:* **S/ 500.00**

### 4.3. Balance de Comprobación de Sumas y Saldos
El Balance de Comprobación consolida la igualdad matemática de la partida doble y la consistencia de los saldos que nutrirán los estados financieros:

| Cód. | Cuenta Contable | Sumas Debe (S/) | Sumas Haber (S/) | Saldo Deudor (S/) | Saldo Acreedor (S/) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1041** | Cuentas Corrientes Bancarias | 75,000.00 | 30,500.00 | 44,500.00 | - |
| **1212** | Facturas por Cobrar Comerciales - Clientes | 8,000.00 | - | 8,000.00 | - |
| **3361** | Equipos para Procesamiento de Información | 12,000.00 | - | 12,000.00 | - |
| **4111** | Remuneraciones por Pagar | - | 1,500.00 | - | 1,500.00 |
| **4212** | Proveedores por Pagar | 2,000.00 | 4,000.00 | - | 2,000.00 |
| **4511** | Préstamos Bancarios a Corto Plazo | - | 10,000.00 | - | 10,000.00 |
| **4699** | Anticipos de Clientes (Ingresos Diferidos) | - | 9,000.00 | - | 9,000.00 |
| **5011** | Capital Social Aportado | - | 40,000.00 | - | 40,000.00 |
| **7041** | Ingresos por Desarrollo de Software | - | 24,000.00 | - | 24,000.00 |
| **6941** | Costo del Servicio - Remuneraciones Desarrollo | 15,000.00 | - | 15,000.00 | - |
| **6942** | Costo del Servicio - Servicios de Nube | 2,000.00 | - | 2,000.00 | - |
| **9411** | Gastos Administrativos - Operativos Generales | 3,000.00 | - | 3,000.00 | - |
| **9412** | Gastos Administrativos - Sueldos Devengados | 1,500.00 | - | 1,500.00 | - |
| **9711** | Gastos Financieros - Intereses Bancarios | 500.00 | - | 500.00 | - |
| **TOT** | **TOTALES BALANCE DE COMPROBACIÓN** | **S/ 119,000.00** | **S/ 119,000.00** | **S/ 86,500.00** | **S/ 86,500.00** |

* **Control de Sumas del Mayor:** $\sum Debe - \sum Haber = 119,000.00 - 119,000.00 = \mathbf{S/\ 0.00}$ (Cuadrado Exacto).
* **Control de Saldos:** $\sum Saldo\ Deudor - \sum Saldo\ Acreedor = 86,500.00 - 86,500.00 = \mathbf{S/\ 0.00}$ (Cuadrado Exacto).

---

## SECCIÓN V: LOS CUATRO ESTADOS FINANCIEROS AL CIERRE DEL MES

### 5.1. Estado de Situación Financiera (Balance General al 30 de Noviembre de 2026)

```
=======================================================================================================
                                 ANDES SOFTWARE - PROYECTO PANVIZ
                     ESTADO DE SITUACIÓN FINANCIERA AL 30 DE NOVIEMBRE DE 2026
                                      (Expresado en Soles - PEN)
=======================================================================================================
ACTIVO                                                PASIVO Y PATRIMONIO NETO
--------------------------------------------------    --------------------------------------------------
ACTIVO CORRIENTE                                      PASIVO CORRIENTE
  Efectivo y Equivalentes (Bancos 1041)  S/ 44,500.00    Proveedores por Pagar (4212)        S/  2,000.00
  Cuentas por Cobrar Clientes (1212)     S/  8,000.00    Préstamos Bancarios Corto P. (4511) S/ 10,000.00
                                                      Anticipos de Clientes (NIIF 15 4699)S/  9,000.00
  TOTAL ACTIVO CORRIENTE                 S/ 52,500.00    Remuneraciones por Pagar (4111)     S/  1,500.00
                                                      --------------------------------------------------
ACTIVO NO CORRIENTE                                   TOTAL PASIVO CORRIENTE              S/ 22,500.00
  Equipos de Cómputo (NIC 16 3361)       S/ 12,000.00
  ------------------------------------------------    PATRIMONIO NETO
  TOTAL ACTIVO NO CORRIENTE              S/ 12,000.00    Capital Social Aportado (5011)      S/ 40,000.00
                                                      Resultados Acumulados (Utilidad 5911)S/ 2,000.00
                                                      --------------------------------------------------
                                                      TOTAL PATRIMONIO NETO               S/ 42,000.00
--------------------------------------------------    --------------------------------------------------
TOTAL ACTIVO                             S/ 64,500.00    TOTAL PASIVO Y PATRIMONIO NETO      S/ 64,500.00
=======================================================================================================
CONTROL DE LA ECUACIÓN CONTABLE: ACTIVO (64,500.00) = PASIVO (22,500.00) + PATRIMONIO (42,000.00) [DIF: 0.00]
```

### 5.2. Estado de Resultados Económico (01 al 30 de Noviembre de 2026)

| Concepto Económico | Código Cuenta | Importe (S/) | % Sobre Ventas | Análisis Estructural |
| :--- | :---: | :---: | :---: | :--- |
| **Ingresos por Desarrollo de Software** | **7041** | **S/ 24,000.00** | **100.00%** | Facturación total por Hito 1 aceptado. |
| **(-) Costo Directo del Servicio PANVIZ** | | **(S/ 17,000.00)** | **70.83%** | Costos técnicos directos del hito. |
| * Remuneraciones de Desarrollo de Software | 6941 | (S/ 15,000.00) | 62.50% | Mano de obra directa técnica devengada. |
| * Servicios de Infraestructura Nube Cloud | 6942 | (S/ 2,000.00) | 8.33% | Servidores cloud consumidos en el mes. |
| **UTILIDAD BRUTA** | | **S/ 7,000.00** | **29.17%** | Margen de contribución técnica del proyecto. |
| **(-) Gastos Administrativos Operativos** | | **(S/ 4,500.00)** | **18.75%** | Carga operativa estructural. |
| * Gastos Operativos Generales Desembolsados | 9411 | (S/ 3,000.00) | 12.50% | Servicios y consumos generales de oficina. |
| * Sueldos Administrativos Devengados | 9412 | (S/ 1,500.00) | 6.25% | Remuneraciones administrativas de cierre. |
| **UTILIDAD OPERATIVA (EBIT)** | | **S/ 2,500.00** | **10.42%** | Beneficio puro de la actividad del negocio. |
| **(-) Gastos Financieros** | | **(S/ 500.00)** | **2.08%** | Costo del capital de trabajo prestado. |
| * Intereses Devengados Préstamo Bancario | 9711 | (S/ 500.00) | 2.08% | Interés bancario mensual devengado y pagado. |
| **UTILIDAD NETA DEL EJERCICIO** | **5911** | **S/ 2,000.00** | **8.33%** | Ganancia neta retenida en el patrimonio. |

### 5.3. Estado de Cambios en el Patrimonio Neto
Explica la transformación patrimonial de Andes Software durante su primer mes:

| Concepto Patrimonial | Capital Social (S/) | Resultados Acumulados (S/) | Total Patrimonio Neto (S/) |
| :--- | :---: | :---: | :---: |
| **Saldo Inicial al 01/11/2026** | **0.00** | **0.00** | **0.00** |
| (+) Aportes Dinerarios de Socios (OP01) | 40,000.00 | - | 40,000.00 |
| (+) Utilidad Neta del Ejercicio (Mes 1) | - | 2,000.00 | 2,000.00 |
| **SALDO FINAL AL 30/11/2026** | **S/ 40,000.00** | **S/ 2,000.00** | **S/ 42,000.00** |

### 5.4. Estado de Flujos de Efectivo (Método Directo NIC 7)
De conformidad con la **NIC 7** (*Estado de Flujos de Efectivo*), a continuación se clasifica cada cobro y pago real de efectivo:

| Actividades de Flujo de Efectivo | Importe Parcial (S/) | Flujo Neto (S/) | Sustento Normativo NIC 7 |
| :--- | :---: | :---: | :--- |
| **ACTIVIDADES DE OPERACIÓN** | | | **Entradas y salidas de la actividad principal.** |
| Cobranza por servicios de software (Hito 1 - OP08) | +16,000.00 | | Cobro al contado de la entidad de salud. |
| Cobranza por anticipo de cliente (Hito 2 - OP04) | +9,000.00 | | Anticipo recibido por módulo próximo mes. |
| (-) Pago de planillas de desarrollo (OP05) | -15,000.00 | | Salida de caja para remuneraciones directas. |
| (-) Pago de servicios de nube cloud (OP06) | -2,000.00 | | Pago a proveedor de infraestructura tecnológica. |
| (-) Pago de gastos operativos administrativos (OP07) | -3,000.00 | | Egresos por consumos administrativos corrientes. |
| (-) Pago de intereses financieros del préstamo (OP11) | -500.00 | | Costo financiero clasificado en operación (NIC 7). |
| **Flujo Neto Procedente de Actividades de Operación** | | **+S/ 4,500.00** | Superávit operacional modesto de caja. |
| **ACTIVIDADES DE INVERSIÓN** | | | **Adquisición de activos a largo plazo.** |
| (-) Pago al contado por compra de hardware (OP02) | -8,000.00 | | Desembolso inicial para compra de computadoras. |
| (-) Pago de deuda a proveedor de equipos (OP09) | -2,000.00 | | *Tratamiento NIC 7:* Cancela pasivo de PPE. |
| **Flujo Neto Utilizado en Actividades de Inversión** | | **-S/ 10,000.00** | Inversión neta en capacidad tecnológica instalada. |
| **ACTIVIDADES DE FINANCIACIÓN** | | | **Cambios en el tamaño del capital y pasivo financiero.** |
| Aporte de capital constitutivo de socios (OP01) | +40,000.00 | | Efectivo aportado para fundar la empresa. |
| Desembolso de préstamo bancario recibido (OP03) | +10,000.00 | | Crédito bancario a 6 meses para fondeo de caja. |
| **Flujo Neto Procedente de Actividades de Financiación**| | **+S/ 50,000.00** | Fondeo total externo del inicio de operaciones. |
| **AUMENTO NETO DE EFECTIVO Y EQUIVALENTES** | | **+S/ 44,500.00** | Variación neta de efectivo durante noviembre. |
| Saldo Inicial de Efectivo al 01/11/2026 | | S/ 0.00 | Empresa inicia operaciones sin saldo anterior. |
| **SALDO FINAL DE EFECTIVO Y EQUIVALENTES AL 30/11/2026** | | **S/ 44,500.00** | **Conciliación exacta con cuenta Bancos 1041 (ESF).** |

* **Nota Técnica NIC 7 sobre la OP09:** Se clasifica el pago de S/ 2,000 al proveedor de equipos como actividad de inversión porque dicho pasivo comercial se contrajo exclusivamente por la compra de Activo Fijo (Propiedad, Planta y Equipo). Pagos relativos a la liquidación de activos no corrientes deben revelarse en inversión para reflejar con fidelidad el costo en efectivo del equipo de cómputo.

---

## SECCIÓN VI: CONCILIACIÓN INTEGRAL HOJA DE CÁLCULO VS. GNUCASH

Conforme al requerimiento obligatorio de la **Sección 8.B y 10** del documento orientador (`trab_53.pdf`), se efectuó la contrastación sistemática entre el modelo de fórmulas desarrollado en **LibreOffice Calc / Excel** (`PANVIZ_Control_Economico.xlsx`) y el libro nativo en **GnuCash** (`PANVIZ.gnucash`):

| Cód. | Cuenta / Indicador Financiero | Saldo Hoja Calc (S/) | Saldo GnuCash (S/) | Diferencia (S/) | Estado de Validación | Enlace a Evidencia y Sustento Técnico |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **1041** | Cuenta Corriente Bancaria | 44,500.00 | 44,500.00 | 0.00 | CONCILIADO EXACTO | Saldo idéntico en cuenta bancaria; ver [captura_1](capturas/captura_1_catalogo_cuentas_gnucash.png). |
| **1212** | Facturas por Cobrar Comerciales | 8,000.00 | 8,000.00 | 0.00 | CONCILIADO EXACTO | Registro manual de derecho comercial; ver balance en GnuCash. |
| **3361** | Equipos de Cómputo (NIC 16) | 12,000.00 | 12,000.00 | 0.00 | CONCILIADO EXACTO | Hardware valuado a costo histórico; ver transacción OP02. |
| **4111** | Remuneraciones por Pagar | 1,500.00 | 1,500.00 | 0.00 | CONCILIADO EXACTO | Pasivo administrativo devengado en OP10; ver balance. |
| **4212** | Proveedores por Pagar | 2,000.00 | 2,000.00 | 0.00 | CONCILIADO EXACTO | Pasivo remanente tras abono OP02 y cargo OP09; ver mayor. |
| **4511** | Préstamos Bancarios Corto Plazo | 10,000.00 | 10,000.00 | 0.00 | CONCILIADO EXACTO | Deuda financiera principal recibida en OP03; ver pasivos. |
| **4699** | Anticipos de Clientes (NIIF 15) | 9,000.00 | 9,000.00 | 0.00 | CONCILIADO EXACTO | Pasivo corriente por Hito 2 diferido; ver catálogo GnuCash. |
| **5011** | Capital Social Aportado | 40,000.00 | 40,000.00 | 0.00 | CONCILIADO EXACTO | Aporte inicial registrado sin duplicar saldos iniciales. |
| **7041** | Ingresos Desarrollo Software | 24,000.00 | 24,000.00 | 0.00 | CONCILIADO EXACTO | Reconocimiento por Hito 1; ver [captura_4](capturas/captura_4_estado_resultados_gnucash.png). |
| **69** | Costo del Servicio PANVIZ | 17,000.00 | 17,000.00 | 0.00 | CONCILIADO EXACTO | Suma de sueldos (15k) y nube (2k); coincide al 100%. |
| **94** | Gastos Administrativos Totales | 4,500.00 | 4,500.00 | 0.00 | CONCILIADO EXACTO | Suma de gastos generales (3k) y planilla devengada (1.5k). |
| **97** | Gastos Financieros (Intereses) | 500.00 | 500.00 | 0.00 | CONCILIADO EXACTO | Interés financiero mensual devengado y pagado en OP11. |
| **5911** | Utilidad Neta del Ejercicio | 2,000.00 | 2,000.00 | 0.00 | CONCILIADO EXACTO | Resultado económico idéntico en ambos entornos de software. |
| **TOT** | **TOTAL ACTIVO** | **64,500.00** | **64,500.00** | **0.00** | **CONCILIADO EXACTO** | Ver [Reporte_GnuCash_Balance_General.pdf](Reporte_GnuCash_Balance_General.pdf). |
| **TOT** | **TOTAL PASIVO Y PATRIMONIO** | **64,500.00** | **64,500.00** | **0.00** | **CONCILIADO EXACTO** | Ver [Reporte_GnuCash_Perdidas_y_Ganancias.pdf](Reporte_GnuCash_Perdidas_y_Ganancias.pdf). |

### Evidencias de Ejecución en GnuCash
1. **Catálogo de Cuentas y Plan de Cuentas:** Se estructuró el árbol en cuentas de Banco, A cobrar, Activo, A pagar, Pasivo, Patrimonio, Ingreso y Gasto ([captura_1](capturas/captura_1_catalogo_cuentas_gnucash.png)).
2. **Transacción Compuesta con Asientos Divididos (Split Transactions):** En la operación **OP02**, se utilizó la funcionalidad de transacción dividida de GnuCash desglosando el cargo en *Equipos (S/ 12,000)* contra dos créditos: *Bancos (S/ 8,000)* y *Proveedores (S/ 4,000)*, garantizando balance cero ([captura_2](capturas/captura_2_transaccion_compuesta_gnucash.png)).
3. **Reportes Exportados a PDF:** Se emitieron los reportes nativos formales requeridos en la Sección 8.D: `Reporte_GnuCash_Balance_General.pdf` y `Reporte_GnuCash_Perdidas_y_Ganancias.pdf`.

---

## SECCIÓN VII: INDICADORES FINANCIEROS Y DIAGNÓSTICO DE SALUD ECONÓMICA

Para profundizar el análisis exigido por Guim-Bustos et al. (2023), se calcularon los principales indicadores de rentabilidad, solvencia y liquidez:

```
+-------------------------------------------------------------------------------------------------------+
|                                    TABLA DE INDICADORES FINANCIEROS                                   |
+--------------------------+---------------------------------+---------------+--------------------------+
| Indicador / Ratio        | Fórmula Contable               | Valor         | Diagnóstico Gerencial    |
+--------------------------+---------------------------------+---------------+--------------------------+
| Margen Bruto             | Utilidad Bruta / Ingresos       | 29.17%        | Eficiencia operativa     |
| Margen Operativo (EBIT)  | Utilidad Operativa / Ingresos   | 10.42%        | Absorbe gastos admin.    |
| Margen Neto              | Utilidad Neta / Ingresos        | 8.33%         | Rentabilidad positiva    |
| Razón Corriente          | Activo Corriente / Pasivo Cte.  | 2.33          | S/ 2.33 respaldo por sol |
| Prueba Ácida             | (Activo Cte. - Inv.) / Pasivo   | 2.33          | Liquidez teórica óptima  |
| Cobertura de Caja Inmed. | Saldo Bancos / Egresos 15 días  | 1.89 veces    | Holgura quincenal segura |
+--------------------------+---------------------------------+---------------+--------------------------+
```

### Diagnóstico de la Situación Financiera
1. **Rentabilidad Técnica Estable pero Vulnerable:** El margen bruto del 29.17% indica que PANVIZ genera S/ 0.29 de excedente por cada sol facturado tras cubrir directamente los sueldos del equipo técnico y la infraestructura cloud. Sin embargo, tras absorber los gastos administrativos (18.75%) y los intereses del crédito bancario (2.08%), el margen neto se contrae a un modesto **8.33% (S/ 2,000.00)**. Cualquier sobrecosto no previsto en el Módulo 2 o incremento en horas de desarrollo transformaría rápidamente este margen en pérdida operativa.
2. **Liquidez Estructural Engañosa:** A simple vista, una razón corriente de **2.33** sugeriría una sólida posición financiera. Sin embargo, este ratio oculta dos distorsiones fundamentales:
   * El pasivo corriente (S/ 22,500.00) contiene S/ 9,000.00 de anticipos de clientes que no demandan desembolso financiero, sino horas hombre de trabajo técnico (NIIF 15).
   * El activo corriente está inflado por S/ 40,000.00 de aportes de capital y S/ 10,000.00 de préstamo, mientras que la cobranza comercial está trabada a 45 días plazo.

---

## SECCIÓN VIII: PRESUPUESTO DE CAJA QUINCENAL Y LA "TRAMPA DE LIQUIDEZ" A 45 DÍAS

### 8.1. Presupuesto de Caja a 15 Días (Visión de Corto Plazo)
El presupuesto de tesorería para la primera quincena de diciembre proyecta los siguientes flujos de efectivo:

| Concepto de Flujo | Importe (S/) | Justificación y Sustento Operacional |
| :--- | :---: | :--- |
| **SALDO INICIAL DISPONIBLE EN BANCOS (Día 1)** | **S/ 44,500.00** | Saldo certificado en cuenta corriente al cierre de noviembre. |
| **(+) Cobros Proyectados Declarados** | **S/ 0.00** | Cliente advirtió cobro de S/ 8,000 a 45 días; no se anticipan cobros. |
| **(-) Egresos Ineludibles Previstos (15 días)** | **(S/ 23,500.00)** | Desembolsos operacionales críticos para la continuidad del servicio: |
| * Remuneraciones previstas del equipo técnico | (S/ 18,000.00) | Nómina técnica requerida para desarrollar el Módulo 2 de alertas. |
| * Servicios de infraestructura en la nube | (S/ 2,000.00) | Mantenimiento de servidores activos y base de datos epidemiológica. |
| * Cancelación de deuda restante con proveedor equipos | (S/ 2,000.00) | Liquidación final del pasivo comercial contraído en la OP02 y OP09. |
| * Remuneraciones administrativas pendientes (OP10) | (S/ 1,500.00) | Pago de salarios administrativos devengados en el cierre previo. |
| **SALDO FINAL PROYECTADO DE CAJA (Día 15)** | **S/ 21,000.00** | **Superávit de caja disponible (Ratio de Cobertura: 1.89 veces).** |

### 8.2. Simulación de Estrés a 45 Días ("La Trampa de Liquidez")
Una gerencia pasiva cometería el grave error de celebrar el superávit de S/ 21,000.00 del día 15. Sin embargo, un análisis riguroso de la tesorería proyectada a 45 días revela una **trampa de liquidez crítica**:

```
                              CRONOGRAMA DE ESTRÉS DE CAJA (DÍAS 1 AL 45)
                                (Demostración de Cesación de Pagos)

  S/ 50k |  [Día 1: S/ 44.5k]
         |       \
  S/ 30k |        \
         |         --> [Día 15: S/ 21.0k]  <-- Aparente tranquilidad
  S/ 10k |                    \
         |                     \
   S/ 0k |-----------------------> [Día 30: S/ 1.0k] -----------------------------
         |                                  \
 -S/ 10k |                                   --> [Día 35-44: -S/ 2.5k DEFICIT] <-- QUIEBRA TÉCNICA
         |                                                    |
         +----------------------------------------------------+--------------------
           Día 1               Día 15              Día 30    Día 44    Día 45 (+S/ 8k)
```

| Intervalo Temporal | Saldo Inicial | Egresos del Ciclo | Cobros Reales | Saldo de Cierre | Alerta y Estado Operativo |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Día 1 al 15 (Quincena 1)** | S/ 44,500.00 | S/ 23,500.00 | S/ 0.00 | **+S/ 21,000.00** | **SUPERÁVIT:** Cobertura de nómina y liquidación de equipos. |
| **Día 16 al 30 (Quincena 2)**| S/ 21,000.00 | S/ 20,000.00 | S/ 0.00 | **+S/ 1,000.00** | **ALARMA EXTREMA:** Nueva nómina (18k) y nube (2k) agotan la caja. |
| **Día 31 al 44 (Días Críticos)**| S/ 1,000.00 | S/ 3,500.00 | S/ 0.00 | **-S/ 2,500.00** | **DEFAULT TÉCNICO:** Imposibilidad de pagar servidores o nómina. |
| **Día 45 (Cobranza Hito 1)** | -S/ 2,500.00 | S/ 0.00 | S/ 8,000.00 | **+S/ 5,500.00** | **RECUPERACIÓN TARDÍA:** El dinero llega después de la parálisis. |

### 8.3. Por qué la Utilidad Contable no Garantiza la Disponibilidad de Efectivo
Este escenario didáctico demuestra de manera irrefutable la tesis de Guim-Bustos et al. (2023):
* Andes Software cerró noviembre con una **Utilidad Neta positiva de S/ 2,000.00**.
* No obstante, dicha utilidad fue generada reconociendo ingresos devengados por S/ 24,000.00 de los cuales la entidad pública solo desembolsó S/ 16,000.00, posponiendo S/ 8,000.00 para dentro de 45 días.
* La empresa mantiene costos fijos operacionales ineludibles (nómina de programadores que no admite mora y servidores cloud que se suspenden automáticamente al tercer día de impago).
* Por lo tanto, entre los días 35 y 44, la empresa experimentará un **déficit neto de caja de S/ 2,500.00**. Si la gerencia no actúa proactivamente antes del día 15, el servicio de salud pública sufrirá la desconexión de PANVIZ por falta de liquidez, demostrando que **la rentabilidad económica mide el éxito comercial, pero solo el flujo de efectivo garantiza la supervivencia institucional**.

---

## SECCIÓN IX: TRES DECISIONES GERENCIALES ESTRATÉGICAS Y CONTINUIDAD SANITARIA

Frente a la brecha financiera diagnosticada, el equipo gerencial de Andes Software formula tres decisiones estratégicas basadas en evidencia contable verificable:

### Decisión 1: Mitigación de la Brecha de Liquidez del Hito 1 mediante Factoring Financiero o Adenda de Pronto Pago
* **Evidencia Contable:** La cuenta *1212 Facturas por Cobrar Comerciales* retiene S/ 8,000.00 con cobranza advertida a 45 días, lo cual desencadena un déficit de -S/ 2,500.00 a partir del día 31.
* **Medida Específica:**
  1. Gestionar de inmediato un contrato de **Factoring Electrónico con recurso** ante la entidad bancaria donde se mantiene la cuenta corriente corporativa, descontando la factura del Hito 1 aceptada por el Estado.
  2. Asumiendo una tasa de descuento mensual de mercado del 2.5%, el costo financiero ascenderá a S/ 200.00, permitiendo la inyección líquida neta inmediata de **S/ 7,800.00** en la cuenta bancaria durante los primeros 7 días de diciembre.
  3. De forma paralela, tramitar ante la administración de la entidad de salud pública una adenda de pronto pago ofreciendo un descuento por pronto desembolso del 2% si liquidan la factura antes del día 15.
* **Responsable Asignado:** Mollo Chuquicaña, Dolly Yadhira (Área de Tesorería y Finanzas).
* **Plazo de Ejecución:** Días 1 al 7 de diciembre (Semana 1 del nuevo ciclo).
* **Impacto en el Servicio de Salud Pública:** Se inyectan S/ 7,800.00 líquidos a la cuenta de bancos, elevando el saldo proyectado del día 35 de -S/ 2,500.00 a un **superávit protegido de +S/ 5,300.00**. Se garantiza el pago puntual e íntegro de los salarios de los desarrolladores, evitando huelgas, deserciones de ingenieros clave y garantizando que la carga diaria de indicadores epidemiológicos continúe operando ininterrumpidamente en los hospitales.

### Decisión 2: Aceleración Técnica y Certificación Anticipada del Módulo 2 (Hito Anticipado)
* **Evidencia Contable:** El pasivo *4699 Anticipos de Clientes* inmoviliza S/ 9,000.00 que figuran como obligación pendiente (NIIF 15). Mientras el Módulo de Alertas y Reportes no cuente con acta de entrega-recepción, no se puede devengar dicho ingreso ni emitir la facturación complementaria del segundo hito contractual.
* **Medida Específica:**
  1. Reorganizar los sprints de desarrollo bajo metodología Scrum focalizando el 100% de la capacidad técnica en las funciones críticas del Módulo 2: motor de detección de brotes epidemiológicos y generación de fichas en PDF.
  2. Implementar un plan de pruebas de integración continua (CI/CD) junto al equipo técnico del Ministerio de Salud para adelantar la validación de aceptación al día 25 de diciembre.
* **Responsable Asignado:** Chambilla Perca, Ricardo Mauricio (Líder Técnico de Desarrollo).
* **Plazo de Ejecución:** Días 1 al 25 de diciembre.
* **Impacto en el Servicio de Salud Pública:** Permite devengar contractualmente los S/ 9,000.00 del anticipo transformándolos de pasivo a ingreso ganado, y habilita legalmente el cobro del segundo desembolso del contrato. En términos sanitarios, adelanta en 10 días la puesta en marcha de las alertas tempranas automatizadas frente a epidemias de dengue e infecciones respiratorias agudas.

### Decisión 3: Reprogramación Comercial de Proveedor de Equipos y Optimización de la Infraestructura en la Nube
* **Evidencia Contable:** El presupuesto de 15 días contempla desembolsar S/ 2,000.00 para cancelar la totalidad de la deuda con el proveedor de hardware (*cuenta 4212*) y S/ 2,000.00 en consumo cloud (*cuenta 6942*), absorbiendo S/ 4,000.00 en la primera quincena.
* **Medida Específica:**
  1. Negociar con el proveedor de equipos informáticos la reprogramación del saldo de S/ 2,000.00 en dos cuotas iguales de S/ 1,000.00 a 15 y 45 días, apalancándose en la relación de socio tecnológico a largo plazo.
  2. Efectuar una auditoría de consumo cloud en el proveedor tecnológico: migrar instancias de desarrollo sobredimensionadas a esquemas *serverless* o adquirir instancias reservadas anuales con descuento del 25%, reduciendo el consumo mensual de nube de S/ 2,000.00 a S/ 1,500.00 sin degradar el rendimiento.
* **Responsable Asignado:** Gutiérrez Ccama, Juan Diego (Operaciones y Contabilidad).
* **Plazo de Ejecución:** Días 5 al 12 de diciembre.
* **Impacto en el Servicio de Salud Pública:** Libera de inmediato S/ 1,500.00 de presión de caja en la primera quincena. Asimismo, la optimización cloud blinda la disponibilidad del sistema garantizando un Acuerdo de Nivel de Servicio (**SLA**) de 99.9% de uptime para la recepción y procesamiento de datos clínicos enviados desde postas y centros de salud remotos.

---

## SECCIÓN X: MATRIZ DE RESPONSABILIDADES Y REVISIÓN CRUZADA

Con el propósito de cumplir rigurosamente el requerimiento de participación verificable y control de calidad entre pares (Sección 8.E de `trab_53.pdf`), se implementó la siguiente matriz circular de revisión cruzada entre los cuatro integrantes del equipo:

| Integrante del Equipo | Rol Operativo | Secciones e Instrumentos Custodiados | Revisión Cruzada Asignada | Estado y Conformidad |
| :--- | :--- | :--- | :--- | :---: |
| **Suclle Suca, Michael Benjamin** | Coordinador General y Auditor Gerencial | Coordinación general, Control de Lectura 43 (Slide 43), Síntesis Crítica de lectura, Integración del Informe Final MD y Presentación HTML interactiva. | **Revisa:** Indicadores, Presupuesto Quincenal, Análisis de Estrés 45 días y Decisiones Gerenciales elaboradas por Mollo Chuquicaña. | **CONFORME (100%)** |
| **Chambilla Perca, Ricardo Mauricio** | Especialista Contable y Modelado de Datos | Catálogo Mínimo de Cuentas, Asientos Libro Diario (OP01–OP11), Libro Mayor, Balance de Comprobación y hojas `Cuentas`, `Diario`, `Mayor`, `Comprobación` en Calc. | **Revisa:** Síntesis Crítica, fundamentos teóricos y respuestas al Control de Lectura 43 formuladas por Suclle Suca. | **CONFORME (100%)** |
| **Gutiérrez Ccama, Juan Diego** | Especialista en Reportes y Conciliación | Estados Financieros (ESF, EERR, EFE, Patrimonio), modelo en GnuCash XML (`PANVIZ.gnucash`), reportes oficiales PDF y hoja `Conciliación GnuCash`. | **Revisa:** Libro Diario, Libro Mayor y consistencia matemática de la partida doble y comprobación de Chambilla Perca. | **CONFORME (100%)** |
| **Mollo Chuquicaña, Dolly Yadhira** | Analista de Liquidez, Ratios y Tesorería | Ratios Financieros, Presupuesto de Caja a 15 y 45 días, Simulación de Déficit de Caja, Hoja `Caja 15 días` y redacción de las Tres Decisiones Estratégicas. | **Revisa:** Estados Financieros (ESF, Resultados, Flujo Directo) y matriz de conciliación Calc vs. GnuCash de Gutiérrez Ccama. | **CONFORME (100%)** |

---

## SECCIÓN XI: CONCLUSIONES Y REFERENCIAS BIBLIOGRÁFICAS

### Conclusiones Principales
1. **La Ecuación Contable como Garantía de Integridad Sistémica:** Se comprobó la vigencia irrestricta de la ecuación fundamental del patrimonio ($\text{Activo} = \text{Pasivo} + \text{Patrimonio}$) totalizando S/ 64,500.00 tanto en la hoja de cálculo de LibreOffice Calc como en la plataforma contable GnuCash, con una diferencia neta absoluta de S/ 0.00 en todas las cuentas y rubros.
2. **La Validez Normativa de las NIIF en el Modelado de Software:** La aplicación estricta de la NIIF 15 (clasificación del anticipo de S/ 9,000 como pasivo) y la NIC 16 (activación de hardware por S/ 12,000 como PPE) evitó distorsiones severas en la utilidad neta de Andes Software, reflejando que la ganancia real del mes fue de S/ 2,000.00 (margen neto del 8.33%).
3. **El Flujo de Efectivo como Determinante de la Supervivencia:** Se confirmó la advertencia teórica de Guim-Bustos et al. (2023): una empresa de software puede reportar ganancias contables legítimas y simultáneamente entrar en suspensión de pagos técnica. El desfase temporal de 45 días en el cobro de facturas a instituciones del Estado absorbe la liquidez disponible, haciendo imperativa la gestión proactiva mediante factoring, control del hito diferido y renegociación de pasivos para salvaguardar un sistema vital para la salud pública como PANVIZ.
4. **Articulación Multidisciplinaria en Ingeniería de Sistemas:** El ejercicio demostró que un ingeniero de software no puede aislarse en la arquitectura tecnológica del código; el dominio del lenguaje económico-contable es indispensable para gobernar presupuestos, negociar contratos y liderar proyectos tecnológicos con viabilidad sostenible.

---

### Referencias Bibliográficas (Normas APA 7ma Edición)

* Guim-Bustos, P., Martillo-Mieles, O., Guerrero-Cortez, V. y Carrillo-Pérez, F. (2023). Los estados financieros y las tomas de decisiones empresariales. *593 Digital Publisher CEIT*, 8(2), 149–160. https://doi.org/10.33386/593dp.2023.2.1679
* International Accounting Standards Board (IASB). (2018). *Norma Internacional de Información Financiera 15: Ingresos de Actividades Ordinarias Procedentes de Contratos con Clientes (NIIF 15)*. Fundación IFRS.
* International Accounting Standards Board (IASB). (2018). *Norma Internacional de Contabilidad 16: Propiedad, Planta y Equipo (NIC 16)*. Fundación IFRS.
* International Accounting Standards Board (IASB). (2018). *Norma Internacional de Contabilidad 7: Estado de Flujos de Efectivo (NIC 7)*. Fundación IFRS.
* Ministerio de Economía y Finanzas del Perú (MEF). (2019). *Plan Contable General Empresarial (PCGE) Modificado 2019*. Dirección General de Contabilidad Pública.
* Pressman, R. S. y Maxim, B. R. (2021). *Ingeniería del software: Un enfoque práctico* (9.ª ed.). McGraw-Hill Interamericana.
