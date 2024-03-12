
def affiche_menu():
    """
        cette fonction permet d'afficher le menu de la calculatrice
    """ 

    print("----MENU----")
    print("1. Addition ")
    print("2. Soustraction ")
    print("3. Multiplication ")
    print("4. Division")
    print("5. Quitter ")

def affiche_resultat(result): 
    """
        affiche le resultat apres calulcule
    """
    print(f"Resultat : {result}")

def recupere_argument():
    return float(input("Donner une valeur : ")) 

def recupere_op(): 
    return input("Chosir votre opération : ")

