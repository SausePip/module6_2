class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.model = __model
        self.owner = owner
        self.engine_power = __engine_power
        self.color = __color

    def get_model(self):
        return f'Model: {self.model}'

    def get_horsepower(self):
        return f'H/p: {self.engine_power}'

    def get_color(self):
        return f'Color: {self.color}'

    def print_info(self):
        model_info = self.get_model()
        horsepower_info = self.get_horsepower()
        color_info = self.get_color()
        print(model_info)
        print(horsepower_info)
        print(color_info)
        print(f'Owner: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self.__class__.__COLOR_VARIANTS]:
            self.color = new_color
            print(f"Color changed to {new_color}")
        else:
            print(f"Can't change the color to {new_color}")

    def set_owner(self, new_owner):
        self.owner = new_owner
        print(f'Owner changed to {new_owner}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()