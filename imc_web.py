# instalar o streamlit
# pip install streamlit

# importando a biblioteca
import streamlit as st
st.write("calculadora de IMC")
st.write("digite seu peso e sua altura.")
peso = st.number_input("Digite seu peso (kg):")
altura = st.number_input("Digite sua altura (m):")
if st.button("Calcular IMC"):
    imc = peso / (altura ** 2)
    st.write(f"Seu IMC é: {imc:.2f}")
    if imc < 18.5:
        st.write("Você está abaixo do peso.")
    elif 18.5 <= imc < 24.9:
        st.write("Você está com peso normal.")
    elif 25 <= imc < 29.9:
        st.write("Você está com sobrepeso.")
    else:
        st.write("Você está com obesidade.")