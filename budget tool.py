class Apples:
  def __init__(self, name, price):
    self.name = name
    self.price = float(price)

  def budgetCheck(self, budget):
    if not isinstance(budget, int, float)):
      print("Invalid entry. Please enter a number.")
      exit()

  def changeAmount(self, budget):
    return(budget - self.budgetCheck)

  def buy(self, budget):
    self.budgetCheck(budget)
    
    if budget >= self.price:
      print(f'You can get some apples. {self.name}')
      
      if budget == self.price:
        print("You have exactly enough money for these apples.")
        
      else: 
        print(f'You can have these apples and you will have ${self.change(budget)} left over')
    
    
