import os

def read_file(fileName):
    f = open(fileName)
    linea = None
    value = []
    while linea != "":
        linea = f.readline()
        if linea != '':
            value.append(linea.split())
        else:
            pass
    f.close()
    return value

def read_elements(name):
    value = read_file(name)
    for e in value:
        n = e[0]
        p = int(e[1])
        if e[2] == True:
            f = True
        else:
            f = False
        q = int(e[3])
        print(n,p,f,q)

def read_players(name):
    for p in read_file(name):
        if p !=[]:
            n = p[0]
            q = [int(p[1]),int(p[2]),int(p[3])]
            print(n,q)

def show_files():
    files = os.listdir()
    c = 0
    for f in files:
        l = len(f)
        if f[l-4]=='.' and f[l-3]=='t' and f[l-2]=='x' and f[l-1]=='t':
            print(str(c)+'. '+f)
        c = c+1

def write_file(path):
    f = open(path+"save_1.txt", "w")
    f.write("Now the file has more content!")
    f.close()

read_elements("elements/elements_1.txt")
read_players("jugadors/jugadors.txt")
print()
write_file("elements/")
show_files()