from sqlalchemy.orm import Session

from app.entities.models import Enrollment


class EnrollmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: int, course_id: int) -> Enrollment:
        enrollment = Enrollment(user_id=user_id, course_id=course_id)
        self.db.add(enrollment)
        self.db.commit()
        self.db.refresh(enrollment)
        return enrollment

    def get_by_user_and_course(self, user_id: int, course_id: int) -> Enrollment | None:
        return (
            self.db.query(Enrollment)
            .filter(Enrollment.user_id == user_id, Enrollment.course_id == course_id)
            .first()
        )
