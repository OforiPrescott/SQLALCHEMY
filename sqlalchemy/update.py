from main import Session,engine,User

local_session=Session(bind=engine)

user_to_update=local_session.query(User).filter(User.username == 'prescott').first()

user_to_update.username = "pres"
user_to_update.email= "pres@hacks.com"


local_session.commit()
