class ClassTool:

    def myType(self):
        return type(self)

    def getType(self, obj):
        return type(obj)

    def equals(self, obj):
        if self.myType() == self.getType(obj):
            return True
        return False

    def equalsType(self, obj1, obj2):
        if self.getType(obj1) == self.getType(obj2):
            return True
        return False