import numpy as np
import datascience as ds
from Worth_packs import Setup

while True:
    setup = input("What is the name of the restaurant: ")
    if setup == "Done":
        break
    Setup(setup)
