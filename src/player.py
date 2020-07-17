# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
  def __init__(self, name):
    self.name = name
    self.items = []
    self.location = None
  def take(self, itemName):
    itemList = [item for item in self.location.items if item.name == itemName]
    if len(itemList) > 0:
      item = itemList[0]
      self.items.append(item)
      self.location.items.remove(item)
    else:
      print('No item by that name')
  def drop(self, itemName):
    itemList = [item for item in self.items if item.name == itemName]
    if len(itemList) > 0:
      item = itemList[0]
      self.items.remove(item)
      self.location.items.append(item)
    else:
      print('No item by that name')