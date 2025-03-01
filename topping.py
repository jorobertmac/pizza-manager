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