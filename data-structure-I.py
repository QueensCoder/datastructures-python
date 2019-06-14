class Stack:
    def __init__(self):
        self.stack = {}
        self.position = 0

    def stack(self, item):
        self.stack[self.position] = item
        self.position += 1

    def unstack(self):
        del self.stack[self.position]
        self.position -= 1

    def check():
        print(self.stack)


test = Stack()

# test.stack(1)
test.check()
# test.unstack()
test.check()
