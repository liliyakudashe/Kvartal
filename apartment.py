import human
import houses


class Apartment:

    houses.House

    def __init__(self, num_ap, ):
        self._num_ap = num_ap
        self._owner = human.Human
        self._owners = houses.House

    def __str__(self):
        return f'{self._num_ap} квартира'

