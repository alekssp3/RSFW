from src.Tokens import Tokens


class Console:
    def __init__(self):
        self.ps1 = '> '
        self.input = input(self.ps1)
        self.last_command = self.input
        self.token = Tokens()
        self.tokens = self.token.get_all()

    def parse_input(self):
        pass


#Test
if __name__ == '__main__':
    console = Console()