# OOP Concepts -> Classes and Objects
# 1. Abstraction
# 2. Inheritance
# 3. Encapsulation
# 4. Polymorphism

# Class -> Car
# Class is nothing but a prototype.

# Car
#     |- 4 wheels
#     |- Color
#     |- Material
#     |- Body
#     |- Engine
#     |- Windows
#     |- Doors
#     |- CanRun
#     |- CanStop

# Class is a prototype in which all the attributes and Funtionalities are defined. Any number of objects can be created from a class.

class Car:
    color: str
    wheels: int
    material: str
    engine: str
    windows: int
    door: int
    engine_status: str
    lights_status: str
    ac_status: str
    headlamp_status: str
    steering_status: str
    
    def __init__(self,color, wheels, material, engine, windows, door):
        self.color = color
        self.wheels = wheels
        self.material = material
        self.engine = engine
        self.windows = windows
        self.door = door
        
    def run(self):
        self.engine_status = 'running'
        self.lights_status = 'oon'
        self.ac_status = 'on'
        self.headlamp_status = 'on'
        self.steering_status = 'unlocked'
        print('Engine Started')
    
    def __kill_the_engine(self):
        self.engine_status = 'stopped'
        self.lights_status = 'off'
        self.ac_status = 'off'
        self.headlamp_status = 'off'
        self.steering_status = 'locked'
    
    def stop(self):
        print('Engine Stopped')
        self.__kill_the_engine()



seltos = Car('White',4,'Metal','1400cc',4,4)

seltos.run()
print(seltos.engine_status)
seltos.stop()
print(seltos.engine_status)