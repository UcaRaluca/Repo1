# Exercitiul 1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat',
'Trabant', 'Opel']
# for i in range(len(masini)):
#     print(f'Masina mea preferata este {masini[i]}')
#
# for i in masini:
#     print(f'Masina mea preferata este {i}')

# i=0
# while i<len(masini):
#     print(f'Masina mea preferata este {masini[i]}')
#     i += 1

# Exercitiul 2
# for i in range(1,len(masini)-1):
#     masini[i] = masini[i].upper()
#     print(masini[i])
# else:
#     print(masini)   # nu imi dau seama cum sa readuc toata lista la valoarea initiala, nu doar prima si ultima masina

# Exercitiul 3
# for i in range(len(masini)):
#     if masini[i]=='Mercedes':
#         print('Am găsit mașina dorită de dumneavoastra.')
#         break
#     else:
#         print(f'Am găsit mașina {masini[i]}. Mai căutam')
#         i += 1

# Exercitiul 4
# for masina in masini:
#     if masina=='Lăstun' or masina=='Trabant':
#         continue
#     print(f'S-ar putea sa va placa masina {masina}')

# Exercitiul 5
# masini_vechi = []
# for masina in masini:
#     if masina == 'Lăstun' or masina == 'Trabant':
#         masini_vechi.append(masina)
#
# for i in range(len(masini)):
#     if masini[i]=='Trabant':
#         masini[i]='Tesla'
#     if masini[i]=='Lăstun':
#         masini[i]='Tesla'
#
# print('Modele vechi:', masini_vechi)
# print('Modele noi:', masini)

# # Exercitiul 6
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# for i,j in pret_masini.items():
#     if j<=15000:
#         print(f'Pentru un buget de sub 15000 euro puteți alege mașina {i} ')

# # Exercitiul 7
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# x=0
# for numar in numere:
#     if numar==3:
#         x=x+1
# print(f'Numarul {numar} apare in lista de {x} ori.')

# # Exercitiul 8
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# suma=0
# for numar in numere:
#     suma=suma+numar
# print(f'Suma numerelor este {suma}')

# # Exercitiul 9
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# max = numere[0]
# for numar in numere:
#     if numar > max:
#         max = numar
# print(f'Cel mai mare numar este {max}')

# # Exercitiul 10
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# lista_negative=[]
# for numar in numere:
#     if numar>0:
#         numar=numar*(-1)
#         lista_negative.append(numar)
# print(f'Noua lista este {lista_negative}')

# # Exercitiul optional 1
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for numar in alte_numere:
#     if numar%2==0:
#         numere_pare.append(numar)
#     else:
#         numere_impare.append(numar)
#     if numar>=0:
#         numere_pozitive.append(numar)
#     else:
#         numere_negative.append(numar)
# print(numere_pare)
# print(numere_impare)
# print(numere_pozitive)
# print(numere_negative)

# # Exercitiul optional 2
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_sort=[]
# while alte_numere:
#     minim = alte_numere[0]
#     for numar in alte_numere:
#         if numar<minim:
#             minim=numar
#     numere_sort.append(minim)
#     alte_numere.remove(minim)
# print(numere_sort)

# # Exercitiul 3
# import random
# numar_secret = random.randint(1,30)
# numar_ales = int(input("Alegeti un numar: "))
# while numar_ales < 1 or numar_ales > 30:
#     print("Alege un numar intre 1 si 30")
#     numar_ales = int(input('Alegeti un numar: '))
# while numar_ales >= 1 and numar_ales <= 30:
#     if numar_secret > numar_ales:
#         print(f'Numarul secret {numar_secret} este mai mare decat numarul ales {numar_ales}')
#         break
#     elif numar_secret < numar_ales:
#         print(f'Numarul secret {numar_secret} este mai mic decat numarul ales {numar_ales}')
#         break
#     else:
#         print(f'Felicitari! Ai ghicit :)) numarul secret este {numar_secret} si ai ales {numar_ales}')
#         break

# # Exercitiul 4
# n=int(input('Introdu un numar: '))
# for i in range(n+1):
#     for j in range(i):
#         print(i, end='')
#     print('')

# # Exercitiul 5
# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# for i in range(len(tastatura_telefon)):
#     for j in range(len(tastatura_telefon[i])):
#         print('Cifra curenta este: ',tastatura_telefon[i][j])
