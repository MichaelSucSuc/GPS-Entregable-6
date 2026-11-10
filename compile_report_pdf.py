import os
import subprocess
import pypdf

BASE_DIR = r"C:\Users\micha\Downloads\Borrar entregable 6\GPS-Entregable-6"
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
output_pdf_path = os.path.join(BASE_DIR, "INFORME_ENTREGABLE_6_CONTROL_ECONOMICO_PANVIZ.pdf")
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
    padding-top: 30px;
    height: 92vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-sizing: border-box;
  }
  .univ-header { font-size: 15pt; font-weight: 800; color: #1e3a8a; text-transform: uppercase; margin-bottom: 3px; }
  .fac-header { font-size: 11.5pt; font-weight: 700; color: #334155; margin-bottom: 2px; }
  .esc-header { font-size: 10.5pt; font-weight: 600; color: #475569; margin-bottom: 15px; }
  .logo-box { margin: 15px auto; width: 90px; height: 90px; border-radius: 50%; background: #f1f5f9; border: 3px solid #1e3a8a; display: flex; align-items: center; justify-content: center; font-size: 28pt; }
  .doc-type { font-size: 10.5pt; font-weight: bold; color: #b45309; text-transform: uppercase; letter-spacing: 1px; margin-top: 10px; }
  .doc-title { font-size: 18pt; font-weight: 800; color: #0f172a; margin: 8px 0 4px; line-height: 1.2; }
  .doc-subtitle { font-size: 11pt; color: #64748b; font-weight: 500; }
  
  .meta-box { background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 12px 20px; margin: 20px auto; text-align: left; max-width: 500px; font-size: 9pt; }
  .meta-row { display: flex; justify-content: space-between; margin-bottom: 3px; }
  .meta-label { font-weight: bold; color: #1e3a8a; }

  .team-table { width: 100%; border-collapse: collapse; margin-top: 6px; font-size: 8.5pt; }
  .team-table th { background: #e2e8f0; padding: 3px 5px; text-align: left; font-weight: bold; }
  .team-table td { padding: 3px 5px; border-bottom: 1px solid #e2e8f0; }

  .portada-foot { font-size: 9.5pt; font-weight: bold; color: #475569; }

  /* Secciones */
  .section-title {
    font-size: 10.5pt;
    font-weight: 800;
    color: #1e3a8a;
    border-bottom: 1.5px solid #1e3a8a;
    padding-bottom: 2px;
    margin-top: 10px;
    margin-bottom: 6px;
    text-transform: uppercase;
  }
  .subsection-title {
    font-size: 9.5pt;
    font-weight: 700;
    color: #0f172a;
    margin-top: 8px;
    margin-bottom: 4px;
  }

  p { margin: 0 0 5px 0; text-align: justify; }

  table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 5px 0 8px;
    font-size: 7.5pt;
  }
  table.data-table th {
    background: #1e3a8a;
    color: #ffffff;
    font-weight: 700;
    padding: 3px 5px;
    border: 1px solid #1e3a8a;
    text-align: left;
  }
  table.data-table td {
    padding: 2.5px 5px;
    border: 1px solid #cbd5e1;
  }
  table.data-table tr:nth-child(even) { background: #f8fafc; }
  .tar { text-align: right; }
  .tac { text-align: center; }
  .fwb { font-weight: bold; }

  .highlight-box {
    background: #f1f5f9;
    border-left: 3px solid #1e3a8a;
    padding: 5px 8px;
    margin: 6px 0;
    font-size: 8pt;
  }
  .alert-box {
    background: #fef2f2;
    border-left: 3px solid #ef4444;
    padding: 5px 8px;
    margin: 6px 0;
    font-size: 8pt;
  }
  .success-box {
    background: #f0fdf4;
    border-left: 3px solid #10b981;
    padding: 5px 8px;
    margin: 6px 0;
    font-size: 8pt;
  }

  .captura-box {
    text-align: center;
    margin: 4px 0;
    border: 1px solid #cbd5e1;
    padding: 4px;
    background: #f8fafc;
    border-radius: 3px;
  }
  .captura-img {
    max-width: 98%;
    height: auto;
    border: 1px solid #94a3b8;
  }
  .captura-caption {
    font-size: 7pt;
    font-weight: 600;
    color: #475569;
    margin-top: 2px;
  }

  .page-container {
    page-break-after: always;
    height: 96vh;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }
  .last-page {
    page-break-after: avoid;
    height: auto;
  }
  .page-num {
    text-align: right;
    font-size: 7.5pt;
    color: #94a3b8;
    margin-top: auto;
    border-top: 1px solid #e2e8f0;
    padding-top: 3px;
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
      
      <div class="logo-box">🏛️</div>

      <div class="doc-type">Entregable 6 · Semana 11</div>
      <div class="doc-title">TRABAJO PARCIAL DE CONTROL ECONÓMICO: PROYECTO PANVIZ</div>
      <div class="doc-subtitle">Evaluación Patrimonial, Desempeño Operativo y Sostenibilidad Financiera en Andes Software</div>
    </div>

    <div class="meta-box">
      <div class="meta-row"><span class="meta-label">Asignatura:</span><span>Gestión de Proyectos de Software</span></div>
      <div class="meta-row"><span class="meta-label">Docente:</span><span>M en C Jesús Martín Silva Fernández</span></div>
      <div class="meta-row"><span class="meta-label">Equipo de Trabajo:</span><span>Equipo 06</span></div>
      <div style="margin-top: 6px; font-weight: bold; color: #1e3a8a;">Integrantes del Equipo:</div>
      <table class="team-table">
        <tr><th>Estudiante</th><th>CUI</th><th>Correo Institucional</th></tr>
        <tr><td>Suclle Suca, Michael Benjamin</td><td>20210678</td><td>msuclles@unsa.edu.pe</td></tr>
        <tr><td>Fernandez Huarca, Rodrigo Alexander</td><td>20210672</td><td>rfernandezh@unsa.edu.pe</td></tr>
        <tr><td>Meza Vizcarra, Cielo Cristal</td><td>20210685</td><td>cmezav@unsa.edu.pe</td></tr>
        <tr><td>Borda Espinoza, Gabriela Nayely</td><td>20210665</td><td>gbordae@unsa.edu.pe</td></tr>
        <tr><td>Ccoscco Alvis, Italo Frankdux</td><td>20210669</td><td>iccosccoa@unsa.edu.pe</td></tr>
      </table>
    </div>

    <div class="portada-foot">
      Arequipa, Perú · Noviembre de 2026
    </div>
  </div>

  <!-- PÁGINA 1 DE CONTENIDO: SÍNTESIS CRÍTICA Y CATÁLOGO DE CUENTAS -->
  <div class="page-container">
    <div class="section-title">1. Síntesis Crítica de la Lectura Obligatoria</div>
    <p><strong>Referencia:</strong> Guim-Bustos, P., Martillo-Mieles, O., Guerrero-Cortez, V. y Carrillo-Pérez, F. (2023). Los estados financieros y las tomas de decisiones empresariales. <em>593 Digital Publisher CEIT</em>, 8(2), 149–160. DOI: 10.33386/593dp.2023.2.1679. (Páginas consultadas: 152–154. Conteo: 305 palabras).</p>
    <p>
      Los estados financieros representan el producto estructurado y culminante del proceso contable, cuyo objetivo fundamental es sintetizar la posición patrimonial, el desempeño operativo y los flujos monetarios de una entidad en un período determinado (Guim-Bustos et al., 2023, p. 152). Limitar la contabilidad al mero cumplimiento formal del registro en libros resulta estéril para la gerencia si la información cuantitativa no se somete a un análisis e interpretación sistemática que fundamente la toma de decisiones estratégicas. Como destacan Castrellón (2021) y Suanders (2006), citados en el texto (pp. 153–154), las decisiones gerenciales no pueden formularse a ciegas: requieren evaluar con certeza si las operaciones generan valor o pérdidas, y si las políticas de financiamiento y comercialización comprometen la viabilidad futura del negocio.
    </p>
    <p>
      Del análisis de las páginas 152 a 154 se desprenden dos ideas medulares aplicables al control económico del proyecto PANVIZ:  
      <strong>1. La diferenciación estricta de la estructura de costos (p. 154):</strong> En el desarrollo de software es indispensable clasificar con precisión los costos directos (remuneraciones técnicas de los desarrolladores y consumo de servidores en la nube asignables al producto) frente a los gastos administrativos indirectos. Esta discriminación previene distorsiones en el cálculo del margen de contribución de cada hito contractual.  
      <strong>2. El desfase temporal entre presupuestación, devengo y liquidez real (pp. 152–153):</strong> Brune (2019) advierte que contar con proyecciones de ingresos resulta inútil sin una confirmación estricta de las fechas efectivas de pago de los clientes. En proyectos tecnológicos, registrar ingresos devengados por hitos aprobados no garantiza liquidez inmediata para solventar nóminas o servidores, demandando un monitoreo riguroso del flujo de caja de corto plazo para evitar la parálisis operativa del servicio.
    </p>

    <div class="section-title">2. Clasificación Contable y Catálogo Mínimo de Cuentas</div>
    <p>Se estructuró el catálogo según el Plan Contable General Empresarial (PCGE) y su equivalencia con GnuCash:</p>
    <table class="data-table">
      <thead>
        <tr><th>Cód.</th><th>Cuenta Contable</th><th>Elemento</th><th>Nat.</th><th>Cuenta Mapeada en GnuCash</th></tr>
      </thead>
      <tbody>
        <tr><td class="tac fwb">1041</td><td>Bancos - Cuentas Corrientes</td><td>Activo Cte.</td><td>Deudora</td><td>Activos:Activo Corriente:Bancos:Cuenta Corriente</td></tr>
        <tr><td class="tac fwb">1212</td><td>Cuentas por Cobrar Comerciales</td><td>Activo Cte.</td><td>Deudora</td><td>Activos:Activo Corriente:Clientes:Facturas por Cobrar</td></tr>
        <tr><td class="tac fwb">3361</td><td>Equipos de Cómputo e Informáticos</td><td>Activo No Cte.</td><td>Deudora</td><td>Activos:Activo Fijo:Equipos Informáticos</td></tr>
        <tr><td class="tac fwb">4111</td><td>Remuneraciones por Pagar</td><td>Pasivo Cte.</td><td>Acreedora</td><td>Pasivos:Pasivo Corriente:Sueldos por Pagar</td></tr>
        <tr><td class="tac fwb">4212</td><td>Cuentas por Pagar Proveedores</td><td>Pasivo Cte.</td><td>Acreedora</td><td>Pasivos:Pasivo Corriente:Proveedores:Equipos</td></tr>
        <tr><td class="tac fwb">4511</td><td>Préstamo Bancario (Corto Plazo)</td><td>Pasivo Cte.</td><td>Acreedora</td><td>Pasivos:Pasivo Corriente:Préstamos Bancarios</td></tr>
        <tr><td class="tac fwb">4699</td><td>Anticipos de Clientes (Diferidos)</td><td>Pasivo Cte.</td><td>Acreedora</td><td>Pasivos:Pasivo Corriente:Anticipos de Clientes</td></tr>
        <tr><td class="tac fwb">5011</td><td>Capital Social (Aportes de Socios)</td><td>Patrimonio</td><td>Acreedora</td><td>Patrimonio:Capital Social:Aportes</td></tr>
        <tr><td class="tac fwb">5911</td><td>Resultado del Ejercicio (Utilidad)</td><td>Patrimonio</td><td>Acreedora</td><td>Patrimonio:Resultados Acumulados:Resultado del Mes</td></tr>
        <tr><td class="tac fwb">7041</td><td>Ingresos por Desarrollo Software</td><td>Ingreso</td><td>Acreedora</td><td>Ingresos:Ventas:Desarrollo de Software</td></tr>
        <tr><td class="tac fwb">6941</td><td>Costo: Remuneraciones Desarrollo</td><td>Costo Serv.</td><td>Deudora</td><td>Gastos:Costo del Servicio:Remuneraciones Desarrollo</td></tr>
        <tr><td class="tac fwb">6942</td><td>Costo: Servicios de Nube</td><td>Costo Serv.</td><td>Deudora</td><td>Gastos:Costo del Servicio:Servicios de Nube</td></tr>
        <tr><td class="tac fwb">9411</td><td>Gastos Administrativos Generales</td><td>Gasto Oper.</td><td>Deudora</td><td>Gastos:Gastos Administrativos:Operativos Generales</td></tr>
        <tr><td class="tac fwb">9412</td><td>Gastos Adm. Sueldos Devengados</td><td>Gasto Oper.</td><td>Deudora</td><td>Gastos:Gastos Administrativos:Remuneraciones</td></tr>
        <tr><td class="tac fwb">9711</td><td>Gastos Financieros (Intereses)</td><td>Gasto Financ.</td><td>Deudora</td><td>Gastos:Gastos Financieros:Intereses Bancarios</td></tr>
      </tbody>
    </table>
    <div class="page-num">Página 1 de 6 (Sin contar portada)</div>
  </div>

  <!-- PÁGINA 2 DE CONTENIDO: LIBRO DIARIO Y BALANCE DE COMPROBACIÓN -->
  <div class="page-container">
    <div class="section-title">3. Registro en Libro Diario y Balance de Comprobación</div>
    <table class="data-table">
      <thead>
        <tr><th class="tac">Fecha</th><th class="tac">Op.</th><th>Cuentas y Glosa / Descripción Técnica</th><th class="tar">Debe (S/)</th><th class="tar">Haber (S/)</th></tr>
      </thead>
      <tbody>
        <tr><td class="tac">02/11</td><td class="tac fwb">OP01</td><td>1041 Bancos / 5011 Capital Social · Aporte inicial socios cuenta bancaria</td><td class="tar">40,000.00</td><td class="tar">40,000.00</td></tr>
        <tr><td class="tac">05/11</td><td class="tac fwb">OP02</td><td>3361 Equipos Informáticos / 1041 Bancos (8k) - 4212 Proveedores (4k)</td><td class="tar">12,000.00</td><td class="tar">12,000.00</td></tr>
        <tr><td class="tac">07/11</td><td class="tac fwb">OP03</td><td>1041 Bancos / 4511 Préstamos Bancarios · Desembolso pagaré a 6 meses</td><td class="tar">10,000.00</td><td class="tar">10,000.00</td></tr>
        <tr><td class="tac">10/11</td><td class="tac fwb">OP04</td><td>1041 Bancos / 4699 Anticipos de Clientes · Cobro adelantado módulo alertas</td><td class="tar">9,000.00</td><td class="tar">9,000.00</td></tr>
        <tr><td class="tac">15/11</td><td class="tac fwb">OP05</td><td>6941 Costo Remun. Desarrollo / 1041 Bancos · Planilla técnica mensual</td><td class="tar">15,000.00</td><td class="tar">15,000.00</td></tr>
        <tr><td class="tac">18/11</td><td class="tac fwb">OP06</td><td>6942 Costo Nube / 1041 Bancos · Infraestructura cloud servidores mes</td><td class="tar">2,000.00</td><td class="tar">2,000.00</td></tr>
        <tr><td class="tac">20/11</td><td class="tac fwb">OP07</td><td>9411 Gastos Administrativos / 1041 Bancos · Gastos operativos generales</td><td class="tar">3,000.00</td><td class="tar">3,000.00</td></tr>
        <tr><td class="tac">25/11</td><td class="tac fwb">OP08</td><td>1041 Bancos (16k) - 1212 Clientes (8k) / 7041 Ingresos Software Hito 1</td><td class="tar">24,000.00</td><td class="tar">24,000.00</td></tr>
        <tr><td class="tac">27/11</td><td class="tac fwb">OP09</td><td>4212 Proveedores / 1041 Bancos · Amortización deuda proveedor hardware</td><td class="tar">2,000.00</td><td class="tar">2,000.00</td></tr>
        <tr><td class="tac">30/11</td><td class="tac fwb">OP10</td><td>9412 Gastos Adm. Sueldos / 4111 Remuneraciones por Pagar · Devengo</td><td class="tar">1,500.00</td><td class="tar">1,500.00</td></tr>
        <tr><td class="tac">30/11</td><td class="tac fwb">OP11</td><td>9711 Gastos Financieros / 1041 Bancos · Pago intereses de préstamo</td><td class="tar">500.00</td><td class="tar">500.00</td></tr>
        <tr style="background:#e2e8f0; font-weight:bold;"><td colspan="3" class="tar">SUMAS TOTALES DEL LIBRO DIARIO</td><td class="tar">S/ 119,000.00</td><td class="tar">S/ 119,000.00</td></tr>
      </tbody>
    </table>

    <div class="subsection-title">Balance de Comprobación de Sumas y Saldos (Mayorización)</div>
    <table class="data-table">
      <thead>
        <tr><th>Cód.</th><th>Cuenta Contable</th><th class="tar">Sumas Debe</th><th class="tar">Sumas Haber</th><th class="tar">Saldo Deudor</th><th class="tar">Saldo Acreedor</th></tr>
      </thead>
      <tbody>
        <tr><td class="tac">1041</td><td>Bancos - Cuentas Corrientes</td><td class="tar">75,000.00</td><td class="tar">30,500.00</td><td class="tar fwb">44,500.00</td><td class="tar">-</td></tr>
        <tr><td class="tac">1212</td><td>Cuentas por Cobrar Comerciales</td><td class="tar">8,000.00</td><td class="tar">0.00</td><td class="tar fwb">8,000.00</td><td class="tar">-</td></tr>
        <tr><td class="tac">3361</td><td>Equipos de Cómputo e Informáticos</td><td class="tar">12,000.00</td><td class="tar">0.00</td><td class="tar fwb">12,000.00</td><td class="tar">-</td></tr>
        <tr><td class="tac">4111</td><td>Remuneraciones por Pagar</td><td class="tar">0.00</td><td class="tar">1,500.00</td><td class="tar">-</td><td class="tar fwb">1,500.00</td></tr>
        <tr><td class="tac">4212</td><td>Proveedores por Pagar</td><td class="tar">2,000.00</td><td class="tar">4,000.00</td><td class="tar">-</td><td class="tar fwb">2,000.00</td></tr>
        <tr><td class="tac">4511</td><td>Préstamo Bancario Corto Plazo</td><td class="tar">0.00</td><td class="tar">10,000.00</td><td class="tar">-</td><td class="tar fwb">10,000.00</td></tr>
        <tr><td class="tac">4699</td><td>Anticipos de Clientes (Diferidos)</td><td class="tar">0.00</td><td class="tar">9,000.00</td><td class="tar">-</td><td class="tar fwb">9,000.00</td></tr>
        <tr><td class="tac">5011</td><td>Capital Social (Aportes)</td><td class="tar">0.00</td><td class="tar">40,000.00</td><td class="tar">-</td><td class="tar fwb">40,000.00</td></tr>
        <tr><td class="tac">7041</td><td>Ingresos por Desarrollo Software</td><td class="tar">0.00</td><td class="tar">24,000.00</td><td class="tar">-</td><td class="tar fwb">24,000.00</td></tr>
        <tr><td class="tac">6941</td><td>Costo: Remuneraciones Desarrollo</td><td class="tar">15,000.00</td><td class="tar">0.00</td><td class="tar fwb">15,000.00</td><td class="tar">-</td></tr>
        <tr><td class="tac">6942</td><td>Costo: Servicios de Nube</td><td class="tar">2,000.00</td><td class="tar">0.00</td><td class="tar fwb">2,000.00</td><td class="tar">-</td></tr>
        <tr><td class="tac">9411</td><td>Gastos Administrativos Generales</td><td class="tar">3,000.00</td><td class="tar">0.00</td><td class="tar fwb">3,000.00</td><td class="tar">-</td></tr>
        <tr><td class="tac">9412</td><td>Gastos Adm. Sueldos Devengados</td><td class="tar">1,500.00</td><td class="tar">0.00</td><td class="tar fwb">1,500.00</td><td class="tar">-</td></tr>
        <tr><td class="tac">9711</td><td>Gastos Financieros (Intereses)</td><td class="tar">500.00</td><td class="tar">0.00</td><td class="tar fwb">500.00</td><td class="tar">-</td></tr>
        <tr style="background:#e2e8f0; font-weight:bold;"><td colspan="2" class="tar">TOTALES GENERALES</td><td class="tar">S/ 119,000.00</td><td class="tar">S/ 119,000.00</td><td class="tar">S/ 86,500.00</td><td class="tar">S/ 86,500.00</td></tr>
      </tbody>
    </table>
    <div class="success-box">
      <strong>Control Partida Doble y Saldos:</strong> Sumas Debe = Haber (S/ 119,000.00) y Saldos Deudores = Acreedores (S/ 86,500.00). Diferencia: <strong>S/ 0.00</strong>.
    </div>
    <div class="page-num">Página 2 de 6 (Sin contar portada)</div>
  </div>

  <!-- PÁGINA 3 DE CONTENIDO: ESTADOS FINANCIEROS -->
  <div class="page-container">
    <div class="section-title">4. Estados Financieros al Cierre del Mes 1 (Noviembre 2026)</div>
    
    <div style="display:flex; gap:12px;">
      <div style="flex:1;">
        <div class="subsection-title">Estado de Situación Financiera al 30/11/2026</div>
        <table class="data-table" style="font-size:7.5pt;">
          <thead><tr><th>Concepto</th><th class="tar">Importe (S/)</th></tr></thead>
          <tbody>
            <tr style="background:#f1f5f9; font-weight:bold;"><td colspan="2">ACTIVO CORRIENTE</td></tr>
            <tr><td>1041 Bancos - Cuenta Corriente</td><td class="tar">44,500.00</td></tr>
            <tr><td>1212 Cuentas por Cobrar Comerciales</td><td class="tar">8,000.00</td></tr>
            <tr class="fwb"><td>Total Activo Corriente</td><td class="tar">52,500.00</td></tr>
            <tr style="background:#f1f5f9; font-weight:bold;"><td colspan="2">ACTIVO NO CORRIENTE</td></tr>
            <tr><td>3361 Equipos Informáticos y Cómputo</td><td class="tar">12,000.00</td></tr>
            <tr class="fwb"><td>Total Activo No Corriente</td><td class="tar">12,000.00</td></tr>
            <tr style="background:#e0f2fe; font-weight:bold; color:#0369a1;"><td>TOTAL ACTIVO</td><td class="tar">S/ 64,500.00</td></tr>
            <tr style="background:#f1f5f9; font-weight:bold;"><td colspan="2">PASIVO CORRIENTE</td></tr>
            <tr><td>4212 Proveedores por Pagar</td><td class="tar">2,000.00</td></tr>
            <tr><td>4511 Préstamos Bancarios (6 meses)</td><td class="tar">10,000.00</td></tr>
            <tr><td>4699 Anticipos de Clientes (Diferidos)</td><td class="tar">9,000.00</td></tr>
            <tr><td>4111 Remuneraciones por Pagar</td><td class="tar">1,500.00</td></tr>
            <tr class="fwb"><td>Total Pasivo Corriente</td><td class="tar">22,500.00</td></tr>
            <tr style="background:#f1f5f9; font-weight:bold;"><td colspan="2">PATRIMONIO NETO</td></tr>
            <tr><td>5011 Capital Social (Aportes de Socios)</td><td class="tar">40,000.00</td></tr>
            <tr><td>5911 Resultado del Ejercicio (Utilidad)</td><td class="tar">2,000.00</td></tr>
            <tr class="fwb"><td>Total Patrimonio Neto</td><td class="tar">42,000.00</td></tr>
            <tr style="background:#e0f2fe; font-weight:bold; color:#0369a1;"><td>TOTAL PASIVO Y PATRIMONIO</td><td class="tar">S/ 64,500.00</td></tr>
          </tbody>
        </table>
      </div>

      <div style="flex:1;">
        <div class="subsection-title">Estado de Resultados (01 al 30/11/2026)</div>
        <table class="data-table" style="font-size:7.5pt;">
          <thead><tr><th>Concepto</th><th class="tar">Soles (S/)</th><th class="tar">%</th></tr></thead>
          <tbody>
            <tr class="fwb"><td>Ingresos por Desarrollo Software</td><td class="tar">24,000.00</td><td class="tar">100.0%</td></tr>
            <tr><td>(-) Remuneraciones Desarrollo</td><td class="tar">(15,000.00)</td><td class="tar">-62.5%</td></tr>
            <tr><td>(-) Servicios de Nube</td><td class="tar">(2,000.00)</td><td class="tar">-8.3%</td></tr>
            <tr class="fwb" style="background:#f1f5f9;"><td>UTILIDAD BRUTA</td><td class="tar">7,000.00</td><td class="tar">29.2%</td></tr>
            <tr><td>(-) Gastos Adm. Generales</td><td class="tar">(3,000.00)</td><td class="tar">-12.5%</td></tr>
            <tr><td>(-) Sueldos Adm. Devengados</td><td class="tar">(1,500.00)</td><td class="tar">-6.3%</td></tr>
            <tr class="fwb" style="background:#f1f5f9;"><td>UTILIDAD OPERATIVA</td><td class="tar">2,500.00</td><td class="tar">10.4%</td></tr>
            <tr><td>(-) Intereses Financieros Préstamo</td><td class="tar">(500.00)</td><td class="tar">-2.1%</td></tr>
            <tr class="fwb" style="background:#ecfdf5; color:#047857;"><td>UTILIDAD NETA DEL MES</td><td class="tar">S/ 2,000.00</td><td class="tar">8.33%</td></tr>
          </tbody>
        </table>

        <div class="subsection-title">Flujo de Efectivo - Método Directo</div>
        <table class="data-table" style="font-size:7.5pt;">
          <thead><tr><th>Actividad</th><th class="tar">Neto (S/)</th></tr></thead>
          <tbody>
            <tr><td>Cobros Hito 1 (16k) + Anticipo (9k)</td><td class="tar">25,000.00</td></tr>
            <tr><td>(-) Pagos Operativos (Nómina+Nube+Adm+Int)</td><td class="tar">(20,500.00)</td></tr>
            <tr class="fwb" style="background:#f1f5f9;"><td>Flujo Neto de Operación</td><td class="tar">+4,500.00</td></tr>
            <tr><td>(-) Pagos Equipos Hardware (8k + 2k)</td><td class="tar">(10,000.00)</td></tr>
            <tr class="fwb" style="background:#f1f5f9;"><td>Flujo Neto de Inversión</td><td class="tar">-10,000.00</td></tr>
            <tr><td>Aporte Socios (40k) + Préstamo (10k)</td><td class="tar">50,000.00</td></tr>
            <tr class="fwb" style="background:#f1f5f9;"><td>Flujo Neto de Financiación</td><td class="tar">+50,000.00</td></tr>
            <tr class="fwb" style="background:#e0f2fe; color:#0369a1;"><td>SALDO FINAL EN BANCOS</td><td class="tar">S/ 44,500.00</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="highlight-box">
      <strong>Declaración del Criterio de Intereses (NIC 7):</strong> Clasificados en Actividades de Operación (S/ 500.00) por sustentar la liquidez operativa diaria del proyecto. El saldo de flujo (S/ 44,500.00) concilia 100% con bancos.
    </div>
    <div class="page-num">Página 3 de 6 (Sin contar portada)</div>
  </div>

  <!-- PÁGINA 4 DE CONTENIDO: COMPROBACIONES TEÓRICAS Y CONCILIACIÓN GNUCASH -->
  <div class="page-container">
    <div class="section-title">5. Verificaciones Teóricas y Conciliación con GnuCash</div>
    
    <div class="subsection-title">Fundamentos Contables Normativos</div>
    <p>
      <strong>• ¿Por qué el anticipo es un pasivo y no una utilidad disponible?</strong><br>
      Bajo la NIIF 15, los ingresos se reconocen cuando se transfiere el control de los bienes o servicios al cliente. En la OP04, los S/ 9,000.00 recibidos por adelantado corresponden al módulo de alertas que aún no ha sido desarrollado ni entregado. Por tanto, no existe ganancia devengada sino una <strong>obligación de desempeño ineludible</strong> que demanda destinar horas de trabajo y servidores futuros. Si el servicio no se ejecuta, nace la obligación jurídica de restituir el dinero. Tratarlo como utilidad disponible induciría a un gasto imprudente de recursos no devengados.
    </p>
    <p>
      <strong>• ¿Por qué comprar equipos no equivale a reconocer un gasto completo del mes?</strong><br>
      Bajo la NIC 16, un activo es un recurso controlado que generará beneficios económicos futuros durante varios ejercicios. Las computadoras adquiridas por S/ 12,000.00 no se extinguen en noviembre; constituyen la plataforma técnica para desarrollar PANVIZ y proyectos subsiguientes durante una vida útil de 3 a 5 años. Asignar el importe total a resultados violaría el <strong>principio de correlación de ingresos y gastos</strong>, arrojando una falsa pérdida artificial. Su costo se reconoce de manera gradual mediante la depreciación sistemática.
    </p>

    <div class="subsection-title">Tabla de Conciliación Integral Calc / Excel vs. GnuCash (Corte 30/11/2026)</div>
    <table class="data-table">
      <thead>
        <tr><th>Cód.</th><th>Cuenta Contable / Indicador</th><th class="tar">Saldo Calc (S/)</th><th class="tar">Saldo GnuCash (S/)</th><th class="tar">Diferencia</th><th class="tac">Estado de Conciliación</th></tr>
      </thead>
      <tbody>
        <tr><td class="tac">1041</td><td>Bancos - Cuentas Corrientes</td><td class="tar">44,500.00</td><td class="tar">44,500.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac">1212</td><td>Cuentas por Cobrar Comerciales</td><td class="tar">8,000.00</td><td class="tar">8,000.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac">3361</td><td>Equipos de Cómputo e Informáticos</td><td class="tar">12,000.00</td><td class="tar">12,000.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac">4111</td><td>Remuneraciones por Pagar</td><td class="tar">1,500.00</td><td class="tar">1,500.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac">4212</td><td>Proveedores por Pagar</td><td class="tar">2,000.00</td><td class="tar">2,000.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac">4511</td><td>Préstamos Bancarios Corto Plazo</td><td class="tar">10,000.00</td><td class="tar">10,000.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac">4699</td><td>Anticipos de Clientes (Diferidos)</td><td class="tar">9,000.00</td><td class="tar">9,000.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac">5011</td><td>Capital Social Aportado</td><td class="tar">40,000.00</td><td class="tar">40,000.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac">7041</td><td>Ingresos por Desarrollo Software</td><td class="tar">24,000.00</td><td class="tar">24,000.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac">6941</td><td>Costo: Remuneraciones Desarrollo</td><td class="tar">15,000.00</td><td class="tar">15,000.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac">6942</td><td>Costo: Servicios de Nube</td><td class="tar">2,000.00</td><td class="tar">2,000.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac">9411</td><td>Gastos Administrativos Generales</td><td class="tar">3,000.00</td><td class="tar">3,000.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac">9412</td><td>Gastos Adm. Sueldos Devengados</td><td class="tar">1,500.00</td><td class="tar">1,500.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac">9711</td><td>Gastos Financieros (Intereses)</td><td class="tar">500.00</td><td class="tar">500.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac fwb">5911</td><td>Utilidad Neta del Ejercicio</td><td class="tar fwb">2,000.00</td><td class="tar fwb">2,000.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr><td class="tac fwb">PAT</td><td>Total Patrimonio Neto</td><td class="tar fwb">42,000.00</td><td class="tar fwb">42,000.00</td><td class="tar fwb">0.00</td><td class="tac" style="color:green; font-weight:bold;">CONCILIADO</td></tr>
        <tr style="background:#ecfdf5; font-weight:bold;"><td colspan="4" class="tar">SUMATORIA TOTAL DE DIFERENCIAS</td><td class="tar" style="color:#047857;">S/ 0.00</td><td class="tac" style="color:#047857;">100% CONCILIADO</td></tr>
      </tbody>
    </table>
    <div class="page-num">Página 4 de 6 (Sin contar portada)</div>
  </div>

  <!-- PÁGINA 5 DE CONTENIDO: EVALUACIÓN ECONÓMICA Y DECISIONES -->
  <div class="page-container">
    <div class="section-title">6. Evaluación Económica, Presupuesto y Riesgo de Caja</div>
    
    <div class="subsection-title">Indicadores Financieros Clave</div>
    <table class="data-table">
      <thead><tr><th>Indicador</th><th class="tac">Valor</th><th>Fórmula Aplicada</th><th>Diagnóstico Crítico</th></tr></thead>
      <tbody>
        <tr><td class="fwb">Margen Neto</td><td class="tac fwb" style="color:#047857;">8.33%</td><td>Resultado / Ingresos (2k / 24k)</td><td>Rentabilidad sobre facturación modesta, absorbida en 70.8% por costos directos.</td></tr>
        <tr><td class="fwb">Razón Corriente</td><td class="tac fwb" style="color:#b45309;">2.33</td><td>Act. Corriente / Pas. Corriente (52.5k / 22.5k)</td><td>Aparente solvencia distorsionada por cuentas por cobrar ilíquidas y pasivo diferido.</td></tr>
        <tr><td class="fwb">Cobertura Inmediata</td><td class="tac fwb" style="color:#0369a1;">1.89</td><td>Bancos / Pagos 15 días (44.5k / 23.5k)</td><td>Liquidez quincenal suficiente, pero altamente vulnerable en las semanas siguientes.</td></tr>
      </tbody>
    </table>

    <div class="subsection-title">Presupuesto de Caja a 15 Días y Estrés Financiero a 45 Días</div>
    <div style="display:flex; gap:12px;">
      <div style="flex:1;">
        <table class="data-table" style="font-size:7.5pt;">
          <thead><tr style="background:#334155;"><th>Presupuesto Días 1 a 15</th><th class="tar">Importe (S/)</th></tr></thead>
          <tbody>
            <tr><td>Saldo Inicial en Bancos al 01/12</td><td class="tar fwb">44,500.00</td></tr>
            <tr><td>(+) Cobros previstos de clientes</td><td class="tar">0.00</td></tr>
            <tr><td>(-) Remuneraciones técnicas previstas</td><td class="tar">(18,000.00)</td></tr>
            <tr><td>(-) Servicios de infraestructura en nube</td><td class="tar">(2,000.00)</td></tr>
            <tr><td>(-) Deuda restante proveedor equipos</td><td class="tar">(2,000.00)</td></tr>
            <tr><td>(-) Sueldos administrativos devengados</td><td class="tar">(1,500.00)</td></tr>
            <tr class="fwb" style="background:#f1f5f9;"><td>TOTAL EGRESOS EN 15 DÍAS</td><td class="tar">(23,500.00)</td></tr>
            <tr class="fwb" style="background:#ecfdf5; color:#047857;"><td>SALDO FINAL DÍA 15 (EXCEDENTE)</td><td class="tar">S/ 21,000.00</td></tr>
          </tbody>
        </table>
      </div>

      <div style="flex:1;">
        <table class="data-table" style="font-size:7.5pt;">
          <thead><tr style="background:#991b1b;"><th>Proyección de Estrés (Días 16 a 45)</th><th class="tar">Importe (S/)</th></tr></thead>
          <tbody>
            <tr><td>Saldo Inicial remanente al Día 16</td><td class="tar fwb">21,000.00</td></tr>
            <tr><td>(+) Cobranzas previstas Día 16 al 44</td><td class="tar">0.00</td></tr>
            <tr><td>(-) Nómina técnica segunda quincena</td><td class="tar">(18,000.00)</td></tr>
            <tr><td>(-) Nube del mes siguiente</td><td class="tar">(2,000.00)</td></tr>
            <tr><td>(-) Gastos administrativos recurrentes</td><td class="tar">(3,500.00)</td></tr>
            <tr class="fwb" style="background:#fee2e2; color:#991b1b;"><td>DÉFICIT PROYECTADO DÍA 44</td><td class="tar">-S/ 2,500.00</td></tr>
            <tr><td>(+) Cobro de factura cliente en Día 45</td><td class="tar">8,000.00</td></tr>
            <tr class="fwb" style="background:#f1f5f9;"><td>Saldo Final en Día 45 tras Cobro</td><td class="tar">S/ 5,500.00</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="alert-box">
      <strong>La Ilusión de la Utilidad y la Razón Corriente:</strong>  
      La utilidad de S/ 2,000.00 es devengada pero no líquida; contiene S/ 8,000.00 que se cobrarán recién en 45 días. Por su parte, la razón corriente de 2.33 incluye ese monto inmovilizado y S/ 9,000.00 de anticipos que demandarán quemar caja en programadores sin inyectar nuevo efectivo. El saldo de bancos actual proviene de préstamos y aportes, no del ciclo comercial. Sin gestión de cobranza, <strong>Andes Software quebraría por falta de caja en el día 35</strong>.
    </div>

    <div class="section-title">7. Tres Decisiones Estratégicas y Continuidad Sanitaria</div>
    <p><strong>1. Negociación de Cobranza Anticipada (Factoring o Pronto Pago):</strong> La Gerencia General negociará en 7 días un pronto pago con 3% de descuento (S/ 7,760 netos) o un factoring bancario de los S/ 8,000. <em>Efecto sanitario:</em> Garantiza liquidez para remuneraciones técnicas sin demoras.</p>
    <p><strong>2. Fondo de Reserva Intangible para Servidores y Personal Crítico:</strong> TI y Finanzas blindarán en 3 días S/ 20,000 del saldo de caja para servidores cloud y salarios clave. <em>Efecto sanitario:</em> Cero interrupciones (99.9% uptime) en la ingesta hospitalaria de datos epidemiológicos.</p>
    <p><strong>3. Partición del Módulo Anticipado en Sub-hitos Quincenales:</strong> El Líder de Proyecto dividirá en 10 días el módulo de alertas en dos entregas quincenales de S/ 4,500 cada una. <em>Efecto sanitario:</em> Los hospitales recibirán alertas tempranas en 15 días, conteniendo brotes epidémicos con anticipación.</p>
    <div class="page-num">Página 5 de 6 (Sin contar portada)</div>
  </div>

  <!-- PÁGINA 6 DE CONTENIDO: EVIDENCIAS GNUCASH, ROLES Y CONCLUSIONES -->
  <div class="page-container last-page">
    <div class="section-title">8. Evidencias Mínimas en GnuCash (Sección 10)</div>
    
    <div style="display:flex; gap:8px;">
      <div class="captura-box" style="flex:1;">
        <img class="captura-img" src="capturas/captura_1_catalogo_cuentas_gnucash.png" alt="Catálogo GnuCash">
        <div class="captura-caption">Captura 1: Catálogo de cuentas y árbol de saldos en GnuCash (Activo: S/ 64,500.00).</div>
      </div>
      <div class="captura-box" style="flex:1;">
        <img class="captura-img" src="capturas/captura_2_transaccion_compuesta_gnucash.png" alt="Transacción OP08">
        <div class="captura-caption">Captura 2: Transacción dividida (Split) OP08 por S/ 24,000.00 balanceada a cero.</div>
      </div>
    </div>

    <div style="display:flex; gap:8px;">
      <div class="captura-box" style="flex:1;">
        <img class="captura-img" src="capturas/captura_3_balance_general_gnucash.png" alt="Balance GnuCash">
        <div class="captura-caption">Captura 3: Reporte de Balance de Situación exportado desde GnuCash.</div>
      </div>
      <div class="captura-box" style="flex:1;">
        <img class="captura-img" src="capturas/captura_4_estado_resultados_gnucash.png" alt="Resultados GnuCash">
        <div class="captura-caption">Captura 4: Reporte de Pérdidas y Ganancias (Utilidad: S/ 2,000.00).</div>
      </div>
    </div>

    <div class="subsection-title">Matriz de Responsabilidades y Revisión Cruzada (Peer Review)</div>
    <table class="data-table" style="font-size:7pt;">
      <thead>
        <tr><th>#</th><th>Integrante</th><th>Responsabilidad Principal</th><th>Entregable Custodiado</th><th>Revisión Cruzada</th><th>Dictamen</th></tr>
      </thead>
      <tbody>
        <tr><td class="tac">1</td><td>Suclle Suca, Michael</td><td>Coordinación y síntesis crítica</td><td>Informe general, Diapositiva 1</td><td>Revisa decisiones del integrante 5</td><td class="tac fwb" style="color:green;">APROBADO</td></tr>
        <tr><td class="tac">2</td><td>Fernandez Huarca, Rodrigo</td><td>Catálogo y registros GnuCash</td><td>Libro .gnucash, Diapositiva 2</td><td>Revisa síntesis del integrante 1</td><td class="tac fwb" style="color:green;">APROBADO</td></tr>
        <tr><td class="tac">3</td><td>Meza Vizcarra, Cielo</td><td>Hoja de cálculo y comprobación</td><td>Diario, Mayor, Comprobación .xlsx</td><td>Revisa registros GnuCash del int. 2</td><td class="tac fwb" style="color:green;">APROBADO</td></tr>
        <tr><td class="tac">4</td><td>Borda Espinoza, Gabriela</td><td>Estados financieros y conciliación</td><td>Estados y conciliación .xlsx</td><td>Revisa mayorización de la int. 3</td><td class="tac fwb" style="color:green;">APROBADO</td></tr>
        <tr><td class="tac">5</td><td>Ccoscco Alvis, Italo</td><td>Indicadores, caja y decisiones</td><td>Caja 15 días, Diapositiva 5</td><td>Revisa estados de la integrante 4</td><td class="tac fwb" style="color:green;">APROBADO</td></tr>
      </tbody>
    </table>

    <div class="subsection-title">Conclusiones Finales</div>
    <p style="font-size:7.5pt; margin-bottom:4px;">
      El control económico formal demostró que Andes Software mantiene una estructura patrimonial balanceada (S/ 64,500.00) y utilidad contable positiva (S/ 2,000.00), pero enfrenta una amenaza severa de iliquidez quincenal debido a que su caja no proviene de la explotación comercial sino de capital y deuda. La adopción de decisiones estratégicas de cobranza acelerada y blindaje de la nube asegura la continuidad ininterrumpida de PANVIZ como plataforma crítica de salud pública.
    </p>

    <div class="subsection-title" style="margin-top:4px;">Referencias Bibliográficas (APA 7)</div>
    <p style="font-size:6.8pt; color:#475569; margin:0;">
      • Guim-Bustos, P., et al. (2023). Los estados financieros y las tomas de decisiones empresariales. <em>593 Digital Publisher CEIT</em>, 8(2), 149–160. · IASB (2018). <em>Marco Conceptual para la Información Financiera</em>. · IASB (2014). <em>NIIF 15: Ingresos de Actividades Ordinarias</em>. · IASB (2001). <em>NIC 7: Estado de Flujos de Efectivo</em>. · IASB (2003). <em>NIC 16: Propiedad, Planta y Equipo</em>. · MEF (2019). <em>Plan Contable General Empresarial (PCGE)</em>.
    </p>
    <div class="page-num">Página 6 de 6 (Sin contar portada)</div>
  </div>

</body>
</html>
"""

with open(report_html_path, "w", encoding="utf-8") as f:
    f.write(html_report)

cmd = [
    EDGE_PATH,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={output_pdf_path}",
    report_html_path
]
subprocess.run(cmd, capture_output=True)

reader = pypdf.PdfReader(output_pdf_path)
print(f"Número total de páginas en el PDF generado: {len(reader.pages)}")

try:
    os.remove(report_html_path)
except:
    pass
