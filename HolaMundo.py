import openai
import os

def main():
	print("--- Consulta de clima usando ChatGPT ---")
	api_key = input("Ingresa tu API key de OpenAI: ")
	openai.api_key = api_key
	ciudad = input("¿Sobre qué ciudad quieres consultar el clima?: ")
	prompt = f"¿Cuál es el clima actual en {ciudad}? Responde como si fueras un asistente meteorológico."
	try:
		response = openai.ChatCompletion.create(
			model="gpt-3.5-turbo",
			messages=[{"role": "user", "content": prompt}]
		)
		print("Respuesta de ChatGPT:")
		print(response.choices[0].message["content"])
	except Exception as e:
		print("Error al consultar ChatGPT:", e)

if __name__ == "__main__":
	main()
