import psycopg2

# Datos de los alumnos a insertar
alumnos = [
    ('Juan', 20),
    ('María', 22),
    ('Carlos', 21)
]

# Sentencia SQL para insertar un alumno
sql_insert = """
INSERT INTO alumnos (nombre, edad)
VALUES (%s, %s);
"""

def insertar_alumnos(conexion, alumnos):
    with conexion.cursor() as cursor:
        for alumno in alumnos:
            cursor.execute(sql_insert, alumno)
    conexion.commit()
    print("Alumnos insertados correctamente.")

def mostrar_alumnos(conexion):
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM alumnos;")
        registros = cursor.fetchall()
        print("\nRegistros actuales en la tabla alumnos:")
        for fila in registros:
            id, nombre, edad = fila  # Ajusta si hay más columnas
            print(f" {id} , {nombre} , {edad}")


if __name__ == "__main__":
    conexion = psycopg2.connect(
        host="localhost",
        port=5432,
        database="practica_db",
        user="postgres",
        password="12345"
    )
    insertar_alumnos(conexion, alumnos)
    mostrar_alumnos(conexion)
    conexion.close()