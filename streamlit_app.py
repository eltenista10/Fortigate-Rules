import paramiko
import streamlit as st

def conectar_ssh(ip, usuario, contraseña):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=usuario, password=contraseña)
        st.success("Conexión establecida con éxito.")
        return ssh
    except paramiko.AuthenticationException:
        st.error("Error de autenticación. Usuario o contraseña incorrectos.")
    except Exception as e:
        st.error(f"Ocurrió un error: {e}")
    return None

def main():
    st.title("Conector SSH")
    ip = st.text_input("Ingrese la IP del servidor")
    usuario = st.text_input("Ingrese el usuario")
    contraseña = st.text_input("Ingrese la contraseña", type="password")

    if st.button("Conectar"):
        if not ip or not usuario or not contraseña:
            st.error("Por favor, complete todos los campos.")
        else:
            ssh = conectar_ssh(ip, usuario, contraseña)

if __name__ == "__main__":
    main()