entrainement=int(input("quel en entrainement?"))
if entrainement==1:
    print(Salut!)


elif entrainement==2:
    n=int(input("choisi un nombre"))
    x=int(input("choisi un autre nombre"))
    p=n+x
    print(p)

elif entrainement==3:
    n=int(input("choisi un nombre"))
    x=int(input("choisi un autre nombre"))
    c=int(input("choisi le dernier nombre"))
    p=n*(x+c)
    print(p)

if entrainement==4:
    n=int(input("choisi un nombre"))
    x=int(input("choisi un autre nombre"))
    p=n/x
    print(p)

elif entrainement==5:
    n=int(input("choisi un nombre"))
    x=int(input("choisi un autre nombre"))
    p=n**x
    print(p)

elif entrainement==6:
    n=int(input("choisi un nombre"))
    x=int(input("choisi un autre nombre"))
    p=n//6
    print(p)
