# # Exercitiul 1
# def sum_numbers(nr1=0,nr2=0):
#     sum=nr1+nr2
#     return sum
# print(sum_numbers(15,21))

# # Exercitiul 2
# def este_par(x):
#     if (x%2)==0:
#         print(f'{x} este numar par')
#     else:
#         print(f'{x} este numar impar')
# este_par(int(input('Introdu un numar: ')))

# # Exercitiul 3
# def nr_caractere_nume(nume, nume_mijlociu, prenume):
#     nume=len(nume)
#     nume_mijlociu=len(nume_mijlociu)
#     prenume=len(prenume)
#     print(f'Numar total caractere este {int(nume)+int(nume_mijlociu)+int(prenume)}')
# nr_caractere_nume('Balaniuc', 'Luciana', 'Raluca')

# # Exercitiul 4
# def aria_dreptunghi(lungime, latime):
#     lungime=int(input('Introdu lungimea: '))
#     latime=int(input('Introdu latimea: '))
#     print(f'Aria dreptunghiului este {lungime*latime}')
# aria_dreptunghi('lungime', 'latime')

# # Exercitiul 5
# def aria_cercului(pi, raza):
#     raza=int(input('Introdu raza cercului: '))
#     pi=3.14159
#     print(f'Aria cercului este {pi*(raza**2)}')
# aria_cercului('pi','raza')

# # Exercitiul 6
# def exista_caracter(string, caracter):
#     if caracter in string:
#         return 'True, exista caracterul in string'
#     else:
#         return 'False, nu exista caracterul in string'
# raspuns=exista_caracter((input('Introdu stringul in care vom cauta: ')), (input('Introdu un caracter: ')))
# print(raspuns)

# # Exercitiul 7
# def nr_caractere(string):
#     litere_mici=0
#     litere_mari=0
#     for i in string:
#         if i.islower():
#             litere_mici=litere_mici+1
#         elif i.isupper():
#             litere_mari=litere_mari+1
#     print(f'Total litere mici este: {litere_mici}')
#     print(f'Total litere mari este {litere_mari}')
# nr_caractere(input('Introdu string: '))

# # Exercitiul 8
# def numere(lista):
#     for i in lista:
#         if i<=0:
#             lista.remove(i)
# lista=[5, 7, 3, 9, -3, 3, -1, 0, -4, 3]
# numere(lista)
# print(lista)

# # Exercitiul 9
# def numere(x,y):
#     if x<y:
#         print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
#     elif y<x:
#         print(f'Primul număr {x} este mai mare decat al doilea nr {y}')
#     elif x==y:
#         print('Numerele sunt egale')
# numere(5, 8)
# numere(9, 3)
# numere(3, 3)

# Exercitiul 10
...