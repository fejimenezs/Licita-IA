import uuid

from sqlalchemy import JSON, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Empresa(Base):
    __tablename__ = "empresas"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre: Mapped[str] = mapped_column(String(255), nullable=False)
    nit: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    membrete_logo: Mapped[str | None] = mapped_column(String(500), nullable=True)
    experiencias: Mapped[list] = mapped_column(JSON, default=list)
    capacidad_financiera: Mapped[dict] = mapped_column(JSON, default=dict)
