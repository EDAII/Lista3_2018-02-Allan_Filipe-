from django.shortcuts import render
import time


def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        byte_str = myfile.file.read()
        # Convert to a "unicode" object
        text_obj = byte_str.decode('UTF-8')
        columns_descriptions, all_data = read_csv(text_obj.splitlines())
        #
        # print("ORDENAÇÃO selectionSort")

        sorted_data, selection_sort_time = selectionSort(all_data)

        # # print("ORDENAÇÃO insertionSort")
        #
        sorted_data, insertion_sort_time = insertionSort(all_data)

        # # print("ORDENAÇÃO bubbleSort")
        sorted_data, bubble_sort_time = bubbleSort(all_data)

        # # print("ORDENAÇÃO shellSort")
        sorted_data, shell_sort_time = shellSort(all_data)

        sorted_data, count_sort_time = countSort(all_data)

        sorted_data, radix_sort_time = radixSort(all_data)

        return render(request, 'result.html', {'columns_descriptions': columns_descriptions,
                                               'sorted_data': sorted_data,
                                               'selection_sort_time': selection_sort_time,
                                               'insertion_sort_time': insertion_sort_time,
                                               'bubble_sort_time': bubble_sort_time,
                                               'shell_sort_time': shell_sort_time,
                                               'count_sort_time': count_sort_time,
                                               'radix_sort_time': radix_sort_time})
    else:
        # Nothing to do
        pass

    return render(request, 'home.html')


def read_csv(file):
    all_data = []
    columns_descriptions = []

    # Save all csv data in a list of lists, removing '\n' at the last line element.
    for line in file:
        if not columns_descriptions:
            columns_descriptions = line.split(",")
            columns_descriptions[-1] = columns_descriptions[-1].strip("\n")
        else:
            line_splitted = line.split(",")
            line_splitted[-1] = line_splitted[-1].strip("\n")
            all_data.append(line_splitted)

    return columns_descriptions, all_data


def selectionSort(dataset):
    sorted_data = list(dataset)
    time_initial = time.time()
    for currently_checked_position in range(len(sorted_data)):
        lower_position = currently_checked_position

        for position_searched in range(currently_checked_position+1, len(sorted_data)):
            if int(sorted_data[lower_position][0]) > int(sorted_data[position_searched][0]):
                lower_position = position_searched

        temporary_register = sorted_data[currently_checked_position]
        sorted_data[currently_checked_position] = sorted_data[lower_position]
        sorted_data[lower_position] = temporary_register

    time_final = time.time() - time_initial
    return sorted_data, time_final


def insertionSort(dataset):
    sorted_data = list(dataset)
    time_initial = time.time()
    for currently_checked_position in range(1, len(sorted_data)):
        currently_checked_data = sorted_data[currently_checked_position]

        position_searched = currently_checked_position - 1

        while (position_searched > -1) and int(currently_checked_data[0]) < int(sorted_data[position_searched][0]):
            sorted_data[position_searched + 1] = sorted_data[position_searched]
            position_searched = position_searched - 1

        sorted_data[position_searched + 1] = currently_checked_data

    time_final = time.time() - time_initial
    return sorted_data, time_final


def bubbleSort(dataset):
    sorted_data = list(dataset)
    time_initial = time.time()
    final_position_to_be_checked = len(sorted_data) - 1
    occurred_swap = True

    while (final_position_to_be_checked > 0) and occurred_swap:
        occurred_swap = False

        for currently_checked_position in range(final_position_to_be_checked):
            if int(sorted_data[currently_checked_position][0]) > int(sorted_data[currently_checked_position + 1][0]):
                occurred_swap = True
                temporary = sorted_data[currently_checked_position]
                sorted_data[currently_checked_position] = sorted_data[currently_checked_position+1]
                sorted_data[currently_checked_position+1] = temporary

        final_position_to_be_checked = final_position_to_be_checked - 1

    time_final = time.time() - time_initial
    return sorted_data, time_final


def shellSort(dataset):
    sorted_data = list(dataset)
    time_initial = time.time()

    dataset_length = len(sorted_data)
    gap = int(dataset_length / 2)
    while gap > 0:
            for num in range(gap, dataset_length):
                data = sorted_data[num]
                position = num
                while position >= gap and int(data[0]) < int(sorted_data[position - gap][0]):
                    sorted_data[position] = sorted_data[position - gap]
                    position = position - gap
                    sorted_data[position] = data
            gap = int(gap / 2)

    time_final = time.time() - time_initial
    return sorted_data, time_final


def countSort(dataset):
    sorted_list = list(dataset)
    time_initial = time.time()

    # The sorted_list character array that will have sorted arr
    output_list = [0 for position in range(max([int(item[0]) for item in dataset]) + 2)]
    print(max([int(item[0]) for item in dataset]) + 2)

    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count_list = [0 for position in range(max([int(item[0]) for item in dataset]) + 2)]

    # For storing the resulting answer since the
    # string is immutable
    sorted_list = [0 for data in dataset]

    # Store count_list of each character
    for data in dataset:
        number = int(data[0])
        count_list[number] += 1

    # Change count_list[i] so that count_list[i] now contains actual
    # position of this character in output_list array
    for position in range(max([int(item[0]) for item in dataset]) + 2):
        count_list[position] += count_list[position-1]

    # Build the output_list character array
    for position in range(len(dataset)):
        output_list[count_list[int(dataset[position][0])]-1] = dataset[position]
        count_list[int(dataset[position][0])] -= 1

    # Copy the output_list array to arr, so that arr now
    # contains sorted characters
    for position in range(len(dataset)):
        sorted_list[position] = output_list[position]

    time_final = time.time() - time_initial
    return sorted_list, time_final


def radixSort(dataset):
    time_initial = time.time()
    dataset_size = int(len(dataset))
    modulus = 10
    divisor = 1
    while True:
        # empty array, [[] for i in range(10)]
        dataset_list = [[], [], [], [], [], [], [], [], [], []]
        for data in dataset:
            least_digit = int(data[0]) % modulus
            least_digit = int(least_digit / divisor)
            dataset_list[least_digit].append(data)
        modulus = modulus * 10
        divisor = divisor * 10

        if len(dataset_list[0]) == dataset_size:
            time_final = time.time() - time_initial
            return dataset_list[0], time_final

        dataset = []
        dataset_append = dataset.append
        for data_list in dataset_list:
            for data in data_list:
                dataset_append(data)
