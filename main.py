class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    current = self.head
    while current.next:
      current = current.next
    current.next = new_node

  def display(self):
    current = self.head
    while current:
      print(current.data, end="->")
      current = current.next
    print("None")

  def insert_at_position(self, data, position):
    new_node = Node(data)
    if position == 0:
      new_node.next = self.head
      self.head = new_node
      return
    current = self.head
    for i in range(position - 1):
      if current is None:
        raise IndexError("Index out of range.")
      current = current.next
    new_node.next = current.next
    current.next = new_node

  def delete(self, data):
    if self.head is None:
      return
    if self.head.data == data:
      self.head = self.head.next
      return
    current = self.head
    while current.next:
      if current.next.data == data:
        current.next = current.next.next
        return
      current = current.next

  def length(self):
    count = 0
    current = self.head
    while current:
      count += 1
      current = current.next
    return count


sports = LinkedList()
sports.append("basketball")
sports.append("formula1")
sports.append("football")
sports.append("sprint")
sports.display()
sports.insert_at_position("tennis", 2)
sports.display()
sports.delete("sprint")
sports.display()
print("length of list is: ",sports.length())
