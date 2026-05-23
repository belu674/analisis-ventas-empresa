# Proyecto: Análisis de Ventas de la Empresa (Escenario B)

Trabajo Práctico: Gestión Colaborativa, Control de Versiones y Organización Empresarial.

---

### 👤 Autoría y Simulación de Roles
* **Estudiante:** Jesica Belén Molina
* **Modalidad:** Individual
* **Estrategia de Desarrollo:** Para cumplir con los requerimientos de metodologías ágiles y control de versiones solicitados en la consigna, el proyecto simuló una célula de trabajo utilizando tres identidades ficticias en el historial de Git:
  1. **Hugo (Líder / P1):** Responsable de la gobernanza, creación del repositorio y configuración inicial del entorno (`.gitignore`).
  2. **Paco (Desarrollador / P2):** Encargado de la lógica del script de análisis estadístico y la manipulación del set de datos.
  3. **Luis (Revisor - QA / P3):** Responsable del control de calidad, revisión por pares (Peer Review) y documentación.

---

### 📊 Descripción del Proyecto y Dataset
Este proyecto tiene como objetivo desarrollar un análisis para procesar el histórico de transacciones comerciales de una pequeña empresa. El sistema calculará indicadores clave de rendimiento (ventas totales, productos destacados y tendencias mensuales) y exportará reportes gráficos automatizados para la toma de decisiones.

* El dataset utilizado (`ventas.csv`) se almacena en la carpeta `/datos` y contiene variables relativas a fechas de venta, productos, cantidades y precios unitarios.

---

### 📁 Estructura del Repositorio
* `/datos`: Contiene los archivos de datos e históricos en formato CSV.
* `/scripts`: Programas y scripts ejecutables en Python para el procesamiento de datos.
* `/resultados`: Gráficos de evolución temporal y tablas de indicadores.

---

### 🚀 Instrucciones de Ejecución
Para replicar el análisis de ventas en Google Colab o de forma local:

1. **Clonar el repositorio de forma completa:**
   ```bash
   git clone [https://github.com/belu674/analisis-ventas-empresa.git](https://github.com/belu674/analisis-ventas-empresa.git)
2. **Navegar a la carpeta del proyecto:**
   %cd analisis-ventas-empresa
3. **Ejecutar el script de procesamiento:**
   !python scripts/analisis_datos.py

### 🛡️ Control de Calidad y Seguridad (QA)
* **Revisión por Pares:** Validada mediante Pull Request con hilos de discusión técnicos en GitHub.
* **Auditoría:** Se verificó que el archivo `.gitignore` excluya correctamente los datos pesados y archivos temporales del entorno.