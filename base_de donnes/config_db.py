import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime


from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float,text
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="myGeocoder")

def get_coordinates(ville):
    location = geolocator.geocode(ville)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

url_base = 'postgresql://admin:rajarabii1@db:5432/immobilier_db'

engine = create_engine(url_base)

Session = sessionmaker(bind=engine)
session = Session()

with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print(result.fetchone())  

Base = declarative_base()


class Annonce(Base):
    __tablename__ = 'annonces'
    
    id = Column(Integer, primary_key=True)
    title = Column(String,nullable=True)
    price = Column(String,nullable=True)
    nb_rooms = Column(Integer,nullable=True)
    nb_baths = Column(Integer,nullable=True)
    surface_area = Column(Float,nullable=True)
    salon = Column(Float,nullable=True)
    link = Column(String,nullable=True)
    city_id = Column(Integer, ForeignKey('villes.id'))

    ville = relationship("Ville", back_populates="annonces")
    equipements = relationship("AnnonceEquipement", back_populates="annonce")


class Ville(Base):
    __tablename__ = 'villes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=True)
    latitude = Column(Float, nullable=True)  
    longitude = Column(Float, nullable=True)
    
    
    annonces = relationship("Annonce", back_populates="ville")


class Equipement(Base):
    __tablename__ = 'equipements'

    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=True)  

    annonces = relationship('AnnonceEquipement', back_populates='equipement')


class AnnonceEquipement(Base):
    __tablename__ = 'annonce_equipement'

    annonce_id = Column(Integer, ForeignKey('annonces.id'), primary_key=True)
    equipement_id = Column(Integer, ForeignKey('equipements.id'), primary_key=True)

    annonce = relationship('Annonce', back_populates='equipements')
    equipement = relationship('Equipement', back_populates='annonces')



Base.metadata.create_all(engine)



data = pd.read_csv('appartements_data_db.csv')





for i , ligne in data.iterrows():
    if pd.isna(ligne['city_name']):
        print(f"City name is missing for index {i}, skipping this entry.")
        continue  # Passer à l'itération suivante si city_name est NaN

   
    city = session.query(Ville).filter_by(name=ligne['city_name']).first()
    if not city:
        lat, lng = get_coordinates(ligne['city_name'])
        city = Ville(name=ligne['city_name'],latitude=lat,longitude=lng)
        session.add(city)
        session.commit()
    ligne['price'] = None if pd.isna(ligne['price']) else ligne['price']
    ligne['nb_rooms'] = None if pd.isna(ligne['nb_rooms']) else ligne['nb_rooms']
    ligne['nb_baths'] = None if pd.isna(ligne['nb_baths']) else ligne['nb_baths']
    ligne['salon'] = None if pd.isna(ligne['salon']) else ligne['salon']




    annonce = Annonce(
        title=ligne['title'],
        price=ligne['price'],
        nb_rooms=ligne['nb_rooms'],
        nb_baths=ligne['nb_baths'],
        surface_area=ligne['surface_area'],
        salon=ligne['salon'],
        link=ligne['link'],
        city_id=city.id
    )
    session.add(annonce)
    session.commit()
    ligne['equipment'] = str(ligne['equipment'])

    equipements = ligne['equipment'].split("/")

    for equipe_name in equipements:
        equip = session.query(Equipement).filter_by(name=equipe_name.strip()).first()
        if not equip:
            equip = Equipement(name=equipe_name.strip())
            session.add(equip)
            session.commit()


        annonce_equipement =AnnonceEquipement(
            annonce_id = annonce.id,
            equipement_id = equip.id
        )
        session.add(annonce_equipement)

        session.commit()

session.close()