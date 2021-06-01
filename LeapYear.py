def leap(a):
    if(a%4==0):
        if(a%100 != 0 ):
            return "Leap Year"
        else:
            return "Not Leap Year"
    
