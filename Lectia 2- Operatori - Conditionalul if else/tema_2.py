# Exercitiul 1
'''
If-else este un set de instructiuni prin care instruim programul sa verifice daca o conditie este adevarata sau falsa.
In cazul in care conditia este True, se executa instructiunea IF.
In cazul in care este False, se executa instructiunea de la ELSE.
'''

# # Exercitiul 2
# x = int(input('Enter a number: '))
# if x>= 0:
#     print('Este un numar natural.')
# else:
#     print('Este un numar negativ.')

# # Exercitiul 3
# x = int(input('Enter a number: '))
# if x > 0:
#     print('Este un numar pozitiv.')
# elif x == 0:
#     print('Este un numar neutru.')
# else:
#     print('Este un numar negativ.')

# Exercitiul 4
# x = int(input('Enter a number: '))
# if x in range(-2,14):
#     print('Este un numar intre -2 si 13.')
# else:
#     print('Nu este un numar intre -2 si 13.')

# # Exercitiul 5
# x = int(input('Enter a number: '))
# y = int(input('Enter another number: '))
# if (x - y) < 5:
#     print('Diferenta este mai mica de 5.')
# else:
#     print('Diferenta este mai mare de 5.')

# # Exercitiul 6
# x = int(input('Enter a number: '))
# if(not(x in range(5,28))):
#     print('Nu este un numar intre 5 si 27.')
# else:
#     print('Este un numar intre 5 si 27.')

# # Exercitiul 7
# x = int(input('Enter a number: '))
# y = int(input('Enter another number: '))
# if x == y:
#     print('X este egal cu Y.')
# elif x < y:
#     print('Y este mai mare.')
# else:
#     print('X este mai mare.')

# Exercitiul 8
# x = int(input('Introdu valoare pentru latura 1: '))
# y = int(input('Introdu valoare pentru latura 2: '))
# z = int(input('Introdu valoare pentru baza: '))
# if x == y != z:
#     print('Este triunghi isoscel.')
# elif x == z != y:
#     print('Este triunghi isoscel.')
# elif y == z != x:
#     print('Este triunghi isoscel.')
# elif x == y == z:
#     print('Este triunghi echilateral.')
# else:
#     print('Este un triunghi oarecare.')

# # Exercitiul 9
# x = input('Alege o litera: ')
# if x in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
#     print('Este o vocala.')
# else:
#     print('Este o consoana.')

# # Exercitiul 10
# x = float(input('Introdu o nota: '))
# if x > 9:
#     print('A')
# elif x > 8:
#     print('B')
# elif x > 7:
#     print('C')
# elif x > 6:
#     print('D')
# elif x > 4:
#     print('E')
# else:
#     print('F')

# Exercitii optionale
# # Exercitiul 1
# x = int(input('Introdu un numar: '))
# if len(str(x)) >= 4:
#     print('Numarul are cel putin 4 cifre.')
# else:
#     print('Numarul are mai putin de 4 cifre.')

# Exercitiul 2
# x = int(input('Introdu un numar: '))
# if len(str(x)) == 6:
#     print('Numarul are exact 6 cifre.')
# else:
#     print('Numarul are mai mult sau mai putin de 6 cifre.')

# # Exercitiul 3
# x = int(input('Introdu un numar: '))
# if x % 2 == 0:
#     print('Numarul este par.')
# else:
#     print('Numarul este impar.')

# # Exercitiul 4
# x = int(input('Introdu primul numar: '))
# y = int(input('Introdu al doilea numar: '))
# z = int(input('Introdu al treilea numar: '))
# if x>y and x>z:
#     print('Primul numar este cel mai mare.')
# elif y>x and y>z:
#     print('Al doilea numar este cel mai mare.')
# elif z>x and z>y:
#     print('Al treilea numar este cel mai mare.')
# else:
#     print('Numerele sunt egale.')

# # Exercitiul 5
# x = float(input('Introdu primul unghi: '))
# y = float(input('Introdu al doilea unghi: '))
# z = float(input('Introdu al treilea unghi: '))
# if x>0 and y>0 and z>0 and x+y+z<=180:
#     print('Este un triunghi valid')
# else:
#     print('Nu este un triunghi valid.')


# Exercitii bonus
# # Exercitiul 1
# a=int(input('Introdu varsta: '))
# b=input('Insotit de mama:Y/N ')
# c=input('Insotit de tata:Y/N ')
# d=input('Are pasaport:Y/N ')
# e=input('Act permisiune mama:Y/N ')
# f=input('Act permisiunee tata:Y/N ')
# if a>=18 and d=='Y':
#     print('Are liber la imbarcare.')
# elif a<18 and d=='Y' and b=='Y' and c=='Y':
#     print('Are liber la imbarcare.')
# elif a<18 and d=='Y' and ((b=='Y' and f=='Y') or (c=='Y' and e=='Y')):
#     print('Are liber la imbarcare.')
# else:
#     print('Nu se poate imbarca.')

# Exercitiul 1.1 - Generare cazuri de test cu toate variantele posibile si expected results
'''am identificat 36 de cazuri posibile, 18 pentru varsta >= 18 ani si 18 pentru varsta < 18 ani
sau: 18 sunt pentru existenta pasaportului,  18 pentru lipsa pasaportului.
daca pornim de la premisa ca fara pasaport nu se poate imbarca nimeni
si ca daca are varsta peste 18 ani nu are nevoie de prezenta sau acordul parintilor
raman urmatoarele conditii:
- are pasaport,  dar are sub 18 ani. Are nevoie de acordul parintilor. 
      Daca unul din parinti nu isi da acordul, este nevoie de act de permisiune din partea lui/ei.
- are pasaport, dar are sub 18 ani. Nu are acordul parintilor, deci are nevoie de act de permisiune din partea lor.
- daca nu are pasaport, nu poate calatori.
'''

# d=input('Are pasaport:Y/N ')
# a=int(input('Introdu varsta: '))
#
# if d=='Y' and a>=18:
#     print('Se poate imbarca, sunt indeplinite conditiile obligatorii.')
# elif d=='Y' and a<18:
#     print('Se verifica daca este insotit de parinti.')
#     b = input('Insotit de mama:Y/N ')
#     c = input('Insotit de tata:Y/N ')
#     if b=='Y' and c=='Y':
#         print('Se poate imbarca')
#     if (b=='Y' and c=='N') or (b=='N' and c=='Y'):
#         print('Se verifica daca exista act de permisiune din partea parintilor')
#         e = input('Act permisiune mama:Y/N ')
#         f = input('Act permisiunee tata:Y/N ')
#         if b=='Y' and c=='N' and (e=='Y' or e=='N') and f=='Y':
#             print('Se poate imbarca')
#         elif b=='N' and c=='Y' and  e=='Y' and (f=='Y' or f=='N'):
#             print('Se poate imbarca')
#         else:
#             print('Nu se poate imbarca')
#     else:
#         print('Nu se poate imbarca')
# else:
#     print('Nu are pasaport valabil')


# # Exercitiul 2
# import random
# x=int(input('Alege un numar de la 1 la 6: '))
# a=random.randrange(1,6)
# if x<a:
#     print(f'Ai pierdut. Ai ales un numar mai mic decat {a}')
# elif x>a:
#     print(f'Ai pierdut. Ai ales un numar mai mare decat {a}')
# else:
#     print(f'Ai ghicit. Felicitari! Ai ales {x} si zarul a fost {a}')





