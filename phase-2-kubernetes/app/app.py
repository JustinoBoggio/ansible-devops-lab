from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Kubernetes nos pasará estas variables de entorno
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_name = os.environ.get('DB_NAME', 'myappdb')
    db_user = os.environ.get('DB_USER', 'postgres')
    db_pass = os.environ.get('DB_PASS', 'password')

    try:
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_pass
        )
        return f"<h1 style='color:green'>KUBERNETES SUCCESS! Connected to {db_name} at {db_host}</h1>"
    except Exception as e:
        return f"<h1 style='color:red'>K8s FAILED: {str(e)}</h1>"

if __name__ == '__main__':
    # Importante: host='0.0.0.0' para que sea accesible desde fuera del contenedor
    app.run(host='0.0.0.0', port=5000)