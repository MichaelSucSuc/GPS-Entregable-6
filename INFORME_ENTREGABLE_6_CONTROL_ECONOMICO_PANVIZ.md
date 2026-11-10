# INFORME TÉCNICO DE CONTROL ECONÓMICO
# PROYECTO DE SOFTWARE PANVIZ (ANDES SOFTWARE)
**Curso:** Gestión de Proyectos de Software (Semana 11)  
**Institución:** Universidad Nacional de San Agustín de Arequipa (UNSA)  
**Facultad:** Facultad de Ingeniería de Producción y Servicios (FIPS)  
**Escuela Profesional:** Escuela Profesional de Ingeniería de Sistemas (EPIS)  
**Docente:** M en C Jesús Martín Silva Fernández (`jsilvaf@unsa.edu.pe`)  
**Equipo de Trabajo:** Equipo 06  
**Fecha de Emisión:** 10 de noviembre de 2026  

---

### Integrantes del Equipo:
1. **Suclle Suca, Michael Benjamin** (CUI: 20210678) — `msuclles@unsa.edu.pe`  
   *Responsabilidad:* Coordinación general, síntesis crítica de lectura e integración del informe.
2. **Fernandez Huarca, Rodrigo Alexander** (CUI: 20210672) — `rfernandezh@unsa.edu.pe`  
   *Responsabilidad:* Catálogo de cuentas y registros en la plataforma contable GnuCash.
3. **Meza Vizcarra, Cielo Cristal** (CUI: 20210685) — `cmezav@unsa.edu.pe`  
   *Responsabilidad:* Libro Diario, Libro Mayor y Balance de Comprobación en hoja de cálculo (Calc/Excel).
4. **Borda Espinoza, Gabriela Nayely** (CUI: 20210665) — `gbordae@unsa.edu.pe`  
   *Responsabilidad:* Elaboración de los 4 estados financieros básicos y matriz de conciliación.
5. **Ccoscco Alvis, Italo Frankdux** (CUI: 20210669) — `iccosccoa@unsa.edu.pe`  
   *Responsabilidad:* Indicadores financieros, presupuesto de caja y formulación de decisiones estratégicas.

---

## 1. Análisis y Síntesis Crítica de la Lectura

**Referencia del artículo:**  
Guim-Bustos, P., Martillo-Mieles, O., Guerrero-Cortez, V. y Carrillo-Pérez, F. (2023). Los estados financieros y las tomas de decisiones empresariales. *593 Digital Publisher CEIT*, 8(2), 149–160. DOI: `10.33386/593dp.2023.2.1679`.  
**Páginas consultadas:** 152–154.  
**Conteo de palabras de la síntesis:** 305 palabras.

### Síntesis Crítica:
Los estados financieros representan el producto estructurado y culminante del proceso contable, cuyo objetivo fundamental es sintetizar la posición patrimonial, el desempeño operativo y los flujos monetarios de una entidad en un período determinado (Guim-Bustos et al., 2023, p. 152). Limitar la contabilidad al mero cumplimiento formal del registro en libros resulta estéril para la gerencia si la información cuantitativa no se somete a un análisis e interpretación sistemática que fundamente la toma de decisiones estratégicas. Como destacan Castrellón (2021) y Suanders (2006), citados en el texto (pp. 153–154), las decisiones gerenciales no pueden formularse a ciegas: requieren evaluar con certeza si las operaciones generan valor o pérdidas, y si las políticas de financiamiento y comercialización comprometen la viabilidad futura del negocio.

Del análisis de las páginas 152 a 154 se desprenden dos ideas medulares aplicables al control económico del proyecto PANVIZ:  
1. **La diferenciación estricta de la estructura de costos (p. 154):** En el desarrollo de software es indispensable clasificar con precisión los costos directos (remuneraciones técnicas de los desarrolladores y consumo de servidores en la nube asignables al producto) frente a los gastos administrativos indirectos. Esta discriminación previene distorsiones en el cálculo del margen de contribución de cada hito contractual.  
2. **El desfase temporal entre presupuestación, devengo y liquidez real (pp. 152–153):** Brune (2019) advierte que contar con proyecciones de ingresos resulta inútil sin una confirmación estricta de las fechas efectivas de pago de los clientes. En proyectos tecnológicos, registrar ingresos devengados por hitos aprobados no garantiza liquidez inmediata para solventar nóminas o servidores, demandando un monitoreo riguroso del flujo de caja de corto plazo para evitar la parálisis operativa del servicio.

---

## 2. Clasificación Contable, Catálogo de Cuentas y Registros

### 2.1 Catálogo Mínimo de Cuentas (PCGE vs. GnuCash)
Para el registro de Andes Software en el proyecto PANVIZ se estableció el siguiente catálogo estructurado bajo el Plan Contable General Empresarial (PCGE) y su mapeo al estándar de cuentas de GnuCash:

| Código PCGE | Cuenta Contable | Elemento Contable | Naturaleza | Categoría GnuCash | Cuenta Mapeada en GnuCash |
|:---:|---|:---:|:---:|:---:|---|
| **1041** | Bancos - Cuentas Corrientes | Activo Corriente | Deudora | `Asset:Bank` | `Activos:Activo Corriente:Bancos:Cuenta Corriente` |
| **1212** | Cuentas por Cobrar Comerciales | Activo Corriente | Deudora | `Asset:Receivable` | `Activos:Activo Corriente:Clientes:Facturas por Cobrar` |
| **3361** | Equipos de Cómputo e Informáticos | Activo No Corriente | Deudora | `Asset:Fixed Asset` | `Activos:Activo Fijo:Equipos Informáticos` |
| **4111** | Remuneraciones por Pagar | Pasivo Corriente | Acreedora | `Liability:Payroll` | `Pasivos:Pasivo Corriente:Sueldos por Pagar` |
| **4212** | Cuentas por Pagar Proveedores | Pasivo Corriente | Acreedora | `Liability:Payable` | `Pasivos:Pasivo Corriente:Proveedores:Equipos` |
| **4511** | Préstamo Bancario (Corto Plazo) | Pasivo Corriente | Acreedora | `Liability:Loan` | `Pasivos:Pasivo Corriente:Préstamos Bancarios` |
| **4699** | Anticipos de Clientes (Diferidos) | Pasivo Corriente | Acreedora | `Liability:Unearned` | `Pasivos:Pasivo Corriente:Anticipos de Clientes` |
| **5011** | Capital Social (Aportes de Socios) | Patrimonio Neto | Acreedora | `Equity:Paid-in` | `Patrimonio:Capital Social:Aportes` |
| **5911** | Resultado del Ejercicio (Utilidad) | Patrimonio Neto | Acreedora | `Equity:Retained` | `Patrimonio:Resultados Acumulados:Resultado del Mes` |
| **7041** | Ingresos por Servicios de Software | Ingresos | Acreedora | `Income:Sales` | `Ingresos:Ventas:Desarrollo de Software` |
| **6941** | Costo: Remuneraciones Desarrollo | Costo del Servicio | Deudora | `Expense:Labor` | `Gastos:Costo del Servicio:Remuneraciones Desarrollo` |
| **6942** | Costo: Alojamiento en la Nube | Costo del Servicio | Deudora | `Expense:Hosting` | `Gastos:Costo del Servicio:Servicios de Nube` |
| **9411** | Gastos Administrativos Generales | Gasto Operativo | Deudora | `Expense:Admin` | `Gastos:Gastos Administrativos:Operativos Generales` |
| **9412** | Gastos Adm. Sueldos Devengados | Gasto Operativo | Deudora | `Expense:Payroll` | `Gastos:Gastos Administrativos:Remuneraciones` |
| **9711** | Gastos Financieros (Intereses) | Gasto Financiero | Deudora | `Expense:Interest` | `Gastos:Gastos Financieros:Intereses Bancarios` |

---

### 2.2 Clasificación y Sustento Técnico de las 11 Operaciones del Mes
A continuación, se detalla la clasificación técnica y el razonamiento contable de cada operación registrada en el mes de noviembre de 2026:

1. **OP01 (02/11/2026) — Aporte inicial de socios:**
   - *Debe:* `1041 Bancos` S/ 40,000.00 (+Activo)
   - *Haber:* `5011 Capital Social` S/ 40,000.00 (+Patrimonio)
   - *Sustento:* Constitución de la entidad con aporte en efectivo de los socios depositado directamente en la cuenta corriente bancaria.
2. **OP02 (05/11/2026) — Compra de equipos informáticos:**
   - *Debe:* `3361 Equipos Informáticos` S/ 12,000.00 (+Activo No Corriente)
   - *Haber:* `1041 Bancos` S/ 8,000.00 (-Activo)
   - *Haber:* `4212 Cuentas por Pagar Proveedores` S/ 4,000.00 (+Pasivo)
   - *Sustento:* Adquisición de servidores y estaciones de trabajo para el desarrollo de PANVIZ. Se cancela el 66.67% de contado y se genera una obligación comercial a corto plazo con el proveedor por el saldo.
3. **OP03 (07/11/2026) — Préstamo bancario recibido:**
   - *Debe:* `1041 Bancos` S/ 10,000.00 (+Activo)
   - *Haber:* `4511 Préstamo Bancario` S/ 10,000.00 (+Pasivo Corriente)
   - *Sustento:* Obtención de financiamiento externo para capital de trabajo con vencimiento a 6 meses. No constituye ingreso por ventas sino una deuda financiera.
4. **OP04 (10/11/2026) — Anticipo de cliente por módulo futuro:**
   - *Debe:* `1041 Bancos` S/ 9,000.00 (+Activo)
   - *Haber:* `4699 Anticipos de Clientes` S/ 9,000.00 (+Pasivo Corriente)
   - *Sustento:* Cobro adelantado por el módulo de alertas y reportes que se desarrollará en el mes siguiente. Al no haberse devengado el servicio, constituye un pasivo por ingresos diferidos (obligación de desempeño exigible).
5. **OP05 (15/11/2026) — Remuneraciones de desarrollo del mes:**
   - *Debe:* `6941 Costo de Servicio - Remuneraciones` S/ 15,000.00 (+Costo / Resultado)
   - *Haber:* `1041 Bancos` S/ 15,000.00 (-Activo)
   - *Sustento:* Desembolso para el pago del equipo de programadores, analistas y arquitectos de software dedicados exclusivamente al hito 1 de PANVIZ. Se reconocen como costo del servicio del mes y no como activo intangible según las bases.
6. **OP06 (18/11/2026) — Servicios de nube consumidos:**
   - *Debe:* `6942 Costo de Servicio - Nube` S/ 2,000.00 (+Costo / Resultado)
   - *Haber:* `1041 Bancos` S/ 2,000.00 (-Activo)
   - *Sustento:* Pago en efectivo de la factura de consumo de servidores, bases de datos y microservicios en la nube requeridos para compilar y desplegar PANVIZ.
7. **OP07 (20/11/2026) — Gastos administrativos pagados:**
   - *Debe:* `9411 Gastos Administrativos Generales` S/ 3,000.00 (+Gasto / Resultado)
   - *Haber:* `1041 Bancos` S/ 3,000.00 (-Activo)
   - *Sustento:* Pago de servicios auxiliares, licenciamiento administrativo y consumos de oficina no asignables directamente a la ingeniería del software.
8. **OP08 (25/11/2026) — Entrega y aceptación de Hito 1 PANVIZ:**
   - *Debe:* `1041 Bancos` S/ 16,000.00 (+Activo)
   - *Debe:* `1212 Cuentas por Cobrar Comerciales` S/ 8,000.00 (+Activo)
   - *Haber:* `7041 Ingresos por Servicios de Software` S/ 24,000.00 (+Ingreso / Resultado)
   - *Sustento:* Reconocimiento del ingreso devengado por la conformidad formal del cliente del módulo de carga y visualización de indicadores. Se cobran S/ 16,000 al contado y S/ 8,000 quedan como derecho exigible con cobro advertido a 45 días.
9. **OP09 (27/11/2026) — Amortización de deuda con proveedor:**
   - *Debe:* `4212 Cuentas por Pagar Proveedores` S/ 2,000.00 (-Pasivo)
   - *Haber:* `1041 Bancos` S/ 2,000.00 (-Activo)
   - *Sustento:* Disminución de la obligación comercial pendiente por los equipos informáticos adquiridos en la OP02 mediante transferencia bancaria.
10. **OP10 (30/11/2026) — Remuneraciones administrativas devengadas pendientes:**
    - *Debe:* `9412 Gastos Adm. Sueldos Devengados` S/ 1,500.00 (+Gasto / Resultado)
    - *Haber:* `4111 Remuneraciones por Pagar` S/ 1,500.00 (+Pasivo)
    - *Sustento:* Devengo del sueldo del personal administrativo correspondiente a noviembre no pagado al cierre, registrando el pasivo laboral correspondiente.
11. **OP11 (30/11/2026) — Pago de intereses bancarios:**
    - *Debe:* `9711 Gastos Financieros - Intereses` S/ 500.00 (+Gasto Financiero / Resultado)
    - *Haber:* `1041 Bancos` S/ 500.00 (-Activo)
    - *Sustento:* Retribución financiera mensual por el préstamo bancario recibido en OP03; no amortiza el capital principal de la deuda.

---

### 2.3 Libro Diario General (Corte 30/11/2026)

| Fecha | N° Op. | Código | Cuenta Contable | Glosa / Descripción | Debe (S/) | Haber (S/) |
|:---:|:---:|:---:|---|---|---:|---:|
| 02/11/2026 | OP01 | 1041 | Bancos - Cuentas Corrientes | Aporte inicial de socios en cta. cte. | 40,000.00 | - |
| 02/11/2026 | OP01 | 5011 | Capital Social | Constitución de capital social | - | 40,000.00 |
| 05/11/2026 | OP02 | 3361 | Equipos Informáticos | Compra de estaciones y servidores | 12,000.00 | - |
| 05/11/2026 | OP02 | 1041 | Bancos - Cuentas Corrientes | Pago 66.7% inicial con transferencia | - | 8,000.00 |
| 05/11/2026 | OP02 | 4212 | Proveedores por Pagar | Saldo pendiente proveedor equipos | - | 4,000.00 |
| 07/11/2026 | OP03 | 1041 | Bancos - Cuentas Corrientes | Desembolso préstamo bancario a 6m | 10,000.00 | - |
| 07/11/2026 | OP03 | 4511 | Préstamo Bancario | Obligación financiera a corto plazo | - | 10,000.00 |
| 10/11/2026 | OP04 | 1041 | Bancos - Cuentas Corrientes | Anticipo recibido por módulo futuro | 9,000.00 | - |
| 10/11/2026 | OP04 | 4699 | Anticipos de Clientes | Ingreso diferido servicio no prestado | - | 9,000.00 |
| 15/11/2026 | OP05 | 6941 | Costo Remuneraciones Dev. | Planilla técnica desarrollo PANVIZ | 15,000.00 | - |
| 15/11/2026 | OP05 | 1041 | Bancos - Cuentas Corrientes | Pago de sueldos de desarrollo | - | 15,000.00 |
| 18/11/2026 | OP06 | 6942 | Costo Servicios de Nube | Consumo de infraestructura cloud | 2,000.00 | - |
| 18/11/2026 | OP06 | 1041 | Bancos - Cuentas Corrientes | Cancelación de factura de nube | - | 2,000.00 |
| 20/11/2026 | OP07 | 9411 | Gastos Administrativos | Gastos de operación administrativa | 3,000.00 | - |
| 20/11/2026 | OP07 | 1041 | Bancos - Cuentas Corrientes | Pago bancario de gastos generales | - | 3,000.00 |
| 25/11/2026 | OP08 | 1041 | Bancos - Cuentas Corrientes | Cobranza contado Hito 1 aceptado | 16,000.00 | - |
| 25/11/2026 | OP08 | 1212 | Cuentas por Cobrar | Saldo por cobrar a 45 días | 8,000.00 | - |
| 25/11/2026 | OP08 | 7041 | Ingresos por Software | Reconocimiento devengado Hito 1 | - | 24,000.00 |
| 27/11/2026 | OP09 | 4212 | Proveedores por Pagar | Amortización deuda hardware | 2,000.00 | - |
| 27/11/2026 | OP09 | 1041 | Bancos - Cuentas Corrientes | Pago transferencia a proveedor | - | 2,000.00 |
| 30/11/2026 | OP10 | 9412 | Gastos Adm. Sueldos | Devengo sueldo administrativo | 1,500.00 | - |
| 30/11/2026 | OP10 | 4111 | Remuneraciones por Pagar | Sueldos por pagar fin de mes | - | 1,500.00 |
| 30/11/2026 | OP11 | 9711 | Gastos Financieros | Intereses devengados préstamo | 500.00 | - |
| 30/11/2026 | OP11 | 1041 | Bancos - Cuentas Corrientes | Pago de intereses desde cuenta | - | 500.00 |
| **TOTALES** | | | | **SUMATORIA GENERAL** | **119,000.00** | **119,000.00** |

> **Control de Partida Doble en Diario:**  
> $\sum \text{Debe} - \sum \text{Haber} = \text{S/ } 119,000.00 - \text{S/ } 119,000.00 = \mathbf{S/\ 0.00}$ (Comprobado y conforme).

---

### 2.4 Libro Mayor y Balance de Comprobación

| Código | Cuenta Contable | Total Debe (S/) | Total Haber (S/) | Saldo Deudor (S/) | Saldo Acreedor (S/) |
|:---:|---|---:|---:|---:|---:|
| **1041** | Bancos - Cuentas Corrientes | 75,000.00 | 30,500.00 | **44,500.00** | - |
| **1212** | Cuentas por Cobrar Comerciales | 8,000.00 | 0.00 | **8,000.00** | - |
| **3361** | Equipos de Cómputo e Informáticos | 12,000.00 | 0.00 | **12,000.00** | - |
| **4111** | Remuneraciones por Pagar | 0.00 | 1,500.00 | - | **1,500.00** |
| **4212** | Cuentas por Pagar Proveedores | 2,000.00 | 4,000.00 | - | **2,000.00** |
| **4511** | Préstamo Bancario Corto Plazo | 0.00 | 10,000.00 | - | **10,000.00** |
| **4699** | Anticipos de Clientes | 0.00 | 9,000.00 | - | **9,000.00** |
| **5011** | Capital Social | 0.00 | 40,000.00 | - | **40,000.00** |
| **7041** | Ingresos por Servicios de Software | 0.00 | 24,000.00 | - | **24,000.00** |
| **6941** | Costo: Remuneraciones Desarrollo | 15,000.00 | 0.00 | **15,000.00** | - |
| **6942** | Costo: Alojamiento en la Nube | 2,000.00 | 0.00 | **2,000.00** | - |
| **9411** | Gastos Administrativos Generales | 3,000.00 | 0.00 | **3,000.00** | - |
| **9412** | Gastos Adm. Sueldos Devengados | 1,500.00 | 0.00 | **1,500.00** | - |
| **9711** | Gastos Financieros (Intereses) | 500.00 | 0.00 | **500.00** | - |
| **TOTALES** | **BALANCE DE COMPROBACIÓN** | **119,000.00** | **119,000.00** | **86,500.00** | **86,500.00** |

> **Controles de Comprobación:**  
> 1. $\sum \text{Sumas Debe} = \sum \text{Sumas Haber} = \text{S/ } 119,000.00$ (Diferencia = S/ 0.00).  
> 2. $\sum \text{Saldos Deudores} = \sum \text{Saldos Acreedores} = \text{S/ } 86,500.00$ (Diferencia = S/ 0.00).

---

## 3. Estados Financieros al Cierre del Mes

### 3.1 Estado de Resultados del 01 al 30 de Noviembre de 2026
*(Expresado en Soles - S/)*

| Código | Concepto | Importe (S/) | Análisis Vertical (%) |
|:---:|---|---:|---:|
| **7041** | **Ingresos de Actividades Ordinarias (Hito 1 PANVIZ)** | **24,000.00** | **100.00%** |
| 6941 | (-) Costo del Servicio: Remuneraciones de Desarrollo | (15,000.00) | -62.50% |
| 6942 | (-) Costo del Servicio: Infraestructura Cloud / Nube | (2,000.00) | -8.33% |
| | **TOTAL COSTO DEL SERVICIO** | **(17,000.00)** | **-70.83%** |
| | **UTILIDAD BRUTA** | **7,000.00** | **29.17%** |
| 9411 | (-) Gastos Administrativos Generales Pagados | (3,000.00) | -12.50% |
| 9412 | (-) Gastos Administrativos: Sueldos Devengados | (1,500.00) | -6.25% |
| | **TOTAL GASTOS ADMINISTRATIVOS** | **(4,500.00)** | **-18.75%** |
| | **UTILIDAD OPERATIVA** | **2,500.00** | **10.42%** |
| 9711 | (-) Gastos Financieros: Intereses del Préstamo Bancario | (500.00) | -2.08% |
| | **RESULTADO ANTES DE IMPUESTOS** | **2,000.00** | **8.33%** |
| | (-) Impuesto a la Renta *(Omitido por bases didácticas)* | 0.00 | 0.00% |
| **5911** | **UTILIDAD NETA DEL EJERCICIO** | **2,000.00** | **8.33%** |

---

### 3.2 Estado de Situación Financiera al 30 de Noviembre de 2026
*(Expresado en Soles - S/)*

```
=============================================================================================
ACTIVO                                           PASIVO Y PATRIMONIO NETO
=============================================================================================
ACTIVO CORRIENTE                                 PASIVO CORRIENTE
1041 Efectivo y Equiv. (Bancos)   S/ 44,500.00   4212 Proveedores Comerciales     S/  2,000.00
1212 Cuentas por Cobrar           S/  8,000.00   4511 Préstamo Bancario (6m)      S/ 10,000.00
----------------------------------------------   4699 Anticipos de Clientes       S/  9,000.00
Total Activo Corriente            S/ 52,500.00   4111 Remuneraciones por Pagar    S/  1,500.00
                                                 --------------------------------------------
ACTIVO NO CORRIENTE                              Total Pasivo Corriente           S/ 22,500.00
3361 Equipos de Cómputo (Fijo)    S/ 12,000.00   
----------------------------------------------   PATRIMONIO NETO
Total Activo No Corriente         S/ 12,000.00   5011 Capital Social              S/ 40,000.00
                                                 5911 Resultado del Ejercicio     S/  2,000.00
                                                 --------------------------------------------
                                                 Total Patrimonio Neto            S/ 42,000.00
=============================================================================================
TOTAL ACTIVO                      S/ 64,500.00   TOTAL PASIVO Y PATRIMONIO        S/ 64,500.00
=============================================================================================
CONTROL ECUACIÓN PATRIMONIAL: ACTIVO - PASIVO - PATRIMONIO = S/ 0.00 (EXACTO Y CONFORME)
=============================================================================================
```

---

### 3.3 Estado de Cambios en el Patrimonio Neto
*(Del 01 al 30 de Noviembre de 2026 - En Soles S/)*

| Concepto Patrimonial | Capital Social (S/) | Resultados Acumulados (S/) | Total Patrimonio Neto (S/) |
|---|---:|---:|---:|
| **Saldo Inicial al 01/11/2026** | **0.00** | **0.00** | **0.00** |
| (+) Aporte de Capital de los Socios (OP01) | 40,000.00 | 0.00 | 40,000.00 |
| (+) Utilidad Neta del Ejercicio (Mes 1) | 0.00 | 2,000.00 | 2,000.00 |
| **SALDO FINAL AL 30/11/2026** | **40,000.00** | **2,000.00** | **42,000.00** |

> **Comprobación Patrimonial:**  
> $\text{Variación Patrimonial sin aportes} = \text{Saldo Final} - \text{Aportes} = \text{S/ } 42,000.00 - \text{S/ } 40,000.00 = \mathbf{S/\ 2,000.00} \equiv \text{Resultado del Mes}$.

---

### 3.4 Estado de Flujos de Efectivo (Método Directo)
*(Del 01 al 30 de Noviembre de 2026 - En Soles S/)*

**Declaración del Criterio Contable de Intereses (NIC 7, párrafo 31):**  
Los intereses pagados por el préstamo bancario (S/ 500.00) se clasifican expresamente en **Actividades de Operación**, debido a que el crédito fue contratado como capital de trabajo para solventar los desfases operativos de nómina e infraestructura del proyecto de software. Se mantiene este criterio en todas las hojas y conciliaciones.

| Concepto / Línea de Flujo de Efectivo | Referencia OP | Cobros / Entradas (S/) | Pagos / Salidas (S/) | Flujo Neto (S/) |
|---|:---:|---:|---:|---:|
| **1. ACTIVIDADES DE OPERACIÓN** | | | | |
| Cobranza en efectivo por entrega de Hito 1 PANVIZ | OP08 | 16,000.00 | - | |
| Anticipo en efectivo recibido de la entidad de salud | OP04 | 9,000.00 | - | |
| (-) Pago de remuneraciones de desarrollo de software | OP05 | - | (15,000.00) | |
| (-) Pago de servicios de nube e infraestructura | OP06 | - | (2,000.00) | |
| (-) Pago de gastos administrativos operativos | OP07 | - | (3,000.00) | |
| (-) Pago de intereses financieros del préstamo | OP11 | - | (500.00) | |
| **Flujo Neto de Actividades de Operación** | | **25,000.00** | **(20,500.00)** | **+4,500.00** |
| | | | | |
| **2. ACTIVIDADES DE INVERSIÓN** | | | | |
| (-) Pago de cuota inicial por compra de equipos | OP02 | - | (8,000.00) | |
| (-) Pago posterior de amortización a proveedor hardware | OP09 | - | (2,000.00) | |
| **Flujo Neto de Actividades de Inversión** | | **0.00** | **(10,000.00)** | **(10,000.00)** |
| | | | | |
| **3. ACTIVIDADES DE FINANCIACIÓN** | | | | |
| Aporte de capital social inicial por los socios | OP01 | 40,000.00 | - | |
| Desembolso de préstamo bancario obtenido (capital) | OP03 | 10,000.00 | - | |
| **Flujo Neto de Actividades de Financiación** | | **50,000.00** | **0.00** | **+50,000.00** |
| | | | | |
| **VARIACIÓN NETA DE EFECTIVO DEL PERIODO** | | | | **+44,500.00** |
| (+) Saldo Inicial de Efectivo al 01/11/2026 | | | | **0.00** |
| **SALDO FINAL DE EFECTIVO EN BANCOS AL 30/11/2026** | | | | **44,500.00** |

> **Control de Flujo:**  
> $\text{Saldo Final de Flujo} - \text{Saldo Cuenta Bancos} = \text{S/ } 44,500.00 - \text{S/ } 44,500.00 = \mathbf{S/\ 0.00}$ (Conciliación perfecta).

---

## 4. Verificación con Fórmulas, Sustentaciones Teóricas y Conciliación

### 4.1 Comprobaciones Obligatorias
1. **Debe = Haber:**  
   Total Debe (S/ 119,000.00) = Total Haber (S/ 119,000.00). **Diferencia: S/ 0.00.**
2. **Activo = Pasivo + Patrimonio:**  
   $\text{S/ } 64,500.00 = \text{S/ } 22,500.00 + \text{S/ } 42,000.00 = \text{S/ } 64,500.00$. **Diferencia: S/ 0.00.**
3. **Resultado del Mes = Variación Patrimonial sin Aportes:**  
   $\text{Variación} = \text{Patrimonio Final (S/ } 42,000.00) - \text{Aportes (S/ } 40,000.00) = \text{S/ } 2,000.00 \equiv \text{Utilidad Neta (S/ } 2,000.00)$. **Diferencia: S/ 0.00.**
4. **Saldo Final del Flujo = Saldo en Bancos:**  
   Saldo Flujo (S/ 44,500.00) = Saldo Cuenta 1041 Bancos (S/ 44,500.00). **Diferencia: S/ 0.00.**

---

### 4.2 Respuestas Conceptuales Rigurosas

#### ¿Por qué el anticipo es un pasivo y no una utilidad o ingreso?
Conforme al Marco Conceptual de las NIIF y a la NIIF 15 (*Ingresos de Actividades Ordinarias Procedentes de Contratos con Clientes*), los ingresos únicamente pueden reconocerse cuando una entidad satisface una obligación de desempeño mediante la transferencia del control de los bienes o servicios comprometidos al cliente.  
En la operación OP04, la entidad de salud pública desembolsó S/ 9,000.00 de manera anticipada por un módulo de software (alertas y reportes) que no ha sido programado ni desplegado al cierre del mes. Ese dinero no constituye ganancia ni rendimiento económico porque no ha existido contraprestación alguna por parte de Andes Software; por el contrario, genera una **obligación presente ineludible** de destinar personal técnico y servidores para construir y entregar dicho módulo en el futuro. Si Andes Software no ejecutase el servicio, la entidad pública tiene el derecho legal exigible de demandar la restitución íntegra de los fondos. Por consiguiente, registrar el anticipo como ingreso distorsionaría la realidad económica inflando fraudulentamente la utilidad, cuando técnicamente es un **pasivo exigible por ingresos diferidos**.

#### ¿Por qué comprar equipos no equivale a reconocer un gasto completo del mes?
De acuerdo con la NIC 16 (*Propiedad, Planta y Equipo*), un activo se define como un recurso económico controlado por la entidad como resultado de sucesos pasados, del cual se espera obtener beneficios económicos futuros durante más de un ejercicio contable.  
Las computadoras y servidores adquiridos en la OP02 por S/ 12,000.00 no se consumen ni se extinguen en los 30 días de noviembre; constituyen la infraestructura técnica sobre la cual el equipo desarrollará el Hito 1, el Hito 2 y futuros proyectos de software durante una vida útil estimada de 3 a 5 años. Asignar los S/ 12,000.00 directamente al Estado de Resultados como un gasto del mes violaría el **principio de correlación de ingresos y gastos** y el postulado de devengo, arrojando una falsa pérdida operativa ficticia. El valor del equipo se capitaliza en el balance y su costo económico se traslada a resultados de forma gradual y sistemática mediante la depreciación a lo largo de su vida útil.

---

### 4.3 Tabla de Conciliación Integral entre Calc / Excel y GnuCash

| Código | Cuenta o Indicador Financiero | Saldo Calc / Excel (S/) | Saldo GnuCash (S/) | Diferencia (S/) | Estado de Conciliación |
|:---:|---|---:|---:|---:|:---:|
| **1041** | Bancos - Cuentas Corrientes | 44,500.00 | 44,500.00 | **0.00** | CONCILIADO EXACTO |
| **1212** | Cuentas por Cobrar Comerciales | 8,000.00 | 8,000.00 | **0.00** | CONCILIADO EXACTO |
| **3361** | Equipos de Cómputo e Informáticos | 12,000.00 | 12,000.00 | **0.00** | CONCILIADO EXACTO |
| **4111** | Remuneraciones por Pagar | 1,500.00 | 1,500.00 | **0.00** | CONCILIADO EXACTO |
| **4212** | Cuentas por Pagar Proveedores | 2,000.00 | 2,000.00 | **0.00** | CONCILIADO EXACTO |
| **4511** | Préstamo Bancario (Corto Plazo) | 10,000.00 | 10,000.00 | **0.00** | CONCILIADO EXACTO |
| **4699** | Anticipos de Clientes | 9,000.00 | 9,000.00 | **0.00** | CONCILIADO EXACTO |
| **5011** | Capital Social | 40,000.00 | 40,000.00 | **0.00** | CONCILIADO EXACTO |
| **7041** | Ingresos por Desarrollo de Software | 24,000.00 | 24,000.00 | **0.00** | CONCILIADO EXACTO |
| **6941** | Costo: Remuneraciones Desarrollo | 15,000.00 | 15,000.00 | **0.00** | CONCILIADO EXACTO |
| **6942** | Costo: Servicios de Nube | 2,000.00 | 2,000.00 | **0.00** | CONCILIADO EXACTO |
| **9411** | Gastos Administrativos Generales | 3,000.00 | 3,000.00 | **0.00** | CONCILIADO EXACTO |
| **9412** | Gastos Adm. Sueldos Devengados | 1,500.00 | 1,500.00 | **0.00** | CONCILIADO EXACTO |
| **9711** | Gastos Financieros (Intereses) | 500.00 | 500.00 | **0.00** | CONCILIADO EXACTO |
| **5911** | Utilidad Neta del Ejercicio | 2,000.00 | 2,000.00 | **0.00** | CONCILIADO EXACTO |
| **PAT** | Total Patrimonio Neto | 42,000.00 | 42,000.00 | **0.00** | CONCILIADO EXACTO |
| **ACT** | Total Activo | 64,500.00 | 64,500.00 | **0.00** | CONCILIADO EXACTO |
| **PAS** | Total Pasivo | 22,500.00 | 22,500.00 | **0.00** | CONCILIADO EXACTO |
| **DIF** | **SUMATORIA DE DISCREPANCIAS** | | | **S/ 0.00** | **100% CONCILIADO** |

---

## 5. Evaluación del Control Económico y Presupuesto de Tesorería

### 5.1 Indicadores Financieros Clave

1. **Margen Neto:**
   $$\text{Margen Neto} = \frac{\text{Resultado del Mes}}{\text{Ingresos Totales}} = \frac{\text{S/ } 2,000.00}{\text{S/ } 24,000.00} = \mathbf{8.33\%}$$
   *Interpretación:* Por cada S/ 100 soles facturados por el Hito 1 de PANVIZ, la empresa genera S/ 8.33 de ganancia limpia. Es un margen positivo pero ajustado, absorbido en un 70.83% por costos técnicos de desarrollo y nube.
2. **Razón Corriente:**
   $$\text{Razón Corriente} = \frac{\text{Activo Corriente}}{\text{Pasivo Corriente}} = \frac{\text{S/ } 52,500.00}{\text{S/ } 22,500.00} = \mathbf{2.33}$$
   *Interpretación:* Aparentemente, Andes Software tiene S/ 2.33 de respaldo a corto plazo por cada S/ 1.00 de deuda corriente. Sin embargo, como se demuestra más adelante, este ratio es engañoso.
3. **Cobertura Inmediata de Tesorería (15 días):**
   $$\text{Cobertura Inmediata} = \frac{\text{Saldo Disponible en Bancos}}{\text{Pagos Previstos en 15 días}} = \frac{\text{S/ } 44,500.00}{\text{S/ } 23,500.00} = \mathbf{1.89}$$
   *Interpretación:* La empresa cuenta con fondos suficientes en banco para cubrir 1.89 veces los compromisos de egreso de la primera quincena.

---

### 5.2 Presupuesto de Caja de 15 Días (Proyección del 01 al 15 de Diciembre)

| Concepto de Tesorería | Importe (S/) | Notas Explicativas |
|---|---:|---|
| **Saldo Inicial en Bancos al 01/12/2026** | **44,500.00** | Saldo conciliado en cuenta corriente al cierre de mes |
| (+) Cobranzas Proyectadas de Clientes | 0.00 | Cliente advirtió pago en 45 días (no en 15 días) |
| **TOTAL EFECTIVO DISPONIBLE** | **44,500.00** | Fondos líquidos para atender el periodo |
| (-) Remuneraciones técnicas de desarrollo | (18,000.00) | Planilla de programadores para módulo de alertas |
| (-) Servicios de nube e infraestructura | (2,000.00) | Cuota mensual hosting para no suspender el servicio |
| (-) Deuda restante proveedor de equipos | (2,000.00) | Cancelación del saldo pendiente de OP02 |
| (-) Remuneraciones administrativas devengadas | (1,500.00) | Pago de pasivo laboral contraído en OP10 |
| **TOTAL EGRESOS PREVISTOS EN 15 DÍAS** | **(23,500.00)** | Salidas de caja obligatorias e ineludibles |
| **SALDO FINAL DE CAJA AL DÍA 15 (EXCEDENTE)** | **21,000.00** | Excedente transitorio favorable al 15 de diciembre |

---

### 5.3 Proyección de Estrés Financiero a 45 Días y la Trampa de la Liquidez

| Periodo de Tiempo | Saldo Inicial | Cobros Previstos | Pagos Operativos Previstos | Saldo Proyectado | Diagnóstico Financiero |
|:---:|---:|---:|---:|---:|:---:|
| **Día 1 al 15** | S/ 44,500.00 | S/ 0.00 | S/ 23,500.00 | **+S/ 21,000.00** | Excedente controlado |
| **Día 16 al 44** | S/ 21,000.00 | S/ 0.00 | S/ 23,500.00 *(1)* | **-S/ 2,500.00** | **¡DÉFICIT / ILIQUIDEZ CRÍTICA!** |
| **Día 45** | -S/ 2,500.00 | S/ 8,000.00 *(2)* | S/ 0.00 | **+S/ 5,500.00** | Recuperación tardía precaria |

*(1) Proyección conservadora: Segunda quincena de remuneraciones técnicas (S/ 18,000) + Nube del mes siguiente (S/ 2,000) + Gastos adm. operativos (S/ 3,500) = S/ 23,500.00.*  
*(2) Cobro advertido de la factura del Hito 1 en el día 45.*

#### ¿Por qué la utilidad contable y la razón corriente no aseguran efectivo oportuno?
El análisis técnico de Andes Software ejemplifica con total contundencia la diferencia entre solvencia contable y liquidez financiera:
1. **La utilidad es un concepto devengado, no monetario:** La empresa muestra S/ 2,000.00 de utilidad neta, pero dentro de los ingresos se incluyeron S/ 8,000.00 de facturación a la entidad de salud que no se han cobrado y que tardarán 45 días en ingresar. Si evaluamos la operación sobre base de caja, el Hito 1 demandó pagos de costos y gastos devengados por S/ 22,000.00 frente a solo S/ 16,000.00 cobrados; es decir, **la operación real tuvo un déficit de caja operativo de S/ 6,000.00**.
2. **La trampa de la Razón Corriente (2.33):** El ratio de 2.33 sugiere que la empresa tiene más del doble de activo corriente frente a su pasivo corriente. No obstante:
   - S/ 8,000.00 del activo corriente corresponden a cuentas por cobrar ilíquidas que no se pueden usar para transferir sueldos el fin de quincena.
   - En el pasivo corriente figuran S/ 9,000.00 por el anticipo del cliente, el cual no exigirá un desembolso de dinero en efectivo, pero sí **obliga a consumir recursos técnicos de nómina y servidores** sin generar ninguna entrada adicional de dinero durante el próximo mes.
3. **Origen artificial del saldo en bancos:** El saldo bancario de S/ 44,500.00 no fue generado por ventas sostenibles: S/ 40,000.00 provienen del capital de los socios y S/ 10,000.00 de un préstamo bancario. Al proyectar la quincena siguiente (días 16 al 44), el consumo de caja para mantener el software y el equipo provocará un **déficit proyectado de S/ 2,500.00** en el día 35 si la gerencia se confía de su aparente liquidez y no adopta medidas inmediatas.

---

## 6. Decisiones Estratégicas y Sustentación Gerencial

Para proteger la viabilidad de la empresa y asegurar la continuidad operativa ininterrumpida de PANVIZ en el sistema de salud pública, se adoptan las tres decisiones gerenciales siguientes:

### Decisión 1: Negociación de Cobranza Anticipada (Factoring o Adenda por Pronto Pago)
- **Evidencia Contable:** El Estado de Situación Financiera registra S/ 8,000.00 en la cuenta `1212 Cuentas por Cobrar`. El presupuesto de tesorería demuestra que aplazar este cobro a 45 días genera un déficit de caja de S/ 2,500.00 en la segunda quincena de diciembre (días 16 al 44), imposibilitando el pago de nómina.
- **Acción y Responsable:** La **Gerencia General** gestionará en un plazo perentorio de **7 días calendario** (antes del 17 de noviembre):  
  a) Una adenda contractual con la entidad de salud para aplicar un descuento por pronto pago del 3% (S/ 240.00), permitiendo cobrar S/ 7,760.00 en un plazo de 10 días; o en su defecto,  
  b) Una operación de descuento de factura negociable (*factoring*) con el mismo banco emisor del pagaré de OP03.
- **Efecto en la Salud Pública:** Evita la paralización del servicio por falta de pago al personal técnico y garantiza la disponibilidad permanente de las bases de datos de vigilancia epidemiológica para los directores de salud.

### Decisión 2: Constitución de una Reserva Intangible para Servidores en la Nube y Nómina Crítica
- **Evidencia Contable:** Los egresos mensuales fijos para mantener PANVIZ en producción ascienden a S/ 2,000.00 en infraestructura cloud (`6942`) y S/ 18,000.00 en sueldos del equipo central de desarrollo (`6941`), totalizando S/ 20,000.00 por quincena.
- **Acción y Responsable:** La **Dirección de Finanzas y la Jefatura de TI** crearán en un plazo de **3 días** una subcuenta bancaria restringida con una asignación presupuestaria intangible de **S/ 20,000.00**, extraída del saldo remanente al día 15 (S/ 21,000.00). Dicha cuenta estará blindada exclusivamente para el débito automático del proveedor cloud y los salarios de los ingenieros clave.
- **Efecto en la Salud Pública:** Previene caídas del sistema (*downtime*) por suspensión del servidor en la nube, garantizando que los hospitales y postas sigan reportando pacientes con enfermedades infecciosas en tiempo real las 24 horas del día.

### Decisión 3: Reestructuración del Módulo Anticipado en Sub-hitos Quincenales
- **Evidencia Contable:** En el pasivo corriente figura la cuenta `4699 Anticipos de Clientes` por S/ 9,000.00. La empresa no puede reconocer este monto como ingreso ni reinvertirlo como nueva ganancia; además, ejecutar el módulo completo sin cobros intermedios agrava la sangría de caja.
- **Acción y Responsable:** El **Líder de Proyecto (Project Manager)** acordará con los supervisores de la entidad sanitaria, en un plazo de **10 días**, la partición formal del segundo módulo en dos entregables parciales:  
  - Sub-hito 2A: Motor de procesamiento y cálculo de alertas (día 15 del mes 2), devengando el 50% del anticipo (S/ 4,500.00).  
  - Sub-hito 2B: Tableros interactivos y reportes automáticos en PDF (día 30 del mes 2), devengando el 50% restante (S/ 4,500.00) y habilitando la facturación inmediata de la fase de mantenimiento anual.
- **Efecto en la Salud Pública:** La entidad de salud pública no tendrá que esperar un mes entero para contar con alertas sanitarias; dispondrá de avisos tempranos de brotes en solo 15 días, permitiendo intervenciones médicas y cercos epidemiológicos oportunos.

---

## 7. Matriz de Distribución de Responsabilidades y Revisión Cruzada (Peer Review)

Conforme a las directrices de la sección 6 del documento rector `trab_53.pdf`, el equipo de 5 estudiantes distribuyó las tareas y ejecutó revisiones cruzadas formales para garantizar la consistencia numérica y metodológica:

| # | Integrante | CUI | Correo Institucional | Responsabilidad Principal | Entregable Producido | Revisión Cruzada Realizada | Dictamen de Calidad |
|:---:|---|:---:|---|---|---|---|:---:|
| **1** | **Suclle Suca, Michael Benjamin** | 20210678 | `msuclles@unsa.edu.pe` | Coordinación, síntesis de lectura e integración del informe | Informe general `.md`, Diapositiva 1 | Revisa las tres decisiones y sustento financiero del Integrante 5 | **APROBADO (100%)** |
| **2** | **Fernandez Huarca, Rodrigo Alexander** | 20210672 | `rfernandezh@unsa.edu.pe` | Catálogo de cuentas y registros en software contable GnuCash | Archivo `.gnucash` y Diapositiva 2 | Revisa la síntesis crítica y criterios contables del Integrante 1 | **APROBADO (100%)** |
| **3** | **Meza Vizcarra, Cielo Cristal** | 20210685 | `cmezav@unsa.edu.pe` | Hoja de cálculo: Diario, Mayor y Balance de Comprobación | Hojas Diario, Mayor, Comprobación en `.xlsx`, Diapositiva 3 | Revisa el árbol de cuentas y transacciones en GnuCash del Integrante 2 | **APROBADO (100%)** |
| **4** | **Borda Espinoza, Gabriela Nayely** | 20210665 | `gbordae@unsa.edu.pe` | Formulación de estados financieros y matriz de conciliación | Hojas Estados Financieros, Flujo y Conciliación en `.xlsx`, Diapositiva 4 | Revisa mayorización y balance de comprobación de la Integrante 3 | **APROBADO (100%)** |
| **5** | **Ccoscco Alvis, Italo Frankdux** | 20210669 | `iccosccoa@unsa.edu.pe` | Ratios financieros, presupuesto de caja y decisiones gerenciales | Hoja Caja 15 días, Sección 5 y 6, Diapositiva 5 | Revisa los 4 estados financieros y el flujo de efectivo de la Integrante 4 | **APROBADO (100%)** |

---

## 8. Conclusiones

1. **Integración Contable-Gerencial en Software:** El control económico de un proyecto de tecnología no puede restringirse al seguimiento de tareas en herramientas como Jira o Trello. La contabilidad por partida doble, sustentada en normas como la NIIF 15 y la NIC 16, proporciona el marco científico verificable para medir si el desarrollo genera margen bruto real o consume capital de trabajo de forma destructiva.
2. **Diferencia Crítica entre Devengo y Caja:** El caso PANVIZ demuestra que una empresa puede ser formalmente rentable en su Estado de Resultados (S/ 2,000.00 de utilidad neta y 8.33% de margen) y aparentemente solvente en su Balance General (Razón Corriente de 2.33), pero encontrarse al borde de la quiebra técnica por iliquidez si sus cobranzas se dilatan a 45 días mientras sus obligaciones laborales y de infraestructura en la nube vencen de manera quincenal.
3. **Rigurosidad del Pasivo por Anticipos:** Tratar el cobro adelantado de S/ 9,000.00 como utilidad disponible hubiera inducido a la gerencia a gastar recursos inexistentes. La correcta clasificación como pasivo diferido protegió a la entidad, recordándole que debe reservar capacidad operativa para entregar el módulo comprometido.
4. **Sostenibilidad del Servicio en Salud Pública:** Las decisiones contables impactan de manera directa sobre la vida y bienestar de los ciudadanos. Blindar la partida de servidores en la nube y asegurar el flujo de caja mediante pronto pago garantiza que PANVIZ no sufra interrupciones, asegurando la vigilancia epidemiológica continua en beneficio de la sociedad.

---

## 9. Referencias Bibliográficas (Normas APA 7.ª Edición)

- Brume, M. (2019). *Estructura organizacional*. Sello Editorial Institución Universitaria Itsa.
- Castrellón Calderón, R., et al. (2021). La importancia de los estados financieros en la toma de decisiones financieras y contables. *Revista FAECO Sapiens*, 4(2), 80–92.
- Guim-Bustos, P., Martillo-Mieles, O., Guerrero-Cortez, V., & Carrillo-Pérez, F. (2023). Los estados financieros y las tomas de decisiones empresariales. *593 Digital Publisher CEIT*, 8(2), 149–160. https://doi.org/10.33386/593dp.2023.2.1679
- International Accounting Standards Board [IASB]. (2018). *Marco Conceptual para la Información Financiera*. IFRS Foundation.
- International Accounting Standards Board [IASB]. (2014). *Norma Internacional de Información Financiera 15: Ingresos de Actividades Ordinarias Procedentes de Contratos con Clientes (NIIF 15)*. IFRS Foundation.
- International Accounting Standards Board [IASB]. (2001). *Norma Internacional de Contabilidad 7: Estado de Flujos de Efectivo (NIC 7)*. IFRS Foundation.
- International Accounting Standards Board [IASB]. (2003). *Norma Internacional de Contabilidad 16: Propiedad, Planta y Equipo (NIC 16)*. IFRS Foundation.
- Llanes, M. (2010). El análisis de los estados contables en un entorno dinámico y gerencial de la empresa. *Revista Universo Contábil*, 6(2), 121–140.
- Ministerio de Economía y Finanzas [MEF]. (2019). *Plan Contable General Empresarial (PCGE) Modificado 2019*. Dirección General de Contabilidad Pública del Perú.
- Suanders, A. (2006). *Toma de decisiones en las organizaciones modernas*. McGraw-Hill Interamericana.
- Turmero, I. (2010). *Decisiones de financiamiento y valoración de proyectos corporativos*. Universidad Nacional Experimental Politécnica.
