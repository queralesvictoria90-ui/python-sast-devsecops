import os

# VULNERABILIDAD 1: Credencial expuesta en texto plano
DB_PASSWORD = "PasswordSecreto123!"

def ejecutar_comando_sistema(parametro_usuario):
    # VULNERABILIDAD 2: Inyección de comandos
    print("Ejecutando comando inseguro...")
    os.system(f"echo {parametro_usuario}")

if __name__ == "__main__":
    print("--- [MODO VULNERABLE] ---")
    ejecutar_comando_sistema("Iniciando_Sistema")
