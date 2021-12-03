from school.academic.domain.student.student import Student


class SendReferencedEmailService:
    def send_to(self, indicated_student: Student) -> None:
        raise NotImplementedError
