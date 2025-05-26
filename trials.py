class Trial:
    MAX_COUNTER = 3

    def __init__(self, name):
        self.name = name

    def __call__(self):
        if self.MAX_COUNTER > 0:
            print(self.MAX_COUNTER)
        else:
            print("Over your call limit!!!")
        
        self.MAX_COUNTER -= 1

trial = Trial("function 1")

trial()
trial()
trial()
trial()
trial()