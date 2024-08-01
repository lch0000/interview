import json, ujson

json.__name__ = 'ujson'
json.dumps = ujson.dumps
json.loads = ujson.loads