# Copilot Instructions for AI Coding Agents

## Visión General
Este proyecto es una práctica para la creación y manipulación de una base de datos PostgreSQL usando Docker. El flujo principal es levantar un contenedor de base de datos, poblarlo con scripts SQL y acceder a los datos desde scripts Python.

## Estructura del Proyecto
- `docker-compose.yml`: Orquesta el servicio de PostgreSQL en Docker.
- `db/`: Contiene scripts SQL para crear tablas e insertar datos (`creaclientes.sql`, `createAlumnos.sql`, etc.).
- `python/`: Scripts Python para interactuar con la base de datos y ejecutar consultas SQL.

## Flujos y Comandos Clave
- **Levantar la base de datos:**
  ```bash
  docker-compose up -d
  ```
- **Ejecutar scripts SQL manualmente:**
  Usar `psql` dentro del contenedor para cargar scripts desde `db/`.
- **Acceso desde Python:**
  Los scripts en `python/` suelen ejecutar consultas SQL almacenadas en archivos `.sql`.

## Convenciones y Patrones
- Los archivos `.sql` en `python/` contienen consultas que los scripts Python ejecutan dinámicamente.
- Los nombres de los archivos SQL reflejan su propósito (`SELECT.sql`, `SELECTid.sql`, etc.).
- No hay un framework web ni backend adicional; la comunicación es directa entre Python y PostgreSQL.

## Integraciones y Dependencias
- **Docker**: Esencial para el entorno de base de datos.
- **PostgreSQL**: Motor de base de datos.
- **Python**: Usado para automatizar consultas y procesamiento de datos.

## Ejemplo de flujo de trabajo
1. Levanta la base de datos con Docker Compose.
2. Inserta datos usando los scripts de `db/`.
3. Ejecuta scripts Python para consultar o manipular datos usando los archivos SQL de `python/`.

## Archivos Clave
- `docker-compose.yml`
- `db/creaclientes.sql`, `db/createAlumnos.sql`, etc.
- `python/main.py`, `python/SELECT.sql`, etc.

## Notas
- No hay tests automatizados ni pipelines CI/CD definidos.
- La estructura es simple y orientada a la práctica educativa.

---

Por favor, mantén estas convenciones y flujos al extender o modificar el proyecto. Si agregas nuevas integraciones o flujos, documenta los cambios aquí.