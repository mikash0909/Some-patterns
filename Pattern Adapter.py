class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        l = []
        o = []
        self.grid = grid
        self.adaptee.set_dim((len(self.grid[0]), len(self.grid)))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    #self.adaptee.grid[i][j]=1
                    l.append((j, i))
                if self.grid[i][j] == -1:
                    #self.adaptee.grid[i][j]=-1
                    o.append((j, i))
        self.adaptee.set_lights(l)
        self.adaptee.set_obstacles(o)

        return self.adaptee.generate_lights()