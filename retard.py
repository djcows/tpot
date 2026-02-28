
# bryan 27-Feb-2026
RETARD = "This is so funny, it is retarded."
for _ in range(pow(len(RETARD), len(RETARD))):
    print(RETARD)
# bryan 27-Feb-2026

# djcows 19-sept-2024
def make_retards(n):
  retards = []
  for i in range(n):
    retards.append('retard')

  return retards
# djcows 19-sept-2024

# sidpatchy 2024-09-20
def djcows_doesnt_know_how_to_python(n): return ['retard'] * n

def djcows_doesnt_know_how_to_python_but_worse(n): return ['retard' for _ in range(n)]
# sidpatchy 2024-09-20

# Judah-Faison 2025-9-18
import os

from ursina import Default, camera
os.system("python import ursina")
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController as fpc

app = Ursina()
smart_dude=fpc()
class Ground(Button):
      def __init__(self, position = (0,0,0), color = color.white):
         super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            color = color,
            scale = 0.5
            
            )

Ground()

Sky()
app.run()
# Judah-Faison 2025-9-18
