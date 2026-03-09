from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.controllers.routes import courses, enrollments, users
from app.entities.models import Base
from app.exceptions import AppException
from app.infrastructure.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="StudyManager API", version="1.0.0")

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(enrollments.router)


@app.exception_handler(AppException)
async def app_exception_handler(_: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "message": exc.message, "data": None},
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"success": False, "message": "Validation error", "data": exc.errors()},
    )


@app.exception_handler(Exception)
async def generic_exception_handler(_: Request, __: Exception):
    return JSONResponse(
        status_code=500,
        content={"success": False, "message": "Internal server error", "data": None},
    )
