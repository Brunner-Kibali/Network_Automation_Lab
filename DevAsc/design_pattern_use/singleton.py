class ConfigValues:
    __instance = None

    @staticmethod
    def getInstance():
        if ConfigValues.__instance is None:
            ConfigValues()
        return ConfigValues.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if ConfigValues.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ConfigValues.__instance = self


s = ConfigValues.getInstance()
print(s)

s = ConfigValues.getInstance()
print(s)

s = ConfigValues()
print(s)
