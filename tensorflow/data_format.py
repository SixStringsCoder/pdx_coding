import random as r
import pickle

INPUTS = list()
OUTPUTS = list()

def equation(w: int, x: int, y: int, z: int):
    first = x * y
    second = w + first + z
    return second / 2


def create_data(num):
    global INPUTS
    global OUTPUTS

    for i in range(num):
        w = r.randint(1, 1000)
        x = r.randint(1, 5000)
        y = r.randint(1, 25_000)
        z = r.randint(1, 100_000)

        INPUTS.append([w,x,y,z])

        answer = equation(w,x,y,z)

        OUTPUTS.append([answer])


create_data(100_000)

train_x = INPUTS[:60_000]
train_y = OUTPUTS[:60_000]

test_x = INPUTS[60_000:]
test_y = OUTPUTS[60_000:]

with open('data_set.pickle', 'wb') as f:
    pickle.dump([train_x,train_y,test_x,test_y], f)