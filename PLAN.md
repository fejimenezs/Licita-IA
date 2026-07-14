# Plan de Trabajo — LicitaIA (Morarci Group)

> Basado en `Licita-IA.md` / `PRD_LicitaIA_MorarciGroup.docx` — MVP 8 semanas
> Estado del repo: proyecto sin iniciar (solo PRD presente)

## Objetivo del MVP

Sistema web que automatiza el ciclo de licitaciones: detección (SECOP II + correo) → análisis IA (técnico/jurídico/económico) → scoring de viabilidad → generación automática de documentos (.docx/PDF).

## Stack confirmado

| Capa            | Tecnología                     |
| --------------- | ------------------------------- |
| Frontend        | React + Tailwind + React Router |
| Backend         | Python + FastAPI                |
| DB              | PostgreSQL + SQLAlchemy         |
| Vectorial (RAG) | ChromaDB + LangChain            |
| IA              | Claude API (Anthropic)          |
| PDF             | PyMuPDF + pdfplumber            |
| Word            | python-docx                     |
| Async/colas     | Celery + Redis                  |
| Email           | Gmail API / IMAP                |
| SECOP           | Socrata API (datos.gov.co)      |
| Auth            | JWT + bcrypt                    |
| Deploy          | Docker + Railway/Render         |

## Fase 0 — Setup inicial (antes de Sprint 1)

- [X] Crear repo GitHub privado, estructura monorepo (`/backend`, `/frontend`, `/docker`)
- [ ] `docker-compose.yml` base: Postgres + Redis + backend + frontend
- [ ] FastAPI esqueleto (`main.py`, routers, config con `.env`)
- [ ] React esqueleto (Vite + Tailwind + React Router)
- [ ] Conexión SQLAlchemy + Alembic (migraciones)
- [ ] Cuenta/API key de Claude configurada y probada
- [ ] `.gitignore`, README inicial con instrucciones de instalación

## Sprint 1 (Semana 1–2) — Base + Autenticación

- [ ] Modelos: `usuarios`, `empresas` (tablas del punto 4.2 del PRD)
- [ ] Endpoints auth: registro, login, JWT, refresh
- [ ] Roles: Administrador / Gerente / Analista (middleware de permisos)
- [ ] CRUD usuarios (solo Admin)
- [ ] Login en frontend + rutas protegidas por rol
- [ ] **Entregable:** login funcional con 3 roles y dashboards diferenciados (aunque vacíos)

## Sprint 2 (Semana 2–3) — Gestión de Procesos

- [ ] Modelo `procesos` y `documentos_pliego`
- [ ] Endpoint: crear proceso manualmente, subir PDF de pliego
- [ ] Extracción de texto con PyMuPDF/pdfplumber
- [ ] Listado de procesos (filtros básicos: estado, modalidad, entidad)
- [ ] **Entregable:** subir un pliego PDF, ver texto extraído, listar procesos

## Sprint 3 (Semana 3–4) — IA Core + Análisis

- [ ] Integración Claude API (cliente + manejo de costos/cacheo de respuestas)
- [ ] Prompt + parsing: análisis técnico (objeto, requisitos habilitantes, criterios)
- [ ] Prompt + parsing: análisis jurídico (capacidad jurídica, inhabilidades, garantías)
- [ ] Prompt + parsing: análisis económico (valor, capacidad financiera, RPC)
- [ ] Modelo `analisis_ia` (json por tipo)
- [ ] **Entregable:** subir pliego → análisis técnico/jurídico/económico en <60s (criterio de aceptación #2)

## Sprint 4 (Semana 4–5) — Biblioteca RAG

- [ ] ChromaDB local + colección `biblioteca_leyes`
- [ ] Ingesta manual: Ley 80, Ley 1150, Decreto 1082, circulares CCE
- [ ] Pipeline LangChain: chunking + embeddings + retrieval
- [ ] Generación de observaciones citando artículo/norma específica
- [ ] **Entregable:** observaciones al pliego con citas reales verificables (criterio #4)

## Sprint 5 (Semana 5) — Motor de Viabilidad

- [ ] Modelo de scoring configurable (pesos: experiencia 30, financiero 25, técnico 20, plazo 10, cuantía 10, inhabilidades 5)
- [ ] Cálculo automático de score 0–100 al terminar análisis IA
- [ ] Semáforo: 🟢 Viable (80–100) / 🟡 Condicional (50–79) / 🔴 No viable (0–49)
- [ ] Asignación automática de analista si es viable; notificación a Gerente si condicional
- [ ] Panel Admin para configurar pesos del scoring
- [ ] **Entregable:** score correcto + acción automática según semáforo (criterio #3)

## Sprint 6 (Semana 6) — Generador de Documentos

- [ ] Plantillas .docx membretadas (python-docx)
- [ ] Generación: Manifestación de Interés
- [ ] Generación: Observaciones al Pliego (con citas RAG)
- [ ] Generación: Propuesta Técnica (6 secciones)
- [ ] Generación: Propuesta Económica y Jurídica
- [ ] Versionado de documentos generados (`documentos_generados`)
- [ ] **Entregable:** generar propuesta técnica completa en .docx con un clic (criterio #5)

## Sprint 7 (Semana 7) — Email + SECOP

- [ ] Job Celery: consulta SECOP II (Socrata API) cada 6h, filtros configurables
- [ ] Import automático de procesos nuevos desde SECOP
- [ ] Integración Gmail/IMAP: monitoreo cada 15 min
- [ ] Detección de PDFs adjuntos + clasificación de correo (licitación/aclaración/adenda/resultado)
- [ ] **Entregable:** proceso nuevo detectado automáticamente desde SECOP o correo (criterios #6, #7)

## Sprint 8 (Semana 8) — Dashboard + Deploy

- [ ] Dashboard Gerente: mapa de procesos, KPIs, alertas de fechas críticas
- [ ] Asignación de procesos a analistas desde dashboard (criterio #8)
- [ ] Exportar CSV de estado de procesos (criterio #9)
- [ ] Panel Analista: lista propia, chat IA sobre el pliego, historial de versiones
- [ ] Dockerizar todo (`docker-compose up` funcional) (criterio #10)
- [ ] Deploy demo pública en Railway/Render
- [ ] README de instalación + video demo (5 min)

## Criterios de aceptación del MVP (checklist final)

- [ ] Login y operación por rol (Admin/Gerente/Analista)
- [ ] Análisis técnico/jurídico/económico en <60s tras subir PDF
- [ ] Score de viabilidad correcto según parámetros configurados
- [ ] Observaciones con citas reales de Ley 80/Decreto 1082 (sin alucinaciones)
- [ ] Generación de propuesta técnica en .docx con un clic
- [ ] Monitoreo de correo detecta pliegos adjuntos automáticamente
- [ ] Consulta a SECOP II con últimos 20 procesos filtrados
- [ ] Gerente asigna proceso a analista desde dashboard
- [ ] Exportación CSV del estado de procesos
- [ ] Sistema corre en Docker local y es desplegable

## Riesgos / restricciones a tener presentes

- Costo de Claude API — cachear respuestas de análisis, no reprocesar el mismo pliego
- Sin firma digital ni integración directa de presentación en SECOP (fuera de alcance MVP)
- Biblioteca de leyes se carga manualmente (no hay scraping automático en MVP)
- Documentos generados requieren revisión humana antes de presentar

## Próximo paso inmediato

Empezar por **Fase 0 (setup)** + **Sprint 1 (auth)**: esto desbloquea todo lo demás y es donde Fausto debe reforzar FastAPI/SQLAlchemy primero (prioridad 🔴 HOY según el PRD).
