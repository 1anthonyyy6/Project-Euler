"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
from math import sqrt; 

def word2num(word):
    sum = 0;
    for i in word:
        sum += ord(i) - 64;
    return sum;

def ifTriangleNumber(num):
    n = (sqrt(1 + 8 * num) - 1)/2;
    if (n).is_integer():
        return True;
    else:
        return False;

words = []; 
r = open('p042_words.txt');
str = r.read();
str = str.replace("\"","");
words = str.strip().split(',');
count = 0;
for i in words:
    if ifTriangleNumber(word2num(i)):
        count += 1;
print(count);
