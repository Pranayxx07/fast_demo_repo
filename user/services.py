from models import User,UserDetails

def create_user(request,db):
    try:
        user_create = User()
        user_details = UserDetails()

        user_create.user_name = request.user_name
        user_details.contact_no = request.contact_no
        user_details.email = request.email

        db.add(user_create)

        db.add(user_details)
        db.commit() 
        db.refresh(user_create)
        db.refresh(user_details)
        return True
    
    except Exception as e:
        print(e)
        return False



