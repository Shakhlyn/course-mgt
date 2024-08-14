import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from ..db_setup import Base
from .mixins import Timestamp

class Role(enum.IntEnum):
    teacher = 1
    student = 2

class User(Timestamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True, index=True)
    email= Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))
    is_active = Column(Boolean, default=False)

    profile = relationship("Profile", back_populates='owner', uselist=False)    # here, 'profile' is the class name; 'owner' is the relation type  
    # here, the useList express the type of relationship: 1-to-1, 1-to-many
    #By default it is 1-to-many. But if it is false, it denotes 1-to-1

class Profile(Timestamp, Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key= True, index=True)
    first_name= Column(String(50), nullable=False)
    last_name= Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates='profile')



