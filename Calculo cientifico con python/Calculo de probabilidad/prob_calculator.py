import copy
import random

class Hat(object):

    def __init__(self, **balls):
        self.contents= []
        self.refill_list=[]
        for ball in balls:
            count = balls[ball]
            index = count
            while(index != 0):
                self.contents.append(ball)
                index -= 1

        self.refill_list = copy.copy(self.contents)
    
    def draw(self, count):
        ballList = list()
        self.contents = copy.copy(self.refill_list)
        for i in range(count):
          choice = random.choice(self.contents)
          ballList.append(choice)
          self.contents.remove(choice)
          if len(self.contents) == 0:
            break
        return ballList

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match = 0
    for i in range(num_experiments):
        ballResult = hat.draw(num_balls_drawn)
        ballArray = {}

        for ball in ballResult:    
            if ball not in ballArray:
                ballArray[ball]=1
            else:
                ballArray[ball]+=1
        countComparation = 0
        if(len(ballArray) >= len(expected_balls)):
            for balls in ballArray:
                if(balls not in expected_balls ):
                    continue
                if(ballArray[balls] >= expected_balls[balls]):
                    countComparation += 1
                if countComparation == len(expected_balls):
                    match += 1
    prob = match/num_experiments
    return prob