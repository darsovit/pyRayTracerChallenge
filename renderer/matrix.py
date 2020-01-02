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