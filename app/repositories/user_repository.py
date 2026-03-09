from sqlalchemy.orm import Session, joinedload

from app.entities.models import Enrollment, User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, email: str) -> User:
        user = User(name=name, email=email)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def list_all(self) -> list[User]:
        return self.db.query(User).all()

    def get_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def update(self, user: User, name: str, email: str) -> User:
        user.name = name
        user.email = email
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()

    def get_with_courses(self, user_id: int) -> User | None:
        return (
            self.db.query(User)
            .options(joinedload(User.enrollments).joinedload(Enrollment.course))
            .filter(User.id == user_id)
            .first()
        )
