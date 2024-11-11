class ListModifier:
    def __init__(self, l ):
        self.l = l

    def integers(self):
        int_ = []
        for i in self.l:
            if isinstance(i,int):
                int_.append(i)
        return int_

    def floats(self):
        float_ = []
        for i in self.l:
            if isinstance(i,float):
                float_.append(i)
        return float_

    def strings(self):
        strings_ = []
        for i in self.l:
            if isinstance(i,str):
                strings_.append(i)
        return strings_

