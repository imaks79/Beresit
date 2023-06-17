import pandas as pd

from tools import wolf_parser
from tools import geodistance_math


def main():

  lng1, lat1 = 55.7522, 37.6156; 
  lng2, lat2 = 44.5888, 33.5224; 
    
  path_length = geodistance_math.geodistance(lng1, lat1, lng2, lat2); 
  print(path_length); 


  filename_wolf = 'coefficient.csv'; 
  try:
    df = pd.read_csv(filename_wolf, index_col = [0]); 
  except:
    wolf_parser.parse()
    df = pd.read_csv(filename_wolf, index_col = [0]); 
  tabular_1 = df.to_dict(); 
  print(tabular_1); 

if __name__ == '__main__':
  main(); 