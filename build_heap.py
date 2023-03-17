# python3

import sys

def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n//2, -1, -1):
        sift_down(data, i, swaps)
    return swaps

def sift_down(data, i, swaps):
    n = len(data)
    min_index = i
    left = 2*i+1
    if left < n and data[left] < data[min_index]:
        min_index = left
    right = 2*i+2
    if right < n and data[right] < data[min_index]:
        min_index = right
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(data, min_index, swaps)


def main():
    input_type = input("I (input from keyboard) or F (input from file): ").strip().upper()
    if input_type == "I":
        n = int(input("Number of elements: "))
        data = list(map(int, input("Elements: ").split()))
    elif input_type == "F":
        filename = input("Filename: ")
        try:
            with open(filename, "r") as f:
                n = int(f.readline().strip())
                data = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("Error: file not found")
            sys.exit()
    else:
        print("Error: invalid input type")
        sys.exit()

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    print(len(swaps))
    assert len(swaps) <= 4*n


    # output all swaps
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

