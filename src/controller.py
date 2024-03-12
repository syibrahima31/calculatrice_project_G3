import model 
import view

def calculate():
    while True:
        # affichage du menu  
        view.affiche_menu()

        # Choix d'une opération 
        op = view.recupere_op()

        # Saisi des nombres 
        if op  in "1234":
            x = view.recupere_argument()
            y = view.recupere_argument()

        if op == "1": 
            result = model.add(x, y)
        
        elif op == "2":
            result = model.sub(x, y)
        
        elif op == "3": 
            result = model.mult(x, y)
        
        elif op == "4": 
            result = model.div(x, y)
        
        else: 
            break 
        
        view.affiche_resultat(result)
        print("-"*50)
    

if __name__ == "__main__": 
    calculate()