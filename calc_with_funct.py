# this code do not support division by zero!
def zero(num=""):
    if "+" in num:
        index = num.find("+")
        num = num[0:index]
        return 0 + int(num)
    elif "-" in num:
        index = num.find("-")
        num = num[0:index]
        return 0 - int(num)
    elif "*" in num:
        index = num.find("*")
        num = num[0:index]
        return 0 * int(num)
    elif "/" in num:
        index = num.find("/")
        num = num[0:index]
        return 0 // int(num)
    else:
        return "0"
def one(num=""):
    if "+" in num:
        index = num.find("+")
        num = num[0:index]
        return 1 + int(num)
    elif "-" in num:
        index = num.find("-")
        num = num[0:index]
        return 1 - int(num)
    elif "*" in num:
        index = num.find("*")
        num = num[0:index]
        return 1 * int(num)
    elif "/" in num:
        index = num.find("/")
        num = num[0:index]
        return 1 // int(num)
    else:
        return "1"

def two(num=""):
    if "+" in num:
        index = num.find("+")
        num = num[0:index]
        return 2 + int(num)
    elif "-" in num:
        index = num.find("-")
        num = num[0:index]
        return 2 - int(num)
    elif "*" in num:
        index = num.find("*")
        num = num[0:index]
        return 2 * int(num)
    elif "/" in num:
        index = num.find("/")
        num = num[0:index]
        return 2 // int(num)
    else:
        return "2"

def three(num=""):
    if "+" in num:
        index = num.find("+")
        num = num[0:index]
        return 3 + int(num)
    elif "-" in num:
        index = num.find("-")
        num = num[0:index]
        return 3 - int(num)
    elif "*" in num:
        index = num.find("*")
        num = num[0:index]
        return 3 * int(num)
    elif "/" in num:
        index = num.find("/")
        num = num[0:index]
        return 3 // int(num)
    else:
        return "3"

def four(num=""):
    if "+" in num:
        index = num.find("+")
        num = num[0:index]
        return 4 + int(num)
    elif "-" in num:
        index = num.find("-")
        num = num[0:index]
        return 4 - int(num)
    elif "*" in num:
        index = num.find("*")
        num = num[0:index]
        return 4 * int(num)
    elif "/" in num:
        index = num.find("/")
        num = num[0:index]
        return 4 // int(num)
    else:
        return "4"

def five(num=""):
    if "+" in num:
        index = num.find("+")
        num = num[0:index]
        return 5 + int(num)
    elif "-" in num:
        index = num.find("-")
        num = num[0:index]
        return 5 - int(num)
    elif "*" in num:
        index = num.find("*")
        num = num[0:index]
        return 5 * int(num)
    elif "/" in num:
        index = num.find("/")
        num = num[0:index]
        return 5 // int(num)
    else:
        return "5"

def six(num=""):
    if "+" in num:
        index = num.find("+")
        num = num[0:index]
        return 6 + int(num)
    elif "-" in num:
        index = num.find("-")
        num = num[0:index]
        return 6 - int(num)
    elif "*" in num:
        index = num.find("*")
        num = num[0:index]
        return 6 * int(num)
    elif "/" in num:
        index = num.find("/")
        num = num[0:index]
        return 6 // int(num)
    else:
        return "6"

def seven(num=""):
    if "+" in num:
        index = num.find("+")
        num = num[0:index]
        return 7 + int(num)
    elif "-" in num:
        index = num.find("-")
        num = num[0:index]
        return 7 - int(num)
    elif "*" in num:
        index = num.find("*")
        num = num[0:index]
        return 7 * int(num)
    elif "/" in num:
        index = num.find("/")
        num = num[0:index]
        return 7 // int(num)
    else:
        return "7"

def eight(num=""):
    if "+" in num:
        index = num.find("+")
        num = num[0:index]
        return 8 + int(num)
    elif "-" in num:
        index = num.find("-")
        num = num[0:index]
        return 8 - int(num)
    elif "*" in num:
        index = num.find("*")
        num = num[0:index]
        return 8 * int(num)
    elif "/" in num:
        index = num.find("/")
        num = num[0:index]
        return 8 // int(num)
    else:
        return "8"

def nine(num=""):
    if "+" in num:
        index = num.find("+")
        num = num[0:index]
        return 9 + int(num)
    elif "-" in num:
        index = num.find("-")
        num = num[0:index]
        return 9 - int(num)
    elif "*" in num:
        index = num.find("*")
        num = num[0:index]
        return 9 * int(num)
    elif "/" in num:
        index = num.find("/")
        num = num[0:index]
        return 9 // int(num)
    else:
        return "9"

def plus(num):
    return num + "+"

def minus(num):
    return num + "-"

def times(num):
    return num + "*"

def divided_by(num):
    return num + "/"

print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))