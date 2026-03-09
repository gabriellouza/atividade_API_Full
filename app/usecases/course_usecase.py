from app.exceptions import AppException
from app.repositories.course_repository import CourseRepository


class CourseUseCase:
    def __init__(self, course_repository: CourseRepository):
        self.course_repository = course_repository

    def create_course(self, title: str, description: str, workload: int):
        return self.course_repository.create(title=title, description=description, workload=workload)

    def list_courses(self):
        return self.course_repository.list_all()

    def get_course(self, course_id: int):
        course = self.course_repository.get_by_id(course_id)
        if not course:
            raise AppException(status_code=404, message="Course not found")
        return course

    def update_course(self, course_id: int, title: str, description: str, workload: int):
        course = self.course_repository.get_by_id(course_id)
        if not course:
            raise AppException(status_code=404, message="Course not found")
        return self.course_repository.update(course, title, description, workload)

    def delete_course(self, course_id: int):
        course = self.course_repository.get_by_id(course_id)
        if not course:
            raise AppException(status_code=404, message="Course not found")
        self.course_repository.delete(course)
