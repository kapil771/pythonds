import array as arr
a = arr.array('i',[1,2,3,4,5])
while True:
    print('1:Print Array')
    print('2:Add Elements')
    print('3:Delete Elements')
    print('4:Exit')
    choice = int(input('Enter your choice:'))
    if choice == 1:
        print('The array elements are:')
        for numbers in a:
            print(numbers)
    elif choice == 2:
        val = int(input('Please enter the integer number:'))
        if isinstance(val,int):
            a.append(val)
    elif choice == 3:
        value = a.pop()
        print('The value deleted was:',value)
    elif choice == 4:
        break
    else:
        print('Please enter valid choice')