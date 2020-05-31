from sqlalchemy import Boolean, Column, Enum, Integer, String, DateTime
from sqlalchemy.sql import func
from leader_bored.db.base_class import Base

class Contests(Base):
    id = Column(Integer, primary_key=True)
    contest_name = Column(String, nullable=False)
    starting_at = Column(DateTime, nullable = True)
    duration_seconds= Column(Integer, default= 0, nullable = False)
    contest_type = Column(Enum('CF', 'IOI', 'ICPC', name="contest_types"), server_default='CF', nullable=False)
    added_at = Column(DateTime, server_default=func.now(), nullable= True)
    reverted_at = Column(DateTime, default=None, nullable = True)
    is_added = Column(Boolean, default=True, nullable=False)
    updated_at = Column(DateTime,server_default=func.now(),onupdate=func.now())