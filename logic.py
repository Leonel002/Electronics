import Inputs
def convert(algo):
    assert Inputs.check(algo)
    if algo==True:
        return 1
    elif algo==False:
        return 0
    else:
        return algo
def _and(uno,otro):
    uno=convert(uno);otro=convert(otro)
    return uno and otro
def _or(uno,otro):
    uno=convert(uno);otro=convert(otro)
    return uno or otro
def _not(uno):
    uno=convert(uno)
    return convert(not uno)
def _or_exclusive(uno,algo):
    uno=convert(uno);algo=convert(algo)
    return _and(_or(uno,algo),_not(_and(uno,algo)))
def main():
    print(_and(True,True))
    print(_or(False,0))
    print(_not(0))
    print("OR_Exclusive :",_or_exclusive(True,True))
if __name__=="__main__":
    main()