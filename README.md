# Simple Api on FastAPI

## Usage
1. Install poetry: `pip install poetry`
2. Install dependencies: `poetry install`
3. To start: `uvicorn src.main:app --reload`
4. Automatic interactive documentation with Swagger UI (from the OpenAPI backend): `http://localhost:8888/docs`

## Backend local development, additional details

### Migrations
Run the alembic `migrate` command to apply schema to your newly created database (at `db:5432`)

```console
$ alembic revision --autogenerate -m "message"

```
```console
$ alembic upgrade head
```

### Poetry packages
To add more packages to poetry use `poetry add {package_name}`