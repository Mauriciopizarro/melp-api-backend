from sqlalchemy import Column, ForeignKey, CheckConstraint
from sqlalchemy.sql.sqltypes import String, Integer, BOOLEAN, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Restaurants(Base):
    __tablename__ = 'restaurants'

    id = Column("id", String(255), primary_key=True)
    rating = Column("rating", Integer, CheckConstraint('rating >= 0 AND rating <= 4'))
    name = Column("name", String(255))
    site = Column("site", String(255))
    email = Column("email", String(255))
    phone = Column("phone", String(255))
    street = Column("street", String(255))
    city = Column("city", String(255))
    state = Column("state", String(255))
    latitude = Column("latitude", Float)
    longitude = Column("longitude", Float)
