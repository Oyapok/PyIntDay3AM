class Stack:
    
    def __init__(self, size):
        self.__maxsize=size
        self.__content=[]
        
    def push(self, element):

        if len(self.__content) < self.__maxsize:
            self.__content.append(element)
        else:
            raise Exception("Stack full")
    
    def __len__(self):
        return  self.__content.__len__()  
    
    def pop(self):
        if len(self.__content) != 0:
            return self.__content.pop()
        else:
            raise Exception("Stack empty")
        
    def maxSize(self):
        return self.__maxsize
    
    def isEmpty(self):
        return len(self.__content) == 0
    
    def __str__(self):
        return f"({len(self.__content)}/{self.__maxsize}) {self.__content}"

#     def __iter__(self):
#         self.index=-1
#         return self
#     def __next__(self):
#         if self.index >= -len(self):
#             elt=self.__content[self.index]
#             self.index -= 1
#             return elt
#         else:
#             raise StopIteration
            
#     def __iter__(self):
#         l=self.__content.copy()
#         l.reverse()
#         for e in l:
#             yield e


if __name__ == "__main__":
    s=Stack(10)
    s.push(10)
    s.push(20)
    s.push(45)
    s.push(8)
    for e in s:
        print(e)
    l=list(s)
    print(l)