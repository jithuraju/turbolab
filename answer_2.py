str1=input("enter the valid string of parenthesis:")
def remove_outer_layer(str1):
    str2 =''
    count=1
    i = 1 
    while (i< len(str1)):
        if (str1[i]=="("):
        	count = count+1 
        if count == 0:
            i =i+2
            count=count+1
            continue
        str2=str2+str1[i]
        i=i+1
    print (str2)

remove_outer_layer(str1)      
  
   
           