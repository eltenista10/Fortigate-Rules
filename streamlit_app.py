import streamlit as st
import paramiko as paramiko


def conectar_ssh(ip, usuario, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=usuario, password=password)
        st.success("Conexión SSH establecida con éxito.")
        return ssh
    except paramiko.AuthenticationException:
        st.error("Error de autenticación. Usuario o contraseña incorrectos.")
    except Exception as e:
        st.error(f"Error al conectar: {e}")
    return None


st.title("Conexión SSH con Paramiko y Streamlit")

ip = st.text_input("Ingrese la IP del servidor")
usuario = st.text_input("Ingrese el usuario")
password = st.text_input("Ingrese la contraseña", type="password")

st.button("Conectar"):
if not ip or not usuario or not password:
    st.warning("Por favor, complete todos los campos.")
else:
    ssh = conectar_ssh(ip, usuario, password)
    st.success("Conexión SSH OK")