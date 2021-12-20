class Bicycle:
    def __init__(self, owner, color, num_gears, current_gear):
        # atributos/propiedades/variables
        self.owner = owner
        self.color = color
        self.num_gears = num_gears
        self.current_gear = current_gear
        # metodos/funciones
    def gear_up(self):
        self.current_gear = self.current_gear+1

if __name__ == '__main__':
    new_bicycle = Bicycle(owner="Kawar", color="blue", num_gears=5, current_gear=2)

    print(type(new_bicycle))
    print(new_bicycle.current_gear)
    new_bicycle.gear_up()
    print(new_bicycle.current_gear)
    print(new_bicycle.color)
    new_bicycle.color = "dark blue"
    print(new_bicycle.color)

    # print(help(Bicycle))