class Node:
    def __init__(self, value, next, previous):
        self.value = value
        self.next = next
        self.previous = previous

    def __repr__(self):
        return f'{self.value}'

class Queue:
    def __init__(self, front, rear):
        self.front = front
        self.rear = rear

    def enqueue(self, new_node):
        self.rear.previous = new_node
        new_node.next = self.rear
        self.rear = new_node
        new_node.previous = None

    def dequeue(self):
        temp_front = self.front
        self.front = self.front.previous
        self.front.next = None
        return temp_front
    
    def print_queue(self):
        curr_node = self.rear
        while curr_node:
            print(curr_node)
            curr_node = curr_node.next
                 

n1 = Node(1,None,None)

q1 = Queue(n1,n1)
n2 = Node(2,None,None)
q1.enqueue(n2)
q1.dequeue()
q1.print_queue()