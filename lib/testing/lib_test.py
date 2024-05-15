#!/usr/bin/env python3

import io
import sys

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < length:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    print(fibonacci_sequence[:length])

class TestPrintFibonacci:
    '''function print_fibonacci()'''

    def test_print_fibonacci_zero(self):
        '''prints empty list when length = 0'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(0)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[]\n'

    def test_print_fibonacci_one(self):
        '''prints [0] when length = 1'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(1)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[0]\n'

    def test_print_fibonacci_two(self):
        '''prints [0, 1] when length = 2'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(2)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[0, 1]\n'

    def test_print_fibonacci_ten(self):
        '''prints [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] when length = 10'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(10)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n'

# Running tests manually
if __name__ == "__main__":
    test_instance = TestPrintFibonacci()
    test_instance.test_print_fibonacci_zero()
    test_instance.test_print_fibonacci_one()
    test_instance.test_print_fibonacci_two()
    test_instance.test_print_fibonacci_ten()
    print("All tests passed!")
