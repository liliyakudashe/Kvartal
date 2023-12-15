import apartment


class House:

    apartments = []

    def __init__(self, num_house, floors, _apartments= apartments):
        self._entrances = 1
        self._floors = floors
        self._num_house = num_house
        self._apartments = apartment.Apartment

    def __str__(self):
        return (f'Количество этажей {self._floors}, '
                f'Номер дома {self._num_house}, {self._apartments}')






