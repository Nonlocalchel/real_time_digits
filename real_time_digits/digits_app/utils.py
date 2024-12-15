import json
from random import randint


def generate_json_digit():
    random_number = randint(1, 1000)
    message_dict = {'number': random_number}
    return json.dumps(message_dict)
