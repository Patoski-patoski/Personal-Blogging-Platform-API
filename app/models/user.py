#!/usr/bin/env python3
"""app/models/user module"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    """User: Model class
       Args:
            Base: Baseclass(declarative)
    """
    __tablename__= "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    email = Column(String(150), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"
    