#!/usr/bin/python3

if __name__ == "__main__":

    def safe_print_division(a, b):

        try : 
            a = int(a)
            b = int(b)
            result = a/b
        except ZeroDivisionError :
            result = None
        finally : 
            print("{:d} / {:d} = {}".format(a, b, result)) 