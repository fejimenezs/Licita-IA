# LicitaIA

Sistema web con IA para automatizar la gestión de licitaciones de Morarci Group: detección de procesos (SECOP II + correo), análisis de pliegos, motor de viabilidad y generación automática de documentos.

Ver [`Licita-IA.md`](Licita-IA.md) (PRD completo) y [`PLAN.md`](PLAN.md) (plan de desarrollo por sprints).

## Estructura del repo

```
backend/    API FastAPI + SQLAlchemy + Alembic
frontend/   React + Vite + Tailwind + React Router
docker-compose.yml
```

## Requisitos

- Docker Desktop
- (Opcional para desarrollo local sin Docker) Python 3.12+, Node 20+

## Instalación y arranque (Docker — recomendado)

1. Copiar los archivos de entorno de ejemplo:
   ```
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env
   ```
2. Completar `backend/.env` con `SECRET_KEY` y `ANTHROPIC_API_KEY`.
3. Levantar todo el stack:
   ```
   docker compose up --build
   ```
4. Servicios disponibles:
   - Backend: http://localhost:8000/health
   - Frontend: http://localhost:5173
   - Postgres: localhost:5432
   - Redis: localhost:6379

## Migraciones de base de datos

Dentro del contenedor del backend (o localmente con el entorno virtual activo):

```
alembic revision --autogenerate -m "descripción"
alembic upgrade head
```

## Desarrollo local sin Docker (opcional)

**Backend:**
```
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Ajustar `DATABASE_URL` en `backend/.env` para apuntar a `localhost` en vez de `db`.

**Frontend:**
```
cd frontend
npm install
npm run dev
```

## Probar la API de Claude

Con `ANTHROPIC_API_KEY` configurada en `backend/.env`:
```
cd backend
python -m scripts.test_claude_api
```
