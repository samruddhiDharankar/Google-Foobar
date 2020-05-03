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