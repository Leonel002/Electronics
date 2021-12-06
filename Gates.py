import Inputs
from logic import _and,_or,_not,_or_exclusive
from random import randint
class Gates(object):
    def __init__(self,inp=[],name=None):
        self.id="Gate "
        self.ID=self
        if type(inp) in (list,tuple)and len(inp)==0  and isinstance(self,NOT)==False:
            self.inputs=Inputs.Inputs([0,0])
        elif type(inp) in (list,tuple) and len(inp)==0 and isinstance(self,NOT):
            self.inputs=Inputs.Inputs([0])
        else:
            self.inputs=Inputs.Inputs(inp)
        assert self.check()
        self.outputs()
        if name==None:
            self.name=str(randint(100000,1000000))
        elif type(name)==str:
            self.name=name
        else:
            self.name="UNKNOWN"
    def outputs(self):
        pass
    def check(self):
        return True
    def __len__(self):
        return len(self.inputs)
    def __repr__(self,i="default"):
        assert self.check()
        if i=="default":
            return str(self.output)
        elif i=="id":
            return self
        else:
            raise ValueError("Don't give commands that's supposed that it will given")
    def __str__(self):
        return self.id+self.name
class Buffer(Gates):
    def check(self):
        if len(self.inputs)==1:
            return True
        elif len(self.inputs)==0:
            self.inputs=Inputs.Inputs([0])
            return True
        else:
            return False
    def outputs(self):
        self.id="Buffer "
        self.output=self.inputs[0]
class AND(Gates):

    def check(self):
        if len(self.inputs)>=2:
            return True
        elif len(self.inputs)==0:
            self.inputs=Inputs.Inputs([0,0])
            return True
        else:
            return False
    def outputs(self):
        self.id="AND "
        out=self.inputs[0]
        for index in range(1,len(self.inputs)):
            out=_and(out,self.inputs[index])
        self.output=out
class OR(Gates):
    def check(self):
        if len(self.inputs)>=2:
            return True
        elif len(self.inputs)==0:
            self.inputs=Inputs.Inputs([0,0])
        else:
            return False

    def outputs(self):
        self.id="OR "
        out = self.inputs[0]
        for index in range(1, len(self.inputs)):
            out = _or(out, self.inputs[index])
        self.output = out

class NOT(Gates):
    def check(self):
        if len(self.inputs)==1:
            return True
        elif len(self.inputs)==0:
            self.inputs=Inputs.Inputs([0])
            return True
        else:
            return False
    def outputs(self):
        self.id="NOT "
        self.output=_not(self.inputs[0])
class XOR(Gates):
    def check(self):
        if len(self.inputs)>=2:
            return True
        elif len(self.inputs)==0:
            self.inputs=Inputs.Inputs([0,0])
            return True
        else:
            return False
    def outputs(self):
        self.id="XOR "
        gateand=AND(self.inputs.inputs)
        gateor=OR(self.inputs.inputs)
        gatenot=NOT(gateand.output)
        out=AND([gateor.output,gatenot.output])
        self.output=out.output
class NOR(OR):
    def outputs(self):
        self.id="NOR "
        out = self.inputs[0]
        for index in range(1, len(self.inputs)):
            out = _or(out, self.inputs[index])
        self.output = _not(out)
class NAND(AND):
    def outputs(self):
        self.id="NAND "
        out = self.inputs[0]
        for index in range(1, len(self.inputs)):
            out = _and(out, self.inputs[index])
        self.output = _not(out)
class XNOR(XOR):
    def outputs(self):
        self.id="XNOR "
        OR_EXC=XOR(self.inputs.inputs)
        self.output=_not(OR_EXC.output)

def main():
    gate=AND()
    print(gate)
    gate = AND([1, 1, 1, 0, 1])
    gate_nand=NAND([1,1,1,0,1])
    print("NAND :",gate_nand)
    print("AND :",gate)
    gate_or = OR([0, 0, 1, 0, 0])
    gate_nor=NOR([0,0,0,1,0])
    print("OR :", gate_or)
    print("NOR :", gate_nor)
    gate_not=NOT([1])
    print("NOT :", gate_not)
    gate_exc=XOR([0,1,1,1])
    print("XOR :",gate_exc)
    gate_xnor=XNOR([])
    print("XNOR :",gate_xnor)
    print(gate_exc.ID)
if __name__=="__main__":
    main()

