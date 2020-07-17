class item():
  def __init__(self, name, description):
    self.name = name
    self.description = description
  def __repr__(self): #ffs
    return self.name + " - " + self.description