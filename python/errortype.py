import sys
import traceback

testdic = {'a': 123, 'b': 'my', 'c': {}}

try:
    value = testdic['m']
except Exception as e:
    traceback.print_exc(file=sys.stdout)

try:
    value = int(testdic['b'])
except Exception as e:
    traceback.print_exc(file=sys.stdout)

try:
    value = int(testdic['c'])
except Exception as e:
    traceback.print_exc(file=sys.stdout)