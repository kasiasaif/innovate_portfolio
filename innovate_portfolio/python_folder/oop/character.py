class Character():
    def __init__(self, real_name, superhero_name) :
        self.real_name = real_name
        self.superhero_name = superhero_name

    def set_power(self, power):
        self.power = power

    def set_real_name(self, real_name):
        self.real_name = real_name

    def set_superhero_name(self, superhero_name):
        self.superhero_name = superhero_name
        
    def get_power(self):
        print(self.power)

    def get_real_name(self):
        print(self.real_name)

    def get_superhero_name(self):
        print(self.superhero_name)

