__author__ = "Prajesh Ananthan"


class Alert(object):
    def __init__(self, user, item, price_limit):
        self.user = user
        self.price_limit = price_limit
        self.item = item

    def __repr__(self):
        return "<Alert for {} on item with price {}>".format(self.user.email, self.item.name, self.price_limit)
