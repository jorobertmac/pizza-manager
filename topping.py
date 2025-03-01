class ToppingList:
  def __init__(self):
    self.list: list = []

  def show(self):
    return self.list.sort()
  
  def add(self, topping: str):
    topping = topping.strip().lower()
    if topping in self.list:
      return
    self.list.append(topping)
  
  def remove(self, topping: str):
    topping = topping.strip().lower()
    if topping in self.list:
      self.list.remove(topping)

  def update(self, old_topping: str, new_topping: str):
    old_topping = old_topping.strip().lower()
    new_topping = new_topping.strip().lower()
    if old_topping not in self.list or new_topping in self.list:
      return
    index = self.list.index(old_topping)
    self.list[index] = new_topping