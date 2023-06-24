from dataclasses import dataclass, field
from core.invoice.application.usecase.dto import EmailOutput
from core.invoice.infra import mediator

from core.invoice.infra.mediator.mediator import Mediator


@dataclass(slots=True, frozen=True)
class EmailSender:
    mediator: Mediator = field(default_factory=lambda : Mediator)

    def send(self, email_data: 'Input') -> 'Output':
        # Lógica para envio de e-mail
        
        # Publica um evento de envio de e-mail
        self.mediator.publish('email_sent', email_data)
        return self.Output(
            sender=email_data.sender,
            recipient=email_data.recipient,
            subject=email_data.subject,
            message=email_data.message
        )

    @dataclass(slots=True, frozen=True)
    class Input:
        sender: str
        recipient: str
        subject: str
        message: str

    @dataclass(slots=True, frozen=True)
    class Output(EmailOutput):
        def __post_init__(self):
            print('\n')
            print(f"Email enviado de {self.sender} para {self.recipient}")
            print('\n')


class EmailLogger:

    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        self.mediator.subscribe("email_sent", self.handle_email_sent)


    def handle_email_sent(self, email_data: 'Input') -> 'Output':
        sender = email_data.sender
        recipient = email_data.recipient
        subject = email_data.subject

        # Lógica para registrar o envio de e-mail em um log
        return self.Output(
            sender=sender, 
            recipient=recipient, 
            subject=subject, 
            message=email_data.message
        )

    
    @dataclass(slots=True, frozen=True)
    class Input:
        sender: str
        recipient: str
        subject: str
        message: str

    @dataclass(slots=True, frozen=True)
    class Output(EmailOutput):

        def __post_init__(self):
            print('\n')
            print(f"Registrando o envio de e-mail de {self.sender} para {self.recipient}")
            print('\n')
