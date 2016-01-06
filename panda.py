class Panda:
    def __init__(self, name, email, gender):
        self.__name = name
        self.__email = email
        self.__gender = gender

    def email(self):
        return self.__email

    def name(self):
        return self.__name

    def gender(self):
        return self.__gender

    def __str__(self):
        return '{} {} {}'.format(self.__name, self.__email, self.__gender)

    def __repr__(self):
        return 'Panda(name: {}, email: {}, gender: {})'\
            .format(self.__name, self.__email, self.__gender)

    def __eq__(self, other_panda):
        return '{} {} {}'.format(self.__name, self.__email, self.__gender) == '{} {} {}'\
                         .format(other_panda.name(), other_panda.email(),
                                 other_panda.gender())

    def __hash__(self):
        return hash(self.__str__())
