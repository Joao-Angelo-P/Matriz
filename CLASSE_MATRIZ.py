class Matriz:
    
    def __init__(self, *vs):
        self.vs = list(vs)
        self.T = 0
        self.Mc, self.l_suporte, self.ls2 = [], [], []
        self.c, self.d, self.e = 0, 0, 0
    
    def fromlist(cls, vs):
        if not isinstance(vs, list):
            raise TypeError
        inst = cls()
        inst.vs = vs
        return inst

    def __repr__(self):
        args = ', '.join(repr(x) for x in self.vs)
        return 'Matrix({})'.format(args)
    
    def __len__(self):
        return len(self.vs)

    def __add__(self, other):
        # Metodo Adição
        self.ls2 = []
        for i in range(len(self.vs)): 
            for j in range(len(self.vs[0])):
                self.c += self.vs[i][j] + other.vs[i][j]
                self.l_suporte.append(self.c)
                self.c = 0
            self.ls2.append(tuple(self.l_suporte))
            self.l_suporte = []
            
        return self.ls2
    
    def __sub__(self, other):
        # Metodo Subtração
        self.ls2 = []
        for i in range(len(self.vs)): 
            for j in range(len(self.vs[0])):
                self.c += self.vs[i][j] - other.vs[i][j]
                self.l_suporte.append(self.c)
                self.c = 0
            self.ls2.append(tuple(self.l_suporte))
            self.l_suporte = []
            
        return self.ls2

    def __mul__(self, other):
        # Metodo Multiplicação
        for i in range(len(self.vs)): 
            for j in range(len(self.vs)):         
                for k in range(len(other.vs)): 
                    self.c += self.vs[i][k] * other.vs[k][j]     
                self.l_suporte.append(self.c)
                self.c = 0
            self.Mc.append(tuple(self.l_suporte))
            self.l_suporte = []
        return self.Mc

    def t(self):
        self.l_suporte = []
        for i in range(len(self.vs)):
            self.l_suporte.append([row[i] for row in self.vs])
        self.T = self.l_suporte
        return self.l_suporte

    def det(self):
        '''
        self.c, self.d, self.e = 1, 1, 1
        for i in range(len(self.vs)):
            for j in range(len(self.vs[0])):
                self.c *= self.vs[i][i]
            self.d = self.vs[i][-j] * self.vs[i][j]
            self.e = self.c - self.d
            
        self.c, self.d = 0, 0
        return self.e
        '''
        matriz_det = self.vs + self.vs[:len(self.vs)][:len(self.vs)-1]
        for i in range(len(self.vs)):
            for j in range(len(self.vs)):
                det_p *= matriz_det[j][j + 1]
                pass
    
    
m1 = Matriz([1, 2], [5, 0])
m2 = Matriz([3, -1], [0, 8])



