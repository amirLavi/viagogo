# viagogo
Viagogo Coding Challenge
------------------------------------------
#Running instructions:
1) Please make sure to run it with python 3.*
2) to run simply type: python Event.py

# Answers to questions from the prompt:
1)**Q: How might you change your program if you needed to support multiple events at the
same location?**

A: If I needed to make my program to support multiple events, I would have created a class for the coordinate system. Each object (i.e. each point)of the coordinate system would have an instance variable (a list) that holds the number of events it would host.

2)**Q: How would you change your program if you were working with a much larger world
size?**

A: If I'm working with a larger world size I'd have to create a more efficient way to first iterate over the data to harvest the information. This means I would implement my coordinate system class (that was talk about in the question above) and in the main class would have them placed in a dictionary (HashMap) that would have a key = (x,y) tuple, and value = the coordinate system object. This would give me faster access to each coordinate. Then I would change my algorithm to basically loop around the input coordinate similar to a growing spiral (essentially implementing Breath First Search). By doing that I would get the closest five events much faster instead of needing to iterate over all the points.
