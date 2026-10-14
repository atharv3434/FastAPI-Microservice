from fastapi import APIRouter, status
from src.schemas.student import StudentCreate, StudentResponse, StudentUpdate
from src.services.student_service import student_service

router = APIRouter(prefix="/students", tags=["Students"])


@router.get(
    "/", response_model=list[StudentResponse], status_code=status.HTTP_200_OK
)
def get_students():
    return student_service.list_all()


@router.get(
    "/{roll_no}", response_model=StudentResponse, status_code=status.HTTP_200_OK
)
def get_student(roll_no: int):
    return student_service.get_by_roll_no(roll_no)


@router.post(
    "/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED
)
def create_student(student: StudentCreate):
    return student_service.create(student)


@router.patch(
    "/{roll