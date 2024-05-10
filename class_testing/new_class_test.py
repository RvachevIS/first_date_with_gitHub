class Character:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level


    def attack(self):
        print(f"{self.character_name}"
              f" attacks with {self.attack_power} power")


    def __str__(self) -> str:
        return (f"{self.character_name} (level: {self.level}"
                f" hp: {self.health_points})")


class Ork(Character):
    base_health_points = 100
    base_attack_power = 10
    character_name = "Ork"


class Elf(Character):
    base_health_points = 50
    base_attack_power = 15
    character_name = "Elf"


    def attack(self):
        print("This method is from class-inheritor")

ork1 = Ork(level=1)
elf1 = Elf(level=3)

if __name__ == '__main__':
    ork1.attack()
    print(ork1)
    elf1.attack()
    print(elf1)