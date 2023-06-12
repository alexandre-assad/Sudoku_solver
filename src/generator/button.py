

class Button:
    def __init__(self,x:int,y:int,image,func):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft= (x,y)
        self.clicked = False
        self.func = func