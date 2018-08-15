""" Models and data base functions for travel app"""

from flask_sqlalchemy import SQLAlchemy
# Create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


class User(db.Model):
    """User of travel app"""
    __tablename__="users"

    user_id = db.Column(db.Integer, autoincrement=True, 
                                    primary_key=True)
    fname = db.Column(db.String(32), nullable=True)
    lname = db.Column(db.String(32), nullable=True)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    # connection to tripsthrough user_trips
    trips = db.relationship("Trip", secondary="user_trips", 
                                    backref="users")

    def __repr__(self):
        """Provide representation on User info"""
        return f"<User: user_id= {self.user_id}, fname= {self.fname}, lname= {self.fname}, email={self.email}>"



class UserTrip(db.Model):
    """Assosiation table between users and trips"""
    __tablename__="user_trips"

    user_trip_id = db.Column(db.Integer, autoincrement=True, 
                             primary_key=True)
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    trip_id = db.Column(db.Integer, 
                        db.ForeignKey('trips.trip_id'),
                        nullable=False)

    def __repr__(self):
        """Provide representation of User-Trip info"""
        return f"<UserTrip: user_trip_id= {user_trip_id}, user_id= {user_id}, trip_id= {trip_id}>"



class Trip(db.Model):
    """Trip Model"""
    
    __tablename__= "trips"

    trip_id = db.Column(db.Integer, autoincrement=True, 
                        primary_key=True, nullable=False)
    trip_name = db.Column(db.String(32), nullable=False)

    start_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)
    is_public = db.Column(db.Boolean, default=True,
                                      nullable=False)

    ##############also can datetime be only date?


    # Defining thae connection to tags through assosiation table trip_tags
    tags = db.relationship("Tag", secondary="trip_tags", backref="trips")

    def __repr__(self):
        """Provide representation of Trip"""
        return f"<Trip: trip_id= {trip_id}, trip_name= {trip_name}, start_date= {start_date}, end_date= {end_date}, is_public= {is_public}>"



class Pinpoint(db.Model):
    """Pinpoint Model"""

    __tablename__="pinpoints"
    
    pp_id = db.Column(db.Integer, autoincrement=True, 
                      primary_key=True, nullable=False)
    pp_name = db.Column(db.String(64), nullable=False)

    trip_id = db.Column(db.Integer, 
                        db.ForeignKey('trips.trip_id'),
                        nullable=True)
    start_time = db.Column(db.DateTime, nullable=True)
    duration = db.Column(db.Float(2), nullable=True)
    lat = db.Column(db.Float, nullable=True)
    lng = db.Column(db.Float, nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    ####put a defalt from google
    description = db.Column(db.String(200), nullable=True)

    #defining the relationship to trips
    trip = db.relationship('Trip', backref='pinpoints')


    def __repr__(self):
        """Provide representation of Pinpoint"""

        return f"<Pinpoint: pp_id= {pp_id}, trip_id= {trip_id}, pp_name= {pp_name}, start_time= {start_time}, duration= {duration}, lat= {lat}, lng= {lng}, rating= {rating}, description= {description}"


class Tag(db.Model):
    """Tag Model- for key words describing trips"""

    __tablename__="tags"

    tag_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    tag_word = db.Column(db.String(50), nullable=True)

    """Provide representation of Tag"""

    def __repr__(self):
        return f"<Tag: tag_id= {tag_id}, tag_word= {tag_word}>"



class TripTag(db.Model):
    """Assosiation table between trips and tags"""

    __tablename__="trip_tags"

    trip_tag_id = db.Column(db.Integer, autoincrement=True, 
                            primary_key=True, nullable=False)
    tag_id = db.Column(db.Integer, 
                       db.ForeignKey('tags.tag_id'), 
                       nullable=False)
    trip_id = db.Column(db.Integer, 
                        db.ForeignKey('trips.trip_id'),
                        nullable=False)


    def __repr__(self):
        """Provide representation of TripTag"""

        return f"<TripTag: trip_tag_id= {trip_tag_id}, tag_id= {tag_id}, trip_id= {trip_id}>"




class Photo(db.Model):
    """Photo Model"""

    __tablename__="photos"

    photo_id = db.Column(db.Integer, autoincrement=True, 
                        primary_key=True, nullable=False)
    file_path = db.Column(db.String(200), nullable=False)
    file_name = db.Column(db.String(64), nullable=False)
    trip_id = db.Column(db.Integer, 
                        db.ForeignKey('trips.trip_id'),
                        nullable=False)
    pp_id = db.Column(db.Integer, 
                      db.ForeignKey('pinpoints.pp_id'),
                      nullable=True)
    # Define relationships to trips and pinpoints
    trip = db.relationship('Trip', backref='photos')
    pinpoint = db.relationship('Pinpoint', backref='photos')

    """Provide representation of Photo"""
    def __repr__(self):
        return f"<Photo: photo_id= {photo_id}, file_path= {file_path}, file_name= {file_name}, trip_id= {trip_id}, pp_id= {pp_id}>"



class Friend(db.Model):
    """Friend Model"""

    __tablename__="friends"

    user_friend_id = db.Column(db.Integer, autoincrement=True, 
                              primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.user_id'), 
                        nullable=False)
    friend_id = db.Column(db.Integer, nullable=False)
   
    """Provide representation of Friend"""
    def __repr__(self):
        return f"<Friend: user_friend_id= {user_friend_id}, user_id= {user_id}, friend_id= {friend_id}>"
#############################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print("Connected to DB.")


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///temp'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)



if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # us in a state of being able to work with the database directly.

    init_app()