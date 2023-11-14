import pickle
import json

with open('group.pickle', 'rb') as f:
    my_friend_favorite_group_pickle = pickle.load(f)

print(type(my_friend_favorite_group_pickle),
      my_friend_favorite_group_pickle)

with open('group.json', 'r', encoding='utf-8') as f:
    my_friend_favorite_group_json = json.load(f)

print(type(my_friend_favorite_group_json),
      my_friend_favorite_group_json)
