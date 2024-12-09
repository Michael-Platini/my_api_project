from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)
    is_electronic = db.Column(db.Boolean, default=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """
        Convert the Item object to a dictionary.
        """
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "is_electronic": self.is_electronic,
            "creation_date": self.creation_date.strftime('%Y-%m-%d %H:%M:%S')
        }
