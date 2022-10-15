import numpy as np
import datascience as ds

def array_to_table(array):
    restaurant_column = np.array([])
    item_column = np.array([])
    pic_column = np.array([])
    cost_column = np.array([])
    for i in np.arange(0, int(len(array)), 4):
        restaurant_column = np.append(restaurant_column, array.item(i))
        item_column = np.append(item_column, array.item(i+1))
        pic_column = np.append(pic_column, array.item(i+2))
        cost_column = np.append(cost_column, array.item(i+3))
    Mother_Table = ds.Table().with_columns("Restaurant", restaurant_column, "Menu Item", item_column, "Pictures", pic_column, "Price", cost_column)
    return Mother_Table

def table_to_array(table):
    conversion = np.array([])
    for i in np.arange(0, table.num_rows, 1):
        conversion = np.append(conversion, np.array(table.row(i)))
    return conversion

def Setup(restaurant):
    sub_lib = np.array([])
    num_rows = 0
    while True:
        menu_item = input("What is the name of your menu item: ")
        if menu_item == "Done":
            break
        num_rows += 1
        item_image = input("Please enter the image file of your item: ")
        item_cost = input("Please enter the cost of the item: ")
        sub_lib = np.append(sub_lib, [restaurant, menu_item, item_image, item_cost])
    sub_lib = np.asarray(sub_lib)
    np.savetxt(f"{restaurant}.csv", sub_lib, delimiter = ",", fmt = '%s')

def array_to_csv(arr, fname):
    np.savetxt(fname, arr, delimiter = ",", fmt = '%s')

def csv_to_array(file):
    array = np.genfromtxt(file, delimiter = ",", dtype = 'str_')
    return array