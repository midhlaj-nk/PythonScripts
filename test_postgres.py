import psycopg2
from psycopg2 import OperationalError

def check_postgres_connection(host, port, dbname, user, password):
    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        connection.close()
        print("Connection successful")
    except OperationalError as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    host = "ec2-13-232-76-225.ap-south-1.compute.amazonaws.com"
    port = 5432
    dbname = "cyllo-cloud-paas"
    user = "odoo17"
    password = "odoo17"

    check_postgres_connection(host, port, dbname, user, password)
