from main import User,Session,engine


local_session=Session(bind=engine)

users=local_session.query(User).all()




#returns all objects
#users=local_session.query(User).all()[:3]
#for user in users:
    #print(user.username)

#query for one object

prescott=local_session.query(User).filter(User.username=="prescott").first()

print(prescott)
