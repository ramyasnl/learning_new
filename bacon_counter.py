# print("Hello world!")
# a = 10 
# b = 20
# c = a+b
# print("the sum is :",c)

# "adding extra lines of code "
# "done"
# s = b - a
# print("the difference is:",s)
# counties_tuple = ("Arapahoe","Denver","Jefferson")
# print(len(counties_tuple))
# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})
# print(voting_data[2])
from mrjob.job import MRJob
class Bacon_count(MRJob):
   def mapper(self, _, line):
       for word in line.split():
           if word.lower() == "bacon":
               yield "bacon", 1

   def reducer(self, key, values):
       yield key, sum(values)
if __name__ == "__main__":
   Bacon_count.run()