#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        first_sequence = [0]
        print(first_sequence)
    elif length == 2:
        second_sequence = [0, 1]
        print(second_sequence)
    else:
        first = 0
        second = 1
        sequence = [0, 1]
        
        length -= 2
        while length > 0:
            temp = second
            second = first + second
            first = temp

            sequence.append(second)

            length -= 1

        print (sequence)
    



