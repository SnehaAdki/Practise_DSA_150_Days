# Valid Mountain Array

def validate_mountain(arr_val):
    first_peak = None
    for i in range(1,len(arr_val)-1):
        if arr_val[i]>arr_val[i-1] and arr_val[i]>arr_val[i+1]:
            first_peak = i
            break
    
    #if no peak
    if first_peak == None :
        return False
    
    for i in range(0,first_peak):
        if not arr_val[i] < arr_val[i+1]:
            return False
        
    for i in range(first_peak,len(arr_val)-1):
        if not arr_val[i] > arr_val[i+1]:
            return False

    return True
arr_val = [2,1]
print(validate_mountain(arr_val))
