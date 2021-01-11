global world
world = ["********************",
         "*                  *",
         "*  ***   **   ***  *",
         "*                  *",
         "*    **      **    *",
         "*    **      **    *",
         "*                  *",
         "*  ***   **   ***  *",
         "*                  *",
         "********************"]

class Stage:
    def __init__(self, level):
        self.level = level


    # Co-ordinate system is messed up because I cba to fix it, starts at the top left corner, not bottom left
    def getPos(self, x, y):
        return self.level[y-1][x-1]


    def changePos(self, char, x, y):
        self.line = self.level[y-1]
        self.line = self.line[:x-1] + char + self.line[x+1:]
        self.level[y-1] = self.line

    def printStage(self):
        for line in self.level:
            print(line)

level = Stage(world)
# print(level.level)
# level.printStage()
# print(level.getPos(1,10))
# level.changePos("A", 1, 1)

