"""
Double-Linked List and Double-Linked Node Data Structures

Copyright (c) 2021 Gabriele Gilardi


Notes
-----
- Written and tested in Python 3.8.5.
- Double-linked list class implementation using a double-list node class.
- The search method returns always only the first occurrence (from the
  list head) of any duplicate data.
- Examples of usage are at the end of the file.
- Reference: "Problem Solving with Algorithms and Data Structures", by
  Miller and Ranum.
- get_node_list() is an helper function that returns a list with the content
  of all connected nodes starting from a given node and moving up or down.


DLnode Class
------------
data            Content of the node.
next_node       Linked next node.
previous_node   Linked previous node.
__init__()      Initializes the node.
__repr__()      Returns the string representation of the node.
set_data()      Set/replaces the content of the node.
get_data()      Returns the content of the node.
set_next()      Sets/replaces the linked next node.
get_next()      Returns the linked next node.
set_previous()  Sets/replaces the linked previous node.
get_previous()  Returns the linked previous node.


DLL Class
---------
head            Node at the front of the DLL.
size            Length of the DLList.
__init__()      Initializes the DLL.
__repr__()      Returns the string representation of the DLL.
is_empty()      Checks if the DLL is empty or not.
nodes()         Returns a list with all items contained in the DLL.
add_front()     Adds a new item to the front of the DLL.
add_back()      Adds a new item to the back of the DLL.
add_before()    Adds a new item before a specified item of the DLL.
add_after()     Adds a new item after a specified item of the DLL.
change()        Changes a specified item of the DLL to another item.
switch()        Switches two items of the DLL.
search()        Searches the DLL for a specified item.
remove()        Removes a specified item/node from the DLL.
pop()           Removes the node at the front of the DLL and returns its content.
peek()          Returns the content of the node at the front of the DLL.
reverse()       Reverses the DLL.
clear()         Removes all items from the DLL.
"""


def get_node_list(current_node, direction='down'):
    """
    Returns a list with the content of all connected nodes starting from
    <current_node>. Returns <None> if the node does not exist. If direction
    is <down> follows the "next" link, if direction is <up> follows the
    "previous" link.

    Note: depending on the way the nodes are linked, some nodes may not be
          returned or there may be an infinite loop.
    """
    # Check if it a valid node
    if (current_node is None):
        return None

    # Add the content of the current node
    node_list = [current_node.get_data()]

    # Loop until the end of the node chain (up)
    if (direction == 'up'):

        current_node = current_node.get_previous()
        while (current_node is not None):

            # Append the content of the current node and move to the next node
            node_list.append(current_node.get_data())
            current_node = current_node.get_previous()

        node_list.reverse()

    # Loop until the end of the node chain (down)
    else:

        current_node = current_node.get_next()
        while (current_node is not None):

            # Append the content of the current node and move to the next node
            node_list.append(current_node.get_data())
            current_node = current_node.get_next()

    return node_list


class DLnode:
    """
    Double-linked node class
    """
    def __init__(self, data, next_node=None, previous_node=None):
        """
        Initializes the node content and (if specified) the linked next and
        previous node.
        """
        self.data = data
        self.next = next_node
        self.previous = previous_node

    def __repr__(self):
        """
        Returns the string representation of the node.
        """
        return ("DLnode object with data = {}".format(self.data))

    def set_data(self, new_data):
        """
        Set/replaces the content of the node.
        """
        self.data = new_data

    def get_data(self):
        """
        Returns the content of the node.
        """
        return self.data

    def set_next(self, new_next):
        """
        Sets/replaces the linked next node.
        """
        self.next = new_next

    def get_next(self):
        """
        Returns the linked next node.
        """
        return self.next

    def set_previous(self, new_previous):
        """
        Sets/replaces the linked previous node.
        """
        self.previous = new_previous

    def get_previous(self):
        """
        Returns the linked previous node.
        """
        return self.previous


class DLL:
    """
    Double-linked list class
    """
    def __init__(self, init_list=None):
        """
        Initializes the double-linked list.
        """
        self.head = None
        self.size = 0

        # Initialize to the initial list
        if (init_list is not None):
            for data in init_list:
                self.add_back(data)

    def __repr__(self):
        """
        Returns the string representation of the list.
        """
        return ("DLL object with head pointing to {}".format(self.head))

    def is_empty(self):
        """
        Returns <True> if the list is empty and <False> if it is not.
        """
        return not self.size

    def nodes(self):
        """
        Returns a list with all items contained in the DLL.
        """
        node_list = []
        current_node = self.head

        # Loop until the end of the list
        while (current_node is not None):

            # Append the content of the current node and move to the next node
            node_list.append(current_node.get_data())
            current_node = current_node.get_next()

        return node_list

    def add_front(self, new_data):
        """
        Adds a new item to the front of the list and returns the new node
        object. Works also with an empty list.
        """
        # If the list is empty
        if (self.size == 0):

            # Create the new node
            new_node = DLnode(new_data)

        # If the list is not empty
        else:

            # Create the new node and link it to the current list head
            new_node = DLnode(new_data, next_node=self.head)

            # Link the current list head to the new node
            self.head.set_previous(new_node)

        # Set the new node as the new list head
        self.head = new_node

        # Increase the list size
        self.size += 1

        return new_node

    def add_back(self, new_data):
        """
        Adds a new item to the back of the list and returns the new node
        object. Works also with an empty list.
        """
        # Traverse the list to reach the back
        current_node = self.head
        previous_node = None
        while (current_node is not None):
            previous_node = current_node
            current_node = current_node.get_next()

        # If the list is empty
        if (self.size == 0):

            # Create the new node
            new_node = DLnode(new_data)

            # Set the new node as the new list head
            self.head = new_node

        # If the list is not empty
        else:

            # Create the new node and link it to the old last node
            new_node = DLnode(new_data, previous_node=previous_node)

            # Link the old last node to the new last node
            previous_node.set_next(new_node)

        # Increase the list size
        self.size += 1

        return new_node

    def add_before(self, new_data, ref_data):
        """
        Adds a new item before a specified item of the list and returns the new
        node object. Returns <None> if the specified item is not in the list.

        Note: if the specified item is at the front of the list the result is
              equivalent to a call to method <add_front>.
        """
        # Search the list for <ref_data>
        current_node = self.search(ref_data)

        # Insert the new node between the previous node and the current node
        if (current_node is not None):

            previous_node = current_node.get_previous()

            # If the current node is at the front of the list
            if (previous_node is None):

                # Create the new node and link it to the current node
                new_node = DLnode(new_data, next_node=current_node)

                # Set the new node as the new list head
                self.head = new_node

            # If the current node is not at the front of the list
            else:

                # Create the new node and link it to the current node and
                # to the previous node
                new_node = DLnode(new_data, next_node=current_node,
                                  previous_node=previous_node)

                # Link the current node to the new node
                current_node.set_previous(new_node)

                # Link the previous node to the new node
                previous_node.set_next(new_node)

            # Increase the list size
            self.size += 1

            return new_node

        # If <ref_data> is not found
        return None

    def add_after(self, new_data, ref_data):
        """
        Adds a new item after a specified item of the list and returns the new
        node object. Returns <None> if the specified item is not in the list.

        Note: if the specified item is at the back of the list the result is
              equivalent to a call to method <add_back>.
        """
        # Search the list for <ref_data>
        current_node = self.search(ref_data)

        # Insert the new node between the current node and the next node
        if (current_node is not None):

            next_node = current_node.get_next()

            # If the current node is at the back of the list
            if (next_node is None):

                # Create the new node and link it to the current node
                new_node = DLnode(new_data, previous_node=current_node)

            # If the current node is not at the back of the list
            else:

                # Create the new node and link it to the current node and
                # to the next node
                new_node = DLnode(new_data, next_node=next_node,
                                  previous_node=current_node)

                # Link the next node to the new node
                next_node.set_previous(new_node)

            # Link the current node to the new node
            current_node.set_next(new_node)

            # Increase the list size
            self.size += 1

            return new_node

        # If <ref_data> is not found
        return None

    def change(self, new_data, ref_data):
        """
        Changes a specified item of the list to another and returns the node
        object. Returns <None> if the specified item is not in the list.
        """
        # Search the list for <ref_data>
        current_node = self.search(ref_data)

        # Change the node content
        if (current_node is not None):

            current_node.set_data(new_data)

        return current_node

    def switch(self, data1, data2):
        """
        Switches two items of the list and returns <True>. Returns <False>
        if either of the items is not in the list.
        """
        # Search the list for <data1> and <data2>
        node1 = self.search(data1)
        node2 = self.search(data2)

        # Switches the content of the two nodes
        if (node1 is not None and node2 is not None):

            node1.set_data(data2)
            node2.set_data(data1)

            return True

        # If either of the items is not found
        return False

    def search(self, data):
        """
        Searches the list for a specified item and returns the corrisponding
        node object. Returns <None> if the specified item is not in the list.
        """
        current_node = self.head

        # Search the list for <data>
        while (current_node is not None):

            # If found, return the current node
            if (current_node.get_data() == data):

                return current_node

            # If not found, move to the successive node in the list
            else:
                current_node = current_node.get_next()

        # If <data> is not found
        return None

    def remove(self, data):
        """
        Removes a specified item/node from the list and returns <True>.
        Returns <False> if the specified item is not in the list.
        """
        # If <data> is a node
        if (isinstance(data, DLnode)):
            current_node = data

        # If <data> is a value
        else:
            current_node = self.search(data)

        # Remove the node
        if (current_node is not None):

            next_node = current_node.get_next()
            previous_node = current_node.get_previous()

            # If there is only one element in the list
            if (self.size == 1):

                # Set the list as an empty list
                self.head = None

            # If the current node is at the front of the list
            elif (previous_node is None):

                # Set the next node as the new list head
                self.head = next_node
                next_node.set_previous(None)

            # If the current node is at the back of the list
            elif (next_node is None):

                # Set the previous node as the last in the list
                previous_node.set_next(next_node)

            # If the current node is not at the front/back of the list
            else:

                # Link the previous node to the next node
                previous_node.set_next(next_node)

                # Link the next node to the previous node
                next_node.set_previous(previous_node)

            # Decrease the list size
            self.size -= 1

            return True

        # If <data> is not found
        return False

    def pop(self):
        """
        Removes the node at the front of the list and returns its content.
        Returns <None> if the list is empty.
        """
        # Check if the list is empty
        if (self.size == 0):
            return None

        # item at the front of the list
        data = self.head.get_data()

        # If there is only one element in the list
        if (self.size == 1):

            # Set the list as an empty list
            self.head = None

        # If there is more than one element in the list
        else:

            # Set the next node as the new list head
            self.head = self.head.get_next()
            self.head.set_previous(None)

        # Decrease the list size
        self.size -= 1

        return data

    def peek(self):
        """
        Returns the content of the node at the front of the list without
        removing it. Returns <None> if the list is empty.
        """
        # Check if the list is empty
        if (self.size == 0):
            return None

        # item at the front of the list
        else:
            return self.head.get_data()

    def reverse(self):
        """
        Reverses the DLL.
        """
        # If the DLL is empty
        if (self.size == 0):
            return

        # If the DLL is not empty
        previous_node = None
        current_node = self.head

        # Loop until the end of the list
        while (current_node is not None):

            # Save the next node link of the next node
            next_node = current_node.get_next()

            # Link the next node to the current and temp node
            current_node.set_next(previous_node)
            current_node.set_previous(next_node)

            # Move to the successive node in the list
            previous_node = current_node
            current_node = next_node

        # Set the new list head
        self.head = previous_node

    def clear(self):
        """
        Removes all items from the list.
        """
        self.head = None
        self.size = 0


if __name__ == '__main__':
    """
    Test the DLnode and DLL classes.
    """
    print('\nCreate the DLL with an initial list')
    dll = DLL([3, (6.4, 3.3), True, 'hello'])
    print('- DLL:', dll.nodes())            # [3, (6.4, 3.3), True, 'hello']
    print('- size:', dll.size)              # 4

    print('\nClear the DLL and check if empty')
    dll.clear()
    print('- DLL:', dll.nodes())            # []
    print('- empty?', dll.is_empty())       # True

    print('\nAdd items')
    dll.add_front(1.5)
    dll.add_front('2')
    dll.add_back(-5)
    dll.add_back('world')
    dll.add_before(-10, -5)
    dll.add_before(111, '2')
    print('- add 1 before 3:', dll.add_before(1, 3))        # None
    dll.add_after(0, '2')
    dll.add_after('hello', 'world')
    print('- add 1 after 3:', dll.add_after(1, 3))          # None
    print('- DLL:', dll.nodes())    # [111, '2', 0, 1.5, -10, -5, 'world', 'hello']

    print('\nChange and switch items')
    dll.change(10, -10)
    dll.change('Charlie', 'world')
    print('- change 3 with 0.2:', dll.change(0.2, 3))       # None
    dll.switch(111, 'hello')
    dll.switch('2', -5)
    print('- switch 3 with 0.2:', dll.switch(0.2, 3))       # False
    print('- DLL:', dll.nodes())    # ['hello', -5, 0, 1.5, 10, '2', 'Charlie', 111]

    print('\nRemove items')
    dll.remove('hello')
    dll.remove(111)
    dll.remove('Charlie')
    print('- remove 3:', dll.remove(3))         # False
    print('- DLL:', dll.nodes())                # [-5, 0, 1.5, 10, '2']

    print('\nSearch items')
    print('-', dll.search(-5))              # DLnode object with data = -5
    print('-', dll.search(1.5))             # DLnode object with data = 1.5
    print('- search 3:', dll.search(3))     # None

    print('\nExamples using <get_node_list>')
    node = dll.search(1.5)
    print('- from 1.5 down:', get_node_list(node, 'down'))   # [1.5, 10, '2']
    print('- from 1.5 up:', get_node_list(node, 'up'))   # [-5, 0, 1.5]

    node = dll.search(-5)
    print()
    print('- from -5 down:', get_node_list(node, 'down'))
    print('- from -5 up:', get_node_list(node, 'up'))
    node = dll.search('2')
    print('- from "2" down:', get_node_list(node, 'down'))
    print('- from "2" up:', get_node_list(node, 'up'))

    print('\nReverse and pop all items plus one')
    print('- reversed DLL:', dll.nodes())       # ['2', 10, 1.5, 0, -5]
    print('- item returned:', dll.pop())        # '2'
    print('- item returned:', dll.pop())        # 10
    print('- item returned:', dll.pop())        # 1.5
    print('- item returned:', dll.pop())        # 0
    print('- item returned:', dll.pop())        # -5
    print('- item returned:', dll.pop())        # None
    print('- DLL:', dll.nodes())                # []
    print('- size:', dll.size)                  # 0
