
exercice=int(input("choisi le numero de l'exercice!"))
if exercice==1:
    prenom =int(input("Your name"))
    print('Hello bro {}'.format(prenom))




elif exercice==2:
    cercle=int((input("Donner votre rayon")))
    perimetre=(cercle*2*3.1415926535898)
    print("le perimetre est égale a {}".format(perimetre))

elif exercice==3:
    a=int(input("Donner l'age du joueur:"))
    if a<10:
        print('Trop jeune!')
    elif 10<=a<12:
        print('U10')
    elif 12<=a<14:
        print('U12')
    elif 14<=a<16:
        print('U14')
    else:
        print('Trop vieux!')

elif exercice==4:
    note=int(input("Ta note pour voir si ta ton bac:"))
    if 0<=note<10:
        print("Ta pas ton bac reviens l'année prochaine")
    elif 10<=note<=20:
        print("chatteux")
    else:
        print("Arrete de mentir, avoue tu as le seum de pas avoir ton bac")

elif exercice==5:
    a=int(input("valeur de a"))
    b=int(input("valeur de b"))
    d=a%b
    if d==0:
        print('divisible')
    elif d>0:
        print('pas divisible')

elif exercice==6:
    prix=35000
    for i in range(11):
        prix=prix-prix*0.1
        print(round(prix,2))
    for y in range(5):
        prix=prix-prix*0.1
        print(round(prix,2))

elif exercice==7:
    n=int(input("choisis un nombre"))
    n>=0
    for n in range(n+1):
        print(n)

elif exercice==8:
    a=int(input('choisis un nombre'))
    b=int(input('choisis un autre nombre'))
    print(a*b)

elif exercice==9:
    L=8
    N=0
    while 12:
        L=12
        N=0

elif exercice==10:
    nioui=int(input("Continuer?"))
    if nioui=='oui':
        nioui=1
        if nioui==1:
            nioui=int(input("Continuer?"))
    elif nioui=='non':
        print('ok')

elif exercice==11:
    n=int(input("choisi un entier"))
    b=n*n
    if n!=0:
        n=int(input("choisi un entier"))

    elif n==0:
        print(n)

else:
    print('choisi un autre exercice')
