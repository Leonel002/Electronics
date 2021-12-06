from Circuit import Circuit
from Gates import *
from Bin_Inp import *

class Truth_Table(Circuit):
    def binare(self,obj):
        assert type(obj) == int
        ret = []
        cont=self.n
        cont=0
        while obj > 0 or cont<self.n:
            ret.append(obj % 2)
            obj = obj // 2
            cont+=1
        ret.reverse()
        return ret
    def __str__(self):
        ret=""
        may=[]
        for i in self.inputs.inputs:
            ret+=str(i)+"       "
            may.append(len(str(i)))
        may=max(may)
        ret+="\n"
        for index in self.table:
            for index2 in index:
                ret+=str(index2)+(" "*(may+7))
            ret+="\n"
        return ret
    def make_Truth_Table(self):
        self.n=len(self.inputs)
        self.table=[]
        self.out=[]
        for index in range(2**self.n):
            self.table.append(self.binare(index))
        for index in self.table:
            self.out.append(self.outputs)
And=AND()
entrada=Bin_Inputs(0)
entrada2=Bin_Inputs(0)
entrada3=Bin_Inputs(1)
entrada4=Bin_Inputs(1)
Table=Truth_Table([And],[entrada,entrada2])
Table.conect(entrada3,{And:2})
Table.conect(entrada4,{And:1})
print(Table.outputs)
Table=Truth_Table([And],[1,1])
Table.conect(entrada3,{And:2})
Table.conect(entrada4,{And:1})
print(Table.outputs)
Table.make_Truth_Table()
Table.copy(Table.gates,[1,1])
#print(Table)