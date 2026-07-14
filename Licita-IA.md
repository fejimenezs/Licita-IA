
MORARCI GROUP
DOCUMENTO DE REQUERIMIENTOS DE PRODUCTO
Sistema LicitaIA — Máquina de Licitaciones con Inteligencia Artificial

Versión	1.0 — MVP

Fecha	Julio 2026

Elaborado por	Gerencia de Producto — Morarci Group

Destinatario	Fausto Enrique Jiménez Suárez — Desarrollador Full Stack

Estado	APROBADO PARA DESARROLLO

CONFIDENCIAL — USO INTERNO
 

1. RESUMEN EJECUTIVO
   Morarci Group es una compañía especializada en procesos de contratación pública y privada en Colombia, que actualmente gestiona licitaciones de manera manual: descargando pliegos, leyendo condiciones, elaborando propuestas y haciendo seguimiento mediante correos y hojas de cálculo.

El objetivo de este proyecto es construir LicitaIA, un sistema web inteligente que automatice el ciclo completo de gestión de licitaciones: desde la detección automática de procesos en SECOP II y por correo electrónico, hasta la generación automática de propuestas técnicas, económicas y jurídicas membretadas, pasando por el análisis de viabilidad y la asignación de procesos a analistas.

LicitaIA debe convertirse en la ventaja competitiva de Morarci Group, permitiéndole participar en más procesos, con mayor calidad y en menos tiempo, reduciendo el trabajo manual en más del 70%.

2. CONTEXTO DEL NEGOCIO Y PROBLEMA A RESOLVER
   2.1 Tipos de procesos de contratación en Colombia
   El sistema debe conocer y operar sobre los siguientes tipos de proceso, conforme a la Ley 80 de 1993, Ley 1150 de 2007 y sus decretos reglamentarios:

Modalidad	Cuantía aprox.	Características clave
Licitación Pública	Mayor cuantía	Proceso más completo. Pliego, observaciones, audiencias, evaluación.
Selección Abreviada	Menor cuantía	Proceso simplificado. Subasta inversa o menor cuantía.
Mínima Cuantía	< 28 SMMLV aprox.	Proceso más rápido. Cotización directa. Sin pliegos extensos.
Subasta Inversa	Variable	Competencia por precio. El menor precio gana. Tiempo crítico.
Concurso de Méritos	Variable	Se evalúa principalmente la calidad técnica, no el precio.
Contratación Directa	Casos especiales	Sin competencia. Causales taxativas definidas en la ley.

2.2 Problema actual (pain points)
▪	Un analista gasta 4–8 horas leyendo y analizando un pliego manualmente
▪	El equipo pierde procesos viables por no detectarlos a tiempo en SECOP
▪	Las propuestas se elaboran desde cero cada vez, sin reutilizar experiencias anteriores
▪	No existe un sistema de viabilidad — la decisión de participar depende del criterio personal
▪	El seguimiento de procesos se hace por correo y WhatsApp, sin trazabilidad
▪	Los formatos (manifestación de interés, propuesta, observaciones) se hacen manualmente en Word
▪	La gerencia no tiene visibilidad en tiempo real del estado de todos los procesos

2.3 Solución: LicitaIA
Un sistema web con IA que automatiza el ciclo completo en 4 etapas:

▪	DETECCIÓN: monitoreo automático de SECOP II + correo electrónico para capturar nuevos procesos
▪	ANÁLISIS: procesamiento inteligente del pliego con IA (análisis técnico, jurídico, económico)
▪	VIABILIDAD: scoring automático basado en la experiencia de la empresa y los requisitos
▪	GENERACIÓN: creación automática de todos los documentos requeridos, membretados y listos
 
3. REQUERIMIENTOS FUNCIONALES
3.1 Módulo 1 — Autenticación y Roles
El sistema debe soportar tres roles con permisos diferenciados:

Rol	Permisos	Dashboard
Administrador	Acceso total. Configura empresa, usuarios, biblioteca de leyes.	Panel de configuración + todo lo del Gerente
Gerente	Ver todos los procesos. Asignar analistas. Aprobar viabilidad. Ver reportes.	Dashboard KPIs, mapa de procesos, asignaciones pendientes
Analista	Ver solo procesos asignados. Cargar documentos. Generar propuestas.	Lista de procesos propios, alertas de fechas, generador de docs

3.2 Módulo 2 — Detección Automática de Procesos
3.2.1 Integración con SECOP II
▪	Conectar con la API pública de SECOP II (datos.gov.co/resource/jbjy-vk9h.json)
▪	Consultar automáticamente cada 6 horas nuevos procesos publicados
▪	Filtrar por: palabras clave configurables, departamento, rango de cuantía, tipo de proceso
▪	Importar automáticamente: nombre del proceso, entidad, objeto, valor, fechas clave, documentos

3.2.2 Integración con Correo Electrónico
▪	Conectar con cuenta Gmail o Outlook vía OAuth2 / IMAP
▪	Monitorear bandeja de entrada cada 15 minutos buscando correos con pliegos adjuntos
▪	Detectar automáticamente PDFs de pliegos por palabras clave en asunto y remitente
▪	Extraer y procesar los PDFs adjuntos automáticamente
▪	Clasificar el correo: licitación, aclaración, adenda, resultado, otro

3.3 Módulo 3 — Análisis Inteligente de Pliegos
Este es el corazón del sistema. Cuando llega un nuevo proceso (por SECOP o correo), la IA debe procesar el pliego y extraer:

3.3.1 Análisis Técnico
▪	Objeto exacto del contrato
▪	Requisitos técnicos habilitantes (experiencia, personal, equipos)
▪	Especificaciones técnicas del bien o servicio requerido
▪	Criterios de evaluación técnica y puntajes

3.3.2 Análisis Jurídico
▪	Capacidad jurídica requerida (RUT, cámara de comercio, certificados)
▪	Inhabilidades e incompatibilidades aplicables
▪	Garantías exigidas (seriedad de la oferta, cumplimiento, calidad)
▪	Marco legal aplicable (Ley 80, Ley 1150, decretos reglamentarios)
▪	Validar contra biblioteca interna de leyes y circulares — sin alucinaciones

3.3.3 Análisis Económico
▪	Valor estimado del contrato y forma de pago
▪	Capacidad financiera requerida (índices: liquidez, endeudamiento, rentabilidad)
▪	Presupuesto oficial y RPC (Riesgo Previsible del Contrato)
▪	Análisis de precio vs. mercado si hay tabla de precios disponible

3.4 Módulo 4 — Motor de Viabilidad
El sistema debe dar un SCORE de viabilidad automático (0–100) con semáforo:

Score	Estado	Acción recomendada por el sistema
80 – 100	🟢 VIABLE	Asignar analista automáticamente. Iniciar generación de documentos.
50 – 79	🟡 CONDICIONAL	Notificar al Gerente para revisión. Lista de requisitos faltantes.
0 – 49	🔴 NO VIABLE	Archivar proceso. Exportar motivos a CSV. No asignar analista.

Variables del scoring (configurable por el Administrador):
▪	¿La empresa tiene experiencia acreditable en el objeto? (+30 pts)
▪	¿Se cumplen los requisitos financieros? (+25 pts)
▪	¿Se cumplen los requisitos técnicos de personal y equipos? (+20 pts)
▪	¿El plazo de presentación es suficiente? (+10 pts)
▪	¿La cuantía está en el rango objetivo de la empresa? (+10 pts)
▪	¿No hay inhabilidades ni conflictos de interés? (+5 pts)
 
3.5 Módulo 5 — Generador de Documentos
El sistema debe generar automáticamente los siguientes documentos en formato Word (.docx) y PDF, con membrete de la empresa:

Documento	Cuándo se genera	Contenido principal
Manifestación de Interés	Al clasificar proceso como viable	Presentación empresa, interés en el proceso, firma
Observaciones al Pliego	Dentro del plazo de observaciones	Observaciones técnicas y jurídicas fundamentadas en ley
Propuesta Técnica	Al aprobar participación	6 secciones: presentación, metodología, equipo, experiencia, cronograma, valor agregado
Propuesta Económica	Al aprobar participación	Tabla de precios, APU si aplica, forma de pago
Propuesta Jurídica	Al aprobar participación	Carta de presentación, certificados, garantías
Resumen Ejecutivo del Proceso	En cualquier momento	Ficha resumen: datos clave, estado, acciones pendientes

3.6 Módulo 6 — Biblioteca de Conocimiento (RAG)
Para eliminar las alucinaciones de la IA y garantizar observaciones basadas en ley real, el sistema debe incluir una biblioteca de conocimiento indexada:

▪	Ley 80 de 1993 — Estatuto General de Contratación
▪	Ley 1150 de 2007 — Modificaciones a la Ley 80
▪	Decreto 1082 de 2015 — Reglamentación única del sector
▪	Circulares de Colombia Compra Eficiente
▪	Manual para determinar y verificar los requisitos habilitantes (CCE)
▪	Guías de pliegos tipo por sector
▪	Historial de pliegos y propuestas anteriores de Morarci Group

Tecnología: ChromaDB como base vectorial. LangChain para indexar y consultar. Cada observación generada debe citar el artículo o norma específica de la que proviene.

3.7 Módulo 7 — Dashboard y Gestión
Dashboard del Gerente:
▪	Mapa de procesos: todos los procesos activos con su estado actual
▪	KPIs: procesos analizados, viables, en preparación, presentados, ganados/perdidos
▪	Alertas de fechas críticas (cierre de observaciones, presentación de propuestas)
▪	Asignación de procesos a analistas con un clic
▪	Exportar reporte CSV con estado de todos los procesos

Panel del Analista:
▪	Lista de procesos asignados con prioridad y fecha límite
▪	Acceso a todos los documentos del proceso
▪	Botones de generación de documentos (un clic por documento)
▪	Historial de cambios y versiones de cada documento
▪	Chat con IA para consultar dudas sobre el pliego específico
 
4. ARQUITECTURA TÉCNICA
4.1 Stack Tecnológico Recomendado

Capa	Tecnología	Justificación
Frontend	React + Tailwind CSS + React Router	Componentes reutilizables. Fausto ya domina este stack.
Backend	Python + FastAPI	Rápido, moderno, perfecto para APIs y procesamiento de IA.
Base de datos	PostgreSQL + SQLAlchemy	Robusta, relacional, ideal para proyectos, usuarios y documentos.
Base vectorial	ChromaDB	Para indexar leyes y pliegos. Consultas semánticas sin alucinaciones.
IA	Claude API (Anthropic)	Análisis de pliegos, generación de propuestas, observaciones.
RAG Framework	LangChain	Conecta Claude con ChromaDB para respuestas basadas en ley.
Procesamiento PDF	PyMuPDF + pdfplumber	Extracción de texto de pliegos en PDF con alta fidelidad.
Generación Word	python-docx	Generar propuestas membretadas en .docx automáticamente.
Tareas async	Celery + Redis	Procesar PDFs y monitorear SECOP en segundo plano.
Email	Gmail API / IMAP + imaplib	Leer correos y adjuntos automáticamente.
SECOP	Socrata API (datos.gov.co)	API pública y gratuita con todos los procesos de contratación.
Despliegue	Docker + Railway / Render	Corre local primero. Desplegable en la nube en una hora.
Autenticación	JWT + bcrypt	Roles y sesiones seguras.

4.2 Estructura de Base de Datos (Tablas principales)
▪	usuarios (id, nombre, email, rol, activo, created_at)
▪	empresas (id, nombre, nit, membrete_logo, experiencias[], capacidad_financiera)
▪	procesos (id, nombre, entidad, modalidad, objeto, valor, fecha_cierre, estado, score_viabilidad, analista_id, fuente)
▪	documentos_pliego (id, proceso_id, tipo, texto_extraido, url_original)
▪	analisis_ia (id, proceso_id, tecnico_json, juridico_json, economico_json, observaciones[], oportunidades[])
▪	documentos_generados (id, proceso_id, tipo_doc, contenido, version, generado_at, aprobado)
▪	biblioteca_leyes (id, nombre, tipo, texto, chunk_id_chroma)
▪	correos (id, proceso_id, asunto, remitente, fecha, clasificacion, adjuntos[])
▪	historial_acciones (id, usuario_id, proceso_id, accion, detalle, timestamp)
 
5. PLAN DE DESARROLLO — MVP 8 SEMANAS

Sprint	Módulo	Entregables	Semana
1	Base + Auth	Proyecto configurado, DB, login, roles, CRUD usuarios	1 – 2
2	Gestión de Procesos	Crear proyecto, cargar PDFs, extraer texto, listar procesos	2 – 3
3	IA Core + Análisis	Integración Claude API, análisis técnico/jurídico/económico	3 – 4
4	Biblioteca RAG	ChromaDB + LangChain, carga de leyes, observaciones con citas	4 – 5
5	Motor Viabilidad	Score automático, semáforo, asignación de analistas	5
6	Generador Docs	Propuesta técnica, manifestación interés, observaciones en .docx	6
7	Email + SECOP	Monitoreo correo, integración SECOP II API, clasificación auto	7
8	Dashboard + Deploy	Dashboard gerente, KPIs, exportar CSV, Docker, despliegue web	8

6. TECNOLOGÍAS QUE DEBES ESTUDIAR
   En orden de prioridad para poder iniciar el desarrollo:

Prioridad	Tecnología	Para qué	Recurso
🔴 HOY	FastAPI (Python)	Crear los endpoints del backend	fastapi.tiangolo.com
🔴 HOY	PostgreSQL + SQLAlchemy	Base de datos de proyectos y usuarios	sqlalchemy.org/docs
🟡 SEMANA 2	PyMuPDF / pdfplumber	Extraer texto de pliegos PDF	pymupdf.readthedocs.io
🟡 SEMANA 2	Claude API + Prompts	Analizar pliegos, generar propuestas	docs.anthropic.com
🟡 SEMANA 3	LangChain + ChromaDB	Biblioteca de leyes sin alucinaciones	python.langchain.com
🟡 SEMANA 4	Celery + Redis	Tareas automáticas (monitoreo SECOP, email)	docs.celeryq.dev
🟢 SEMANA 5	Gmail API (Python)	Leer correos con pliegos adjuntos	developers.google.com/gmail
🟢 SEMANA 5	Socrata API (SECOP)	Consultar procesos de contratación	data.socrata.com/developers
🟢 SEMANA 6	python-docx	Generar propuestas en Word membretadas	python-docx.readthedocs.io
🟢 SEMANA 7	Docker	Empaquetar y desplegar todo el sistema	docs.docker.com
 
7. CRITERIOS DE ACEPTACIÓN DEL MVP
El MVP se considera completo y entregable cuando:

1. Un usuario puede registrarse, iniciar sesión y operar según su rol (Admin / Gerente / Analista)
2. El sistema recibe un PDF de pliego y en menos de 60 segundos muestra el análisis técnico, jurídico y económico
3. El motor de viabilidad asigna un score correcto basado en los parámetros configurados
4. La IA genera observaciones al pliego citando artículos reales de la Ley 80 o Decreto 1082 (sin alucinaciones)
5. Se puede generar una propuesta técnica completa en .docx con un clic
6. El sistema monitorea un correo electrónico y detecta nuevos pliegos adjuntos automáticamente
7. Se puede consultar SECOP II y ver los últimos 20 procesos publicados filtrados por objeto
8. El Gerente puede asignar un proceso a un analista desde el dashboard
9. Se puede exportar el estado de todos los procesos en formato CSV
10. El sistema corre en Docker local y es desplegable en Railway o Render
11. RESTRICCIONES Y CONSIDERACIONES
    ▪	El MVP no incluye firma digital de documentos (fase 2)
    ▪	El MVP no integra directamente con el portal de presentación de propuestas de SECOP (requiere registro manual externo)
    ▪	La biblioteca de leyes debe ser cargada manualmente en la versión inicial
    ▪	El costo de la API de Claude debe monitorearse — se recomienda cachear respuestas de análisis para no reprocesar
    ▪	Los documentos generados requieren revisión humana antes de presentarse oficialmente
12. ENTREGABLES ESPERADOS
    Entregable	Fecha	Formato
    Repositorio GitHub con código fuente	Semana 8	GitHub privado compartido
    Sistema corriendo en local (Docker)	Semana 8	docker-compose up funcionando
    README con instrucciones de instalación	Semana 8	Markdown en repositorio
    Demo funcional desplegada en web	Semana 8	URL pública Railway/Render
    Video demo (5 min) con todos los módulos	Semana 8	MP4 o enlace YouTube privado

Gerencia de Producto — Morarci Group  •  Julio 2026  •  Documento aprobado para inicio de desarrollo
