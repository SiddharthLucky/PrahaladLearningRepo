class Cookie:
    def __init__(self,colour):
        self.colour = colour
        
    def get_colour(self):
        return self.colour
    
    def set_colour(self,colour):
        self.colour = colour
    
Cookie_one = Cookie('green')
Cookie_two = Cookie('blue')

print('Cookie one is', Cookie_one.get_colour)
print('Cookie two is', Cookie_two.get_colour)

Cookie_one.set_colour('yellow')

print('\nCookie one is now', Cookie_one.get_colour())
print('Cookie two is stil', Cookie_two.get_colour())

    