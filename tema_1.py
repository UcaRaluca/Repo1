# Exercitiul 1
# variabila este un spatiu de memorie in care se stocheaza informatii
# in functie de tipul de informatii stocat, variabila poate fi de mai multe feluri: string, line, float, boolean


# Exercitiul 2
nume = 'Raluca'
print(nume)
anul_nasterii = 1977
print(anul_nasterii)
varsta = 45.1
print(varsta)
copii = False
print(copii)


# Exercitiul 3
print(type(nume))
print(type(anul_nasterii))
print(type(varsta))
print(type(copii))


# Exercitiul 4
varsta = round(varsta)
print(varsta)
print(type(varsta))


# Exercitiul 5
print('Numele meu este ' + nume)
print(f'Numele meu este {nume} si am varsta de {varsta} ani.')
print(f'Numele meu este {nume}, sunt nascuta in {anul_nasterii}, am varsta de {varsta} ani.')
print(f'Pana acum am  2 copii = {bool(copii)}')


# Exercitiul 6
nume_1 = input('Va rugam sa introduceti numele: ')
prenume_1 = input('Va rugam sa introduceti prenumele: ')
print(f'Numele complet are {len(nume_1)} caractere')


# Exercitiul 7
lungime = input('Lungimea dreptunghiului este: ')
latime = input('Latimea dreptunghiului este: ')
print(f'Aria dreptunghiului este: {int(lungime)*int(latime)}')


# Exercitiul 8
declaratie = 'Coral is either the stupidest animal or the smartest rock'
numar = int(input('Alegeti un numar: '))
print(declaratie[0:-numar])


# Exercitiul 9
    # punctul a)
print(declaratie[0:5:] + declaratie[-5:])

    # punctul b)
print(declaratie.count(' the'))

    # Punctul c)
print(declaratie.replace(' the', ' THE'))

    # Punctul d)
x = declaratie.index('rock')
print(x)
print(declaratie[0:x])


# Exercitiul 10
cuvant = input('Cuvant care incepe si se termina cu aceeasi litera: ')
x = cuvant.startswith(('A', 'a'))
y = cuvant.endswith(('A','a'))
assert x == y, f'Caracterele nu sunt egale'
print('Sunt egale')


# Exercitiul 11
declaratie_2 = '0123456789'
print(declaratie_2[2::2])
print(declaratie_2[1::2])


# Exercitiul 12
z = declaratie[0:53]
print(z)
w = z.isnumeric()
print(w)

# Exercitii optionale
# Exercitiul 1
impar = input('Scrie un strig de dimensiune impara: ')
print(len(impar))
print(impar[round(len(impar)/2)])

# Exercitiul 2
pali = 'radar'
assert pali == pali[::-1], f'Nu este un palindrom'
print('Este un palindrom')

# Exercitiul 3
cuvant_1, cuvant_2 = input('Scrie alabala portocala: ').split()
print(cuvant_1)
print(cuvant_2)

# Exercitiul 4

# Exercitiul 5












