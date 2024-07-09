from flask import Flask, render_template
import os
import psycopg2
from psycopg2 import OperationalError

# Initialize Flask application
app = Flask(__name__)

# Database connection parameters
db_params = {
    'user': os.getenv('DB_USER', 'myuser'),
    'password': os.getenv('DB_PASSWORD', 'pwadmin'),
    'host': os.getenv('DB_HOST', '192.168.49.2'),   # or the IP of your PostgreSQL server
    'port': os.getenv('DB_PORT', '30550'),        # PostgreSQL default port
    'database': os.getenv('DB_NAME', 'mydatabase')
}

@app.route('/')
def index():
    try:
        # Attempt to connect to PostgreSQL
        conn = psycopg2.connect(**db_params)

        # If connection successful, render success template
        return render_template('index.html', message="Successfully connected to PostgreSQL!")

    except OperationalError as e:
        # If connection fails, render error template with error message
        return render_template('index.html', message=f"Error: {e}")

    finally:
        if 'conn' in locals() and conn is not None:
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
