# # Exercitiul 1
# note_muzicale=['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# # punctul 1
# x=note_muzicale[::-1]
# print(note_muzicale[::-1])
# note_muzicale=x
# # punctul 2
# print(note_muzicale)
# # punctul 3
# note_muzicale.reverse()
# # punctul 4
# print(note_muzicale)
#
# # Exercitiul 2
# print(note_muzicale.count('do'))
#
# # Exercitiul 3
# list_1=[3, 1, 0, 2]
# list_2=[6, 5, 4]
# print(list_1+list_2)
# list_1.extend(list_2)
# print(list_1)
#
# # # Exercitiul 4
# # list_1.sort()
# # print(list_1)
# # x=list_1.pop(0)
# # print(x)
# # print(list_1)
#
# # Exercitiul 5
# if len(list_1)==0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')
#
# # Exercitiul 6
# list_1.clear()
# print(list_1)
#
# # Exercitiul 7
# if len(list_1)==0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')

# # Exercitiul 8
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1.keys())
#
# # Exercitiul 9
# x=dict1.get('Ana')
# y=dict1.get('Gigel')
# z=dict1.get('Dorel')
# print(f'Ana a luat nota {x}')
# print(f'Gigel a luat nota {y}')
# print(f'Dorel a luat nota {z}')
# #sau
# print('Ana a luat nota ' + str(dict1.get('Ana')))
# print('Gigel a luat nota ' + str(dict1.get('Gigel')))
# print('Dorel a luat nota ' + str(dict1.get('Dorel')))
#
# # Exercitiul 10
# dict1['Dorel']=6
# print(dict1['Dorel'])
#
# # Exercitiul 11
# dict1.pop('Gigel')
# print(dict1)
# dict1.update({'Ionica': 9})
# print(dict1)

# # Exercitiul 12
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# zile_sapt.add('luni')
# print(zile_sapt)  # setul nu se modifica pentru ca luni ar fi duplicat, insa nici nu da eroare
#
# # Exercitiul 13
# if weekend.issubset(zile_sapt):
#     print('Weekend este un subset al zilelor saptamanii.')
# else:
#     print('Weekend nu este un subset al zilelor saptamanii.')
#
# # Exercitiul 14
# print(zile_sapt-weekend)
# print(weekend-zile_sapt)
# # sau
# print(zile_sapt.difference(weekend))
# print(weekend.difference(zile_sapt))
#
# # Exercitiul 15
# print(zile_sapt.intersection(weekend))
# # sau
# zile_sapt=set(zile_sapt)
# weekend=set(weekend)
# if (zile_sapt&weekend):
#     print('Elementele comune sunt '+str(zile_sapt&weekend))
# else:
#     print('Nu au elemente comune.')


# Exercitiu optional
players=['McCaw', 'Carter', 'Jones', 'O’Driscoll', 'Campese']
if 1<= int(input('Introdu numarul de schimbari (1 -3): '))<=3:
    # restul codului
else:
    print('Numarul introdus nu este valabil.')
schimbari_max=3
    # va urma :)





