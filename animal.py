import animales

from animales import tiburon, serpiente, paloma, leon
#menu
#while
#decisiones
#dibujos
#clase
menu = {
   
   '1': '1. tiburon',
   '2': '2. serpiente',
   '3': '3. paloma',
   '4': '4. leon',
   '0': '0. exit'
}
   
class Animal():
   def __init__(self):
      self.tiburon = tiburon
      self.serpiente = serpiente
      self.paloma = paloma
      self.leon = leon
      pass
   
   def mostrar_animal(self, animal):
      animal_art = getattr(animales, animal)
      return animal_art
      pass

# ejecucion principal

if __name__ == '__main__':
   for option in menu:
      print(menu.get(option))
   animal = Animal()   
   
   
   while True:
      user_input = input('ingresa una opcion: ')
      if user_input == '0':
         print("salir")
         break
      elif user_input in menu:
         menu_value = menu.get(user_input)
         print(menu_value.split(' ')[1])
         #animal =Animal()
         
         print("mostrar", animal.mostrar_animal(menu_value.split(' ')[1]))
         pass
      else:
         print("invalido")
  
  
  
  