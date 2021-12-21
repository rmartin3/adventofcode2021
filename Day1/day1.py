import numpy as np

def main():
    #Part 1
    count = 0
    input_data = np.loadtxt('input.txt', dtype=np.int64)
    for i, input in enumerate(input_data):
        #Can't start enumerate past first index so simple check to skip
        if input > input_data[i-1] and i > 0:
            count = count + 1
    print(count)

    #Part 2
    count = 0
    a_total = input_data[0] + input_data[1] + input_data[2]
    for i, input in enumerate(input_data):
        if(i > input_data.size-4):
            break
        b_total = input_data[i+1] + input_data[i+2] + input_data[i+3]
        if(b_total > a_total):
            count = count + 1
        a_total = b_total
    print(count)

if __name__ == "__main__":
    main()