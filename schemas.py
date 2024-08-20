from pydantic import BaseModel


class UserCreate(BaseModel):
    user_name : str
    
class UserDetailCreate(UserCreate):
    contact_no : int 
    email : str