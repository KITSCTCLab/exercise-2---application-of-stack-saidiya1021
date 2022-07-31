class Evaluate:
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
  # Write your code here
  
  
  def __init__(self, size):
    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
      size_of_stack: An integer to set the size of stack."""
    
    self.top = -1
    self.size_of_stack = size
    self.stack = []

  def isEmpty(self):
    """
    Check whether the stack is empty.
    Returns:
      True if it is empty, else returns False.
    """
    if self.top==-1:
      return True
    else:
      return False


  def pop(self):
    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
    if not self.isEmpty():
      return self.stack.pop()


  def push(self, operand):
    """
    Push the operand to stack if the stack is not full.
    Arguments:
      operand: The operand to be pushed.
    """
    if self.top!=self.size_of_stack-1:
      self.stack.append(operand)


  def validate_postfix_expression(self, expression):
    """
    Check whether the expression is a valid postfix expression.
    Arguments:
      expression: A String which represents the expression to be validated.
    Returns:
      True if the expression is valid, else returns False.
    """
    for ch in expression:
      if ch not in '1234567890' or ch not in '+-*/^' or ch in '':
        return False
      else:
      return True
    
    def evaluation(self,num1,num2,opr):
      if self.opr=='+':
        return num2 + num1
      elif self.opr=='-':
        return num2 - num1
      elif self.opr=='*':
        return num1*num2
      elif self.opr=='/':
        return num2/num1
      elif self.opr=='^':
        return num2**num1


  def evaluate_postfix_expression(self, expression):
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    for ch in self.expression:
      if ch in '1234567890':
        evaluate.push(ch)
      else: 
        self.num1=int(evaluate.pop)
        self.num2=int(evaluate.pop)
        self.value=evaluate.evaluation(num1,num2,ch)
    print(self.stack[0])
          


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression') 
