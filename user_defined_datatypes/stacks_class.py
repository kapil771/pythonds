class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()
    

s = Stack()
while True:
    print('1. Push')
    print('2. Pop')
    print('3. Display')
    print('4. Quit')
    do = int(input('What would you like to do? '))
    if do == 1:
        val = input('Enter the value: ')
        s.push(val)
    elif do == 2:
        if s.is_empty():
            print('Stack is empty \n')
        else:
            print('Popped value: ',s.pop())
    elif do == 3:
        print(s.items)
    elif do == 4:
        break