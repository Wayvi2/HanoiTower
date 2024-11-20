from defpile import *

# Fonction pour vérifier si un déplacement est valide
def deplvalide(TA, TB):
    if estvide(TA):
        return False
    if estvide(TB):
        return True

    return sommet(TA) < sommet(TB)


# Fonction pour déplacer un disque d'une tour à une autre
def deplace(TA, TB):
    if deplvalide(TA, TB):
        TB = empile(sommet(TA), TB)
        TA = depile(TA)
    else:
        print("Déplacement invalide.")
    return TA, TB

# Fonction principale
def principale():

    # Initialisation des tours
    TA = creepile()
    TB = creepile()
    TC = creepile()


    print("""        
        hhhhhhh                                                                    iiii
        h:::::h                                                                   i::::i
        h:::::h                                                                    iiii
        h:::::h
        h::::h hhhhh         aaaaaaaaaaaaa   nnnn  nnnnnnnn       ooooooooooo   iiiiiii
        h::::hh:::::hhh      a::::::::::::a  n:::nn::::::::nn   oo:::::::::::oo i:::::i
        h::::::::::::::hh    aaaaaaaaa:::::a n::::::::::::::nn o:::::::::::::::o i::::i
        h:::::::hhh::::::h            a::::a nn:::::::::::::::no:::::ooooo:::::o i::::i
        h::::::h   h::::::h    aaaaaaa:::::a   n:::::nnnn:::::no::::o     o::::o i::::i
        h:::::h     h:::::h  aa::::::::::::a   n::::n    n::::no::::o     o::::o i::::i
        h:::::h     h:::::h a::::aaaa::::::a   n::::n    n::::no::::o     o::::o i::::i
        h:::::h     h:::::ha::::a    a:::::a   n::::n    n::::no::::o     o::::o i::::i
        h:::::h     h:::::ha::::a    a:::::a   n::::n    n::::no:::::ooooo:::::oi::::::i
        h:::::h     h:::::ha:::::aaaa::::::a   n::::n    n::::no:::::::::::::::oi::::::i
        h:::::h     h:::::h a::::::::::aa:::a  n::::n    n::::n oo:::::::::::oo i::::::i
        hhhhhhh     hhhhhhh  aaaaaaaaaa  aaaa  nnnnnn    nnnnnn   ooooooooooo   iiiiiiii""")

    print("Bienvenue dans le jeu des tours de Hanoï !")
    print("Votre objectif est de déplacer tous les disques de TA à TC.")
    print("Les tours sont représentées par TA (A), TB (B), et TC (C).")


    nombre_disque = int(input("Entrez le nombre de disque : "))
    # Empiler les disques sur la tour A (du plus grand au plus petit)
    for i in range(nombre_disque, 0, -1):  # Les disques sont numérotés de 6 à 1
        TA = empile(i, TA)





    while taille(TC) != nombre_disque:  # Le jeu se termine lorsque TC contient tous les disques
        # Afficher l'état actuel des tours
        print("\nÉtat actuel :")
        print("TA:", TA)
        print("TB:", TB)
        print("TC:", TC)

        # Demander un déplacement à l'utilisateur
        source = input("Entrez la tour source (A, B, C) : ").strip().upper() #.strip() enlève les espaces , .upper() met en majuscule
        destination = input("Entrez la tour destination (A, B, C) : ").strip().upper()

        # Identifier les tours correspondantes
        if source not in ["A", "B", "C"] or destination not in ["A", "B", "C"]:
            print("Tour source ou destination invalide.")
            continue

        # Effectuer le déplacement
        if source == "A" and destination == "B":
            TA, TB = deplace(TA, TB)
        elif source == "A" and destination == "C":
            TA, TC = deplace(TA, TC)
        elif source == "B" and destination == "A":
            TB, TA = deplace(TB, TA)
        elif source == "B" and destination == "C":
            TB, TC = deplace(TB, TC)
        elif source == "C" and destination == "A":
            TC, TA = deplace(TC, TA)
        elif source == "C" and destination == "B":
            TC, TB = deplace(TC, TB)
        else:
            print("Déplacement impossible. Réessayez.")

    print("\nFélicitations ! Vous avez gagnez!")
    print("État final :")
    print("TA:", TA)
    print("TB:", TB)
    print("TC:", TC)

# Lancer le programme
principale()


