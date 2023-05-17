class Block:
    def __init__(self, x, y, gameMap):
        self.x = x
        self.y = y
        self.gameMap = gameMap

    def move(self, x, y, caller=False):
        try:
            if self.gameMap[self.x + x][self.y + y]:
                self.gameMap[self.x + x][self.y + y].move(x, y, caller=self)
            self.gameMap[self.x][self.y] = 0
            self.x += x
            self.y += y
            self.gameMap[self.x][self.y] = self
        except:
            pass