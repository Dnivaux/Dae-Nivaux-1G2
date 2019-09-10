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
