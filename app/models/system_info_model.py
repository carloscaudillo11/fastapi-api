from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SystemInfo(Base):
    __tablename__ = "system_info"

    id = Column(Integer, primary_key=True, index=True)
    host = Column(String(100), index=True)
    cpu_usage = Column(Float)
    memory_usage = Column(Float)
    disk_usage = Column(String) 
    top_processes = Column(String)  
    failed_services = Column(String)  
    uptime = Column(String)
    network_info = Column(String) 
    connections = Column(String) 
    swap_usage = Column(String)
    error_logs = Column(String)
    timestamp = Column(DateTime, default=func.now())
