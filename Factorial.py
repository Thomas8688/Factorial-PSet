#Reverse String Challenge
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return string[-1] + reverse(string[:-1])

def reverseoneline(string):
    return string if len(string) == 0 else string[-1] + reverse(string[:-1])

#Factorial of a Number Challenge
def fact(num):
    if isinstance(num, int):
        if num == 1:
            return 1
        else:
            return num * fact(num-1)
    else:
        print("Num must be an Integer")
