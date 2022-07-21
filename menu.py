#imports bibli
import time

# init var(int only)
nb_lines = 2
ligne_val_connue = 0
val_connue = 0.0
coef = 0.0

# init listes
noms_grandeurs = list()
liste_valeur_col_1 = list()
liste_val_col2_calculées =list()

#intro
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('Bienvenu dans calculator2000!\n')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

time.sleep(3)

# _______________________________________étape 1_______________________________________:
nb_lines = int(input('Combien y a t\'il de lignes dans ce tableau ?\n'))

#--------------------
for a in range (nb_lines):
    nom_grandeur = input(f"\nQuel est le nom de la grandeur à la ligne n°{a+1} ?\n")
    noms_grandeurs.append(nom_grandeur)

print('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

#_______________________________________étape n°2_______________________________________:
for a in range (nb_lines):
    val_col_1 = float(input(f"Valeur de «{noms_grandeurs[a]}» dans la 1ère colonne: "))
    liste_valeur_col_1.append(val_col_1)

print('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

#_______________________________________étape n°3_______________________________________:
print('A quelle ligne appartient la valeur connue de la 2ème colonne ?')

for a in range (nb_lines):
    print(f'\t ♣ n°{a}: \"{noms_grandeurs[a]}\"')

#--------------------
ligne_val_connue = int(input(""))
print('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#--------------------
val_connue = float(input(f'Quelle est la valeur de \"{noms_grandeurs[ligne_val_connue]}\" dans la 2ème colone ?\n'))

# _______________________________________étape n°4_______________________________________:
coef = val_connue/liste_valeur_col_1[ligne_val_connue]

for a in range (nb_lines):
    liste_val_col2_calculées.append(liste_valeur_col_1[a]*coef)

print('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# _______________________________________étape n°5_______________________________________:
for a in range (nb_lines):
    print(f' ◊ {noms_grandeurs[a]}:\n\t col 1 ≈ {liste_valeur_col_1[a]}\n\t col 2 ≈ {liste_val_col2_calculées[a]}\n━━━━━━━━━━━━━━━')

time.sleep(8)