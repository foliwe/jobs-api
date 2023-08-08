from enum import Enum
from sqlalchemy import Boolean, Column, Integer, String, Float, Text

from . database import Base




class JobType(str, Enum):
    PERMANENT = 'Permanent'
    CONTRACT = 'Contract'
    TEMPORARY = 'Temporary'
    PART_TIME = 'Part-Time'


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(300), unique=True, nullable=False, index=True)
    description = Column(Text)
    salary = Column(Float)
    job_type = JobType

    

# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(255), unique=True, nullable=False, index=True)
#     description = Column(Text)
#     price = Column(Float)
#     on_offer = Column(Boolean, default=False)
    
#     def __repr__(self):
#         return f" {self.name}"


#     def __repr__(self):
#         return f" {self.title}"
    

