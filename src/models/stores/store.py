__author__ = "Prajesh Ananthan"

class Store(object):
    def __init__(self, name, url_prefix):
        self.name = name
        self.url_prefix = url_prefix

    def __repr__(self) -> str:
        return "<Store {}>".format(self.name)


