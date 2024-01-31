# Day 95
# Regular expression in python
# it is used to match the pattern that you have created to mathch on that string.
# suppose that you have a 100 lines of strings and you want to find any specific word or character then just create a pattern so that you can fiind it in your string.

# there are many meta characters in regular expressions you can explore it in reference.
# reference:
# ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions
# docs.python.org/3/library/re.html#
# https://regxr.com/

import re
pattern = "course"
text = '''
The 100 day coding challenge course by Code With Harry on YouTube is an excellent resource for anyone who wants to learn coding. The course is well-structured and covers a wide range of topics, starting from the basics of programming and gradually moving towards more advanced concepts.

Day 91 of the course is a continuation of the previous days' lessons and focuses on developing a project using Python. The project involves creating a GUI-based program to generate random passwords with user-defined parameters. The video tutorial is easy to follow and provides step-by-step instructions on how to create the program using Python and the Tkinter library.

One of the best things about this course is the practical approach taken by the instructor, Harry. He doesn't just teach the theory of programming but also encourages students to apply their knowledge by building projects. This hands-on approach is essential for learning how to code, and it helps students to develop their problem-solving skills.

Overall, I highly recommend the 100 day coding challenge course by Code With Harry on YouTube to anyone who wants to learn programming. The course is suitable for both beginners and intermediate-level students, and the instructor, Harry, is an excellent teacher who explains complex concepts in a clear and concise manner. Completing Day 91 course provides students with the opportunity to create a useful program and reinforces the concepts learned in the previous lessons.

'''

# if it find its first match then it will terminate the program and return.
# matches = re.search(pattern,text)
# print(matches)

# you can find all the matches by using for loop
matches = re.finditer(pattern,text)
for match in matches:
    # print(match)
    print(match.span()) # this will print only indexes of the matches.
    # print(text[match.span()[0]:match.span()[1]]) # this will only print characters that are matched with the pattern
    