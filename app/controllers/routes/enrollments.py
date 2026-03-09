from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.infrastructure.database import get_db
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.user_repository import UserRepository
from app.schemas import ApiResponse, EnrollmentCreate, EnrollmentOut
from app.usecases.enrollment_usecase import EnrollmentUseCase

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_enrollment(payload: EnrollmentCreate, db: Session = Depends(get_db)):
    use_case = EnrollmentUseCase(
        EnrollmentRepository(db),
        UserRepository(db),
        CourseRepository(db),
    )
    enrollment = use_case.create_enrollment(payload.user_id, payload.course_id)
    return ApiResponse(
        success=True,
        message="Enrollment created",
        data=EnrollmentOut.model_validate(enrollment).model_dump(),
    )
