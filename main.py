class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        previous = self.head  # Ambas as variáveis apontam para a 'HEAD' do Node.
        while (temp.next):
            previous = temp
            temp = temp.next
        self.tail = previous
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0:  # Se tivermos 0 itens na lista, retorne
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:  # Verifica se o cumprimento do nó é zero, se for, cria uma nova HEAD e TAIL
            self.head = new_node
            self.tail = new_node
        else:  # Se não for zero, o novo Node criado é anexado ao inicio do Node existente
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index > self.length:  # Checa se o index é negativo ou maior do que o comprimento.
            return None  # Indice inexistente
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value


my_linked_list = LinkedList(0)  # Primeiro elemento da Linked List
my_linked_list.append(1)  # Todos os outros anexos (appends) ao valor anterior (zero)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(2))

print(my_linked_list.pop_first())

print(my_linked_list.pop_first())

print(my_linked_list.pop_first())
