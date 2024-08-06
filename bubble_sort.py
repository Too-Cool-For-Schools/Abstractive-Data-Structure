def bubble_sort(arr):  
    array_size=len(arr)  
    # your previous question last week, if you want to check the array 
    # use len function to check the length of the array 
    for i in range(array_size):
        ''''For the elements in array'''
        swapped=False  
        ''' before inner loop starts initialization is set to false 
        because if the array is already sorted which means all array elements of array index j 
        is no longer greater than index j+1 the for for j loop will no longer run. 
        '''
        for j in range(0,array_size-1-i):  
            '''#for works  (from, to)
            #(0 is your starting condition and it start at 0 because 
            first element of the array is 0 index)
            '''
            if arr[j]>arr[j+1]:     
                '''#if left index is bigger than the right neighbor cell'''
                arr[j],arr[j+1]=arr[j+1],arr[j] 
                #swap condition (neighbor cells will swap)
                swapped=True   
                '''swap will happen'''
                if not swapped:
                    break
                    '''#if every things get correct. if not is similar to else condition
                    break program stop''' 
        