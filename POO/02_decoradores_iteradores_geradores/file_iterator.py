class FileIterator:
    def __init__(self, filename):
        self.file = open(filename)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.file.readline()
        if line != '':
            return line
        else:
            self.file.close()
            raise StopIteration
        
for line in FileIterator('large.txt'):
    print(line)