
# coding: utf-8

# In[1]:

class UTCourse:
      def __init__(self,dict):
            for key,value in dict.items():
                if "year" in key:
                   setattr(self,key,int(value))
                else:
                    setattr(self,key,value)


# In[ ]:



