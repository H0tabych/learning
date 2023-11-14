import pickle
import json

my_favorite_group = {
                    'name': 'Г.М.О.',
                    'tracks': ['Последний месяц осени', 'Шапито'],
                    'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
                               {'name': 'Шапито', 'year': 2014}],
                    }

print(pickle.dumps(my_favorite_group))
print(json.dumps(my_favorite_group))

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favorite_group, f)

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favorite_group, f)
