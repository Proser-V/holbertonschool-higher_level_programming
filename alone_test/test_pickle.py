#!/usr/bin/python3

import pickle


class Pickletest:
    def __init__(self):
        self.another_dic = {"color": "white"}
        self.string = "Je suis un string"
        self.liste = [1, 2, 3, "Nous irons au bois"]
        self.tuple = ([4, 5, 6], "Cueillir des cerises")
        self.big_thick_dic = {"user": self.another_dic}

my_obj = Pickletest()

with open("data.pkl", "wb") as file:
    pickle.dump(my_obj, file)

with open("data.pkl", "rb") as file:
    loaded_obj = pickle.load(file)
    print(loaded_obj.string)
    print(loaded_obj.liste)
    print(loaded_obj.tuple)
    print(loaded_obj.big_thick_dic)
