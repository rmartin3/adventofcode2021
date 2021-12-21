import numpy as np

def main():
    input_data = np.loadtxt('input.txt', dtype=str)
    horizontal = 0
    vertical = 0
    for i, input in enumerate(input_data):
        if(input[0] == 'down'):
            vertical = vertical + int(input[1])
        elif(input[0] == 'up'):
            vertical = vertical - int(input[1])
        elif(input[0] == 'forward'):
            horizontal = horizontal + int(input[1])
    print(horizontal * vertical)

    horizontal = 0
    vertical = 0
    aim = 0
    for i, input in enumerate(input_data):
        if(input[0] == 'down'):
            aim = aim + int(input[1])
        elif(input[0] == 'up'):
            aim = aim - int(input[1])
        elif(input[0] == 'forward'):
            horizontal = horizontal + int(input[1])
            vertical = vertical + (aim * int(input[1]))
    print(horizontal * vertical)

if __name__ == "__main__":
    main()