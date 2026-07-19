import random

class StringGenerator:
    __slots__ = () ## doesn't have any attributes and doesn't need any!
    @staticmethod
    def generate_random_string(length: int = 10) -> str:
        characters = '0123456789abcdefghijklmnopqrstuvwxyz'
        return 'fifa_' + ''.join(random.choice(characters) for _ in range(length))
