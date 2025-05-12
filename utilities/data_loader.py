"""  #Reusable Data Loader Utilit# """
import json
import os


def load_test_data(filename):
    filepath = os.path.join("data", filename)
    with open(filepath) as f:
        return json.load(f)


