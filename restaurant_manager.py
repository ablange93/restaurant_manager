### CLASSES ###
class Menu():
  # CONSTRUCTOR #
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  # STRING REP. should print menu's name and open/close time. #
  def __repr__(self):
    return "The {name} menu is available from {start_time} to {end_time}.".format(name=self.name,start_time=self.start_time,end_time=self.end_time)
  # METHOD to calculate total cost of items purchased from a menu) #
  def calculate_bill(self, purchased_items):
    bill = 0
    for item in purchased_items:
      if item in self.items:
        bill += self.items[item]
    return bill

class Franchise():
  # CONSTRUCTOR #
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  # STRING REP. should print franchise's address. #
  def __repr__(self):
    return "{address}".format(address=self.address)
  #ITERATOR to enable looping through menu class attributes. #
  def __iter__(self):
    return iter(self.menus)
  # METHOD to show what menus are availible at a certain time (military time - rounded to the hour as input). #
  def available_menus(self, time):
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        print(menu.name)

class Business():
  # CONSTRUCTOR #
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  # STRING REP. to show Business name and franchises. #
  def __repr__(self):
    return "BUSINESS: {name}, FRANCHISES LOCATED AT:{franchises}".format(name=self.name,franchises=self.franchises)
  
### INSTANTIATE OBJECTS ###
# MENUS #
brunch = Menu("brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)

early_bird = Menu("early bird dinner", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 15, 18)

dinner = Menu("dinner", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)
                 
kids = Menu("kids", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 11, 21)

arepas_menu = Menu("arepas", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 20)
                 
# FRANCHISES #
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# BUSINESSES #
fakeBusiness_Arepas = Business("Take a' Arepa", [arepas_place])
fakeBusiness_Bens = Business("Benjamins's Business", [flagship_store, new_installment])

### MAIN ###  
# Return bill for 2x items. #
#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

# Return bill for 2x items. #
#print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Return menus availible at 5PM. #
#flagship_store.available_menus(17)

#Show businesses and related franchises. #
print(fakeBusiness_Arepas)

print(fakeBusiness_Bens)
