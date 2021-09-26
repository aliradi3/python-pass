"""
Instructions:

1. Create a class named ReversedString that inherits from StringOperations class
2. Implement the function reverse
3. reverse function should be a one liner function that returns the reverse string to_be_reversed
4. Instantiate the class ReversedString
5. Print to show your function implementation result
"""



class StringOperations:
    def reverse(self, *, to_be_reversed: str ):return to_be_reversed[::-1]
       
class ReversedString (StringOperations):
    def init(self):
        super().reverse()

message = ReversedString.reverse(self=None,to_be_reversed="!nohtyP ot emocleW")

#The output = Welcome to Python!
print(message)
