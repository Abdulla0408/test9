# 5-DARS VAZIFALAR
# 1 - VAZIFA

class Car:
    def __init__(self, model: str, color: str, speed: int, price: int):
        self._model = model 
        self._color = color 
        self._speed = speed
        self._price = price 
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, new_model):
        self._model = new_model
    
    @model.deleter
    def model(self):
        del self._model
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new_color):
        self._color = new_color
    
    @color.deleter
    def color(self):
        del self._color
    
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_speed):
        self._speed = new_speed
    
    @speed.deleter
    def speed(self):
        del self._speed
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = new_price
    
    @price.deleter
    def price(self):
        del self._price
# Avtomobil yaratamiz
a = Car("Toyota", "qora", 180, 20000)

print(a.model)

a.color = "oq"

print(a.color)

del a.price

print(a.price)


# -----------------------------------------------------------------------------

# 2-VAZIFA

# class Figure:
#     @staticmethod
#     def triangle_perimeter(a, b, c):
#         return a + b + c
    
#     @staticmethod
#     def triangle_area(a, b, c):
#         p = Figure.triangle_perimeter(a, b, c) / 2
#         return (p * (p - a) * (p - b) * (p - c)) ** 0.5 

#     @staticmethod
#     def rectangle_perimeter(a, b):
#         return 2 * (a + b)
    
#     @staticmethod
#     def rectangle_area(a, b):
#         return a * b 
    
# print(Figure.triangle_perimeter(3, 4, 5))

# print(Figure.triangle_area(3, 4, 5))

# print(Figure.rectangle_perimeter(6, 8))

# print(Figure.rectangle_area(6, 8))

# -----------------------------------------------------------------------------

# class Animal:
#     def __init__(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)
    
#     def get_attr(self, attr):
#         return getattr(self, attr)
    
#     def has_attr(self, attr):
#         return hasattr(self, attr)
    
#     def del_attr(self, attr):
#         delattr(self, attr)

# a = Animal(name="Tom", type="mushuk", color="sariq")

# print(a.get_attr("name"))

# print(a.has_attr("type"))

# a.del_attr("color")

# print(a.get_attr("color"))
