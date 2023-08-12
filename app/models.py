from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, nullable=False)
    description = db.Column(db.String(400))
    total = db.Column(db.Integer, nullable=False, default=0)
    available = db.Column(db.Integer)
    halfDay = db.Column(db.String(8))
    day = db.Column(db.String(8))
    week = db.Column(db.String(8))
    month = db.Column(db.String(8))


    def __repr__(self):
        if len(self.description) > 30:
            desc = self.description[:30] + '...'
        else:
            desc = self.description
        return '<Item {}, {}>'.format(self.name, desc)

