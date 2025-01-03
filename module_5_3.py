import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self,speed):
        self._cords = [0, 0, 0]
        self.speed = int(speed)

    def move(self, dx, dy, dz):
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed

        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] = new_x
            self._cords[1] = new_y
            self._cords[2] = new_z

    def get_cords(self):
        x, y, z = self._cords
        print(f'X: {x}, Y: {y}, Z: {z}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1,4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):  # написано так, как я понял из ТЗ
        dz = abs(dz)
        new_z = self._cords[2] - dz
        if new_z >= 0:
            self._cords[2] = new_z
            self.speed /= 2
        else:
            print("It's too deep, i can't dive :(, no changes made")

    def dive_in0(self, dz): # как будто это требуется от задания, потому что как еще добиться 0 я не знаю))
        self.speed /= 2
        dz = abs(dz) * self.speed
        new_z = self._cords[2] - dz
        if new_z >= 0:
            self._cords[2] = int(new_z)
        else:
            print("It's too deep, i can't dive :(, no changes made")


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    def __init__(self, speed):
        super().__init__(speed)

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)


db = Duckbill(10)

print(db.live)
print(db.beak)
db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()

db.dive_in0(6)
db.get_cords()

db.lay_eggs()

