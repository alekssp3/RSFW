from src.ClassTool import ClassTool


class ArgParser:
    def __init__(self, *param):
        self.args = []
        if len(param) > 0:
            self.args = param[0]
        self.flags = []
        self.isReady = False

    def parse(self, name):
        if name not in "":
            if len(self.args) > 0:
                if name in self.args and name not in self.flags:
                    self.flags.append(name)
                    return True
        return False

    def add_args(self, args):
        class_tool = ClassTool()
        if len(self.args) > 0:
            if class_tool.equalsType(args, []):
                for i in args:
                    if i not in self.args:
                        self.args.append(i)
            elif class_tool.equalsType(args, ''):
                if args not in self.args:
                    self.args.append(args)
            else:
                raise TypeError
        else:
            self.args = args

    def info(self):
        print("Arguments: %s"
              "\n\tFlags: %s" % ([i for i in self.args], [i for i in self.flags]))


# Test
if __name__ == '__main__':
    import sys

    ap = ArgParser(sys.argv[1:])
    ap.parse('test')
    ap.parse('error')
    ap.parse('--test')
    ap.info()
    ap.add_args(['error', 'error1'])
    ap.parse('error')
    ap.parse('error1')
    # ap.add_args({}) TypeError
    ap.info()
    ap.add_args('newError')
    ap.parse('newError')
    ap.info()
