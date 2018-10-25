
class Singleton:

    def __init__(self, my_class):
        self.my_class = my_class
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.my_class(*args, **kwargs)
        return self.instance
