import Gates
import Bin_Inp
def check(entrada):
    bin=(0,1,True,False)
    if type(entrada)==bool:
        return True
    if type(entrada)==int:
        if entrada in bin:
            return True
        else:
            return False
    elif isinstance(entrada,Gates.Gates):
        return True
    elif type(entrada)==list:
        for index in entrada:
            if index not in bin and not isinstance(index,(Gates.Gates,Bin_Inp.Bin_Inputs)):
                return False
        return True
    elif type(entrada)==Inputs:
        return check(entrada.inputs)
class Inputs(list):
    def __init__(self,inp):
        assert check(inp)
        if type(inp)==int:
            self.inputs = [inp]
        else:
            self.inputs=inp
    def __add__(self,inp):
        assert check(inp)
        if type(inp)==int:
            self.inputs.append(inp)
            return self
        elif type(inp)==list:
            self.inputs+=inp
            return self
        elif type(inp)==Inputs:
            return self+inp.inputs
        elif isinstance(inp,Gates.Gates):
            self.inputs.append(inp)
            return self
    def __str__(self):
        ret=""
        for index in self.inputs:
            if index ==True:
                ret+="1  "
                continue
            elif index==False:
                ret+="0  "
                continue
            #elif isinstance(index,Gates.Gates):
            #    ret+=str(index.__repr__("id"))+'   '
            #    continue
            else:
                ret+=repr(index)+'  '
        return ret
    def __len__(self):
        return len(self.inputs)
    def __getitem__(self, item):
        assert type(item)==int
        return self.inputs[item]
    def __repr__(self):
        return str(self.inputs)
    def destroy(self,item=-1):
        del(self.inputs[item])
    def check(self):
        return check(self.inputs)
def main():
    gateand=Gates.AND([0,0])
    print(gateand)
    in1=Inputs([0,1,False,gateand])
    print(in1)
if __name__=="__main__":
    main()
