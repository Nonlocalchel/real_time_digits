import json
from random import randint


def generate_json_digits():
    random_number = randint(1, 1000)
    message_dict = {'message': random_number}
    return json.dumps(message_dict)
