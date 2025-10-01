import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="practica_db",
    user="postgres",
    password="12345"
)

# Crear cursor
cursor = conn.cursor()

# Consultar tabla usuarios
print("Tabla: Alumnos")
cursor.execute("SELECT * FROM alumnos;")
alumnos = cursor.fetchall()
for fila in alumnos:
    print(fila)

# Cerrar conexión
cursor.close()
conn.close()