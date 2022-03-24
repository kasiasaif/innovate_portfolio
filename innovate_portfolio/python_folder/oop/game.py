from character import Character

spiderman = Character("Peter Parker", "Spiderman")

spiderman.set_power("1000")
spiderman.get_power()
spiderman.get_real_name()
spiderman.get_superhero_name()
spiderman.set_power("10")
spiderman.get_power()
spiderman.set_real_name("Andrew Garfield")
spiderman.get_real_name()
print(spiderman.__dict__)