from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello():
    db_host = os.environ.get('DB_HOST')
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_name = os.environ.get('DB_NAME')

    try:
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_pass
        )
        return f"<h1 style='color:green'>SUCCESS! Connected to Database {db_name} at {db_host}</h1>"
    except Exception as e:
        return f"<h1 style='color:red'>FAILED: {str(e)}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)