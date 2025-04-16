'''
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

'''

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def getWords(i):
            # get words for a single line within maxwidth 
            curr_line = [] 
            curr_len = 0 

            while i < len(words) and curr_len + len(words[i]) <= maxWidth:
                curr_line.append(words[i])
                curr_len += len(words[i]) + 1 
                i += 1 
            
            return curr_line 

        def createLine(line, i):
            # using words in line, create a line of words with spaces 
            # count line length 
            base_len = -1 
            for word in line:
                base_len += len(word) + 1 

            extra_spaces = maxWidth - base_len 
            # edge case: one word in line or last word
            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extra_spaces 
            
            word_count = len(line) - 1 
            # count spaces needed between words 
            spaces_between = extra_spaces // word_count 
            # spaces needed after last word 
            spaces_after = extra_spaces % word_count 

            # add spaces between words 
            for j in range(word_count):
                line[j] += " " * spaces_between
            # add extra spaces 
            for j in range(spaces_after):
                line[j] += " "
            
            return " ".join(line) 
        
        res = [] 
        i = 0 

        while i < len(words): 
            curr_line = getWords(i)
            i += len(curr_line) 
            res.append(createLine(curr_line, i))
        
        return res 