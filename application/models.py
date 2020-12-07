from application import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(100), nullable=False)
    week = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Item('{self.link}', '{self.id}')'"

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"Item('{self.group_name}', '{self.id}')'"

class SubGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subgroup_name = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"Item('{self.group_name}', '{self.id}')'"