import animales

from animales import tiburon, serpiente, paloma, leon
#menu
#while
#decisiones
#dibujos
#clase

menu = {
   
   '1': '1. tiburon,',
   '2': '2. serpientes',
   '3': '3. paloma',
   '4': '4. leon',
   '0': '0. exit'

}
   

class Animal():
   def __init__(self):
      self.type = type
      pass
   
   def mostrar_animal(self):
      
      animal_art = getattr(animales, self.type)
      return animal_art
      pass


# ejecucion principal

if __name__ == '__main__':
   for option in menu:
      print(menu.get(option))
       
   while True:
      user_input = input('ingresa una opcion: ')
      if user_input == '0':
         print("salir")
         break
      elif user_input in menu:
         menu_value = menu.get(user_input)
         print(menu_value.split(' '))
         #animal =Animal()
         print("mostrar", animales.menu)
         pass
      else:
         print("invalido")
  
  
  
  