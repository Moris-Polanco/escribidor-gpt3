import openai
import streamlit as st

# Inicializa la API de GPT-3
openai.api_key = ""

# Crea un título y una caja de texto para que el usuario pueda escribir lo que quiera que GPT-3 escriba
st.title("Escribidor de GPT-3")
text_input = st.text_input("Escribe lo que quieres que GPT-3 escriba:")

# Si el usuario ha escrito algo en la caja de texto, usa GPT-3 para completar el texto
if text_input:
    # Utiliza GPT-3 para completar el texto con el modelo "text-davinci-003"
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text_input,
        max_tokens=3900,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Obtiene la primera sugerencia de GPT-3 y la muestra al usuario
    suggestion = completions.choices[0].text
    st.write(f"Sugerencia de GPT-3: {suggestion}")
