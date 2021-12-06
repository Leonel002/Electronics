from Gates import *
import Inputs
def ret_type_gate(gate):
    gate=gate.upper()
    if gate=="AND":
        return AND
    elif gate=="OR":
        return OR
    elif gate=="NOT":
        return NOT

    elif gate=="NAND":
        return NAND

    elif gate=="NOR":
        return NOR

    elif gate=="XOR":
        return XOR

    elif gate=="XNOR":
        return XNOR
def op_is(obj):
    tup=("AND","OR","NOT","NAND","NOR","XOR","XNOR")
    for i in  tup:
        if obj=="%s *"%(i):
            return True
    return False
def modify_gate(gate,other):
    if type(other)==str:
        gate.name=other
    elif type(other) in (tuple,list):
        gate.inputs=Inputs.Inputs(other)
    elif isinstance(other,Inputs.Inputs):
        gate.inputs=other
    elif type(other) in (AND,OR,NOT,NAND,NOR,XOR,XNOR):
        gate=other
    return gate
def show_gates(obj):
    ret=''
    cont=0
    print("obj",obj)
    for i in range(len(obj.inputs)):
        ret+=str(i)+"     "+str(obj[i])+"\n"
    return ret
class Gate_Generator:
    def __init__(self,gate_type,numbers):
        self.id=0
        if type(gate_type)==str:
            gate_type=ret_type_gate(gate_type)
        self.gates=Inputs.Inputs([])
        assert gate_type in (AND,OR,NOT,NAND,NOR,XOR,XNOR)
        assert type(numbers)==int
        for i in range(numbers):
            self.gates.inputs.append(gate_type(name=str(self.id)))
            self.id+=1
        print(self.id)
    def __getitem__(self, item):
        return self.gates[item]
    def modify(self, gate,other):
        if type(gate)==int:
            print(self[gate])
            self.gates.inputs[gate]=modify_gate(self[gate],other)
        elif type(gate)==str:
            pass
    def __len__(self):
        return len(self.gates)
    def __repr__(self):
        return self.gates
    def __str__(self):
        return show_gates(self.gates)
def main():
    f=Gate_Generator("And",67)
    print(f.gates)
    print(len(f.gates))
    f.modify(9,OR([0,1],name="Hello"))
    print(f)
if __name__=="__main__":
    main()