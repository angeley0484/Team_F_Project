from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    games_played = db.Column(db.Integer, default=0)
    # Other player stats can go here, like cards, level, etc.

    def __repr__(self):
        return f"<Player {self.name}>"

# You may also add other models for game state or history if needed
