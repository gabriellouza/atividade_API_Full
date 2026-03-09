from app.exceptions import AppException
from app.repositories.user_repository import UserRepository


class UserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, name: str, email: str):
        if self.user_repository.get_by_email(email):
            raise AppException(status_code=409, message="Email already exists")
        return self.user_repository.create(name=name, email=email)

    def list_users(self):
        return self.user_repository.list_all()

    def get_user(self, user_id: int):
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise AppException(status_code=404, message="User not found")
        return user

    def update_user(self, user_id: int, name: str, email: str):
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise AppException(status_code=404, message="User not found")

        existing_email = self.user_repository.get_by_email(email)
        if existing_email and existing_email.id != user_id:
            raise AppException(status_code=409, message="Email already exists")

        return self.user_repository.update(user=user, name=name, email=email)

    def delete_user(self, user_id: int):
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise AppException(status_code=404, message="User not found")
        self.user_repository.delete(user)

    def get_user_courses(self, user_id: int):
        user = self.user_repository.get_with_courses(user_id)
        if not user:
            raise AppException(status_code=404, message="User not found")

        courses = [
            {
                "id": enrollment.course.id,
                "title": enrollment.course.title,
                "description": enrollment.course.description,
                "workload": enrollment.course.workload,
            }
            for enrollment in user.enrollments
        ]
        return {
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
            },
            "courses": courses,
        }
