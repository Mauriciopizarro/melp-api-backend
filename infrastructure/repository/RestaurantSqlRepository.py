import uuid
from sqlalchemy import Column, ForeignKey, CheckConstraint, create_engine, select
from sqlalchemy.sql.sqltypes import String, Integer, BOOLEAN, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session
from domain.interface.restaurant_repository import RestaurantRepository
from domain.models.Restaurant import Restaurant

Base = declarative_base()


class RestaurantRepo(RestaurantRepository):
    instance = None

    def __init__(self):
        self.engine = self.get_database()

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()

        return cls.instance

    @staticmethod
    def get_database():
        engine = create_engine('mysql+pymysql://user:password@mysql/restaurants')
        Base.metadata.create_all(engine)
        return engine

    def get(self, restaurant_id):
        session = Session(self.engine)
        restaurant_db = session.query(RestaurantDb).filter_by(id=restaurant_id).first()
        return Restaurant(**restaurant_db.__dict__)

    def save(self, restaurant: Restaurant) -> str:
        session = Session(self.engine)
        restaurant_db = RestaurantDb(**restaurant.dict())
        session.add(restaurant_db)
        session.commit()
        session.refresh(restaurant_db)
        session.close()
        return restaurant_db.id

    def update(self, restaurant: Restaurant, restaurant_id):
        session = Session(self.engine)
        restaurant_db = session.query(RestaurantDb).filter_by(id=restaurant_id).first()
        restaurant_db.rating = restaurant.rating
        restaurant_db.name = restaurant.name
        restaurant_db.site = restaurant.site
        restaurant_db.email = restaurant.email
        restaurant_db.phone = restaurant.phone
        restaurant_db.street = restaurant.street
        restaurant_db.city = restaurant.city
        restaurant_db.state = restaurant.state
        restaurant_db.latitude = restaurant.latitude
        restaurant_db.longitude = restaurant.longitude
        session.commit()
        session.close()
        return restaurant

    def delete(self, restaurant_id: str):
        session = Session(self.engine)
        restaurant_db = session.query(RestaurantDb).filter_by(id=restaurant_id).first()
        if restaurant_db:
            session.delete(restaurant_db)
            session.commit()
        session.close()

class RestaurantDb(Base):
    __tablename__ = 'restaurant'

    id = Column("id", String(36), primary_key=True, default=uuid.uuid4)
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
