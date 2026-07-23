# 🎓 Esto es una aplicación de estudio con IA para alumnos de Bachillerato que se estan preparando la EBAU/PEvAU. En ella los alumnos podrán subir sus temarios y la aplicación utilizará la Inteligencia Artificial para crear resúmenes, esquemas, tendrán exámenes personalizados para practicar...


## 🚀Características: 

- **Gestor de Apuntes:** Sube tus temarios en formato PDF o texto.
- **Resúmenes Automáticos:** Extrae las ideas clave y crea esquemas al instante para facilitar el estudio.
- **Generador de Exámenes:** Crea exámenes tipo test basados *estrictamente* en el temario subido para practicar antes de la prueba real.
- **Privacidad y Seguridad:** Configurado con variables de entorno para proteger las credenciales de la IA.


## 🔨 Herramientas utilizadas:

- **Lenguaje:** Python 🐍
- **Backend / API:** FastAPI.
- **Inteligencia Artificial:** (Modelo `gemini-2.5-flash`) API de Google Gemini.
- **Procesamiento de Archivos:** Librería `pypdf` para la lectura y extracción de texto.


## ⚙️ Instalación y uso:

Si quieres ejecutar este proyecto en tu ordenador, sigue estos pasos:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/SusanaSH/app_PEVAU.git
   

2. **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows:
        venv\Scripts\activate
    # En Mac/Linux:
        source venv/bin/activate


3. **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt


4. **Configura las variables de entorno:**
    ```bash
    # Crea un archivo llamado .env en la raíz del proyecto (este archivo ya está ignorado en Git por seguridad) y añade tu API_key:

    API_SECRET_KEY=tu_clave_aqui


5. **Arranca la aplicacióon:**
    ```bash
    uvicorn main:app --reload


## 🧠 Próximas Mejoras:
[ ] Implementar sistema de usuarios y contraseñas.

[ ] Añadir exámenes modelos de años anteriores.

[ ] Guardar el historial de exámenes del alumno en una base de datos SQLite.



Desarrollado con ❤️ y 🧠 por [SusanaSH]

