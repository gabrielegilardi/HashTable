"""
Dictionary Data Structures Using a Hash Table

Copyright (c) 2021 Gabriele Gilardi


Notes
-----
- Written and tested in Python 3.8.5.
- Hash table class implementation using lists.
- Hashing methods: folding, multiplication, remainder.
- Collision methods: rehashing with arbitrary slot skip, quadratic, chaining
  using double-linked-lists.
- Item conversion to integer using the ordinal value with positional weight.
- Examples of usage are at the end of the file.
- Reference: "Problem Solving with Algorithms and Data Structures", by
  Miller and Ranum. (runestone.academy/runestone/books/published/pythonds/index.html)

- Size prime numbers
- helper function: determine if a numer is prime (deterministic or probabilistic)
- determine the first prime number larger than given size
- Computation of prime numbers (geeksforgeeks.org/prime-numbers/).


HashTable Class
---------------

- check comments
- add intro
- add examples

"""


from random import randint
from math import modf, floor

from DoubleLinkedList import DLL

def is_prime_deterministic(n) : 
    """
    Returns <True> if <n> is a prime number, returns <False> otherwise. It
    uses an optimized systematic method to guarantee the answer.
    """
    # No prime numbers smaller than 2
    if n <= 3:
        return n > 1
    
    # Corner cases for next loop
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    
    # Using (6k-1) and (6k+1) optimization
    i = 5
    while (i * i <= n):
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i += 6

    return True

	
def is_prime_probabilistic(n, k):
    """
    Returns <True> if <n> is a prime number, returns <False> otherwise. It uses
    a probabilistic method based on the Fermat little theorem.
    
    - The probability of error when returns <True> is zero.
    - The probability of error when returns <False> is 2^-k.
    """
    def power(a, n, p):
        """
        Returns (a ^ n) % p using an iterative procedure to avoid overflow for
        large values of <n>.
        """        
        res = 1
        a = a % p

        # Loop until the exponent is reduced to zero
        while (n > 0):
            
            # If n is odd
            if (n % 2):
                res = (res * a) % p
                n = n - 1

            # If n is even
            else:
                a = (a ** 2) % p
                n = n // 2
                
        return res % p

	# 1 and 4 are not prime numbers
    if (n == 1 or n == 4):
        return False

	# 2 and 3 are prime numbers
    elif (n == 2 or n == 3):
        return True
	
	# Repeat k times for n > 4 and use Fermat little theorem to check if it is
    # not a prime number
    else:
        for i in range(k):
            a = randint(2, n-2)
            if (power(a, n-1, n) != 1):
                return False

    return True
			

def find_prime(value, method='deterministic', k=5):
    """
    Returns the closest (higher) prime number to the given value.
    """
    n = value

    # Probabilistic method
    if (method == 'probabilistic'):
        prime = is_prime_probabilistic(n, k)
        while (not prime):
            n += 1
            prime = is_prime_probabilistic(n, k)

    # Deterministic method
    else:
        prime = is_prime_deterministic(n)
        while (not prime):
            n += 1
            prime = is_prime_deterministic(n)

    return n


class HashTable:
    """
    """
    def __init__(self, size, init_list=None, hashing='remainder',
                 collision='chaining', c=0.618034, digit=2, skip=1):
        """
        """
        self.size = size
        self.hashing = hashing
        self.collision = collision
        self.c = c
        self.digit = digit

        self.table = [None] * self.size
        self.n_slots = 0
        self.n_items = 0

        # If necessary create state table
        # False = the slot has never been deleted
        if (self.collision == 'rehashing'):
            self.state = [False] * self.size
            self.skip = skip
            self.fact = 0
        elif (self.collision == 'quadratic'):
            self.state = [False] * self.size
            self.skip = 0
            self.fact = 1
        
        # Insert the initial list
        if (init_list is not None):
            for item in init_list:
                self.insert(item)
       

    def __repr__(self):
        """
        Returns the string representation of the hash table.
        """
        return ("\nHashTable object: \
                 \n- total size = {} \
                 \n- occupied slots = {} \
                 \n- number of items = {} \
                 \n- load factor = {:5.3f} \
                 \n- hashing method = {} \
                 \n- collision method = {}" \
                .format(self.size, self.n_slots, self.n_items,
                        self.load_factor(), self.hashing, self.collision))

    def items(self):
        """
        Returns a list with all items in the hash table.
        """
        items_list = [None] * self.n_slots
        idx = 0

        # If using chaining
        if (self.collision == 'chaining'):

            for slot in range(self.size):
                if (self.table[slot] is not None):
                    items_list[idx] = (slot, self.table[slot].nodes())
                    idx += 1

        # If using rehashing/quadratic
        else:

            for slot in range(self.size):
                if (self.table[slot] is not None):
                    items_list[idx] = (slot, self.table[slot])
                    idx += 1

        return items_list

    def load_factor(self):
        """
        Returns the load factor of the hash table.
        """
        return self.n_slots / self.size

    def insert(self, item):
        """
        Inserts an item in the hash table using the specified method, checks
        for collisions, and returns <True>. Returns <False> if could not find
        an empty slot (only when using rehashing/quadratic).
        """
        # Convert the item to an integer value
        value = self.convert(item)

        # Call hashing method
        slot = self.hashing_method(value)

        # If the slot is empty insert the item
        if (self.table[slot] is None):

            # If using chaining
            if (self.collision == 'chaining'):
                self.table[slot] = DLL([item])
            
            # If using rehashing/quadratic
            else:
                self.table[slot] = item

            self.n_slots += 1

        #  If the slot is not empty solve collision problem
        else:

            # If using chaining
            if (self.collision == 'chaining'):
                self.table[slot].add_back(item)
            
            # If using rehashing/quadratic
            else:
                i = 0
                new_slot = slot
                while (self.table[new_slot] is not None):
                    i += 1
                    if (i == self.size):
                        return False
                    new_slot = (slot + (self.skip + self.fact * i) * i) % self.size
                self.table[new_slot] = item
                self.n_slots += 1

        self.n_items += 1

        return True

    def delete(self, item):
        """
        Deletes an item from the table and return <True>. Returns <False> if
        the item is not found.
        """
        # If using chaining
        if (self.collision == 'chaining'):

            # Search for the item
            slot, node = self.search(item)

            # If the item is not found
            if (node is None):
                return False

            # If the item is found
            else:
                self.table[slot].remove(node)

                # Delete the list if no items left
                if (self.table[slot].size == 0):
                    self.table[slot] = None
                    self.n_slots -= 1

        # If using rehashing/quadratic
        else:

            # Search for the item
            slot = self.search(item)

            # If the item is not found
            if (slot is None):
                return False
            
            # If the item is found
            else:
                self.table[slot] = None
                self.state[slot] = True
                self.n_slots -= 1

        self.n_items -= 1

        return True

    def search(self, item):
        """
        Searches an item in the hash table. When using chaining returns slot
        and node object, when using rehashing/quadratic returns the slot.
        Returns <None> if not found.
        """
        # Convert the item to an integer value
        int_value = self.convert(item)

        # Call hashing method
        slot = self.hashing_method(int_value)

        # If using chaining
        if (self.collision == 'chaining'):

            # If the slot is empty
            if (self.table[slot] is None):
                return (slot, None)
            
            # If the slot is not empty
            else:
                node = self.table[slot].search(item)
                return (slot, node)
        
        # If using rehashing/quadratic
        else:

            # If the slot is empty
            if (self.table[slot] is None):
                return None
            
            # If the slot is not empty
            else:
                i = 0
                new_slot = slot

                while ((self.table[new_slot] is not None) or
                    (self.state[new_slot] is True)):
                    i += 1
                    if (i == self.size):
                        return None
                    new_slot = (slot + (self.skip + self.fact * i) * i) % self.size
                    if (self.table[new_slot] == item):
                        return new_slot
                
                return None

    def convert(self, item):
        """
        Returns the integer value associated with the item.
        """
        # Convert to a string
        str_item = str(item)

        # Add the ordinal values with positional weight
        int_value = 0
        for i in range(len(str_item)):
            int_value += ord(str_item[i]) * (i + 1)

        return int_value

    def hashing_method(self, value):
        """
        Returns the hash index.
        """
        # Folding
        if (self.hashing == 'folding'):
            str_value = str(value)
            n = len(str_value)
            slot = 0
            for i in range(0, n, digit):
                slot += int(str_value[i:min(i+digit,n)])
            slot = slot % self.size
            
        # Multiplication
        elif (self.hashing == 'multiplication'):
            slot = floor(self.size * modf(value * self.c)[0])

        # Remainder
        else:
            slot = value % self.size

        return slot

if __name__ == '__main__':

    # aa = HashTable(11, hashing='remainder', collision='chaining', skip=1)
    aa = HashTable(11, init_list=[54, 26, 93, 17])
    aa.insert(77)
    aa.insert(31)
    aa.insert(44)
    aa.insert(55)
    aa.insert(20)

    # print(aa.table)
    # print(aa.search(44))
    # print(aa.state)

    # print(aa.delete(77))
    # print(aa.delete(55))
    # print(aa.table)
    # print(aa.state)

    print(aa)
    items = aa.items()
    for item in items:
        print(item)
