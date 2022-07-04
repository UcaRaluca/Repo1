# # Exercitiul 1
# class Cerc:
#
#     def __init__(self, raza, culoare):
#         self.raza=raza
#         self.culoare=culoare
#
#     def descrie_cerc(self):
#         print(f'Cercul nostru are raza de {self.raza} si culoarea {self.culoare}')
#
#     def aria(self,pi):
#         print(f'Cercul nostru are aria de {(pi*self.raza*self.raza)}')
#
#     def diametrul(self):
#         print(f'Cercul nostru are diametrul de {(self.raza*2)}')
#
#     def circumferinta(self,pi):
#         print(f'Cercul nostru are circumferinta de {(2*pi*self.raza)}')
#
# cerc_1=Cerc(5,'verde')
#
# cerc_1.descrie_cerc()
# cerc_1.aria(3.1416)
# cerc_1.diametrul()
# cerc_1.circumferinta(3.1416)

# # Exercitiul 2
# class Dreptunghi:
#
#     def __init__(self, lungime, latime, culoare):
#         self.lungime=lungime
#         self.latime=latime
#         self.culoare=culoare
#
#     def descrie(self):
#         print(f'Dreptunghiul nostru are lungimea de {self.lungime}, latimea de {self.latime} si culoarea {self.culoare}')
#
#     def aria(self):
#         print(f'Dreptunghiul nostru are aria de {(self.lungime*self.latime)}')
#
#     def perimetru(self):
#         print(f'Dreptunghiul nostru are diametrul de {(2*(self.lungime+self.latime))}')
#
#
#
# dreptunghi1=Dreptunghi(5,10,'verde')
#
# dreptunghi1.descrie()
# dreptunghi1.aria()
# dreptunghi1.perimetru()
# dreptunghi1.culoare='albastru'
# dreptunghi1.descrie()

# # Exercitiul 3
# class Angajat:
#
#     def __init__(self, nume, prenume, salariu):
#         self.nume=nume
#         self.prenume=prenume
#         self.salariu=salariu
#
#     def descrie(self):
#         print (f'Angajatul cu nume si prenume {self.nume} {self.prenume}, are salariul de {self.salariu}')
#
#     def nume_complet(self):
#         print(f'Angajatul are numele complet {self.nume} {self.prenume}')
#         self.nume_complet=self.nume+self.prenume
#         return self.nume_complet
#
#     def salariu_lunar(self):
#         print(f'Angajatul are salariul de {self.salariu}')
#
#     def salariu_anual(self):
#         print(f'Salariul anual este {12*self.salariu}')
#
#     def marire_salariu(self,procent_majorare):
#         self.marire_salariu=self.salariu*procent_majorare
#         print(f'Salariul lunar a fost majorat cu {self.marire_salariu}')
#
#
# angajat1=Angajat('Popescu','Stefan',3000)
# angajat1.descrie()
# angajat1.nume_complet()
# angajat1.salariu_lunar()
# angajat1.salariu_anual()
# angajat1.marire_salariu(0.07)


# # Exercitiul 4
# class Cont:
#     def __init__(self,titular_cont,iban):
#         self.titular_cont=titular_cont
#         self.iban=iban
#         self.sold=0
#
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

#     def creditare_cont(self, suma_adaugata):
#         self.sold+=suma_adaugata
#         print(f'{self.titular_cont} ,ati adaugat suma de {suma_adaugata}')
#         print(f'Soldul actual pentru contul {self.iban} este {self.sold}')
#
#     def debitare_cont(self, suma_retrasa):
#         if suma_retrasa<=self.sold:
#             self.sold-=suma_retrasa
#             print(f'{self.titular_cont} ,ati retras suma de {suma_retrasa}')
#             print(f'Soldul actual pentru contul {self.iban} este {self.sold}')
#         else:
#             print(f'{self.titular_cont} Atentie,fonduri insuficiente')
#
# cont1=Cont('Raluca B', 'RO89BTRL')
# cont2=Cont('Dan O', 'RO32RNCB')
#
# cont1.afisare_sold()
# cont2.afisare_sold()
#
# cont1.creditare_cont(600)
# cont2.creditare_cont(800)
#
# cont1.debitare_cont(700)
# cont1.debitare_cont(500)
# cont2.debitare_cont(800)

# Exercitii optionale
# # Exercitiul 1
# from tabulate import tabulate
# from datetime import date
#
#
# class Factura:
#     seria = 'FN'
#
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def antet_factura(self,seria='FN'):
#         print(f'Factura seria {seria} nr. {self.numar}')
#
#     def schimba_cantitatea(self):
#         print(f'Cantitatea facturata este de {self.cantitate}')
#
#     def schimba_pretul(self):
#         print(f'Pretul pe bucata este {self.pret_buc}')
#
#     def schimba_nume_produs(self):
#         print(f'Numele produsului este {self.nume_produs}')
#
#     def genereaza_factura(self):
#         pret_total = self.cantitate * self.pret_buc
#         print(tabulate([[self.nume_produs, self.cantitate, self.pret_buc, pret_total]],
#                        headers=['nume_produs', 'cantitate', 'pret_buc', 'pret_total']))
#
# today=date.today()
# factura1=Factura(1,'bicicleta',10,150)
# factura1.antet_factura()
# print(f'Data facturii: {today}')
# factura1.genereaza_factura()

# # Exercitiul 2
# class Masina:
#     marca = 'Suzuki'
#     viteza_actuala = 0
#     culoare = 'Gri'
#     culori_disponibile = ['Rosu', 'Bleu', 'Portocaliu', 'Argintiu', 'Negru']
#     inmatriculata = False
#
#     def __init__(self, model, viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#
#     def descrie(self):
#         print(
#             f'Masina este marca {self.marca}, model {self.model}, culoare {self.culoare}, inmatriculata {self.inmatriculata},'
#             f'are viteza actuala de {self.viteza_actuala} si viteza maxima de {self.viteza_maxima}')
#
#     def inmatriculare(self):
#         self.inmatriculata = True
#         print(f'Masina este inmatriculata: {self.inmatriculata}')
#
#     def vopseste(self, noua_culoare):
#         for i in self.culori_disponibile:
#             if noua_culoare == i:
#                 self.culoare = noua_culoare
#                 return self.culoare
#             else:
#                 return f'Eroare. {noua_culoare} nu este in lista de culori disponibile'
#
#     def accelereaza(self):
#         if self.viteza_actuala < 0:
#             return f'Eroare. {self.viteza_actuala} este viteza negativa.'
#         elif self.viteza_actuala > self.viteza_maxima or self.viteza_actuala < self.viteza_maxima:
#             self.viteza_actuala = self.viteza_maxima
#             return self.viteza_actuala
#
#     def franeaza(self):
#         if self.viteza_actuala > 0:
#             self.viteza_actuala = 0
#             return f'Ai franat. Viteza actuala este {self.viteza_actuala}'
#         elif self.viteza_actuala == 0:
#             return f'Viteza este zero. Ramai pe loc.'
#         else:
#             return f'Eroare. {self.viteza_actuala} este viteza negativa.'
#
#
# masina1 = Masina('Ignis', 160)
#
# masina1.descrie()
#
# masina1.inmatriculare()
#
# print(masina1.vopseste('Alb'))
# print(masina1.vopseste('Rosu'))
#
# masina1.viteza_actuala=200
# print(masina1.accelereaza())
# masina1.viteza_actuala=130
# print(masina1.accelereaza())
# masina1.viteza_actuala=-5
# print(masina1.accelereaza())
#
# masina1.viteza_actuala=180
# print(masina1.franeaza())
# masina1.viteza_actuala=0
# print(masina1.franeaza())
# masina1.viteza_actuala=-5
# print(masina1.franeaza())


# # Exercitiul 3
# class ToDoList:
#     dict={}
#
#     def adauga_task(self,nume,descriere):
#         self.nume=nume
#         self.descriere=descriere
#         self.dict[nume]=descriere
#         return self.dict
#
#     def finalizează_task(self,nume):
#         self.nume=nume
#         del self.dict[nume]
#         return self.dict
#
#     def afiseaza_keys_lista(self):
#         return self.dict.keys()
#
#     def afișează_detalii_suplimentare(self):
#         task_nou = input('Adauga un task: ')
#         for self.nume in self.dict.keys():
#             if task_nou != self.nume:
#                 task_nou = input('Adauga un task: ')
#                 raspuns = input('Vrei sa adaugi un task? ')
#                 if raspuns == 'Nu':
#                     print('La revedere!')
#                 elif raspuns == 'Da':
#                     nume2 = task_nou
#                     descriere2 = input('Adauga detalii task: ')
#                     self.dict[nume2] = descriere2
#                     return self.dict
#                 else:
#                     print('Raspuns gresit. Te rog raspunde cu Da sau Nu.')
#             else:
#                 print('Lista de taskuri ramane neschimbata.')
#         return self.dict
#
#
# agenda=ToDoList()
# print(agenda.adauga_task('tema1', '10 exercitii'))
# agenda.adauga_task('tema2', '11 exercitii')
# agenda.adauga_task('tema3', '12 exercitii')
# print(agenda.adauga_task('tema4', '7 exercitii'))
#
# print(agenda.finalizează_task('tema2'))
#
# print(agenda.afiseaza_keys_lista())
#
# print(agenda.afișează_detalii_suplimentare())