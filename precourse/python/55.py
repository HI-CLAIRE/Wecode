class Database:
    def __init__(self, name, size):
      self.name = name
      self.size = size
      self.dictionary = {}

    def insert(self, field, value):
      if self.size > len(self.dictionary):
        self.dictionary[field] = value
      else:
        return

    def select(self, field):
        return self.dictionary.get(field)

    def update(self, field, value):
      if field in self.dictionary:
        self.dictionary[field] = value

    def delete(self, field):
      if field in self.dictionary:
        del self.dictionary[field]
