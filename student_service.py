from fastapi import HTTPException, status
from src.schemas.student import StudentCreate, StudentResponse, StudentUpdate


class StudentService:

    def __init__(self):
        # In-memory storage mock for demo/test isolation
        self._db: dict[int, dict] = {
            101: {"roll_no": 101, "name": "Amit", "marks": 85.0, "city": "Pune"},
            102: {"roll_no": 102, "name": "Neha", "marks": 90.0, "city": "Mumbai"},
            103: {
                "roll_no": 103,
                "name": "Rahul",
                "marks": 78.0,
                "city": "Nashik",
            },
        }

    def list_all(self) -> list[StudentResponse]:
        return [StudentResponse(**record) for record in self._db.values()]

    def get_by_roll_no(self, roll_no: int) -> StudentResponse:
        record = self._db.get(roll_no)
        if not record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Student with roll number {roll_no} not found",
            )
        return StudentResponse(**record)

    def create(self, student_in: StudentCreate) -> StudentResponse:
        if student_in.roll_no in self._db:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Student with roll number {student_in.roll_no} already exists",
            )
        data = student_in.model_dump()
        self._db[student_in.roll_no] = data
        return StudentResponse(**data)

    def update(
        self, roll_no: int, student_in: StudentUpdate
    ) -> StudentResponse:
        record = self._db.get(roll_no)
        if not record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Student with roll number {roll_no} not found",
            )
        update_data = student_in.model_dump(exclude_unset=True)
        record.update(update_data)
        return StudentResponse(**record)

    def delete(self, roll_no: int) -> None:
        if roll_no not in self._db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Student with roll number {roll_no} not found",
            )
        del self._db[roll_no]


student_service = StudentService()