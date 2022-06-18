

num =  ["ravi","anshu", "rahul","manish","jen","ajay","fkjdsh","jfsdfhgdf","lkfgdfjgd","lela"]



def my_func(num):
    for index in range(len(num)):
        if index % 2 == 0:
            #return num.upper()
            print(" ", num[index])
        else:
          #  return num.lower()
            print("#",num[index])
            
        
my_func(num)
          
    
    
        