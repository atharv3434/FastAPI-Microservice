from pydantic import BaseModel, Field


class StudentBase(BaseModel):
    roll_no: int = Field(..., gt=0, description="Unique positive student ID")
    name: str = Field(..., min_length=2, max_length=50, examples=["Neha"])
    marks: float = Field(..., ge=0.0, le=100.0, examples=[95.0])
    city: str = Field(..., min_length=2, max_length=50, examples=["Pune"])


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=50)
    marks: float | None = Field(None, ge=0.0, le=100.0)
    city: str | None = Field(None, min_length=2, max_length=50)


class StudentResponse(StudentBase):
    pass