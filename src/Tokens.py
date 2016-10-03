class Tokens:
    def __init__(self):
        self.tokens = []
        self.auto_add()

    def get_all(self):
        return self.tokens

    def add(self, token):
        if token not in self.tokens:
            self.tokens.append(token)

    def get_exit_tokens(self):
        return ['q', 'quit', 'exit']

    def auto_add(self):
        self.add('help')
        self.add('exit')
        self.add('+')
        self.add('-')


