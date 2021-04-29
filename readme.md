Se instalo venv 
python -m venv venv   

Se activo venv en powershell
venv\Scripts\Activate.ps1

Se instalo werkzeug en su version 1.0.1
pip install werkzeug

Se instalo mysql
pip install mysql-connector-python 

Se instalo Flask
pip install Flask


$env:FLASK_APP = "todo"
flask run