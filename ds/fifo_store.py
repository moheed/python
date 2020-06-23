class MyQueue:
    fifostore=None#use this to store values
    lifostore=None#use this to retriev values, One of this is always empty
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.fifostore=[]#use this to store values[python lists are same as stack]
        self.lifostore=[]#use this to retriev values, One of this is always empty
   

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        
        self.lifostore.append(x)
                

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        #Always try to pop from fifostore, which stores element in
        #fifo order, if there is an element
        if len(self.fifostore):
            return self.fifostore.pop()
        #we need to do some work to adjust these store.
        while len(self.lifostore)!=0:
            #take everything from lifo and put in fifo
            self.fifostore.append(self.lifostore.pop())
        return self.fifostore.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.fifostore):
            val=self.fifostore.pop()
            self.fifostore.append(val)
            return val
        #we need to do some work to adjust these store.
        while len(self.lifostore)!=0:
            #take everything from lifo and put in fifo
            self.fifostore.append(self.lifostore.pop())
        val=self.fifostore.pop()
        self.fifostore.append(val)
        return val


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if (len(self.lifostore) ==0 and len(self.fifostore)==0) else False
        