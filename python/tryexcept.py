path = None

def write_to_file(path):
    pass

f = open(path, 'w')
try:
    write_to_file(f)
finally:
    f.close()

try:
    write_to_file(f)
except:
    print('Failed')
else:
    print('Success')
finally:
    f.close()