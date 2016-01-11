from collections import deque
import json
from exceptions import PandaAlreadyThere
from exceptions import PandasAlreadyFriends


class SocialNetwork:
    social_network_members = []
    count_social_network_members = 0

    def __init__(self):
        self.__social_network = self.load()

    def load(self):
        try:
            with open('network.json', 'r') as f:
                return json.load(f)
        except:
            return {}

    def save(self):
        with open('network.json', 'w') as f:
            json.dump(self.__social_network, f, indent=4)

    def add_panda(self, panda):
        if self.has_panda(panda):
            try:
                raise PandaAlreadyThere('Panda is in network')
            except PandaAlreadyThere as p:
                print(p)
        else:
            self.__social_network[panda.email()] = []
            if panda not in SocialNetwork.social_network_members:
                SocialNetwork.social_network_members.append(panda)
                SocialNetwork.count_social_network_members += 1

    def has_panda(self, panda1):
        for panda_mail in self.__social_network:
            if panda1.email() == panda_mail:
                return True
        return False

    def are_friends(self, panda1, panda2):
        try:
            if panda2.email() in self.__social_network[panda1.email()]\
               and panda1.email() in self.__social_network[panda2.email()]:
                return True
        except PandaNotFound:
            print('Panda not in social network.')
        else:
            return False

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        if not self.has_panda(panda1):
            self.add_panda(panda1)
            # print(self.__social_network)
        if not self.are_friends(panda1, panda2):
            self.__social_network[panda1.email()].append(panda2.email())
            self.__social_network[panda2.email()].append(panda1.email())
        else:
            try:
                raise PandasAlreadyFriends
            except PandasAlreadyFriends:
                print('Pandas already friends.')

    def friends_of(self, panda):
        return '\n'.join(str(i) for i in self.__social_network[panda.email()])

    def __bfs(self, start, end):
        visited = set()
        queue = deque()
        queue.append((0, start))
        visited.add(start)

        while len(queue) != 0:
            current_node = queue.popleft()
            node = current_node[1]
            level = current_node[0]

            if node == end:
                return level

            for neighbour in self.__social_network[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((level + 1, neighbour))
        return -1

    def connection_level(self, panda1, panda2):
        if not has_panda(panda1) or not has_panda(panda2):
            return False
        return self.__bfs(panda1, panda2)

    def are_connected(self, panda1, panda2):
        if self.__bfs(panda1, panda2) == -1:
            return False
        return True

    def how_many_gender_in_network(self, level, panda, gender):
        counter = 0
        level_count = 0
        visited = set()
        queue = deque()
        queue.append((0, panda.email()))
        visited.add(panda.email())

        while level_count < level:
            current_node = queue.popleft()
            level_count = current_node[0]
            node = current_node[1]

            for neighbour in self.__social_network[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((level_count + 1, neighbour))
                    print(neighbour)
                    print(SocialNetwork.social_network_members)
                    print(self.__find_member(neighbour))
                    if self.__find_member(neighbour) == gender:
                        counter += 1
        return counter

    def __find_member(self, email):
        for member in SocialNetwork.social_network_members:
            if member.email() == email:
                return member.gender()
