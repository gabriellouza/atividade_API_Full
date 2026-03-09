from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.infrastructure.database import get_db
from app.repositories.user_repository import UserRepository
from app.schemas import ApiResponse, UserCreate, UserOut, UserUpdate
from app.usecases.user_usecase import UserUseCase

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    use_case = UserUseCase(UserRepository(db))
    user = use_case.create_user(name=payload.name, email=payload.email)
    return ApiResponse(success=True, message="User created", data=UserOut.model_validate(user).model_dump())


@router.get("")
def list_users(db: Session = Depends(get_db)):
    use_case = UserUseCase(UserRepository(db))
    users = [UserOut.model_validate(user).model_dump() for user in use_case.list_users()]
    return ApiResponse(success=True, message="Users retrieved", data=users)


@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    use_case = UserUseCase(UserRepository(db))
    user = use_case.get_user(user_id)
    return ApiResponse(success=True, message="User retrieved", data=UserOut.model_validate(user).model_dump())


@router.put("/{user_id}")
def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    use_case = UserUseCase(UserRepository(db))
    user = use_case.update_user(user_id=user_id, name=payload.name, email=payload.email)
    return ApiResponse(success=True, message="User updated", data=UserOut.model_validate(user).model_dump())


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    use_case = UserUseCase(UserRepository(db))
    use_case.delete_user(user_id)
    return ApiResponse(success=True, message="User deleted", data=None)


@router.get("/{user_id}/courses")
def get_user_courses(user_id: int, db: Session = Depends(get_db)):
    use_case = UserUseCase(UserRepository(db))
    data = use_case.get_user_courses(user_id)
    return ApiResponse(success=True, message="User courses retrieved", data=data)
