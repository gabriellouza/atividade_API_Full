from app.exceptions import AppException
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.user_repository import UserRepository


class EnrollmentUseCase:
    def __init__(
        self,
        enrollment_repository: EnrollmentRepository,
        user_repository: UserRepository,
        course_repository: CourseRepository,
    ):
        self.enrollment_repository = enrollment_repository
        self.user_repository = user_repository
        self.course_repository = course_repository

    def create_enrollment(self, user_id: int, course_id: int):
        if not self.user_repository.get_by_id(user_id):
            raise AppException(status_code=404, message="User not found")

        if not self.course_repository.get_by_id(course_id):
            raise AppException(status_code=404, message="Course not found")

        if self.enrollment_repository.get_by_user_and_course(user_id, course_id):
            raise AppException(status_code=409, message="Duplicate enrollment is not allowed")

        return self.enrollment_repository.create(user_id=user_id, course_id=course_id)
