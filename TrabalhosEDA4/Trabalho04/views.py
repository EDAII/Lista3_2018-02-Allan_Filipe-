from django.shortcuts import render
from Trabalho04.AVLTree import AVLTree


def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        byte_str = myfile.file.read()

        # Convert to a "unicode" object
        text_obj = byte_str.decode('UTF-8')
        columns_descriptions, all_data = read_csv(text_obj.splitlines())

        AVLTree.rotationlog = []
        AVLTree.displaylog = []

        register_tree = createAvlTree(all_data)

        register_tree.display()

        sorted_data = register_tree.inorder_traverse()

        return render(request, 'result.html', {'columns_descriptions': columns_descriptions,
                                               'sorted_data': sorted_data,
                                               'displaylog': AVLTree.displaylog,
                                               'rotationlog': AVLTree.rotationlog})
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


def createAvlTree(dataset):
    register_tree = AVLTree()

    for register in dataset:
        register_tree.insert(register)

    return register_tree
