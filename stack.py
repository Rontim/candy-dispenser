

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print("pushed item: " + str(item))

    def check_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.check_empty():
            return "stack is empty"

        return self.stack.pop()

    def peek(self):
        if self.check_empty():
            return "stack is empty"

        return self.stack[len(self.stack)-1]
