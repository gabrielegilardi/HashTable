"""
Dictionary Data Structure Using a Hash Table

Copyright (c) 2021 Gabriele Gilardi


Notes
-----
- Written and tested in Python 3.8.5.
- Dictionary data structure implementation using a hash table.
- Hash table uses 'remainder' as hashing method and 'rehashing' as collision
  resolution method.
- Possible to pass an initial list of items when creating the dictionary.
- Possible to define the skip value to be used in the hash table.
- Easy to resize the dictionary and change the skip value (see example).
- Methods in this class has been written trying to use the HashTable class as
  is, and thus they may not be the best in term of speed.
- Examples of usage are at the end of the file.
- Reference: "Problem Solving with Algorithms and Data Structures", by
  Miller and Ranum.

Dict Class
----------
size            Size of the dictionary.
skip            Skip value in the rehashing collision resolution method.
n_items         Number of items (pair key-values) in the dictionary.
keys            Hash table with the dictionary keys.
values          List with the dictionary values.
__init__()      Initializes the dictionary.
__repr__()      Returns info about the dictionary.
is_empty()      Checks if the dictionary is empty or not.
get_items()     Returns a list of all items in the dictionary.
get_keys()      Returns a list of all keys in the dictionary.
get_value()     Returns a list of all values in the dictionary.
put()           Adds a new item to the dictionary.
get()           Returns the value associated with a key.
search()        Searches the dictionary for a key.
remove()        Removes an item from the dictionary.
clear()         Removes all items from the dictionary.
"""


from HashTable import *


class Dict:
    """
    Dictionary class.
    """
    def __init__(self, size, init_list=None, skip=1):
        """
        Initializes the dictionary.
        """
        self.size = size
        self.skip = skip
        self.n_items = 0

        # Init hash table (keys) and data table (values)
        self.keys = HashTable(size, collision='rehashing', param=skip)
        self.values = [None] * self.size

        # Add the initial list of (key, value) to the dictionary
        if (init_list is not None):
            for key, value in init_list:
                self.put(key, value)

    def __repr__(self):
        """
        Returns info about the dictionary.
        """
        return ("\nDictionary object \
                 \n- total size = {} \
                 \n- number of items = {} \
                 \n- load factor = {:5.3f}" \
                .format(self.size, self.n_items, self.n_items / self.size))

    def is_empty(self):
        """
        Returns <True> if the dictionary is empty and <False> if it is not.
        """
        return not self.n_items

    def get_items(self):
        """
        Returns a list of all items in the dictionary (as tuples key-data).
        """
        items_list = [None] * self.n_items
        idx = 0

        for slot in range(self.size):
            if (self.keys.table[slot] is not None):
                items_list[idx] = (self.keys.table[slot], self.values[slot])
                idx += 1

        return items_list

    def get_keys(self):
        """
        Returns a list of all keys in the dictionary.
        """
        keys_list = [None] * self.n_items
        idx = 0

        for slot in range(self.size):
            if (self.keys.table[slot] is not None):
                keys_list[idx] = self.keys.table[slot]
                idx += 1

        return keys_list

    def get_values(self):
        """
        Returns a list of all the values in the dictionary.
        """
        values_list = [None] * self.n_items
        idx = 0

        for slot in range(self.size):
            if (self.keys.table[slot] is not None):
                values_list[idx] = self.values[slot]
                idx += 1

        return values_list

    def put(self, key, value):
        """
        Adds a new item (pair key-value) to the dictionary and returns the
        slot. Returns <None> if could not find any empty slot. If the key
        is already in the dictionary, the corresponding value is overwritten.
        """
        # Search the specified key
        slot = self.keys.search(key)

        # Overwrite the value if found the key
        if (slot is not None):
            self.values[slot] = value

        # Add the new item if not found the key
        else:

            # Add the key to the hash table
            slot = self.keys.insert(key)

            # Add the value if found an empty slot
            if (slot is not None):
                self.values[slot] = value
                self.n_items += 1

        return slot

    def get(self, key):
        """
        Returns the value associated with a specified key. Returns <None> if
        could not find the key.
        """
        # Search the specified key
        slot = self.keys.search(key)

        # Return the value if found the key
        if (slot is not None):
            return self.values[slot]

        # Otherwise return <None>
        else:
            return None

    def search(self, key):
        """
        Returns <True> if the specified key is in the dictionary, <False>
        otherwise.
        """
        # If found the key
        if (self.keys.search(key) is not None):
            return True

        # If not found the key
        else:
            return False

    def remove(self, key):
        """
        Removes the specified key and the associated value from the dictionary
        and returns <True>. Returns <False> if the key is not found.
        """
        # Search the specified key
        slot = self.keys.search(key)

        # If found the key
        if (slot is not None):
            self.keys.table[slot] = None
            self.values[slot] = None
            self.n_items -= 1
            return True

        # If not found the key
        else:
            return False

    def clear(self):
        """
        Removes all items from the dictionary.
        """
        self.n_items = 0
        self.keys.clear()                       # Clear the hash table
        self.values = [None] * self.size        # Clear the data table


if __name__ == '__main__':
    """
    Test the dictionary class.
    """
    print('\n==== Create a dictionary with size of 17 and add items:')
    init_list = [('key1', 320), ('key2', (6.4, 3.3)), ('key3', 's'),
                 ('key4', True), ('key5', 'hello'), ('key6', -10.2)]
    d = Dict(17, init_list=init_list, skip=3)
    d.put('key7', 77)
    d.put('key8', -997)
    d.put('key9', 'hello world')
    d.put('key10', False)
    d.put('key11', 25.453)

    # ('key5', 'hello')
    # ('key1', 320)
    # ('key10', False)
    # ('key6', -10.2)
    # ('key2', (6.4, 3.3))
    # ('key7', 77)
    # ('key3', 's')
    # ('key11', 25.453)
    # ('key8', -997)
    # ('key4', True)
    # ('key9', 'hello world')
    items = d.get_items()
    for item in items:
        print(item)

    print('\nEmpty?', d.is_empty())           # False

    # Dictionary object
    # - total size = 17
    # - number of items = 11
    # - load factor = 0.647
    print(d)

    print('\n==== Keys and values:')
    # ['key5', 'key1', 'key10', 'key6', 'key2', 'key7', 'key3', 'key11', 'key8', 'key4', 'key9']
    # ['hello', 320, False, -10.2, (6.4, 3.3), 77, 's', 25.453, -997, True, 'hello world']
    print(d.get_keys())
    print(d.get_values())

    print('\n==== Examples with get:')
    print(d.get('key7'))                # 77
    print(d.get('key11'))               # 25.453
    print(d.get('key0'))                # None

    print('\n==== Examples with search:')
    print(d.search('key10'))                # True
    print(d.search('key2'))                 # True
    print(d.search('key0'))                 # False

    print('\n==== Examples with remove:')
    print(d.remove('key6'))                 # True
    print(d.remove('key3'))                 # True
    print(d.remove('key5'))                 # True
    print(d.remove('key11'))                # True
    print(d.remove('key0'))                 # False

    print('\n==== Resulting dictionary and stats after remove:')
    # ('key1', 320)
    # ('key10', False)
    # ('key2', (6.4, 3.3))
    # ('key7', 77)
    # ('key8', -997)
    # ('key4', True)
    # ('key9', 'hello world')
    items = d.get_items()
    for item in items:
        print(item)

    # Dictionary object
    # - total size = 17
    # - number of items = 7
    # - load factor = 0.412
    print(d)

    print('\n==== Resulting dictionary and stats after resizing:')
    init_list = d.get_items()
    d = Dict(13, init_list=init_list, skip=1)

    # ('key2', (6.4, 3.3))
    # ('key10', False)
    # ('key9', 'hello world')
    # ('key7', 77)
    # ('key4', True)
    # ('key1', 320)
    # ('key8', -997)
    items = d.get_items()
    for item in items:
        print(item)

    # Dictionary object
    # - total size = 13
    # - number of items = 7
    # - load factor = 0.538
    print(d)

    d.clear()
    print('\n==== Resulting stats after clear:')
    # Dictionary object
    # - total size = 13
    # - number of items = 0
    # - load factor = 0.000
    print(d)
