class testAccess():
    def __init__(self, value):
        self.data = value
    @property
    def data(self):
        return self.data
    @data.setter
    def data(self, another):
        self.data = another
if __name__=="__main__":
    test = testAccess(5)
