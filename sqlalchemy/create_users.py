from main import User,Session,engine




users=[
    {
        "username":"prince",
        "email":"prince@hacks.com"
    },
        {
        "username":"joel",
        "email":"joel@hacks.com"
    },
        {
        "username":"emmanuel",
        "email":"emmanuel@hacks.com"
    },
        {
        "username":"elvis",
        "email":"elvis@hacks.com"
    },
        {
        "username":"owura",
        "email":"owura@hacks.com"
    },
        {
        "username":"nii",
        "email":"nii@hacks.com"
    },
        
]

local_session=Session(bind=engine)

#new_user=User(username="prescott",email="pres@hacks.com")

#local_session.add(new_user)

#local_session.commit()

for u in users:
    new_user=User(username=u["username"],email=u["email"] )
    

    local_session.add(new_user)

    local_session.commit()

    print("Added {u['username']}")

