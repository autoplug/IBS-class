class Test:
    var1 = "ppp"

    def get_var1(self, var1):
        self.var1 = var1
        print(var1)
        print(self.var1)

    def set_var1(self):
        pass


v = Test()
v.get_var1("llll")


print(v.var1)

s = v.get_var1
