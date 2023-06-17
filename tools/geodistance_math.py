from math import radians, cos, sin, asin, sqrt

def geodistance(lat1:float, lng1:float, lat2:float, lng2:float):
  '''
  Функция вычисления кратчайшего расстояния от одной точки до другой
  ====================
  @param latitude    -   широта первой точки
  @param longitude   -   долгота первой точки
  @param latitude    -   широта второй точки
  @param longitude   -   долгота второй точки
  '''
  lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)]); # долгота и широта конвертируются в радианы
  dlng = lng2 - lng1; 
  dlat = lat2 - lat1; 
  a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2; 
  distance = 2 * asin(sqrt(a)) * 6371e3; # Средний радиус Земли, 6371 км
  
  return round(distance / 1000, 3); 