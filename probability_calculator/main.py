import copy
import random

class Hat:
  
  def __init__(self,**all_item):
    self.contents=[]
    for key,value in all_item.items():
        for itr in range(value):
          self.contents.append(key)
  

  def draw(self, amount):
    draw_list = []
   
    if amount >= len(self.contents):
        draw_list = self.contents.copy()  
        self.contents.clear() 
        return draw_list

    for i in range(amount):
        name = self.contents.pop(random.randrange(len(self.contents)))
        draw_list.append(name)
    return draw_list


  

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    final_count=0
    for _ in range(num_experiments):
      copyhat = copy.deepcopy(hat)
      temp_list = copyhat.draw(num_balls_drawn)
      success=True
      for key,value in expected_balls.items():
        if temp_list.count(key) < value:
          success=False
          break
      if success:
        final_count+=1
    return final_count/num_experiments
