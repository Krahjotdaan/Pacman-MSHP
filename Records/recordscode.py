class Records():
    def __init__(self, name = "User", score = 0):
        self.n = name
        self.s = score
        self.data = dict()

    def read(self):
        self.f = open("C:\\Users\\Student\\not_tyubik\\Records\\recordsdata", "r")
        for line in self.f:
            x, y = line.split()
            self.data[x] = y

    def sort(self):
        self.sorted_tuple = sorted(self.data.items(), key=lambda x: x[1])

    def write(self):
        f = open("C:\\Users\\Student\\not_tyubik\\Records\\recordsdata", "w")
        for t in self.sorted_tuple:
            line = ' '.join(str(x) for x in t)
            f.write(line + '\n')
        f.close()

c = Records()
c.read()
c.sort()
c.write()

