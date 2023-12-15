class Human:

    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def __str__(self):
        return f'{self._name}, {self._age}, {self._gender}'
