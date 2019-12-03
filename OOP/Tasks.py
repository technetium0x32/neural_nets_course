import datetime

class Task():
    def changeDone(self):
        self.isDone = not self.isDone
        
    
    def __init__(self, description, isDone, time, deadline):
        self.description = description
        self.isDone = isDone
        self.time = time
        
        d, m, y = list(map(int, deadline.split(".")))
        self.deadline = datetime.date(y, m, d)
        
        
class Scedule():
    
    def addTask(self, description = "New task", isDone = False, time = 1, deadline = "01.01.2020"):
        task = Task(description, isDone, time, deadline)
        self.tasks[self.ident] = task
        self.ident += 1
        return self.ident - 1
    
    def completion(self, ident):
        self.tasks[ident].changeDone()
        
    def lineExpired(self):
        currentDate = datetime.date.today()
        
        for key in self.tasks:
            task = self.tasks[key]
            
            
            d1, m1, y1 = task.deadline.day, task.deadline.month, task.deadline.year
            
            d2, m2, y2 = currentDate.day, currentDate.month, currentDate.year
            
            if y2 > y1 or (y2 == y1 and (m2 > m1 or (m2 == m1 and d2 > d1))):
                print(f"Time for task <{task.description}> is expired!")
                
        
    
    def __init__(self):
        self.ident = 0x0
        self.tasks = {}
        
#Test Code       
