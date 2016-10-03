from src.ConsoleInput import Console
from src.Tokens import Tokens

class RSFW:
    def __init__(self, *params):
        self.tokens = Tokens()
        self.main_loop()

    def main_loop(self):
        last_command = ''
        while(last_command not in self.tokens.get_exit_tokens()):
            self.console = Console()
            last_command = self.console.last_command


# Test
if __name__ == '__main__':
    RSFW()