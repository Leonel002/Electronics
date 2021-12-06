import Inputs
import random
class Bin_Inputs:
    def __init__(self,input=0,name=""):
        self.id="Input "
        if len(name)==0:
            self.name=str(random.randint(100000,1000000))
        if input in (0,1):
            self.logical_input=input
        elif (type(input) in (list,tuple) and len(input)==1 and input[0] in (0,1)):
            self.logical_input=input[0]
        self.output=self.logical_input
    def change(self):
        self.logical_input=int(not self.logical_input)
        self.output=self.logical_input
    def __str__(self):
        return str(self.id+self.name)
    def __repr__(self):
        return str(self.logical_input)