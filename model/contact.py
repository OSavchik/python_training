from sys import maxsize

class Contact:


    def __init__(self, first_name=None, middle_name=None, last_name=None, nick_name=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
