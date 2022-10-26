class items:
    def __init__(self, name, stre, agi, cons):
        self.name = name
        self.stre = stre
        self.agi = agi
        self.cons = cons
        
    def get_attrib(self):
        return self.name, self.stre, self.agi, self.cons
    
    def 