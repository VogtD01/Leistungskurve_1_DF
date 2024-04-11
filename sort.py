def bubble_sort(data):
    for number in range(len(data)-1):
        for number2 in range(len(data)-1):
            if data[number2] > data[number2+1]:
                data[number2], data[number2+1] = data[number2+1], data[number2]
    return data