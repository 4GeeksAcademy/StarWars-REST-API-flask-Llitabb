from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    terrain = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "climate": self.climate,
            "population": self.population,
            # do not serialize the password, its a security breach
        }
    
class Characters(db.Model):
    __tablename__ = 'character'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(250), nullable=False)
    height = Column(db.String(250), nullable=False)
    mass = Column(db.String(250), nullable=False)
    haircolor = Column(db.String(250), nullable=False)
    skincolor = Column(db.String(250), nullable=False)
    planet_id = Column(db.Integer, ForeignKey('planet.id'))
    planet = relationship(Planets)

def __repr__(self):
        return '<Characters %r>' % self.username

def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "climate": self.climate,
            "population": self.population,
            # do not serialize the password, its a security breach
        }
