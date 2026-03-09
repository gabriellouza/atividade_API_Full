from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class ApiResponse(BaseModel):
    success: bool
    message: str
    data: dict | list | None


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr

    @field_validator("name")
    @classmethod
    def normalize_name(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            raise ValueError("name must not be blank")
        return normalized_value


class UserUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr

    @field_validator("name")
    @classmethod
    def normalize_name(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            raise ValueError("name must not be blank")
        return normalized_value


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    created_at: datetime


class CourseCreate(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    description: str = Field(min_length=5, max_length=500)
    workload: int = Field(gt=0)

    @field_validator("title", "description")
    @classmethod
    def normalize_text_fields(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            raise ValueError("text fields must not be blank")
        return normalized_value


class CourseUpdate(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    description: str = Field(min_length=5, max_length=500)
    workload: int = Field(gt=0)

    @field_validator("title", "description")
    @classmethod
    def normalize_text_fields(cls, value: str) -> str:
        normalized_value = value.strip()
        if not normalized_value:
            raise ValueError("text fields must not be blank")
        return normalized_value


class CourseOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    workload: int


class EnrollmentCreate(BaseModel):
    user_id: int = Field(gt=0)
    course_id: int = Field(gt=0)


class EnrollmentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    course_id: int
    enrolled_at: datetime
