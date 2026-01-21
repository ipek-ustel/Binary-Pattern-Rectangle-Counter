def count_rectangles(Pattern):

    total_rec_number = 0

    def check_if_rectangle(r1,c1,r2,c2):
    
        for r in range(r1, r2+1):
            if Pattern[r][c1] != "1" or Pattern[r][c2] != "1":      
                return False                                          
        
           
        for c in range(c1, c2+1):
            if Pattern[r1][c] != "1" or Pattern[r2][c] != "1":      
                return False                                          
            
         

        for c in range(c1+1, c2):
            for r in range(r1+1, r2):
                if Pattern[r][c] == "0":                            
                    return True
            
        return False
    
    def rectangle_number(r1, c1):                       
        
        number_of_rec = 0

        for r2 in range(r1+1, len(Pattern)):                
            for c2 in range(c1+1, len(Pattern[0])):         
                if check_if_rectangle(r1,c1,r2,c2):
                    number_of_rec += 1
                    
        return number_of_rec
    


    for r1 in range(0, len(Pattern)):                     
        for c1 in range(0, len(Pattern[0])):
            if Pattern[r1][c1] == "1":
                total_rec_number += rectangle_number(r1, c1)

    return total_rec_number


        
        
         

