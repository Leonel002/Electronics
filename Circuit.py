from Gates import *        #THIS IMPORT ALL THE GATES CLASSES THAT IS IN THE "Gates.py"
from Bin_Inp import Bin_Inputs

def check_gates(obj=[]):   #THIS FUNCTION CHECK THE FIRST PARAMETERS TO SEE IF IS AN INSTANCES OF THE CLASS GATE
    if type(obj) ==list:
        for index in obj:
            if not isinstance(index, Gates):
                return False
        return True
    elif isinstance(obj,Gates):
        return True
    elif type(obj)==dict:
        for index in list(obj.keys()):
            if not isinstance(index,Gates,Bin_Inputs):
                return False
        return True
    elif isinstance(obj,Bin_Inp.Bin_Inputs):
        return True
    else:
        return False
def gate_space_delete(gate):
    ret=''
    for index in gate:
        if index==" ":
            break
        else:
            ret+=index
    return ret
class Circuit:                      #CLASE CIRCUITO
    def __init__(self,gates=[],Bin_Ent=[]):           #CONSTRUCTOR
        assert (type(Bin_Ent)==list and ([isinstance(i,Bin_Inputs) for i in Bin_Ent]) or len(Bin_Ent)==0) or type(Bin_Ent)==Inputs.Inputs
        assert check_gates(gates)
        self.inputs=Inputs.Inputs(Bin_Ent)
        self.gates=gates
        self.names=[index.name for index in self.gates]
        self.gates_dict={}
        self.conection={}
        for index in self.gates:
            try:
                self.gates_dict[gate_space_delete(index.id)].append(index.name)
            except KeyError:
                self.gates_dict[gate_space_delete(index.id)]=[index.name]
    def add_gates_all(self,puertas):
        assert check_gates(puertas)
        if type(puertas) in (tuple,list):
            self.gates+=puertas
            for index in puertas:
                try:
                    self.gates_dict[gate_space_delete(index.id)].append(index.name)
                except KeyError:
                    self.gates_dict[gate_space_delete(index.id)]=[index.name]
                self.names.append(index.name)
        elif isinstance(puertas,Gates):
            self.add_gates_all([puertas])

    def __add__(self,puertas):
        self.add_gates_all(puertas)
    def in_gates(self,gates):
        if isinstance(gates,Gates):
            for index in self.gates_dict.values():
                for index2 in index:
                    if gates.name==index2:
                        return True
            return False
        else:
            return False
    def conect(self, origen, destino, Index=-1):
        if type(destino)==dict:
            if isinstance(origen,Bin_Inputs):
                for i in list(destino.keys()):
                    self.conect(Buffer([origen]), i, destino[i])
            else:
                for i in list(destino.keys()):
                    self.conect(origen,i,destino[i])
        elif isinstance(origen,Bin_Inputs):
            self.conect(Buffer([origen]),destino,Index)
        elif Index==-1:
            assert check_gates(destino)
            assert check_gates(origen)
            print(self.in_gates(origen) or isinstance(origen, Bin_Inp.Bin_Inputs))
            if type(destino) in (list,tuple) and (self.in_gates(origen) or isinstance(origen,Bin_Inp.Bin_Inputs)):
                for index in destino:
                    assert self.in_gates(index)
                try:
                    for otra2 in destino:
                        if not isinstance(otra2,NOT):
                            self.conection[str(origen)].append([otra2, len(otra2)])
                        else:
                            self.conection[str(origen)].append([otra2, len(otra2)-1])
                except:
                    for otra2 in destino:
                        if not isinstance(otra2,NOT):
                            self.conection[str(origen)]=[[otra2,len(otra2)]]
                        else:
                            self.conection[str(origen)] = [[otra2, len(otra2)-1]]

                for index in destino:
                    if type(index)==NOT:
                        index.inputs.inputs[0]=int(repr(origen))
                        index.outputs()
                    else:
                        index.inputs.inputs.append(int(repr(origen)))
                        index.outputs()
                    assert index.check()
            elif isinstance(destino,Gates):
                self.conect(origen,[destino])
        elif Index>=0 and isinstance(destino,Gates):
            assert check_gates(destino)
            assert check_gates(origen)
            assert Index<=len(destino.inputs)
            k=list(self.conection.keys())
            for index in k:
                for i in range(len(self.conection[index])):
                    if self.conection[index][i][0]==destino and self.conection[index][i][1]==Index-1:
                        del (self.conection[index])
            try:
                self.conection[origen].append([destino,Index-1])
            except KeyError:
                self.conection[origen]=[[destino,Index-1]]
            destino.inputs.inputs[Index - 1] = int(repr(origen.output))
            destino.outputs()
        self.output()
    def __str__(self):
        return self.show_gates_conected()
    def show_gates_conected(self):
        ret={}
        for index in self.conection.keys():

            for index2 in self.conection[index]:
                try:
                    ret[str(index)].append([str(index2[0]), index2[1]])
                except KeyError:
                    ret[str(index)]=[[str(index2[0]), index2[1]]]
        return ret
    def output(self):
        ret=[]
        for i in self.gates:
            if i not in self.conection.keys():
                ret.append(i)
        self.outputs=ret
        return ret
    def conect_inp(self,inp,gate,entrada=-1):
        assert check_gates(gate)
        assert isinstance(inp,Bin_Inp.Bin_Inputs)
        if entrada==-1:
            gate.inputs=gate.inputs+inp.logical_input
        else:
            gate.inputs.inputs[entrada-1]=inp.logical_input
        gate.outputs()

    def copy(self,gates,entrada):
        circuito=Circuit(gates,entrada)
        for index in list(self.conection.keys()):
            for index2 in self.conection[index]:
                circuito.conect(index,index2[0], index2[1] + 1)
                print(circuito.conection,"\n",self.conection)
        print("out",circuito.outputs)
def main():
    And=AND()
    Or=OR()
    Not=NOT()
    entrada1=Bin_Inputs(1)
    entrada2=Bin_Inputs(1)
    entrada3=Bin_Inputs(0)
    entrada4=Bin_Inputs(0)
    circuito=Circuit([And],[entrada1,entrada2])
    circuito.conect(entrada1,{And:1})
    circuito.conect(entrada2,{And:2})
    circuito.copy(circuito.gates,[entrada3,entrada4])
    print(circuito.outputs)
if __name__=="__main__":
    main()