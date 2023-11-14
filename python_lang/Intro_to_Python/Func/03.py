from random import randint


def battle(dmg, hlt, arm):
    def n_dmg(d, a):
        return d/a

    return hlt - n_dmg(dmg, arm)


user_name: tuple = (input('Введите имя атакующего игрока: '),
                    input('Введите имя защищающегося игрока: '))
health: list = [100, 100]
armor: tuple = (randint(100, 200)/100, randint(100, 200)/100)
damage: tuple[float, float] = (randint(0, 100), randint(0, 100))
player: dict = {'name': user_name[0], 'health': health[0], 'damage': damage[0], 'armor': armor[0]}
enemy: dict = {'name': user_name[1], 'health': health[1], 'damage': damage[1], 'armor': armor[1]}

print(player['damage'], enemy['health'], battle(player['damage'], enemy['health'], enemy['armor']))
