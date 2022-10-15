import numpy as np
import Image as im
import datascience as ds
from Worth_packs import array_to_csv

mother_table = np.array([])

while True:
    add_table_string = input("What is the name of the table you would like to append: ")
    if add_table_string == "Done":
        break
    add_table = np.genfromtxt(add_table_string, delimiter = ",", dtype = 'str_')
    mother_table = np.append(mother_table, add_table)



