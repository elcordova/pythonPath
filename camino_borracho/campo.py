class Campo:
  def __init__(self):
    self.coordenadas_de_borracho = {}
  
  def anadir_borracho(self, borracho, coordenada):
    self.coordenadas_de_borracho[borracho] = coordenada

  def mover_borracho(self,borracho):
    delta_x, delta_y = borracho.camina()
    coordenada_actual = self.coordenadas_de_borracho[borracho]
    nueva_coodenada = coordenada_actual.mover(delta_x, delta_y)

    self.coordenadas_de_borracho[borracho] = nueva_coodenada

  def obtener_coordenada(self, borracho):
    return self.coordenadas_de_borracho[borracho]