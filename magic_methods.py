"""
Magic methods in python are the special methods that are used to define the behavior of objects when they are used with an operator
The methods are called by the python interpreter when certain operations are performed on the objects.
"""
class Book:
  def __init__(self,name,author):
    """
    Constructor for this class
    """
    self.name = name
    self.author = author
  
  def __str__(self) -> str:
    """
    This method returns the string value of an object
    """
    return f"{self.name} by {self.author}"
  
  def __eq__(self, other: object) -> bool:
    """
    This defines the condition by which the equal operator on two objects
    will be evaluated
    """
    return self.name==other.name and self.author==other.author
  
  def __lt__(self,other):
    """
    This defines the condition by which the less than operator on two objects
    will be evaluated
    """
    return self.name<other.name

  def __gt__(self,other):
    """
    This defines the condition by which the greater than operator on two objects
    will be evaluated
    """
    return self.name>other.name
  
  def __add__(self,other):
    """
    This defines the condition by which the + operator on two objects
    will be evaluated
    """
    return self.name+other.name
  
  def __contains__(self,value):
    """
    This defines the condition by which the in operator on two objects
    will be evaluated
    """
    return value in self.name or value in self.author
  
  def __getitem__(self,key):
    """
    Access the attributes of the object by indexing
    """
    if key=='name':
      return self.name
    elif key=='author':
      return self.author
  

book1 = Book("Opu","Zafar Iqbal")
book2 = Book("Topu","Humayun")

print(book1)
print(book1==book2)
print(book1<book2)
print("Opu" in book1)
print(book1['name'])