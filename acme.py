
# coding: utf-8

# In[1]:


from numpy import random

class Product(object):
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000,999999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability        

    def stealability(self):
        st = self.price/self.weight
        if st < .5:
            return "Not so stealable..."
        elif st >= .5 and st <1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        ex = self.flammability * self.weight
        if ex < 10:
            return "fizzle..."
        elif ex >= 10 and ex <50:
            return "...boom!"
        else:
            return "...BABOOM!!"
class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000,999999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability        

    def stealability(self):
        st = self.price/self.weight
        if st < .5:
            return "Not so stealable..."
        elif st >= .5 and st <1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
            return "...it's a glove."
        
    def punch(self):
        pu = self.weight
        if pu < 5:
            return "That tickles."
        elif pu >= 5 and pu <15:
            return "Hey that hurt!"
        else:
            return "OUCH!"

