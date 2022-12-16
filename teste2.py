import json

def log():
    posty = open('log.json')
    logi = json.loads(posty.read())
      
    return logi

update = []
log1 = log()
update = log1[-1]

print (update['materias'])