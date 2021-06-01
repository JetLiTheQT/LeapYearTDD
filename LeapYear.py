def leap(a):
    if(a%4==0):
        if(a%100 != 0 ):
            return "Leap Year"
        else:
            if(a%400==0):
                return "Leap Year"
            return "Not Leap Year"
    
