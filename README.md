# NOC Syslog Inteligente - Versión Alfa

Aplicación web modular para administración y gestión de redes (Cisco, Fortinet, Huawei) desarrollada en Python con FastAPI y SQLite.

## 🚀 Características
- **CRUD de Dispositivos:** Registro de inventario con IP única y validación de atributos.
- **Normalización Syslog:** Estructura basada en severidades RFC (0 a 7).
- **Dashboard Web:** Interfaz gráfica responsive desarrollada con Bootstrap 5 y Jinja2.
- **Generador Multivendor:** Generación de plantillas CLI comentadas en modo solo lectura.
- **Seguridad Integrada:** Ingesta tratada como datos no confiables, ausencia de secretos en código, sanitización de entrada de datos.

## 🛠️ Requisitos e Instalación
1. Clonar el repositorio.
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt