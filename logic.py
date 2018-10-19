def cleanGUID(input): #Removes accessory characters from GUID
    removedChar = '{}- '
    for char in removedChar:  
        input = input.replace(char,"")
    return input

def addbrackets(input): #Adds accessory characters to PID
    return '{{{0}-{1}-{2}-{3}-{4}}}'.format(input[:8], input[8:12], input[12:16], input[16:20], input[20:])

def isvalid(input): #Checks if length of input is 32 characters
    return len(input) == 32

def flip(input): #Flips order of input
    order = [7,6,5,4,3,2,1,0,11,10,9,8,15,14,13,12,17,16,19,18,21,20,23,22,25,24,27,26,29,28,31,30]
    output = ""    
    for i in order:
        output = output + input[i]
    return output
   
def flipguid(input): #Checks if input is GUID or PID, and converts accordingly
    if input[0] == '{' and isvalid(cleanGUID(input)): #Returns true if input is a valid GUID
        return flip(cleanGUID(input))

    if isvalid(input): #Returns true if input is a valid PID
        return (addbrackets(flip(input)))

    else: #If the output is invalid
        return ("Invalid input, please try again.")
    




    
    
    
    
    



    


