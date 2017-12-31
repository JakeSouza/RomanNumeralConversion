'''
Created on Dec 30, 2017

@author: Jake
'''
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #turn string into list of chars
        numerals = list(s)
        #dictionary containing all numerals with corresponding values
        comp = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        #make array with value bigger than any Roman numerals
        arr = [1001]
        count = 0
        total = 0
        #for each roman numeral
        for x in numerals:
            #convert into an integer
            temp = comp[x]
            #if this int is larger than the last, take off last from total and add difference instead
            if(temp > arr[count]):
                total -= arr[count]
                total += (temp - arr[count])
            #else add the integer to the total
            else:
                total += temp
            arr.append(temp)
            count += 1

        return total    