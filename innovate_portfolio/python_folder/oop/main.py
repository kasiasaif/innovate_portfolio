from person import Person

liam = Person("Liam","30", "6'7",)
jordan = Person("Jordan",27, "5'7")
liam.set_hair("blond")
jordan.set_hair("black")
print(liam)
print(liam.age)
print(jordan.age)
print(jordan.hair)
print(f"{liam.height}")

jordan.get_hair()
liam.get_hair()
liam.set_hair("pink")
liam.get_hair()
