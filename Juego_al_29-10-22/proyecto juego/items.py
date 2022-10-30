class Items:
    def __init__(self, name, strength, agi, con, cons):
        self.name = name
        self.strength = strength
        self.agi = agi
        self.con = con
        self.cons = cons

    def get_attrib(self):
        return self.name, self.strength, self.agi, self.con, self.cons
