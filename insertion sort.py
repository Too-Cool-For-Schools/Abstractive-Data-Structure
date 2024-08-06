def insertion_sort(list_a):
    
    indexing_length=range(1,len(list_a))
    ''''we check the second index of the table first that's why range starts 
    at 1 until the end of the list'''
    
    for i in indexing_length:     
        # for the number of elements in the length of the set
        
        value_to_sort=list_a[i] 
     
        #value we want to sort is the all the elements i in the whole index
        
        while list_a[i-1]>value_to_sort and i>0:
            #While right index is smaller than left index
            list_a[i-1],list_a[i]=list_a[i],list_a[i-1]
            # left index kept swapping  
            
            i=i-1   
            #until it goes to right most area
            '''i=i-1 because right most index say we have 5 element 
            index starts from 0 therefore index ends at index number 4 for 
            the 5 elements'''
            

