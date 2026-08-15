# Autor: Ruan Lucas
# Projeto: IMC com steamlit

 # importando a biblioteca
import streamlit as st

st.title("Calculadora de IMC")
peso = st.number_input("Digite seu peso (kg):")
altura = st.number_input("Digite sua altura (m):")

st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #0000ff;
        color: white;
    }
    div.stButton > button:hover {
        background-color: #0000cc;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# ação do botão

if st.button("Calcular IMC"):
    imc = peso / (altura ** 2)
    st.write(f"Seu IMC é: {imc:.2f}")

    if peso <= 0 or altura <= 0:
        st.warning("Digite um valor válido", icon="⚠️")
    if imc <=18.5:
        st.error("abaixo do peso", icon="❌")
    elif imc <= 24.9:
        st.success("peso normal", icon="✅")
    elif imc <= 29.9:
        st.warning("sobrepeso", icon="⚠️")
    elif imc <= 34.9:
        st.warning("obesidade grau 1", icon="⚠️")
    elif imc <= 39.9:
        st.warning("obesidade grau 2", icon="⚠️")
    else:
        st.error("obesidade grau 3", icon="❌")
else:
    st.warning("Digite um valor válido", icon="⚠️")



