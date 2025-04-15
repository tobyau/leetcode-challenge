class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        '''
        1. get words that make a line within maxWidth
        2. create line with spaces if necessary to reach maxWidth 
        3. put it all together 
        '''
        def getWords(i):
            curr_line = [] 
            curr_len = 0 

            while i < len(words) and curr_len + len(words[i]) <= maxWidth:
                curr_line.append(words[i]) 
                curr_len += len(words[i]) + 1
                i += 1 
            
            return curr_line 
        
        def createLine(line, i):
            base_len = -1 
            for word in line:
                base_len += len(word) + 1 
            
            extra_spaces = maxWidth - base_len

            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extra_spaces
            
            # find how many spaces needed 
            word_count = len(line) - 1 
            spaces_per_word = extra_spaces // word_count 
            needs_extra_space = extra_spaces % word_count 

            for j in range(needs_extra_space):
                line[j] += " "
            
            for j in range(word_count):
                line[j] += " " * spaces_per_word 
            
            return " ".join(line) 
        
        res = [] 
        i = 0 

        while i < len(words):
            curr_line = getWords(i) 
            i += len(curr_line) 
            res.append(createLine(curr_line, i))
        
        return res 

