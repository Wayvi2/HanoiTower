#
# Prend rien en argument
# Renvoie un tableau vide
#
def creepile():
    return []

#
# Prend en argument la pile
#
# Renvoie True si le tableau est vide
# Renvoie False si il n'est pas vide
#
def estvide(pile):
    if len(pile) == 0:
        return True
    return False

def taille(pile):
    return len(pile)
#
#
# Prend en argument un élément et une pile
# Renvoie un tableau avec l'élément ajouter
#
def empile(element, pile):
    return [element] + pile

#
# Prend une pile en argument
# Supprime en tete de la liste
#
def depile(pile):
    return pile[1:]

#
# Prend une pile en argument
# Renvoie la tête de la pile (élement 0)
#
def sommet(pile):
    return pile[0]