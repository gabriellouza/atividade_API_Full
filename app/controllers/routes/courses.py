from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.infrastructure.database import get_db
from app.repositories.course_repository import CourseRepository
from app.schemas import ApiResponse, CourseCreate, CourseOut, CourseUpdate
from app.usecases.course_usecase import CourseUseCase

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_course(payload: CourseCreate, db: Session = Depends(get_db)):
    use_case = CourseUseCase(CourseRepository(db))
    course = use_case.create_course(payload.title, payload.description, payload.workload)
    return ApiResponse(success=True, message="Course created", data=CourseOut.model_validate(course).model_dump())


@router.get("")
def list_courses(db: Session = Depends(get_db)):
    use_case = CourseUseCase(CourseRepository(db))
    courses = [CourseOut.model_validate(course).model_dump() for course in use_case.list_courses()]
    return ApiResponse(success=True, message="Courses retrieved", data=courses)


@router.get("/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):
    use_case = CourseUseCase(CourseRepository(db))
    course = use_case.get_course(course_id)
    return ApiResponse(success=True, message="Course retrieved", data=CourseOut.model_validate(course).model_dump())


@router.put("/{course_id}")
def update_course(course_id: int, payload: CourseUpdate, db: Session = Depends(get_db)):
    use_case = CourseUseCase(CourseRepository(db))
    course = use_case.update_course(course_id, payload.title, payload.description, payload.workload)
    return ApiResponse(success=True, message="Course updated", data=CourseOut.model_validate(course).model_dump())


@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    use_case = CourseUseCase(CourseRepository(db))
    use_case.delete_course(course_id)
    return ApiResponse(success=True, message="Course deleted", data=None)
