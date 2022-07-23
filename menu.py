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
taille_max = len(str(liste_valeur_col_1[0]))
taille_max_noms_grandeurs = len(noms_grandeurs[0])

for a in range (nb_lines):
    if len(str(liste_valeur_col_1[a])) > taille_max:
        taille_max = len(str(liste_valeur_col_1[a]))
    
    if len(str(liste_val_col2_calculées[a])) > taille_max:
        taille_max = len(str(liste_val_col2_calculées[a]))

    if len(noms_grandeurs[a]) > taille_max_noms_grandeurs:
        taille_max_noms_grandeurs = len(noms_grandeurs[a])

taille_max = taille_max + 2
taille_max = int(taille_max/2)

titre_colonne1 = " Colone n°1 "
titre_colonne2 = " Colone n°2 "
if len(titre_colonne1) != taille_max*2:
    taille_col1 = len(titre_colonne1)

    taille_col1 = int(taille_col1/2)

    taille_col1 = taille_max*2 - taille_col1

    titre_colonne1 = " " * taille_col1 + titre_colonne1 + " "*taille_col1
    titre_colonne2 = " " * taille_col1 + titre_colonne2 + " "*taille_col1

if taille_max < len(titre_colonne1):
    taille_max = int(len(titre_colonne1)/2)

print(" "*taille_max_noms_grandeurs+"  ║"+titre_colonne1+" ║"+titre_colonne2)

for a in range(nb_lines):
    print("═"*taille_max_noms_grandeurs+"══""╬"+"═"*taille_max*2+"═╬"+"═"*taille_max*2)

    col1_len = len(str(liste_valeur_col_1[a]))
    col2_len = len(str(liste_val_col2_calculées[a]))
    grandeur_len = len(noms_grandeurs[a])

    col1_len = int(col1_len/2)
    col2_len = int(col2_len/2)
    grandeur_len = int(grandeur_len/2)

    col1_len = taille_max-col1_len
    col2_len = taille_max-col2_len
    grandeur_len = int(taille_max_noms_grandeurs/2)-grandeur_len

    print(" "*grandeur_len+noms_grandeurs[a]+" "*grandeur_len+"  ║"+" "*col1_len+str(liste_valeur_col_1[a])+" "*col1_len+"║"+" "*col2_len+str(liste_val_col2_calculées[a])+" "*col2_len)

time.sleep(8)