#Reverse String Challenge
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return string[-1] + reverse(string[:-1])

def reverseoneline(string):
    return string if len(string) == 0 else string[-1] + reverse(string[:-1])

print(reverse("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
