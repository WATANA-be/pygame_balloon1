banpei = {}
banpei['prev']=banpei
banpei['next']=banpei

def show():
    s = []
    c = banpei['next']

    while(c != banpei):
        s.append(c['key'])
        c = c['next']
    print(*s ,end = '\n')

def insert(key):
    x = {}
    x['key']=key
    x['next']=banpei['next']
    banpei['next']['prev']=x
    banpei['next']=x
    x['prev']=banpei

def delete(key):
    