def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Dzielenie przez zero!"

def mult(x, y):
    return x * y

def mod(x, y):
    if y != 0:
        return x % y
    else:
        return "Error: Modulo przez zero!"
