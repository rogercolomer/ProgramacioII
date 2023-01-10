class Qualitats:
    def __init__(self,f,v,m):
        self.forca= f
        self.velocitat = v
        self.magia = m

    def set_q(self,f,v,m):
        self.forca = f
        self.velocitat = v
        self.magia = m

    def get_q(self):
        return self.forca, self.velocitat, self.magia