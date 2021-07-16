import os.path
import pickle
from pprint import pprint

from husteblume.api import Stations, Forecast
from husteblume.user import AgeGroup, User, Gender

if __name__ == '__main__':
    s = Stations.fetch()
    pprint(s)

    station_for_hannover = s.from_name('Hannover')
    pprint(station_for_hannover)

    u = None

    if os.path.lexists('user.pickle'):
        with open('user.pickle', 'rb') as f:
            u = pickle.load(f)
    else:
        u = User.register(AgeGroup.TWENTY_ONE_TO_FORTY, birth_month=12, gender=Gender.FEMALE)
        with open('user.pickle', 'wb') as f:
            pickle.dump(u, f)

    pprint(u)

    f = Forecast.get(station_for_hannover, user=u)
    pprint(f)
    pprint(f.json)
