import os

# REMEDIACIÓN 1: Variables de entorno
DB_PASSWORD = os.getenv("DB_PASSWORD", "Valor_Por_Defecto_Seguro")

def ejecutar_mensaje_seguro(mensaje):
    # REMEDIACIÓN 2: Evitar ejecuciones inseguras
    print(f"[LOG SEGURIDAD]: Mensaje procesado de forma segura -> {mensaje}")

if __name__ == "__main__":
    print("--- [MODO REMEDIADO / DEVSECOPS] ---")
    ejecutar_mensaje_seguro("Iniciando_Sistema")
