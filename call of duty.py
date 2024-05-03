class Weapon:
    def __init__(self, name, price, damage, fire_rate, accuracy, range):
        self.name = name
        self.price = price
        self.damage = damage
        self.fire_rate = fire_rate
        self.accuracy = accuracy
        self.range = range

    def compare(self, other_weapon):
        comparison = {}
        if self.damage > other_weapon.damage:
            comparison['damage'] = self.name
        else:
            comparison['damage'] = other_weapon.name

        if self.fire_rate > other_weapon.fire_rate:
            comparison['fire_rate'] = self.name
        else:
            comparison['fire_rate'] = other_weapon.name

        if self.accuracy > other_weapon.accuracy:
            comparison['accuracy'] = self.name
        else:
            comparison['accuracy'] = other_weapon.name

        if self.range > other_weapon.range:
            comparison['range'] = self.name
        else:
            comparison['range'] = other_weapon.name

        return comparison


class Holger26(Weapon):
    def __init__(self, name, price, damage, fire_rate, accuracy, range, passenger_capacity):
        super().__init__(name, price, damage, fire_rate, accuracy, range)
        self.passenger_capacity = passenger_capacity


# ورودی‌ها
holger_26 = Holger26("Holger 26", 31, 80, 53, 60, 70, 1)
m13 = Weapon("M13", 25, 42, 91, 77, 61)
m4 = Weapon("M4", 29, 49, 80, 71, 43)

# مقایسه و چاپ برتری‌ها
print("Comparison Results:")
print("Damage: ", holger_26.compare(m13)['damage'])
print("Fire Rate: ", holger_26.compare(m13)['fire_rate'])
print("Accuracy: ", holger_26.compare(m13)['accuracy'])
print("Range: ", holger_26.compare(m13)['range'])
