from collections import deque
import json
from panda import Panda
from social_network import SocialNetwork


def main():
    mecho = Panda('mecho', 'panda@panda.com', 'male')
    kiki = Panda('kiki', 'kiki@panda.com', 'female')
    mecho2 = Panda('mecho2', 'panda@panda.com', 'male')
    ciki = Panda('Ciki', 'ciki@mail.com', 'female')
    ruci = Panda('ruci', 'ruci@mail.com', 'male')
    koki = Panda('koki', 'koki@mail.com', 'male')

    nw = SocialNetwork()

    nw.add_panda(mecho)
    nw.add_panda(mecho2)
    nw.add_panda(ciki)
    nw.add_panda(ruci)
    nw.add_panda(koki)
    nw.add_panda(mecho2)

    nw.make_friends(kiki, ciki)
    nw.make_friends(ciki, ruci)
    nw.make_friends(ruci, koki)
    nw.make_friends(mecho, kiki)
    nw.make_friends(koki, mecho)
    nw.make_friends(kiki, ciki)

    print(nw.how_many_gender_in_network(2, mecho, 'male'))
    print(SocialNetwork.count_social_network_members)
    nw.save()

if __name__ == '__main__':
    main()