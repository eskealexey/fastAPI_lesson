from app.backend.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Index
from sqlalchemy.orm import relationship

from app.models import *


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(Integer, unique=True, index=True)
    tasks = relationship("Task", back_populates="user")


#
# from sqlalchemy.schema import CreateTable
#
# print(CreateTable(User.__table__))
