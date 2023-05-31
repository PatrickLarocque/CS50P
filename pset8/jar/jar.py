# Suppose that you’d like to implement a cookie jar in which to store cookies.

class Jar:
    def __init__(self, capacity = 12):
        if capacity < 0:
            raise ValueError("Invalid capacity.")
        self.capacity = capacity
        self.size = 0
    
    # ToString/Stringify method for the contents of a jar.
    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if (n > self.capacity) or (self.size + n > self.capacity):
            raise ValueError("Insufficient capacity.")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies in the jar.")
        self.size -= n
        
# Setters and Getters
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size