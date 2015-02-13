import sys
source = open(sys.argv[1], 'r').readlines()

for line in source:
    array = line.split()
    result = []
    for word in array:
        result.append(word.replace(word[0], word[0].upper(), 1))
    print ' '.join(result)
    

   
#Write a program which capitalizes the first letter of each word in a sentence.
#Input sample:

#Hello world
#javaScript language
#a letter
#1st thing

#Your program should accept as its first argument a path to a filename. Input example is the following
#Output sample:
#
#Print capitalized words in the following way.

#Hello World
#JavaScript Language
#A Letter
#1st Thing