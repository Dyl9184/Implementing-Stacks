
class array:
  def __init__(self,size):
    self.array=[]
    for x in range(size):
        self.array.append("")


myarray=array(8)
#print(myarray.array[2])

class stack():
  def __init__(self,size):
    self.size = size
    self.pointer = -1
    self.array=myarray
   

  def isempty(self):
    if self.pointer == -1:
      return(True)
    else:
      return(False)
    
  def isFull(self):
    if self.pointer == self.size:
      return(True)
    else:
      return(False)

  def pop(self):
    if self.isempty() == True:
      return("the stack is empty")
    else:
      self.pointer -= 1
      return(self.array.array[self.pointer])
     

  def push(self,item):
    if self.isFull() == True:
      return("The stack is full")
    else:
      self.pointer = self.pointer + 1
      self.array.array[self.pointer - 1]=item

      
      

  def peek(self):
    if self.isempty() == True:
      return("The list is empty")
    else:
      return(self.array.array[self.pointer])
      


  

      
#myarray=array(6)
#myarray.array[2]
#print(myarray.array[2])



stackvalue = stack(8)
stackvalue.push("OwO")
stackvalue.push("UwU")
print(stackvalue.pop())
print(stackvalue.pop())
