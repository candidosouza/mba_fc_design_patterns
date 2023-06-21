from dataclasses import dataclass, field
from core.invoice.application.usecase.dto import EmailOutput
from core.invoice.infra import mediator

from core.invoice.infra.mediator.mediator import Mediator


@dataclass(slots=True, frozen=True)
class EmailSender:
    mediator: Mediator = field(default_factory=lambda : Mediator)

    def send(self, email_data: EmailOutput):
        # Lógica para envio de e-mail
        print('\n')
        print(f"Email enviado de {email_data.sender} para {email_data.recipient}")
        print('\n')

        # Publica um evento de envio de e-mail
        self.mediator.publish('email_sent', email_data)


class EmailLogger:

    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        self.mediator.subscribe("email_sent", self.handle_email_sent)


    def handle_email_sent(self, email_data: 'Output'):
        sender = email_data.sender
        recipient = email_data.recipient
        subject = email_data.subject

        # Lógica para registrar o envio de e-mail em um log
        print('\n')
        print(f"Registrando o envio de e-mail de {sender} para {recipient}")
        print('\n')

    @dataclass(slots=True, frozen=True)
    class Output(EmailOutput):
        pass
