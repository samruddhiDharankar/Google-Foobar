'''
You’ve caught two of your fellow minions passing coded notes back and forth – while they’re on duty, no less! Worse, you’re pretty sure it’s not job-related – they’re both huge fans of the space soap opera “Lance & Janice”. You know how much Commander Lambda hates waste, so if you can prove that these minions are wasting her time passing non-job-related notes, it’ll put you that much closer to a promotion.

Fortunately for you, the minions aren’t exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched. That is, ‘a’ becomes ‘z’, ‘b’ becomes ‘y’, ‘c’ becomes ‘x’, etc. For instance, the word “vmxibkgrlm”, when decoded, would become “encryption”.

Write a function called answer(s) which takes in a string and returns the deciphered string so you can show the commander proof that these minions are talking about “Lance & Janice” instead of doing their jobs.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
(string) s = “wrw blf hvv ozhg mrtsg’h vkrhlwv?”
Output:
(string) “did you see last night’s episode?”

Inputs:
(string) s = “Yvzs! I xzm’g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!”
Output:
(string) “Yeah! I can’t believe Lance lost his job at the colony!!”

'''

x = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"


def solution(x):
    arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  #initial array
    y = ""                                                       #empty string
    
    for i in range(len(x)):
        if (x[i].isspace() == True):                             #checking spaces in the string
            y = y + " "
        else:
            if (x[i].isalpha() == True):                         #checking if alphabet or not
                if(x[i].islower() == True):                      #checking for lower case letters
                    a = ord(x[i])                                #getting ascii value of letter
                    pos = a - 97                                 #calculating postion by subtracting ascii value of letter from ascii value of 'a'
                    new_pos = (25 - pos) % 26                    #calculating new position for substitution
                    y = y + arr[new_pos]                         #appending it to the new string
                else:
                    y = y + x[i]
            else:
                y = y + x[i]
        
    return y
w = solution(x)
print(w)