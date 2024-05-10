class Ork:
    def __init__(self, level: int) -> None:
        self.level = level
        self.healthpoints = 100 * level
        self.attack_power = 100 * level


    def attack(self):
        print(f"Ork attacks with {self.attack_power} power")


    def __str__(self):
        return f"Ork (level: {self.level} hp: {self.healthpoints})"


ork = Ork(level=2)


if __name__ == '__main__':
#    print(ork.attack_power)
#    ork.attack()
    print(ork)