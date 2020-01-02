#! python
#
# Matrix class data

class Row:
    def __init__(self,data):
        self.data = data
    def Size(self):
        return len(self.data)
    def __getitem__(self,column):
        return self.data[column]
    def __eq__(self,rhs):
        if len(self.data) != len(rhs.data):
            return False
        for i in range(len(self.data)):
            if self[i] != rhs[i]:
                return False
        return True

class Matrix:
    def __init__(self,x,y,data):
        self.data = []
        for row in data:
            self.data += [ Row(row) ]
        assert len(self.data) == y, 'Expected num rows {} not equal to num rows {}'.format(y,len(self.data))
        for row in self.data:
            assert row.Size() == x, 'Expected size of row {} is not equal to size of row {}'.format(x,row.Size())
    
    def __getitem__(self,pos):
        return self.data[pos[0]][pos[1]]
        
    def __eq__(self,rhs):
        if len(rhs.data) != len(self.data):
            return False
        for i in range(len(self.data)):
            if self.data[i] != rhs.data[i]:
                return False
        return True