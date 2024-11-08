# Taller_4
Desarrollo de una Aplicación Web Backend con Azure Board, GitHub, Github Actions y Azure Web app

Ejecutar servidor
uvicorn main:app --reload

Crear virtual environment python -m venv .venv

Activar virtual environment .venv\Scripts\Activate.ps1

Instalar paquetes pip install "fastapi[standard]" 

Crear archivo requirements.txt python -m pip freeze > requirements.txt

Crear main.py

Correr servidor fastapi dev app/main.py

En Azure el comando para iniciar la app en producción es: fastapi run app/main.py

Instalar Testclient pip install httpx

Instalar pytest pip install pytest
