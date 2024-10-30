<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Residencias API</title>
</head>
<body>
    <h1>FastAPI Residencias API</h1>
    <p>Esta es una API RESTful construida con FastAPI y SQLAlchemy, diseñada para gestionar proyectos en una base de datos PostgreSQL. La API permite realizar operaciones CRUD en los proyectos.</p>

    <h2>Requisitos</h2>
    <ul>
        <li><a href="https://www.docker.com/get-started">Docker</a></li>
        <li><a href="https://docs.docker.com/compose/">Docker Compose</a></li>
    </ul>

    <h2>Estructura del Proyecto</h2>
    <pre>
/project-directory
│
├── docker-compose.yml      # Archivo para orquestar los contenedores
├── Dockerfile               # Dockerfile para construir la imagen de la API
├── requirements.txt         # Dependencias de la API
├── main.py                  # Punto de entrada de la aplicación
├── database.py              # Configuración de la base de datos
└── routes/
    └── project_route.py     # Rutas de la API para la gestión de proyectos
    </pre>

    <h2>Configuración</h2>
    <ol>
        <li><strong>Clonar el Repositorio:</strong>
            <pre>
git clone &lt;URL_DEL_REPOSITORIO&gt;
cd project-directory
            </pre>
        </li>
        <li><strong>Construir y Ejecutar los Contenedores:</strong>
            <p>Ejecuta el siguiente comando para construir la imagen y levantar los contenedores:</p>
            <pre>
docker-compose up --build
            </pre>
        </li>
        <li><strong>Acceder a la API:</strong>
            <p>Una vez que los contenedores estén en funcionamiento, la API estará disponible en <code>http://localhost:8000</code>.</p>
        </li>
    </ol>

    <h2>Endpoints</h2>
    <h3>1. <code>GET /projects</code></h3>
    <p>Obtiene una lista de todos los proyectos.</p>
    <p><strong>Respuesta:</strong></p>
    <ul>
        <li>Código de estado: <code>200 OK</code></li>
        <li>Contenido: lista de proyectos.</li>
    </ul>

    <h3>2. <code>POST /projects</code></h3>
    <p>Crea un nuevo proyecto.</p>
    <p><strong>Cuerpo de la Solicitud:</strong></p>
    <pre>
{
  "name": "Nombre del Proyecto",
  "description": "Descripción del proyecto"
}
    </pre>
    <p><strong>Respuesta:</strong></p>
    <ul>
        <li>Código de estado: <code>201 Created</code></li>
        <li>Contenido: proyecto creado.</li>
    </ul>

    <h3>3. <code>GET /projects/{id}</code></h3>
    <p>Obtiene un proyecto específico por ID.</p>
    <p><strong>Respuesta:</strong></p>
    <ul>
        <li>Código de estado: <code>200 OK</code></li>
        <li>Contenido: datos del proyecto.</li>
    </ul>

    <h3>4. <code>PUT /projects/{id}</code></h3>
    <p>Actualiza un proyecto existente.</p>
    <p><strong>Cuerpo de la Solicitud:</strong></p>
    <pre>
{
  "name": "Nuevo Nombre del Proyecto",
  "description": "Nueva descripción del proyecto"
}
    </pre>
    <p><strong>Respuesta:</strong></p>
    <ul>
        <li>Código de estado: <code>200 OK</code></li>
        <li>Contenido: proyecto actualizado.</li>
    </ul>

    <h3>5. <code>DELETE /projects/{id}</code></h3>
    <p>Elimina un proyecto específico por ID.</p>
    <p><strong>Respuesta:</strong></p>
    <ul>
        <li>Código de estado: <code>204 No Content</code></li>
    </ul>

    <h2>Ejemplos de Uso</h2>
    <p>Puedes utilizar herramientas como <a href="https://www.postman.com/">Postman</a> o <code>curl</code> para interactuar con la API. Aquí hay algunos ejemplos con <code>curl</code>:</p>

    <ol>
        <li>Obtener todos los proyectos:
            <pre>
curl -X GET http://localhost:8000/projects
            </pre>
        </li>
        <li>Crear un nuevo proyecto:
            <pre>
curl -X POST http://localhost:8000/projects -H "Content-Type: application/json" -d '{"name": "Nuevo Proyecto", "description": "Descripción del nuevo proyecto"}'
            </pre>
        </li>
        <li>Obtener un proyecto por ID:
            <pre>
curl -X GET http://localhost:8000/projects/1
            </pre>
        </li>
        <li>Actualizar un proyecto:
            <pre>
curl -X PUT http://localhost:8000/projects/1 -H "Content-Type: application/json" -d '{"name": "Proyecto Actualizado", "description": "Descripción actualizada"}'
            </pre>
        </li>
        <li>Eliminar un proyecto:
            <pre>
curl -X DELETE http://localhost:8000/projects/1
            </pre>
        </li>
    </ol>

    <h2>Contribuciones</h2>
    <p>Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue estos pasos:</p>
    <ol>
        <li>Realiza un fork del proyecto.</li>
        <li>Crea una nueva rama (<code>git checkout -b feature/nueva-funcionalidad</code>).</li>
        <li>Realiza tus cambios y haz commit (<code>git commit -m 'Añadir nueva funcionalidad'</code>).</li>
        <li>Haz push a la rama (<code>git push origin feature/nueva-funcionalidad</code>).</li>
        <li>Abre un Pull Request.</li>
    </ol>

    <h2>Licencia</h2>
    <p>Este proyecto está bajo la Licencia MIT. Consulta el archivo <code>LICENSE</code> para más información.</p>
</body>
</html>
