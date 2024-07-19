import dis

def func():
    a = 0
    a += 1
    b = 1
    a,b = b,a

dis.dis(func)