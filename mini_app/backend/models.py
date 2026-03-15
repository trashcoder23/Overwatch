from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )


class IncidentLog(Base):

    __tablename__ = "incident_logs"

    id = Column(Integer, primary_key=True, index=True)

    incident_id = Column(String(255), nullable=False)

    classification = Column(String(255))

    strategy = Column(String(255))

    status = Column(String(50))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )