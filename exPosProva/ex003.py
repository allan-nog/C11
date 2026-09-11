import numpy as np

colors = [
    {"color": "black", "type": "primary", "code": {"rgba": [255, 255, 255, 1], "hex": "#000"}},
    {"color": "green", "type": "secondary", "code": {"rgba": [0, 255, 0, 0.1], "hex": "#0F0"}},
    {"color": "yellow", "type": "primary", "code": {"rgba": [255, 255, 0, 0.7], "hex": "#FF0"}},
    {"color": "blue", "type": "primary", "code": {"rgba": [0, 0, 255, 1], "hex": "#00F"}}
]

for cor in colors:
    if cor["type"] == "primary":
        print(cor["color"])

for cor in colors:
    if cor["code"]["rgba"][2] == 255:
        print(cor["code"]["hex"])

array = []
for cor in colors:
    array.append(cor["color"])
    array.append(cor["code"]["hex"])

array = np.array(array)
print(array)

array = array.reshape(4, 2)
print(array)

array[0, 0] = "preto"
array[1, 0] = "verde"
array[2, 0] = "amarelo"
array[3, 0] = "azul"

print(array)