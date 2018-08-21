"""Utility file to seed database from data in """

import datetime
from sqlalchemy import func
from model import User, Trip, UserTrip, Pinpoint, Tag, Photo, Friend, connect_to_db, db
from server import app



def load_users(users_filename):
    """Load users from u.user into database."""

    print("Users")
    User.query.delete()

    for row in open(users_filename):
        row = row.rstrip()
        fname, lname, email, password = row.split(",")

        user = User(fname=fname,
                    lname=lname,
                    email=email,
                    password=password)

        # We need to add to the session or it won't ever be stored
        db.session.add(user)

    # Once we're done, we should commit our work
    db.session.commit()


# def set_val_user_id():
#     """Set value for the next user_id after seeding database"""

#     # Get the Max user_id in the database
#     result = db.session.query(func.max(User.user_id)).one()
#     max_id = int(result[0])

#     # Set the value for the next user_id to be max_id + 1
#     query = "SELECT setval('users_user_id_seq', :new_id)"
#     db.session.execute(query, {'new_id': max_id + 1})
#     db.session.commit()



def load_trips(trips_filename):
    print("Trips")
    Trip.query.delete()

    for row in open(trips_filename):
        row = row.rstrip()
        trip_name, start_trip, end_trip, is_public = row.split(",")
        if (is_public=='True'):
            is_public = True
        else:
            is_public = False
        trip = Trip(trip_name=trip_name,
                    start_trip=start_trip,
                    end_trip=end_trip,
                    is_public=is_public)
                    

        # We need to add to the session or it won't ever be stored
        db.session.add(trip)

    # Once we're done, we should commit our work
    db.session.commit()



def load_user_trips(user_trips_filename):
    print("UserTrips")
    UserTrip.query.delete()

    for row in open(user_trips_filename):
        row = row.rstrip()
        user_id, trip_id = row.split(",")
        
        user_trip = UserTrip(user_id=user_id,
                              trip_id=trip_id)
                    

        # We need to add to the session or it won't ever be stored
        db.session.add(user_trip)

    # Once we're done, we should commit our work
    db.session.commit()




def load_pinpoints(pinpoints_filename):
    print("Pinpoints")
    Pinpoint.query.delete()

    for row in open(pinpoints_filename):
        row = row.rstrip()
        name, trip_id, start, end, lat, lng, rating, description = row.split(",")

        pinpoint = Pinpoint(name=name,
                    trip_id=trip_id,
                    start=start,
                    end=end,
                    lat=lat,
                    lng=lng,
                    rating=rating,
                    description=description)
                    

        # We need to add to the session or it won't ever be stored
        db.session.add(pinpoint)

    # Once we're done, we should commit our work
    db.session.commit()
    
   
def load_tags(tags_filename):
    print("Tags")
    Tag.query.delete()

    for row in open(tags_filename):
        row = row.rstrip()
        tag = Tag(tag_word=row)

        # We need to add to the session or it won't ever be stored
        db.session.add(tag)
    # Once we're done, we should commit our work
    db.session.commit()

  
    
def load_photos(photos_filename):

    print("Photos")
    Photo.query.delete()

    for row in open(photos_filename):
        row = row.rstrip()
        file_path, file_name, trip_id, pp_id = row.split(",")
        photo = Photo(file_path=file_path,
                      file_name=file_name,
                      trip_id=trip_id,
                      pp_id=pp_id)
        # We need to add to the session or it won't ever be stored
        db.session.add(photo)
    # Once we're done, we should commit our work
    db.session.commit()
      




def load_friends(friends_filename):
    print("Friends")
    Friend.query.delete()

    for row in open(friends_filename):
        row = row.rstrip()
        user_id,friend_id = row.split(",")
        friend = Friend(user_id=user_id,
                        friend_id=friend_id)
        # We need to add to the session or it won't ever be stored
        db.session.add(friend)
    # Once we're done, we should commit our work
    db.session.commit()




if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    users_filename = "data/users_data.csv"
    trips_filename = "data/trips_data.csv"
    user_trips_filename = "data/user_trips_data.csv"

    pinpoints_filename = "data/pinpoints_data.csv"
    tags_filename = "data/tags_data.csv"
    photos_filename = "data/photos_data.csv"
    friends_filename = "data/friends_data.csv"

    
    load_users(users_filename)
    load_trips(trips_filename)
    load_user_trips(user_trips_filename)

    load_pinpoints(pinpoints_filename)
    load_tags(tags_filename)
    load_photos(photos_filename)
    load_friends(friends_filename)
    # first_user = User(email="user@gmail.com", password="ok")
    # db.session.add(first_user)
    # db.session.commit()

    # # Add our user
    # jessica = User(email="jessica@gmail.com",
    #                password="love",
    #                age=42,
    #                zipcode="94114")
    # db.session.add(jessica)
    # db.session.commit()