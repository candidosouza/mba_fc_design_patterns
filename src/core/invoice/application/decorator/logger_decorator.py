from dataclasses import dataclass
from core.invoice.application.usecase.use_case import UseCase

@dataclass(slots=True, frozen=True)
class LoggerDecorator(UseCase):
    use_case: UseCase

    def execute(self, input_params: 'Input') -> 'Output':
        print('\n')
        print(f"User-Agent: {input_params['user_agent']}")
        print('\n')
        return self.use_case.execute(input_params)

    @dataclass(slots=True, frozen=True)
    class Input:
        pass

    @dataclass(slots=True, frozen=True)
    class Output:
        pass