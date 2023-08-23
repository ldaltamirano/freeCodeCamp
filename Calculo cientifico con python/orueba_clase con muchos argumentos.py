import copy
import random
# Consider using the modules imported above.

class Hat:
  #init function stores passed arguments as variables and creates a refill variable that is the same as contents
  def __init__(self,**balls):
    self.content_list=[]
    self.contents=[]
    self.refill_list=[]
#for loop passes KWargs from hat defining call into list of tuples
    for color,count in balls.items():
      self.content_list.append((color,count))
    #for loop turns list of tupples into list color strings (effectively the balls)
    for color,count in self.content_list:
      itervar=count
      while itervar>0:
        self.contents.append(str(color))
        itervar=itervar-1
    #construct a refill list for the draw function later by deep copying the contents    
    self.refill_list=copy.deepcopy(self.contents)
    

    #draw function sets a length variable to keep track of how many balls are still in the hat and sets self.contents to the default state
  def draw(self,count):
    lenvar=len(self.contents)
    self.contents=copy.deepcopy(self.refill_list)
#sets a variable as return list into which we will pass the drawn balls
    return_list=[]
    
    for i in range(count):
      #if statement detects if the bag is empty and fills it up again by deep copying the refill list
      if lenvar == 0:
        self.contents=copy.deepcopy(self.refill_list)
        lenvar=len(self.contents)

      #pick random entry on contents, remove it from contents, and append it to return list
      draw_var = random.choice(list(self.contents))
      self.contents.remove(draw_var)
      lenvar=lenvar-1
      return_list.append(draw_var)
    
    return return_list
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  #section that parses the passed arguments
  comparison_dict=expected_balls
  match_count=0
  comparison_var=len(comparison_dict)
  
  #within loop:
  #section that calls the draw function num_experiments times. stores the returned list as result_list  
  for i in range(num_experiments):
    result_list=hat.draw(num_balls_drawn)
    result_dic={}
    loop_comparison_var=0
    #section that parses the return from draw function and turns it into a dictionary
    for x in result_list:
        
      if x not in result_dic:
        result_dic[x]=1
        continue
      result_dic[x]+=1
    
# section that compares results to the expected results by iterating over the keys in the result dictionary and seeing if they are >= values in the comparison dictionary
    for x in result_dic:
      if x not in comparison_dict:
        continue
      if result_dic[x]>=comparison_dict[x]:
        loop_comparison_var=loop_comparison_var+1
    if loop_comparison_var == comparison_var:
        match_count=match_count+1

  #section that calculates probability and sets return variable
  probability_var=match_count/num_experiments
  
  return probability_var