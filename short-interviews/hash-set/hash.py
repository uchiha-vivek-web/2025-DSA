

class HashSet:
    def __init__(self,size=100):
        self.size=size
        # creating buckets
        self.table = [[] for _ in range(size)]

    def _hash(self,key):
        return hash(key)%self.size
    
    def add(self,key):
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def remove(self,key):
        index = self._hash(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def contains(self,key):
        index = self._hash(key)
        return key in self.table[index]
    def __str__(self):
        return str([bucket for bucket in self.table if bucket]) 
    

if __name__=="__main__":
    hs = HashSet()
    hs.add(10)
    hs.add(20)
    hs.add(10)
    print(hs.contains(30))
    # hs.remove(20)
    print(hs)