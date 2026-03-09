from sqlalchemy.orm import Session

from app.entities.models import Course


class CourseRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, title: str, description: str, workload: int) -> Course:
        course = Course(title=title, description=description, workload=workload)
        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)
        return course

    def list_all(self) -> list[Course]:
        return self.db.query(Course).all()

    def get_by_id(self, course_id: int) -> Course | None:
        return self.db.query(Course).filter(Course.id == course_id).first()

    def update(self, course: Course, title: str, description: str, workload: int) -> Course:
        course.title = title
        course.description = description
        course.workload = workload
        self.db.commit()
        self.db.refresh(course)
        return course

    def delete(self, course: Course) -> None:
        self.db.delete(course)
        self.db.commit()
