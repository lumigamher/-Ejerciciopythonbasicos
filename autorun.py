import os
import subprocess

# Programa para iniciar  
programa = "/usr/bin/firefox"  

# Verifica si el sistema está iniciando
if os.getenv("DESKTOP_AUTOSTART_ID"):
  print("Sistema iniciando, ejecutando programa")
  
  # Inicia el programa   
  subprocess.call(programa)