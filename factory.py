class Developer:
    def training(self):
        pass

    def deliver(self):
        pass


class PhpDeveloper(Developer):
    def training(self):
        print('train Php')

    def deliver(self):
        print('deliver Php')


class PythonDeveloper(Developer):
    def training(self):
        print('train Python')

    def deliver(self):
        print('deliver Python')


class DevelopersFactory:

    def _create_developer(self, type):
        if type == 'Php':
            return PhpDeveloper()
        if type == 'Python':
            return PythonDeveloper()

    def produce_developer(self, type):
        developer = self._create_developer(type)

        developer.training()
        developer.deliver()
        return developer
