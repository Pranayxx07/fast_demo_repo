from fastapi import APIRouter,Depends,HTTPException,status

from schemas import UserDetailCreate
from db import get_session
from .services import create_user


user_rout = APIRouter()


@user_rout.post(
    'create_user/'
)
def create_user_details(
    *,
    request : UserDetailCreate,
    db= Depends(get_session)
):
    try:
        create_status = create_user(request,db)
        if create_status:
            return {"status": 201,
                    "message":"user created succesfully"}
    except Exception as e:
        raise HTTPException(detail=e,status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


