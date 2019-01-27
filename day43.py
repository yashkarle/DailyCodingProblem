class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return True if self.root is None else False

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.root
        self.root = new_node
        print(data, "pushed to stack")

    def pop(self):
        if self.is_empty():
            return float("-inf")

        temp = self.root
        self.root = self.root.next
        popped = temp.data

        return popped

    def top(self):
        if self.is_empty():
            return float("inf")

        return self.root.data


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.pop(), "popped from stack")
    print(stack.pop(), "popped from stack")

    print("Top element is ", stack.top())
