import sys 
import os 
sys.path.insert(0, "/Users/ibrahima/Desktop/Mes Projets/calculatrice_project")
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import model 


def test_add(): 
    assert model.add(1, 3) == 4 
    assert model.add(4, 2) == 6

def test_mult(): 
    assert model.mult(2, 3) == 6

