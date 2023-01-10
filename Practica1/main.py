import os
from partida import Partida
p = 0



def show_menu():
    '''
    Realitza un display del menó, comprova si la opció entrada
    és correcte i si ho és es guarda a la variable s per canviar
    d'estat
    '''
    print()
    print("Seleccioni la opció que vol realitzar")
    print("1. Afegir un Jugador")
    print("2. Elimniar Jugador")
    print("3. Decrementar Salut")
    print("4. Utilitzar element")
    print("5. Comprar element")
    print("6. Mostrar partda")
    print("7.Sortir de la partida")
    i1 = input()
    if i1=='1' or i1=='2' or i1=='3' or i1=='4' or i1=='5' or i1=='6' or i1=='7':
        s = int(i1)+1
    else:
        print("El valor no és correcte")
        s=9
    return s

def inicialitzacio():
    '''Menu inicial que determina si es vol començar a importar la partida o es vol sortir'''
    print("Benvingut, vols començar la partida? [s/n]")
    i1 = input()
    if i1=='s':
        s = 1
    elif i1 == 'n':
        s = 8
        print('Sortir de la partida')
    else:
        s = 0
        print('El valor entrat no és correcte')
    return s

def show_files(p):
    files = os.listdir(p)
    c = 0
    li = []
    for f in files:
        l = len(f)
        if f[l-4]=='.' and f[l-3]=='t' and f[l-2]=='x' and f[l-1]=='t':
            print(str(c)+'. '+f)
            li.append(f)
        c = c+1
    return c,li

def importar_partida():

    print("Quina partida de jugadors vols importar?")
    n,file = show_files('jugadors/')
    correct = 0
    while correct == 0:
        i1 = input()
        for i in range(n+1):
            if i1 == str(i):
                p.read_players(file[i])
                correct = 1
        if correct == 0:
            print('Torna a entrar una opció correcte')
    n, file = show_files('elements/')
    correct = 0
    while correct == 0:
        i1 = input()
        for i in range(n+1):
            # print(n, i)
            if i1 == str(i):
                if i<=n-1:
                    p.read_elements(file[i])
                    correct = 1
                else:
                    print("Valor fora de rang")
        if correct == 0:
            print('Torna a entrar una opció correcte')
    s = 9

    return s

def comp_int(st):
    c=0
    while(c==0):
        print(st)
        i = input()
        try:
            o = int(i)
            if o>=0 and o<=100:
                c=1
            else:
                print('Valor fora de rang')
                c=0
        except:
            print('Valor introduit no correcte')
    return o

def afegir_jugador():
    print("S'ha seleccionat crear un jugador")
    print("Introdueix nom del jugador:")
    n = input()
    while p.comp_player(n) == True:
        print("El jugador introduit ja existeix, introdueix un altre nom")
        n = input()
    q0 = comp_int("Introdueix la força del jugador [0-100]")
    q1 = comp_int("Introdueix la velocitat del jugador [0-100")
    q2 = comp_int("Introdueix la magida del jugador [0-100]")
    p.add_player(n,[q0,q1,q2])
    s = 9
    return s

def eliminar_jugador():
    print("S'ha seleccionat elmiminar un jugador")
    print("Escrigui el nom del jugador: ")
    n = input()
    p.delete_player(n)
    s = 9
    return s

def decrementar_salut():
    print("S'ha seleccionat decrementar vida de un jugador")
    print("Escrigui el nom del jugador:)")
    n = input()
    while p.comp_player(n)==False:
        print("El jugador introduit no és correcte")
        n = input()
    i1 = comp_int("Valor que s'ha de decrementar la vida : [0-100]")

    p.dec_salut(n,i1)
    s = 9
    return s

def utilitzar_element():
    print("S'ha seleccionat que un jugador utilitzi un element")

    print("Escrigui el nom del jugador: ")
    n = input()
    while p.comp_player(n) == False:
        print("El jugador introduit no existeix")
        n = input()
    print("Introdueixi el nom de l'element que vol seleccionar")
    e = input()
    while p.comp_element(e) == False:
        print("L'element introduit no existeix")
        e = input()

    p.use_element(n,e)
    s = 9
    return s

def comprar_elements():
    print("S'ha seleccionat comprar un element")
    print("Escrigui el nom del jugador que vol comprar un element: ")
    n = input()
    while p.comp_player(n) == False:
        print("El jugador introduit no existeix")
        n = input()
    print("Introdueixi el nom de l'element que vol comprar")
    e = input()
    while p.comp_element(e) == False:
        print("L'element introduit no existeix")
        e = input()
    p.buy_element(n,e)
    s = 9
    return s

def mostrar_partida():
    print(p)
    s = 9
    return s

p = Partida()
s = 0
while(True):
    if s == 0:
         s = inicialitzacio()
    elif s == 1:
        s = importar_partida()
    elif s == 2:
        s = afegir_jugador()
    elif s == 3:
        s = eliminar_jugador()
    elif s == 4:
        s = decrementar_salut()
    elif s == 5:
        s = utilitzar_element()
    elif s == 6:
        s = comprar_elements()
    elif s == 7:
        s = mostrar_partida()
    elif s == 9:
        s = show_menu()
    elif s == 8:
        break
    else:
        pass


# a.read_players('jugadors.txt')
# a.read_elements('elements_1.txt')
# a.show_players()
# a.show_elements()
# print(a)
# print(a.partides)
