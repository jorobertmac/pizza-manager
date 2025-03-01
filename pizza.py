class Pizza:
  def __init__(self):
    self.toppings = []
  
  def add_topping(self, topping):
    if topping in self.toppings:
      return
    self.toppings.append(topping)
  
  def remove_topping(self, topping):
    if topping in self.toppings:
      self.toppings.remove()