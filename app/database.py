from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./uptime_logs.db"

# Connect to SQLite (no separate DB server needed)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for table models
Base = declarative_base()

# Define your table
class UptimeLog(Base):
    __tablename__ = "uptime_logs"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    status = Column(String)
    checked_at = Column(DateTime, default=datetime.datetime.utcnow)

# Actually create the table if it doesn't exist
Base.metadata.create_all(bind=engine)
