from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = """
Genera un script de prueba en Python con Selenium. 
Requisitos:
- Abrir el navegador y acceder al módulo de informes.
- Validar que existan los campos: fecha inicio, fecha fin, tipo de informe, usuario. 
- Validar que los botones buscar y exportar estén visibles y habilitados.
- Incluir un assert por cada campo/botón.
Responde solo con el código en Python, sin explicaciones.
"""

respuesta = client.responses.create(
    model="gpt-4o-mini",  # rápido y económico
    input=prompt,
)

print(respuesta.output_text)