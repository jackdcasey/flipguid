def GUIDtoPID(GUID):

    # Remove characters we do not want

    removedChar = '{}- '
    for char in removedChar:  
        GUID = GUID.replace(char,"")

    # Ensure there are 32 characters in the string

    if len(GUID) == 32:
        print ("GUID Valid: Converting...")
    else:
        print ("GUID Invalid. Please try again.")
        return
        
    # Arrange the characters in the reversed format

    order = [7,6,5,4,3,2,1,0,11,10,9,8,15,14,13,12,17,16,19,18,21,20,23,22,25,24,27,26,29,28,31,30]
    PID = ""    
    for i in order:
        PID = PID + GUID[i]
    print(PID)
    return PID

GUIDtoPID(input("Enter GUID: "))
    
    
    
    
    
    
    



    


