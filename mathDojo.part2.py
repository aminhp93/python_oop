class MathDojo(object):
    def __init__(self):
        self.value = 0

    def add(self, *arg):
        for i in range(0, len(arg)):
            if type(arg[i]) is list or type(arg[i]) is tuple:
                for j in range(0, len(arg[i])):
                    self.value += arg[i][j]
            else:
                self.value += arg[i]
        return self

    def subtract(self, *arg):
        for i in range(0, len(arg)):
            if type(arg[i]) is list or type(arg[i]) is tuple:
                for j in range(0, len(arg[i])):
                    self.value -= arg[i][j]
            else:
                self.value -= arg[i]
        return self

    def result(self):
        print "Result: " + str(self.value)

md = MathDojo().add(2, [5, 4,2,4,1], [4,2.3,2.1]).subtract(4,2,(2,3,4.2), [2,1.3]).result()
print md

