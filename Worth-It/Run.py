
# %%
import matplotlib.pylab as plt
import matplotlib as mpl
import numpy as np
import datascience as ds
import pandas as pd
from Worth_packs import array_to_table
from Worth_packs import table_to_array
from Worth_packs import array_to_csv
from Worth_packs import csv_to_array
# %% 

final_array = np.genfromtxt("Big_Library.csv", delimiter = ",", dtype = 'str_')
Final_Lib = array_to_table(final_array)

i = 0
error_array = np.array([])
swiped_dish = np.array([])
guess_array = np.array([])
while True:
    if i >= Final_Lib.num_rows:
        break
    cont = input("Show Food Item?: ")
    if cont == "No":
        break
    print(np.array(Final_Lib.select(1,2).row(i)))
    approximation = int(input("What do you think is the price of this dish: "))
    guess_array = np.append(guess_array, approximation)
    swiped_dish = np.append(swiped_dish, np.array(Final_Lib.row(i)).item(1))
    exact = int(np.array(Final_Lib.row(i)).item(3))
    error_array = np.append(error_array, ((approximation - exact) / exact))
    i += 1

error_table = ds.Table().with_columns("Menu Item", swiped_dish, "Guessed Price", guess_array, "Error", error_array)
match = table_to_array(Final_Lib.join('Menu Item', error_table).sort("Error", descending = True))
array_to_csv(match, "Matches.csv")

output = Final_Lib.join("Menu Item", error_table)
print(output)



# %%
print(plt.hist(output.column("Error")))
plt.show()
# %%
