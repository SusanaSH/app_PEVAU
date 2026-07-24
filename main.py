from fastapi import FastAPI, UploadFile, File, Response
from google import genai
from dotenv import load_dotenv
from database import engine
import pypdf
import os
import models

models.Base.metadata.create_all(bind=engine)

load_dotenv() #Para leer el archivo secreto .env

api_key = os.getenv("GEMINI_API_KEY") # Guarda la clave en la variable api_key

if not api_key:
    raise ValueError("No se ha encontrado la clave.")


app = FastAPI(
    title="Backend PEvAU Andalucía v2",
    description="API ultrarrápida con Google Gemini para resúmenes de selectividad.")

client = genai.Client(api_key=api_key)

@app.get("/")
def inicio():
    return {"mensaje": "Servidor listo y conectado a la nube de Google."}

@app.post("/generar-resumen")
def generar_resumen(archivo: UploadFile = File(...)):
    try:
        # El lector de PDF es idéntico a antes
        lector_pdf = pypdf.PdfReader(archivo.file)
        texto_extraido = ""
        for pagina in lector_pdf.pages:
            texto_pagina = pagina.extract_text()
            if texto_pagina:
                texto_extraido += texto_pagina + "\n"
        
        if not texto_extraido.strip():
            return {"status": "error", "detalle": "El PDF no contiene texto legible."}
        
        prompt_andalucia = f"""
        Eres un profesor de bachillerato experto en la PEvAU (Andalucía).
        Analiza el siguiente texto de apuntes y genera un resumen claro, estructurado por apartados
        y enfocado en los conceptos clave que suelen preguntar en los exámenes de la Junta de Andalucía.
        
        Texto de los apuntes:
        {texto_extraido}
        """
        
        # Llamamos al modelo 'gemini-2.5-flash', que es el más rápido de Google
        respuesta = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_andalucia,
        )
        
        # Guardamos el resultado (en Gemini se saca simplemente con .text)
        resumen_final = respuesta.text
        return {"status": "éxito", "resumen": resumen_final}
        
    except Exception as e:
        return {"status": "error", "detalle": str(e)}
    

@app.post("/descargar-resumen")
def descargar_resumen(archivo: UploadFile = File(...)):
    """
    Hace lo mismo que la anterior, pero en vez de mostrar el texto en pantalla,
    fuerza al ordenador o móvil del alumno a descargar un archivo 'resumen_pevau.txt'.
    """
    try:
        # Extraemos el texto del PDF igual que antes
        lector_pdf = pypdf.PdfReader(archivo.file)
        texto_extraido = ""
        for pagina in lector_pdf.pages:
            texto_pagina = pagina.extract_text()
            if texto_pagina:
                texto_extraido += texto_pagina + "\n"
        
        # Pedimos el resumen a Gemini
        prompt_andalucia = f"Resume de forma excelente para selectividad de Andalucía:\n{texto_extraido}"
        respuesta = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_andalucia,
        )
        resumen_final = respuesta.text
        
        # Creamos una respuesta especial enviando el texto puro ('content=resumen_final')
        # e indicamos en las "cabeceras" (headers) que es un archivo adjunto que debe descargarse.
        return Response(
            content=resumen_final,
            media_type="text/plain", # Indica que es un archivo de texto normal
            headers={
                "Content-Disposition": "attachment; filename=resumen_pevau.txt" # Define el nombre del archivo descargado
            }
        )
        
    except Exception as e:
        return Response(content=f"Error al generar la descarga: {str(e)}", media_type="text/plain")