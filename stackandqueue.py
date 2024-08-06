class Stack:
    def __init__(self, max_size): 
        '''self represent the class name itself. Init means initialization of the 
        main function  to open instances instances are opened as stack one, 
        stack_two and stack_three 
        '''
        self.max_size = max_size
        self.stack = []
        self.top = -1  
        
        ''' function defining the max size of the array.
 Here, max size is defined by the stack top pointer -1 because array index starts
 at zero. say if array is [1,2,3],the index is 0 to 2 where element 3 stays at 
 index 2 '''    
    def __str__(self):
        return str(self.stack)   
    '''I wrote this to be able to print the stack 
    using print function statement'''
    def push(self, item):
        if self.is_full():  #stack full condition. is_full method is defined in line number 48 isempty in line 44
            print("Stack Overflow") #if adding more element than stack max size
            # stack overflow  statement will be generated. 
            return
        self.top += 1  #top pointer move to 1 place to the right.  
        self.stack.append(item)  # add the element to the stack 

    def pop(self):
        if self.is_empty(): #if your index instance is empty
            print("Stack Underflow") # underflow condition will be generated
            return
        item = self.stack.pop()
        self.top = -1  
        
        '''pop condition happen when top pointer move to the left
        '''
        return item # popped  elements is printed out

    def peek(self):
        if self.is_empty(): 
            print("Stack is empty")
            return
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1 #empty condition happen when top pointer is -1
    #once stack as single element in it the top pointer shift to zero index

    def is_full(self):
        return self.top == self.max_size - 1 
    # stack is full when top pointer is at max_size-1 because the array start at 
    #0 index so the max index is always -1,  e.g. [1,2,3,4] index end at 3rd cell
    #since index begins at zero
   
    def display_table(self):   #you can run this function to  see how your stack array looks like
        if self.is_empty():     #if you run this function on empty stack
            print("Stack is empty") # output will generate stack is empty
            return              #if not it will return
        print("Stack Table:")     #stack table(string) on top row of table
        print("Index\tValue")     #stack value (string) on top row of table
        for i in range(self.top, -1, -1):
            print(f"{i}\t{self.stack[i]}")

# Example usage
stack_one = Stack(2)  # Create a stack with a maximum size of 2, you can type any number of size
stack_two=Stack(10)  # create a stack with  max size of 10
stack_three=Stack(3)# means i open the stack which allows 3 elements. more than 3 element

class Queue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.base = 0  
        self.top = -1  #Top pointer start at empty set
        self.max_size = max_size # array u define

    def enqueue(self, item):
        if self.is_full():     #if queue is full using method is_full
            print("Queue Overflow") # print overflow statement
            return  # if not return
        self.top += 1  # old top pointer move forward, because queue is added and data po
        self.queue[self.top] = item #top pointer become new item

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return
        item = self.queue[self.base]
        self.base += 1   #base     
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.queue[self.base]

    def is_empty(self):
        return self.base > self.top # remember base pointer stays at 0. If top pointer is less than base pointer its always less than zero
                                    # which is -1

    def is_full(self):
        return self.top == self.max_size - 1   
    # max size index-1 is full condtion remember index starts at 0 and not one

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        for i in range(self.base, self.top + 1):
            print(self.queue[i], end=" ")
        print()
        
        ''' This is the fully scale class. How u run it is u open the instance 
        with any defined array size. There is the function on somethingg ?'''
        
   
   