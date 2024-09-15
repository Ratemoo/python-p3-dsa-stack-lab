class Stack:
    def __init__(self, items=None, limit=100):
        """Initialize the stack with an optional list of items and a limit."""
        self.items = items if items is not None else []  # Initialize with provided items or an empty list
        self.limit = limit  # Limit the stack size, default to 100

    def isEmpty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Push an item onto the stack if it's not full."""
        if not self.full():
            self.items.append(item)

        
    def pop(self):
        """Pop the top item from the stack and return it. Return None if the stack is empty."""
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it. Return None if the stack is empty."""
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def full(self):
        """Return True if the stack has reached its limit."""
        return len(self.items) >= self.limit

    def search(self, target):
        """Return the distance from the top of the stack to the target item."""
        if target in self.items:
            return len(self.items) - 1 - self.items.index(target)
        return -1  # Return -1 if the item is not in the stack
