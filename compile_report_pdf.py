import os
import subprocess
import pypdf

BASE_DIR = r"C:\Users\micha\Downloads\Borrar entregable 6\GPS-Entregable-6"
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
output_pdf_path = os.path.join(BASE_DIR, "INFORME_ENTREGABLE_6.pdf")
report_html_path = os.path.join(BASE_DIR, "informe_compilado.html")

html_report = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Informe Técnico de Control Económico - PANVIZ</title>
<style>
  @page {
    size: A4 portrait;
    margin: 12mm 14mm 12mm 14mm;
  }

  body {
    font-family: 'Segoe UI', Arial, sans-serif;
    color: #1e293b;
    font-size: 8.5pt;
    line-height: 1.35;
    margin: 0;
    padding: 0;
  }

  /* Portada */
  .portada {
    page-break-after: always;
    text-align: center;
    padding-top: 25px;
    height: 92vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-sizing: border-box;
  }
  .univ-header { font-size: 15pt; font-weight: 800; color: #1e3a8a; text-transform: uppercase; margin-bottom: 3px; }
  .fac-header { font-size: 11.5pt; font-weight: 700; color: #334155; margin-bottom: 2px; }
  .esc-header { font-size: 10.5pt; font-weight: 600; color: #475569; margin-bottom: 15px; }
  .logo-box { margin: 15px auto; width: 85px; height: 85px; border-radius: 50%; background: #f1f5f9; border: 3px solid #1e3a8a; display: flex; align-items: center; justify-content: center; font-size: 24pt; font-weight: bold; color: #1e3a8a; }
  .doc-type { font-size: 10.5pt; font-weight: bold; color: #b45309; text-transform: uppercase; letter-spacing: 1px; margin-top: 10px; }
  .doc-title { font-size: 17pt; font-weight: 800; color: #0f172a; margin: 8px 0 4px; line-height: 1.2; }
  .doc-subtitle { font-size: 10.5pt; color: #64748b; font-weight: 500; }
  
  .meta-box { background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 12px 20px; margin: 15px auto; text-align: left; max-width: 500px; font-size: 9pt; }
  .meta-row { display: flex; justify-content: space-between; margin-bottom: 3px; }
  .meta-label { font-weight: bold; color: #1e3a8a; }
  
  .team-box { margin: 10px auto; max-width: 580px; text-align: left; }
  .team-title { font-size: 9.5pt; font-weight: bold; color: #1e293b; margin-bottom: 6px; text-align: center; }
  .team-table { width: 100%; border-collapse: collapse; font-size: 8.5pt; }
  .team-table th { background: #1e3a8a; color: #fff; padding: 5px 8px; text-align: left; }
  .team-table td { padding: 4px 8px; border-bottom: 1px solid #e2e8f0; }

  /* Contenido */
  .page {
    page-break-after: always;
    box-sizing: border-box;
    padding-top: 4px;
  }
  .page:last-child {
    page-break-after: avoid;
  }

  .running-header {
    border-bottom: 1.5px solid #1e3a8a;
    padding-bottom: 4px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    font-size: 7.5pt;
    color: #64748b;
    font-weight: 600;
    text-transform: uppercase;
  }

  h1 { font-size: 11pt; color: #1e3a8a; border-left: 4px solid #1e3a8a; padding-left: 6px; margin: 8px 0 5px 0; text-transform: uppercase; }
  h2 { font-size: 9.5pt; color: #0f172a; margin: 6px 0 3px 0; font-weight: 700; }
  p { margin: 0 0 5px 0; text-align: justify; }

  table.data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.5pt;
    margin: 5px 0 8px 0;
  }
  table.data-table th {
    background: #1e3a8a;
    color: #fff;
    padding: 3.5px 5px;
    text-align: left;
    font-weight: 600;
  }
  table.data-table td {
    padding: 3px 5px;
    border-bottom: 1px solid #e2e8f0;
  }
  table.data-table tr:nth-child(even) td {
    background: #f8fafc;
  }
  .num { text-align: right; font-family: 'Consolas', monospace; }
  .bold { font-weight: bold; }
  .highlight { background: #e0f2fe !important; font-weight: bold; }
  .success { color: #047857; font-weight: bold; }
  .danger { color: #b91c1c; font-weight: bold; }
  .warning { color: #b45309; font-weight: bold; }

  .callout {
    background: #f1f5f9;
    border-left: 3px solid #1e3a8a;
    padding: 5px 8px;
    margin: 5px 0;
    font-size: 7.8pt;
  }
  .callout-alert {
    background: #fef2f2;
    border-left: 3px solid #ef4444;
    padding: 5px 8px;
    margin: 5px 0;
    font-size: 7.8pt;
  }

  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }

  .img-box {
    text-align: center;
    margin: 4px 0;
  }
  .img-box img {
    max-width: 98%;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
  }
  .img-caption {
    font-size: 7pt;
    color: #64748b;
    font-style: italic;
    margin-top: 2px;
  }
</style>
</head>
<body>

  <!-- PORTADA -->
  <div class="portada">
    <div>
      <div class="univ-header">Universidad Nacional de San Agustín de Arequipa</div>
      <div class="fac-header">Facultad de Ingeniería de Producción y Servicios</div>
      <div class="esc-header">Escuela Profesional de Ingeniería de Sistemas</div>
      <div class="logo-box">UNSA</div>
      <div class="doc-type">Entregable 6 · Semana 11 · Gestión de Proyectos de Software</div>
      <div class="doc-title">Control Económico y Diseño Contable de PANVIZ</div>
      <div class="doc-subtitle">Caso de Estudio: Andes Software en Vigilancia Epidemiológica de Salud Pública</div>
    </div>

    <div class="meta-box">
      <div class="meta-row"><span class="meta-label">Asignatura:</span> <span>Gestión de Proyectos de Software</span></div>
      <div class="meta-row"><span class="meta-label">Docente:</span> <span>Docente del Curso de Gestión de Proyectos</span></div>
      <div class="meta-row"><span class="meta-label">Fecha de Entrega:</span> <span>16 de Noviembre de 2026</span></div>
      <div class="meta-row"><span class="meta-label">Herramientas:</span> <span>LibreOffice Calc (.xlsx) & GnuCash (.gnucash)</span></div>
      <div class="meta-row"><span class="meta-label">Sistema:</span> <span>PANVIZ (Salud Pública - Vigilancia Epidemiológica)</span></div>
    </div>

    <div class="team-box">
      <div class="team-title">EQUIPO DE TRABAJO (4 INTEGRANTES)</div>
      <table class="team-table">
        <thead>
          <tr>
            <th>Estudiante Integrante</th>
            <th>Rol Asignado</th>
            <th>Responsabilidad Principal</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Chambilla Perca, Ricardo Mauricio</strong></td>
            <td>Especialista Contable</td>
            <td>Catálogo, Libro Diario (OP01-OP11), Mayor y Comprobación</td>
          </tr>
          <tr>
            <td><strong>Gutiérrez Ccama, Juan Diego</strong></td>
            <td>Especialista en Reportes</td>
            <td>Estados Financieros (4) y Conciliación Integral GnuCash</td>
          </tr>
          <tr>
            <td><strong>Mollo Chuquicaña, Dolly Yadhira</strong></td>
            <td>Analista de Liquidez</td>
            <td>Ratios, Presupuesto Quincenal, Estrés 45 días y Decisiones</td>
          </tr>
          <tr>
            <td><strong>Suclle Suca, Michael Benjamin</strong></td>
            <td>Coordinador y Auditor</td>
            <td>Coordinación general, Control 43, Síntesis e Integración</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div style="font-size: 8pt; color: #64748b; padding-bottom: 10px;">
      Arequipa, Perú · Noviembre de 2026
    </div>
  </div>

  <!-- PÁGINA 1: CONTROL DE LECTURA 43 Y SÍNTESIS CRÍTICA -->
  <div class="page">
    <div class="running-header">
      <span>Andes Software · Control Económico PANVIZ</span>
      <span>Sección I & II: Fundamentos Teóricos</span>
    </div>

    <h1>Sección I: Control de Lectura 43 (Slide 43 PPTX)</h1>
    <div class="callout">
      <strong>Pregunta 1: Propósito de los estados financieros e insuficiencia del registro sin análisis gerencial:</strong><br>
      Según Guim-Bustos et al. (2023, pp. 152–154), los estados financieros proveen una representación estructurada, fidedigna y comprensible del desempeño económico, patrimonial y de liquidez de una organización. Registrar operaciones mecánicamente (teneduría de libros) resulta insuficiente porque compila hechos pasados sin diagnóstico predictivo. Sin un análisis e interpretación profunda de ratios y flujos, la gerencia no puede anticipar insolvencias, evaluar el ciclo de conversión de efectivo ni respaldar la toma de decisiones estratégicas.
    </div>
    <div class="callout">
      <strong>Pregunta 2: Tres componentes contables en una empresa de software:</strong><br>
      1. <em>Activos:</em> Hardware informático y servidores de desarrollo (NIC 16), recursos tecnológicos que generan beneficios futuros.<br>
      2. <em>Pasivos:</em> Anticipos de clientes por hitos de software pendientes de entrega (NIIF 15) y deuda cloud devengada.<br>
      3. <em>Costos del Servicio:</em> Remuneraciones directas de programadores y consumo mensual de infraestructura en la nube asignable al proyecto.
    </div>
    <div class="callout">
      <strong>Pregunta 3: Empresa de software con utilidades pero sin caja para pagar remuneraciones:</strong><br>
      Debe contrastarse el <em>Estado de Resultados</em> (evalúa ganancias por devengo al entregar el hito) con el <em>Estado de Flujos de Efectivo</em> (evalúa dinero real en banco). Si la facturación es a 45 días, la utilidad es en papel mientras la caja se extingue. <strong>Decisión Inmediata:</strong> Gestionar factoring bancario o descuento por pronto pago sobre la factura aceptada para inyectar liquidez inmediata y pagar la nómina del equipo técnico.
    </div>

    <h1>Sección II: Síntesis Crítica (Guim-Bustos et al., 2023, pp. 152–154)</h1>
    <p><em>(Extensión: 288 palabras · Rango normativo: 250 a 350 palabras)</em></p>
    <p>
      Los estados financieros constituyen el compendio estructurado de la realidad económica, patrimonial y financiera de una entidad, cuyo propósito central trasciende la obligación legal o tributaria para erigirse en el fundamento analítico de la toma de decisiones gerenciales. En las páginas examinadas (152–154), los autores demuestran que registrar transacciones mediante partida doble es meramente instrumental; si la gerencia no analiza los saldos mediante indicadores ni interpreta la interacción entre devengo y liquidez, la organización opera en la incertidumbre. La dirección estratégica exige comprender el comportamiento del balance general, las pérdidas y ganancias, y el flujo de caja para evaluar solvencia, anticipar insolvencias y respaldar decisiones de inversión o endeudamiento con evidencia contable verificable.
    </p>
    <p>
      De este análisis se desprenden dos ideas aplicables directamente al control económico de PANVIZ:
      <strong>1) La autonomía analítica del flujo de caja frente al resultado contable:</strong> Reconocer ingresos por hitos aprobados produce utilidades en el estado de resultados, pero no garantiza solvencia inmediata si los plazos de cobranza exceden las obligaciones laborales quincenales. Para PANVIZ, el control debe basarse en un presupuesto de caja proyectado que evite la asfixia de tesorería por retrasos del sector público.
      <strong>2) La categorización rigurosa de las obligaciones de desempeño como pasivo corriente:</strong> Los fondos recibidos de forma anticipada antes de prestar el servicio tecnológico no deben registrarse como ingresos ganados, sino como un pasivo diferido. Esto asegura que la gerencia visualice con precisión las obligaciones técnicas comprometidas y salvaguarde los recursos requeridos para completar los módulos sanitarios pendientes sin comprometer la continuidad operativa del sistema.
    </p>
  </div>

  <!-- PÁGINA 2: CASO PANVIZ, CATÁLOGO Y LIBRO DIARIO -->
  <div class="page">
    <div class="running-header">
      <span>Andes Software · Control Económico PANVIZ</span>
      <span>Sección III & IV: Catálogo y Libro Diario</span>
    </div>

    <h1>Sección III: Caso de Estudio PANVIZ y Criterios Normativos</h1>
    <p>
      Andes Software ejecuta el desarrollo de PANVIZ para salud pública. En el mes 1 entrega el Hito 1 (ingesta e indicadores) y recibe un anticipo para el Hito 2 (alertas y reportes). Criterios NIIF aplicados:
      <strong>NIIF 15 (Anticipo OP04 S/ 9,000):</strong> Se clasifica como pasivo (ingreso diferido) por constituir una obligación de desempeño no satisfecha.
      <strong>NIC 16 (Hardware OP02 S/ 12,000):</strong> Se activa como PPE a costo histórico (sin depreciación por delimitación académica).
      <strong>Devengo (OP10 S/ 1,500):</strong> Sueldos administrativos del mes se reconocen como gasto del ejercicio aun impagos.
    </p>

    <h1>Sección IV: Libro Diario General (OP01 - OP11)</h1>
    <table class="data-table">
      <thead>
        <tr>
          <th style="width:6%;">ID</th>
          <th style="width:9%;">Fecha</th>
          <th style="width:7%;">Cód.</th>
          <th style="width:30%;">Cuenta Contable</th>
          <th style="width:34%;">Glosa / Explicación de la Operación</th>
          <th style="width:7%; text-align:right;">Debe (S/)</th>
          <th style="width:7%; text-align:right;">Haber (S/)</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>OP01</td><td>02/11</td><td>1041<br>5011</td><td>Cuentas Corrientes Bancarias<br>Capital Social Aportado</td><td>Aporte de capital inicial de los socios en cuenta corriente bancaria</td><td class="num">40,000.00<br>-</td><td class="num">-<br>40,000.00</td></tr>
        <tr><td>OP02</td><td>04/11</td><td>3361<br>1041<br>4212</td><td>Equipos para Procesamiento Inf.<br>Cuentas Corrientes Bancarias<br>Proveedores por Pagar</td><td>Compra de equipos informáticos (S/ 12,000 total): pago S/ 8,000 en bancos y saldo S/ 4,000 pendiente a proveedor</td><td class="num">12,000.00<br>-<br>-</td><td class="num">-<br>8,000.00<br>4,000.00</td></tr>
        <tr><td>OP03</td><td>06/11</td><td>1041<br>4511</td><td>Cuentas Corrientes Bancarias<br>Préstamos Bancarios Corto Plazo</td><td>Desembolso de préstamo bancario recibido para capital a 6 meses</td><td class="num">10,000.00<br>-</td><td class="num">-<br>10,000.00</td></tr>
        <tr><td>OP04</td><td>09/11</td><td>1041<br>4699</td><td>Cuentas Corrientes Bancarias<br>Anticipos Clientes (Diferidos)</td><td>Recepción de anticipo por Hito 2 de salud pública (NIIF 15)</td><td class="num">9,000.00<br>-</td><td class="num">-<br>9,000.00</td></tr>
        <tr><td>OP05</td><td>13/11</td><td>6941<br>1041</td><td>Costo Serv. - Remuneraciones Dev.<br>Cuentas Corrientes Bancarias</td><td>Pago desde bancos de planillas de desarrollo técnico del mes</td><td class="num">15,000.00<br>-</td><td class="num">-<br>15,000.00</td></tr>
        <tr><td>OP06</td><td>16/11</td><td>6942<br>1041</td><td>Costo Serv. - Servicios de Nube<br>Cuentas Corrientes Bancarias</td><td>Pago de consumo mensual de infraestructura en nube para PANVIZ</td><td class="num">2,000.00<br>-</td><td class="num">-<br>2,000.00</td></tr>
        <tr><td>OP07</td><td>19/11</td><td>9411<br>1041</td><td>Gastos Admin. - Operativos<br>Cuentas Corrientes Bancarias</td><td>Pago de gastos administrativos operativos del mes en bancos</td><td class="num">3,000.00<br>-</td><td class="num">-<br>3,000.00</td></tr>
        <tr><td>OP08</td><td>23/11</td><td>1041<br>1212<br>7041</td><td>Cuentas Corrientes Bancarias<br>Facturas por Cobrar Clientes<br>Ingresos Desarrollo Software</td><td>Entrega y aceptación de Hito 1: Factura S/ 24,000 (cobro S/ 16,000 y saldo S/ 8,000 a 45 días)</td><td class="num">16,000.00<br>8,000.00<br>-</td><td class="num">-<br>-<br>24,000.00</td></tr>
        <tr><td>OP09</td><td>25/11</td><td>4212<br>1041</td><td>Proveedores por Pagar<br>Cuentas Corrientes Bancarias</td><td>Amortización de deuda con proveedor de equipos desde bancos</td><td class="num">2,000.00<br>-</td><td class="num">-<br>2,000.00</td></tr>
        <tr><td>OP10</td><td>28/11</td><td>9412<br>4111</td><td>Gastos Admin. - Sueldos Dev.<br>Remuneraciones por Pagar</td><td>Devengo de remuneraciones administrativas del mes pendientes</td><td class="num">1,500.00<br>-</td><td class="num">-<br>1,500.00</td></tr>
        <tr><td>OP11</td><td>30/11</td><td>9711<br>1041</td><td>Gastos Financieros - Intereses<br>Cuentas Corrientes Bancarias</td><td>Pago de intereses devengados del préstamo bancario recibido</td><td class="num">500.00<br>-</td><td class="num">-<br>500.00</td></tr>
        <tr class="highlight">
          <td colspan="5" style="text-align:right;">TOTALES DEL LIBRO DIARIO (CONTROL PARTIDA DOBLE: DIFERENCIA S/ 0.00):</td>
          <td class="num">S/ 119,000.00</td>
          <td class="num">S/ 119,000.00</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- PÁGINA 3: BALANCE DE COMPROBACIÓN Y ESTADOS FINANCIEROS -->
  <div class="page">
    <div class="running-header">
      <span>Andes Software · Control Económico PANVIZ</span>
      <span>Sección IV & V: Comprobación y Estados Financieros</span>
    </div>

    <h1>Balance de Comprobación de Sumas y Saldos</h1>
    <table class="data-table">
      <thead>
        <tr>
          <th>Cód.</th>
          <th>Cuenta Contable</th>
          <th style="text-align:right;">Sumas Debe</th>
          <th style="text-align:right;">Sumas Haber</th>
          <th style="text-align:right;">Saldo Deudor</th>
          <th style="text-align:right;">Saldo Acreedor</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>1041</td><td>Cuentas Corrientes Bancarias</td><td class="num">75,000.00</td><td class="num">30,500.00</td><td class="num">44,500.00</td><td class="num">-</td></tr>
        <tr><td>1212</td><td>Facturas por Cobrar Clientes</td><td class="num">8,000.00</td><td class="num">-</td><td class="num">8,000.00</td><td class="num">-</td></tr>
        <tr><td>3361</td><td>Equipos para Procesamiento Inf.</td><td class="num">12,000.00</td><td class="num">-</td><td class="num">12,000.00</td><td class="num">-</td></tr>
        <tr><td>4111</td><td>Remuneraciones por Pagar</td><td class="num">-</td><td class="num">1,500.00</td><td class="num">-</td><td class="num">1,500.00</td></tr>
        <tr><td>4212</td><td>Proveedores por Pagar</td><td class="num">2,000.00</td><td class="num">4,000.00</td><td class="num">-</td><td class="num">2,000.00</td></tr>
        <tr><td>4511</td><td>Préstamos Bancarios Corto Plazo</td><td class="num">-</td><td class="num">10,000.00</td><td class="num">-</td><td class="num">10,000.00</td></tr>
        <tr><td>4699</td><td>Anticipos de Clientes (Diferidos)</td><td class="num">-</td><td class="num">9,000.00</td><td class="num">-</td><td class="num">9,000.00</td></tr>
        <tr><td>5011</td><td>Capital Social Aportado</td><td class="num">-</td><td class="num">40,000.00</td><td class="num">-</td><td class="num">40,000.00</td></tr>
        <tr><td>7041</td><td>Ingresos por Desarrollo Software</td><td class="num">-</td><td class="num">24,000.00</td><td class="num">-</td><td class="num">24,000.00</td></tr>
        <tr><td>6941</td><td>Costo Servicio - Remuneraciones Dev.</td><td class="num">15,000.00</td><td class="num">-</td><td class="num">15,000.00</td><td class="num">-</td></tr>
        <tr><td>6942</td><td>Costo Servicio - Servicios de Nube</td><td class="num">2,000.00</td><td class="num">-</td><td class="num">2,000.00</td><td class="num">-</td></tr>
        <tr><td>9411</td><td>Gastos Admin. - Operativos Generales</td><td class="num">3,000.00</td><td class="num">-</td><td class="num">3,000.00</td><td class="num">-</td></tr>
        <tr><td>9412</td><td>Gastos Admin. - Sueldos Devengados</td><td class="num">1,500.00</td><td class="num">-</td><td class="num">1,500.00</td><td class="num">-</td></tr>
        <tr><td>9711</td><td>Gastos Financieros - Intereses</td><td class="num">500.00</td><td class="num">-</td><td class="num">500.00</td><td class="num">-</td></tr>
        <tr class="highlight">
          <td colspan="2">TOTALES BALANCE DE COMPROBACIÓN:</td>
          <td class="num">S/ 119,000.00</td><td class="num">S/ 119,000.00</td><td class="num">S/ 86,500.00</td><td class="num">S/ 86,500.00</td>
        </tr>
      </tbody>
    </table>

    <div class="grid-2">
      <div>
        <h1>Estado de Situación Financiera al 30/11/2026</h1>
        <table class="data-table">
          <tr><th colspan="2">ACTIVOS</th></tr>
          <tr><td>Bancos (1041)</td><td class="num">S/ 44,500.00</td></tr>
          <tr><td>Clientes Facturas por Cobrar (1212)</td><td class="num">S/ 8,000.00</td></tr>
          <tr class="bold"><td>Total Activo Corriente</td><td class="num">S/ 52,500.00</td></tr>
          <tr><td>Equipos de Cómputo (NIC 16 3361)</td><td class="num">S/ 12,000.00</td></tr>
          <tr class="highlight"><td>TOTAL ACTIVO</td><td class="num">S/ 64,500.00</td></tr>
          <tr><th colspan="2">PASIVOS Y PATRIMONIO</th></tr>
          <tr><td>Proveedores por Pagar (4212)</td><td class="num">S/ 2,000.00</td></tr>
          <tr><td>Préstamos Bancarios Corto Plazo (4511)</td><td class="num">S/ 10,000.00</td></tr>
          <tr><td>Anticipos de Clientes (NIIF 15 4699)</td><td class="num">S/ 9,000.00</td></tr>
          <tr><td>Remuneraciones por Pagar (4111)</td><td class="num">S/ 1,500.00</td></tr>
          <tr class="bold"><td>Total Pasivo Corriente</td><td class="num">S/ 22,500.00</td></tr>
          <tr><td>Capital Social Aportado (5011)</td><td class="num">S/ 40,000.00</td></tr>
          <tr><td>Resultados Acumulados (Utilidad 5911)</td><td class="num">S/ 2,000.00</td></tr>
          <tr class="bold"><td>Total Patrimonio Neto</td><td class="num">S/ 42,000.00</td></tr>
          <tr class="highlight"><td>TOTAL PASIVO Y PATRIMONIO</td><td class="num">S/ 64,500.00</td></tr>
        </table>
      </div>

      <div>
        <h1>Estado de Resultados Económico</h1>
        <table class="data-table">
          <tr><th>Concepto</th><th style="text-align:right;">Importe (S/)</th><th style="text-align:right;">%</th></tr>
          <tr><td>Ingresos Desarrollo Software (7041)</td><td class="num">24,000.00</td><td class="num">100.0%</td></tr>
          <tr><td>(-) Nómina de Desarrollo (6941)</td><td class="num">(15,000.00)</td><td class="num">62.5%</td></tr>
          <tr><td>(-) Infraestructura Cloud (6942)</td><td class="num">(2,000.00)</td><td class="num">8.3%</td></tr>
          <tr class="bold"><td>UTILIDAD BRUTA</td><td class="num">7,000.00</td><td class="num">29.2%</td></tr>
          <tr><td>(-) Gastos Administrativos Operativos (9411)</td><td class="num">(3,000.00)</td><td class="num">12.5%</td></tr>
          <tr><td>(-) Sueldos Administrativos Devengados (9412)</td><td class="num">(1,500.00)</td><td class="num">6.3%</td></tr>
          <tr class="bold"><td>UTILIDAD OPERATIVA (EBIT)</td><td class="num">2,500.00</td><td class="num">10.4%</td></tr>
          <tr><td>(-) Intereses Préstamo Bancario (9711)</td><td class="num">(500.00)</td><td class="num">2.1%</td></tr>
          <tr class="highlight"><td>UTILIDAD NETA DEL EJERCICIO</td><td class="num">S/ 2,000.00</td><td class="num">8.33%</td></tr>
        </table>

        <h1>Estado de Flujos de Efectivo (NIC 7)</h1>
        <table class="data-table">
          <tr><th>Actividad</th><th style="text-align:right;">Neto (S/)</th></tr>
          <tr><td>Flujo Neto Actividades de Operación</td><td class="num success">+S/ 4,500.00</td></tr>
          <tr><td>Flujo Neto Actividades de Inversión</td><td class="num danger">-S/ 10,000.00</td></tr>
          <tr><td>Flujo Neto Actividades de Financiación</td><td class="num success">+S/ 50,000.00</td></tr>
          <tr class="highlight"><td>SALDO FINAL EFECTIVO (BANCOS)</td><td class="num">S/ 44,500.00</td></tr>
        </table>
      </div>
    </div>
  </div>

  <!-- PÁGINA 4: CONCILIACIÓN INTEGRAL Y EVIDENCIAS GNUCASH -->
  <div class="page">
    <div class="running-header">
      <span>Andes Software · Control Económico PANVIZ</span>
      <span>Sección VI: Conciliación Calc vs. GnuCash</span>
    </div>

    <h1>Sección VI: Matriz de Conciliación Integral Hoja de Cálculo vs. GnuCash</h1>
    <table class="data-table">
      <thead>
        <tr>
          <th>Cód.</th>
          <th>Cuenta / Renglón Financiero</th>
          <th style="text-align:right;">Saldo Calc (S/)</th>
          <th style="text-align:right;">Saldo GnuCash (S/)</th>
          <th style="text-align:right;">Diferencia</th>
          <th style="text-align:center;">Estado</th>
          <th>Sustento y Validación Técnica</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>1041</td><td>Cuentas Corrientes Bancarias</td><td class="num">44,500.00</td><td class="num">44,500.00</td><td class="num">0.00</td><td class="num success">CONFORME</td><td>Saldo idéntico en cuenta corriente; coincidencia directa.</td></tr>
        <tr><td>1212</td><td>Facturas por Cobrar Clientes</td><td class="num">8,000.00</td><td class="num">8,000.00</td><td class="num">0.00</td><td class="num success">CONFORME</td><td>Derecho exigible por Hito 1 aceptado (cobro 45 días).</td></tr>
        <tr><td>3361</td><td>Equipos para Cómputo (NIC 16)</td><td class="num">12,000.00</td><td class="num">12,000.00</td><td class="num">0.00</td><td class="num success">CONFORME</td><td>Hardware reconocido a costo histórico en activos.</td></tr>
        <tr><td>4111</td><td>Remuneraciones por Pagar</td><td class="num">1,500.00</td><td class="num">1,500.00</td><td class="num">0.00</td><td class="num success">CONFORME</td><td>Pasivo laboral administrativo devengado al cierre OP10.</td></tr>
        <tr><td>4212</td><td>Proveedores por Pagar</td><td class="num">2,000.00</td><td class="num">2,000.00</td><td class="num">0.00</td><td class="num success">CONFORME</td><td>Saldo deudor tras amortización de S/ 2,000 en OP09.</td></tr>
        <tr><td>4511</td><td>Préstamos Bancarios Corto Plazo</td><td class="num">10,000.00</td><td class="num">10,000.00</td><td class="num">0.00</td><td class="num success">CONFORME</td><td>Deuda financiera recibida en bancos a 6 meses.</td></tr>
        <tr><td>4699</td><td>Anticipos Clientes (NIIF 15)</td><td class="num">9,000.00</td><td class="num">9,000.00</td><td class="num">0.00</td><td class="num success">CONFORME</td><td>Obligación de desempeño diferida del Hito 2.</td></tr>
        <tr><td>5011</td><td>Capital Social Aportado</td><td class="num">40,000.00</td><td class="num">40,000.00</td><td class="num">0.00</td><td class="num success">CONFORME</td><td>Aporte constitutivo inicial de los socios.</td></tr>
        <tr><td>7041</td><td>Ingresos Desarrollo Software</td><td class="num">24,000.00</td><td class="num">24,000.00</td><td class="num">0.00</td><td class="num success">CONFORME</td><td>Ingreso por Hito 1 aceptado formalmente.</td></tr>
        <tr><td>69</td><td>Costo del Servicio PANVIZ</td><td class="num">17,000.00</td><td class="num">17,000.00</td><td class="num">0.00</td><td class="num success">CONFORME</td><td>Sueldos técnicos (15k) y consumo de nube (2k).</td></tr>
        <tr><td>94</td><td>Gastos Administrativos Totales</td><td class="num">4,500.00</td><td class="num">4,500.00</td><td class="num">0.00</td><td class="num success">CONFORME</td><td>Gastos operativos generales (3k) y nómina dev. (1.5k).</td></tr>
        <tr><td>97</td><td>Gastos Financieros Intereses</td><td class="num">500.00</td><td class="num">500.00</td><td class="num">0.00</td><td class="num success">CONFORME</td><td>Interés devengado mensual pagado en OP11.</td></tr>
        <tr><td>5911</td><td>Utilidad Neta del Ejercicio</td><td class="num">2,000.00</td><td class="num">2,000.00</td><td class="num">0.00</td><td class="num success">CONFORME</td><td>Resultado del ejercicio idéntico en ambas plataformas.</td></tr>
        <tr class="highlight">
          <td colspan="2">TOTAL ACTIVO</td>
          <td class="num">64,500.00</td><td class="num">64,500.00</td><td class="num">0.00</td><td class="num success">CONFORME</td><td>Equilibrio patrimonial certificado al 100%.</td>
        </tr>
      </tbody>
    </table>

    <h2>Evidencias de la Plataforma Contable GnuCash (PANVIZ.gnucash)</h2>
    <div class="grid-2">
      <div class="img-box">
        <img src="capturas/captura_1_catalogo_cuentas_gnucash.png" alt="Catálogo GnuCash">
        <div class="img-caption">Evidencia 1: Árbol de Cuentas y Saldos en GnuCash (Total Activo: S/ 64,500.00)</div>
      </div>
      <div class="img-box">
        <img src="capturas/captura_2_transaccion_compuesta_gnucash.png" alt="Transacción Compuesta OP02">
        <div class="img-caption">Evidencia 2: Transacción Compuesta OP02 con Asiento Dividido (Split Transaction)</div>
      </div>
    </div>
  </div>

  <!-- PÁGINA 5: INDICADORES, PRESUPUESTO Y ESTRÉS A 45 DÍAS -->
  <div class="page">
    <div class="running-header">
      <span>Andes Software · Control Económico PANVIZ</span>
      <span>Sección VII & VIII: Indicadores y Presupuesto</span>
    </div>

    <h1>Sección VII: Indicadores Financieros y Diagnóstico</h1>
    <table class="data-table">
      <thead>
        <tr>
          <th>Indicador</th>
          <th>Fórmula Contable</th>
          <th style="text-align:right;">Valor</th>
          <th>Diagnóstico e Interpretación Gerencial</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Margen Bruto</td><td>Utilidad Bruta / Ventas</td><td class="num">29.17%</td><td>Eficiencia técnica: se retienen S/ 0.29 por sol facturado tras nómina y servidores.</td></tr>
        <tr><td>Margen Neto</td><td>Utilidad Neta / Ventas</td><td class="num">8.33%</td><td>Rentabilidad final modesta; cualquier desvío operativo puede convertirla en pérdida.</td></tr>
        <tr><td>Razón Corriente</td><td>Activo Cte. / Pasivo Cte.</td><td class="num">2.33</td><td>S/ 2.33 de respaldo contable por cada sol adeudado (incluye S/ 9k de anticipo diferido).</td></tr>
        <tr><td>Prueba Ácida</td><td>(Activo Cte. - Inv.) / Pasivo Cte.</td><td class="num">2.33</td><td>Empresa tecnológica sin inventarios físicos; liquidez formal excelente.</td></tr>
        <tr><td>Cobertura Inmediata</td><td>Saldo Bancos / Egresos 15 días</td><td class="num">1.89 veces</td><td>Caja disponible en bancos cubre 1.89 veces los compromisos ineludibles de 15 días.</td></tr>
      </tbody>
    </table>

    <h1>Sección VIII: Presupuesto de Caja Quincenal y la "Trampa de Liquidez" a 45 Días</h1>
    <div class="grid-2">
      <div>
        <h2>Presupuesto Quincenal (15 Días)</h2>
        <table class="data-table">
          <tr><th>Concepto de Flujo</th><th style="text-align:right;">Importe (S/)</th></tr>
          <tr><td>SALDO INICIAL BANCOS (Día 1)</td><td class="num">S/ 44,500.00</td></tr>
          <tr><td>(+) Cobros Proyectados Declarados</td><td class="num">S/ 0.00</td></tr>
          <tr><td>(-) Nómina de Desarrollo Prevista</td><td class="num danger">(S/ 18,000.00)</td></tr>
          <tr><td>(-) Infraestructura en la Nube</td><td class="num danger">(S/ 2,000.00)</td></tr>
          <tr><td>(-) Deuda Proveedor Equipos</td><td class="num danger">(S/ 2,000.00)</td></tr>
          <tr><td>(-) Sueldos Admin. Pendientes (OP10)</td><td class="num danger">(S/ 1,500.00)</td></tr>
          <tr class="bold"><td>Total Egresos Ineludibles (15 días)</td><td class="num danger">(S/ 23,500.00)</td></tr>
          <tr class="highlight"><td>SALDO PROYECTADO DÍA 15 (Superávit)</td><td class="num success">S/ 21,000.00</td></tr>
        </table>
      </div>

      <div>
        <h2>Simulación de Estrés a 45 Días</h2>
        <table class="data-table">
          <thead>
            <tr><th>Ventana</th><th style="text-align:right;">Egresos</th><th style="text-align:right;">Cobros</th><th style="text-align:right;">Saldo Caja</th></tr>
          </thead>
          <tbody>
            <tr><td>Día 1 – 15</td><td class="num">23,500</td><td class="num">0</td><td class="num success">S/ 21,000</td></tr>
            <tr><td>Día 16 – 30</td><td class="num">20,000</td><td class="num">0</td><td class="num warning">S/ 1,000</td></tr>
            <tr style="background:#fee2e2;">
              <td><strong>Día 31 – 44</strong></td>
              <td class="num">3,500</td>
              <td class="num">0</td>
              <td class="num danger"><strong>-S/ 2,500 (DEFAULT)</strong></td>
            </tr>
            <tr><td>Día 45 (Cobro)</td><td class="num">0</td><td class="num">8,000</td><td class="num success">S/ 5,500</td></tr>
          </tbody>
        </table>
        <div class="callout-alert">
          <strong>Riesgo Crítico de Cesación de Pagos:</strong> Entre los días 35 y 44, Andes Software enfrentará un déficit de <strong>-S/ 2,500.00</strong>. Aunque el cliente pagará S/ 8,000 en el día 45, la empresa no puede suspender salarios ni servidores cloud sin paralizar el servicio sanitario.
        </div>
      </div>
    </div>
  </div>

  <!-- PÁGINA 6: DECISIONES ESTRATÉGICAS, MATRIZ Y CONCLUSIONES -->
  <div class="page">
    <div class="running-header">
      <span>Andes Software · Control Económico PANVIZ</span>
      <span>Sección IX, X & XI: Decisiones y Cierre</span>
    </div>

    <h1>Sección IX: Tres Decisiones Gerenciales Estratégicas</h1>
    <div class="callout">
      <strong>Decisión 1: Factoring / Descuento del Hito 1 para Eliminar la Brecha de Liquidez:</strong><br>
      <em>Evidencia Contable:</em> Cuenta 1212 retiene S/ 8,000 a 45 días. <em>Medida:</em> Negociar factoring bancario o adenda de pronto pago al día 15 con descuento del 2.5% (costo financiero: S/ 200). <em>Responsable:</em> Mollo Chuquicaña (Plazo: Días 1 a 7). <em>Impacto:</em> Inyecta S/ 7,800 líquidos, elimina el déficit de -S/ 2,500 y blinda los salarios de desarrollo.
    </div>
    <div class="callout">
      <strong>Decisión 2: Aceleración Técnica y Certificación Anticipada del Módulo 2:</strong><br>
      <em>Evidencia Contable:</em> Pasivo 4699 acumula S/ 9,000 de anticipo no devengado (NIIF 15). <em>Medida:</em> Reorganizar sprints técnicos para entregar alertas y reportes el día 25, devengando el pasivo y habilitando la facturación siguiente. <em>Responsable:</em> Chambilla Perca (Plazo: 25 días). <em>Impacto:</em> Adelanta la vigilancia epidemiológica automatizada.
    </div>
    <div class="callout">
      <strong>Decisión 3: Reprogramación Comercial de Equipos y Optimización Cloud:</strong><br>
      <em>Evidencia Contable:</em> Pasivo 4212 (S/ 2k) y gasto cloud 6942 (S/ 2k/mes). <em>Medida:</em> Diferir saldo de hardware en dos cuotas y optimizar instancias cloud reduciendo costos un 20% (-S/ 500/mes). <em>Responsable:</em> Gutiérrez Ccama (Plazo: Días 5 a 12). <em>Impacto:</em> Libera S/ 1,500 de caja y asegura SLA 99.9% de uptime para postas de salud.
    </div>

    <h1>Sección X: Matriz de Revisión Cruzada del Equipo (4 Integrantes)</h1>
    <table class="data-table">
      <thead>
        <tr>
          <th>Integrante</th>
          <th>Rol Operativo</th>
          <th>Sección Custodiada</th>
          <th>Revisión Cruzada Realizada</th>
          <th style="text-align:center;">Conformidad</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>Suclle Suca, Michael B.</strong></td><td>Coordinador / Auditor</td><td>Control 43, Síntesis e Integración</td><td>Revisa Ratios y Decisiones de Mollo Chuquicaña</td><td class="num success">APROBADO (100%)</td></tr>
        <tr><td><strong>Chambilla Perca, Ricardo M.</strong></td><td>Especialista Contable</td><td>Diario, Mayor y Comprobación</td><td>Revisa Control 43 y Síntesis de Suclle Suca</td><td class="num success">APROBADO (100%)</td></tr>
        <tr><td><strong>Gutiérrez Ccama, Juan D.</strong></td><td>Especialista en Reportes</td><td>Estados Financieros y Conciliación</td><td>Revisa Diario, Mayor y Balances de Chambilla Perca</td><td class="num success">APROBADO (100%)</td></tr>
        <tr><td><strong>Mollo Chuquicaña, Dolly Y.</strong></td><td>Analista de Liquidez</td><td>Ratios, Presupuesto y Decisiones</td><td>Revisa Estados Financieros de Gutiérrez Ccama</td><td class="num success">APROBADO (100%)</td></tr>
      </tbody>
    </table>

    <h1>Sección XI: Conclusiones y Referencias Bibliográficas</h1>
    <p>
      1. Se demostró la consistencia matemática de la partida doble y la ecuación contable (Activo = Pasivo + Patrimonio = S/ 64,500.00) con conciliación exacta entre LibreOffice Calc y GnuCash.
      2. La aplicación de la NIIF 15 (anticipos como pasivo diferido) y la NIC 16 (hardware como activo PPE) evitó distorsiones en el resultado económico del proyecto.
      3. Se comprobó que la utilidad contable (S/ 2,000.00) no garantiza la liquidez de caja: la brecha de cobranza a 45 días exige aplicar factoring para proteger la continuidad de PANVIZ en salud pública.
    </p>
    <div style="font-size:7.5pt; color:#64748b; margin-top:5px;">
      <strong>Referencias (APA 7ma):</strong> Guim-Bustos, P., et al. (2023). Los estados financieros y las tomas de decisiones empresariales. <em>593 Digital Publisher CEIT</em>, 8(2), 149–160. · IASB. (2018). <em>NIIF 15: Ingresos</em>, <em>NIC 16: Propiedad, Planta y Equipo</em> & <em>NIC 7: Estado de Flujos de Efectivo</em>. · MEF. (2019). <em>Plan Contable General Empresarial (PCGE)</em>.
    </div>
  </div>

</body>
</html>
"""

# Guardar HTML compilado
with open(report_html_path, "w", encoding="utf-8") as f:
    f.write(html_report)

# Compilar a PDF usando Edge headless
print("Compilando informe a PDF usando Microsoft Edge headless...")
cmd = [
    EDGE_PATH,
    "--headless",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={output_pdf_path}",
    report_html_path
]
subprocess.run(cmd, check=True)

# Verificar páginas del PDF
reader = pypdf.PdfReader(output_pdf_path)
num_pages = len(reader.pages)
print(f"PDF generado exitosamente en: {output_pdf_path}")
print(f"Total de páginas: {num_pages} (Portada + {num_pages - 1} páginas de contenido)")

# Limpiar HTML temporal
try:
    os.remove(report_html_path)
except:
    pass
