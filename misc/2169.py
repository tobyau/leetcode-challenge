class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        '''
        subtract larger number by smallest until zero 
        return answer if either num1 or num2 is zero 
        '''
        operations = 0 

        while num1 != 0 and num2 != 0:
            if num1 >= num2: 
                num1 -= num2 
            else:
                num2 -= num1 
            
            operations += 1 
        
        return operations 
        
