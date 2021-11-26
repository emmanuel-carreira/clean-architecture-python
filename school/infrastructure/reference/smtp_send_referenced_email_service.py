import os
from smtplib import SMTP

from school.application.reference.send_referenced_email_service import SendReferencedEmailService
from school.domain.student.student import Student


class SMTPSendReferencedEmailService(SendReferencedEmailService):
    def send_to(self, indicated_student: Student) -> None:
        server = os.getenv("SMTP_SERVER")
        host_name = os.getenv("SMTP_HOST_NAME")
        host_password = os.getenv("SMTP_HOST_PASSWORD")
        with SMTP(server) as smtp:
            smtp.login(host_name, host_password)
            smtp.sendmail(
                from_addr=host_name,
                to_addrs=indicated_student.email.address,
                msg="Welcome to our School!"
            )
