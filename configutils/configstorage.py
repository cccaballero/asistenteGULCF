
class ConfigStorage(dict):

    def __getattr__(self, name):
        """
        Return mapped attributes from dict keys values
        :rtype: object
        """
        if name in self:
            return self[name]
        else:
            return None

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)