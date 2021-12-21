import numpy as np
import copy

def main():
    #Part 1
    input_data = np.loadtxt('input.txt', dtype=str)
    gamma = np.zeros(shape=(len(input_data[0])))
    for input in range(input_data.size):
        for bit in range(len(input_data[0])):
            if int(input_data[input][bit]) == 0:
                gamma[bit] = gamma[bit] - 1
            elif int(input_data[input][bit]) == 1:
                gamma[bit] = gamma[bit] + 1

    #Not gunna lie, things started to fall apart a bit here
    epsilon = np.zeros_like(gamma)
    gamma_str = ""
    epsilon_str = ""
    for bit in range(gamma.size):
        if gamma[bit] > 0:
            gamma_str = gamma_str + "1"
            epsilon_str = epsilon_str + "0"
        else:
            gamma_str = gamma_str + "0"
            epsilon_str = epsilon_str + "1"
    print(int(gamma_str, 2) * int(epsilon_str, 2))

    #Part 2
    tmp_input = copy.deepcopy(input_data)
    del_array = copy.deepcopy(input_data)
    count = 0
    while tmp_input.size != 1:
        for input in range(tmp_input.size):
            if int(tmp_input[input][0]) == 0:
                count = count - 1
            else:
                count = count + 1
        if count > 0:
            delete = 0
        else:
            delete = 1
        for input in range(tmp_input.size):
            if int(tmp_input[input][0]) != delete:
                del_array = np.delete(del_array, input)
        break
    print(del_array.size)


if __name__ == "__main__":
    main()