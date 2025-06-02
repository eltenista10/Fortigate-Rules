import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
cantidad = st.slider("Selecciona la cantidad")

st.write(f'la cantidad seleccionada es: {cantidad}')

for i in range(cantidad):
    st.button(f'{i}')