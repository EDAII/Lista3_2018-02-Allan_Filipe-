class Node():
    def __init__(self, register):
        self.key = int(register[0])
        self.left = None
        self.right = None
        self.register = register


class AVLTree():
    rotationlog = []
    displaylog = []

    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return (self.height == 0)

    def insert(self, register):
        tree = self.node

        newnode = Node(register)

        if tree is None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            # print("Inserted register [" + str(register) + "]")

        elif int(register[0]) < tree.key:
            self.node.left.insert(register)

        elif int(register[0]) > tree.key:
            self.node.right.insert(register)

        else:
            print("Key [" + str(register) + "] already in tree.")

        self.rebalance()

    def rebalance(self):
        '''
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        # Rotate left pivoting on self
        AVLTree.rotationlog.append('Registro ->  ' + str(self.node.register) + '  rotacionado para DIREITA.')
        print('Rotating ' + str(self.node.key) + ' right')
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        # Rotate left pivoting on self
        AVLTree.rotationlog.append('Registro ->  ' + str(self.node.register) + '   rotacionado para ESQUERDA.')
        print('Rotating ' + str(self.node.key) + ' left')
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def display(self, level=0, pref=''):
        self.update_heights()  # Must update heights before balances
        self.update_balances()
        if self.node is not None:
            AVLTree.displaylog.append("{} {} {} {} {}".format('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'Leaf' if self.is_leaf() else ' '))
            print('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'Leaf' if self.is_leaf() else ' ')
            if self.node.left is not None:
                self.node.left.display(level + 1, '<')
            if self.node.left is not None:
                self.node.right.display(level + 1, '>')

    def inorder_traverse(self):
        if self.node is None:
            return []

        inlist = []
        temp_list = self.node.left.inorder_traverse()
        for i in temp_list:
            inlist.append(i)

        inlist.append(self.node.register)

        temp_list = self.node.right.inorder_traverse()
        for i in temp_list:
            inlist.append(i)

        return inlist
