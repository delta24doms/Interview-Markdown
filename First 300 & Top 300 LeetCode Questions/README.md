# First 300 & Top 300 LeetCode Questions


[OCTOBER 14, 2017](https://nishmathcs.wordpress.com/2017/10/14/first-300-leetcode-questions/) / [NISHANTHCALTECH](https://nishmathcs.wordpress.com/author/nishanthcaltech/)


### 1. Two Sum


Problem: Two numbers in an array sum to a target, find them. 


This is one is pretty straight forward. Hash ![target - arr[i]](img/latex-php) and keep on looking for it. If no space is allowed all you have to do is sort the list, and approach from either end decrementing the tail pointer or incrementing the head pointer based on whether or not the current sum is below or above the target.


### 2. Add Two Numbers


Problem: Two numbers are represented by linked lists, add them. 


Reverse the lists, add the lists while keep a carry going forward, at the end create a new node if necessary, reverse the list again.


### 3. Longest Substring Without Repeated Characters


Problem: Name says it all


Keep a hashmap of all the characters possible, with the key being the character and the value being the index it was last seen at. Keep start and end pointers, and advance them forward while updating this hashmap, and moving the start pointer forward when needed. The start pointer is updated based of the hashed location, (move it one after it). 


### 4. Median Of Two Sorted Arrays


Problem: Name says it all


`def` `findkth(l1, m, l2, n, k):`


`if` `m > n:`


`return` `findkth(l2, n, l1, m, k)`


`if` `m` `=``=` `0``:`


`return` `l2[k` `-` `1``]`


`if` `k` `=``=` `1``:`


`return` `min``(l1[``0``], l2[``0``])`


`i, j` `=` `min``(m, k``/``2``),` `min``(n, k``/``2``)`


`if` `l1[i` `-` `1``] > l2[j` `-` `1``]:`


`return` `findkth(l1, m, l2[j:], n` `-` `j, k` `-` `j)`


`return` `findkth(l1[i:], m` `-` `i, l2, n, k` `-` `i)`


`ind1` `=` `(``len``(nums1)` `+` `len``(nums2)` `+` `2``)``/``2`


`ind2` `=` `(``len``(nums1)` `+` `len``(nums2)` `+` `1``)``/``2`


`return` `(findkth(nums1,` `len``(nums1), nums2,` `len``(nums2), ind1)`


`+` `findkth(nums1,` `len``(nums1), nums2,` `len``(nums2), ind2))``/``2.0`


|


The trick here is to write the ![findkth](img/latex-php) function,\
which runs in ![O(log(n))](img/latex-php) time, and then this program happens entirely in ![O(log(n))](img/latex-php) time. Read code for additional details. Simple recursion if you understand it.


### 5. Longest Palindromic Substring


Problem: Name says it all. 


The key observation here is that you as you add one letter to a string, the max palindrome length increases by either 1 or 2 (if the new max palindrome holds the character you just added). So, you can greedily go through the list, and check if the last ![P + 1](img/latex-php) characters or ![P + 2](img/latex-php) characters are a palindrome. Checking if a string is a palindrome is ![O(n)](img/latex-php) so the entire algorithm comes out to ![O(n^2)](img/latex-php) time and ![O(1)](img/latex-php) space.


### 6. ZigZag Conversion


Problem: Need to see it graphically, go look at this one.


`def` `convert(``self``, s, numRows):`


`"""`


`:type s: str`


`:type numRows: int`


`:rtype: str`


`"""`


`ans` `=` `[]`


`period` `=` `max``(``1``,``2``*``numRows` `-` `2``)`


`for` `i` `in` `range``(numRows):`


`k` `=` `i`


`while` `k <` `len``(s):`


`ans` `+``=` `s[k]`


`k` `+``=` `period` `-` `((``2` `*` `k)` `%` `period)`


`return` `''.join(ans)`


|


Takes two minutes to understand. The one tricky part is ![k += period - ((2 * x) \% period)](img/latex-php). This is because this is how you advance to the next number in the same congruence class, in ![\mod period](img/latex-php).


### 7. Reverse Integer


Problem: Name says it all


`def` `reverse\_integer(x):`


`# Not shown, but handle case of negative input.`


`tmp` `=` `0`


`while` `(x):`


`tmp` `*``=` `10`


`tmp` `+``=` `x` `%` `10`


`x` `/``=` `10`


`return` `tmp`


|


### 8. Atoi


Problem: String to integer conversion


String to integer. Use a state machine if needed, otherwise bash it out. Easy.


### 9. Palindrome Number


Problem: Name says it all


Check if the number is equal to itself reversed, use problem 7 solution if needed.


### 10. Regular Expression Matching


Problem: Implement Regular expression checking for regular expressions with "." and "*"


`def` `Match(s, p):`


`# Let dp[i][j] = isMatch(s[:i], p[:j])`


`dp` `=` `[[``0` `for` `i` `in` `range``(``len``(p)` `+` `1``)]` `for` `j` `in` `range``(``len``(s)` `+` `1``)]`


`# Obviously the empty strings match.`


`dp[``0``][``0``]` `=` `1`


`# So the string can sometimes match with`


`# the empty string.`


`for` `i` `in` `range``(``2``,` `len``(dp[``0``])):`


`dp[``0``][i]` `=` `int``((p[i` `-` `1``]` `=``=` `'*'` `and` `dp[``0``][i` `-` `2``]))`


`for` `i` `in` `range``(``1``,` `len``(dp)):`


`for` `j` `in` `range``(``1``,` `len``(dp[``0``])):`


`# Obvious case when matching happens.`


`if` `s[i` `-` `1``]` `=``=` `p[j` `-` `1``]` `or` `p[j` `-` `1``]` `=``=` `'.'``:`


`dp[i][j]` `=` `dp[i` `-` `1``][j` `-` `1``]`


`elif` `p[j` `-` `1``]` `=``=` `'*'``:`


`# If they dont match right before, look two characters ago.`


`if` `s[i` `-` `1``] !``=` `p[j` `-` `2``]` `and` `p[j` `-` `2``] !``=` `'.'``:`


`dp[i][j]` `=` `dp[i][j` `-` `2``]`


`else``:`


`dp[i][j]` `=` `dp[i][j` `-` `1``]` `or` `dp[i` `-` `1``][j]` `or` `dp[i][j` `-` `2``]`


`return` `True` `if` `dp[``-``1``][``-``1``]` `else` `False`


|


Easy to understand from the code, very common question.


### 11. Container With Most Water


Problem: An array of values containing wall heights, find container with most water.


Start with the widest container. Now decrease the width by one, and choose the height that is higher among the boundaries to remain. We can safely remove the other one without affecting the maximum.


### 12. Integer To Roman


Problem: Name says it all


Create dictionary. Convert one digit at a time, passing in the tens, five, and one digit character as you do it.


### 13. Roman To Integer


Problem: Name says it all


Create a dictionary. If the preceding character is less than the next character, subtract their worth and add that to the total. Proceed till entire string is processed.


### 14. Longest Common Prefix


Problem: Name says it all


Keep advancing pointers in all the strings until you don't find a match.


### 15. 3Sum


Problem: Name says it all


You can either do this with two sum, and have a quadratic run time, or simply sort the array, hold one index fixed at a time, then do two sum (sorted technique), which will give also give you a quadratic running time.


### 16. 3Sum Closest


Problem: Name says it all


Sort and then do same thing as before, except keep track of the closest you got. Quadratic running time.


### 17. Letter Combinations Of A Phone Number


Problem: A phone number, what words can it make?


`digit\_to\_string` `=` `{``'1'``: [``'*'``],`


`'2'``: [``'a'``,` `'b'``,` `'c'``],`


`'3'` `: [``'d'``,` `'e'``,` `'f'``],`


`'4'` `: [``'g'``,` `'h'``,` `'i'``],`


`'5'` `: [``'j'``,` `'k'``,``'l'``],`


`'6'` `: [``'m'``,` `'n'``,` `'o'``],`


`'7'` `: [``'p'``,` `'q'``,` `'r'``,` `'s'``],`


`'8'` `: [``'t'``,``'u'``,` `'v'``],`


`'9'``: [``'w'``,` `'x'``,` `'y'``,` `'z'``]}`


`if` `digits` `=``=` `"":`


`return` `[]`


`list` `=` `reduce``(``lambda` `lst, new\_num: [x` `+` `[y]` `for` `y` `in` `digit\_to\_string[new\_num[``0``]]` `for` `x` `in` `lst],`


`[[x]` `for` `x` `in` `digits],`


`[[]])`


`return` `[''.join(w)` `for` `w` `in` `list``]`


|


Pretty cool little ditty above, self explanatory.


### 18. 4Sum


Problem: Name says it all


Call 3Sum


### 19. Remove Nth Node From End Of List


Problem: Name says it all


Two pointer scan, delete node in place.


### 20. Valid Parentheses


Problem: Name says it all


Specifically, given an expression, is it valid?


Keep a counter of left and right, that needs to never trip and has to end with 0 and you're good.


### 21. Merge Two Sorted Lists


Problem: Name says it all


lol


### 22. Generate Parentheses


Problem: Generate all possible strings with n parentheses


DFS, keep track of how many left and right parentheses there are left to add and pass that along.


### 23. Merge K Sorted Lists


Problem: Name says it all


Priority Queue, you can do it in ![O(n * log(k))](img/latex-php).


### 24. Swap Nodes In Pairs


Problem: Name says it all


`def` `swapPairs(``self``, head):`


`pre, pre.``next` `=` `self``, head`


`while` `pre.``next` `and` `pre.``next``.``next``:`


`a` `=` `pre.``next`


`b` `=` `a.``next`


`pre.``next``, b.``next``, a.``next` `=` `b, a, b.``next`


`pre` `=` `a`


`return` `self``.``next`


|


Reasonably easy to understand.


### 25. Reverse Nodes In K-Group


Problem: Name says it all


`def` `reverseKGroup(``self``, head, k):`


`dummy` `=` `jump` `=` `ListNode(``0``)`


`dummy.``next` `=` `l` `=` `r` `=` `head`


`while` `True``:`


`count` `=` `0`


`while` `r` `and` `count < k:` `# use r to locate the range`


`r` `=` `r.``next`


`count` `+``=` `1`


`if` `count` `=``=` `k:` `# if size k satisfied, reverse the inner linked list`


`pre, cur` `=` `r, l`


`for` `\_` `in` `range``(k):`


`cur.``next``, cur, pre` `=` `pre, cur.``next``, cur` `# standard reversing`


`jump.``next``, jump, l` `=` `pre, l, r` `# connect two k-groups`


`else``:`


`return` `dummy.``next`


|


### 26. Remove Duplicates From Sorted Array


Problem: Name says it all


Scanning index, insertion index.


### 27. Remove Element


Problem: Name says it all


Have a scanning index, and insertion index, and return the scanning index.


### 28. isSubstring


Problem: Name says it all


`def` `is\_substring(haystack, needle):`


`"""`


`:type haystack: str`


`:type needle: str`


`"""`


`# Understand KMP`


`if` `needle` `=``=` `"":`


`return` `0`


`# First we have to do preprocessing on the needle.`


`# We will calculate its lps, and return this list.`


`def` `preprocessing(needle):`


`# lps[i] will be the length of the longest proper`


`# suffix of lps[:i + 1] that is also a prefix.`


`lps` `=` `[``0` `for` `i` `in` `range``(``len``(needle))]`


`length` `=` `0`


`i` `=` `0`


`# Obviously lps[0] = 0`


`lps[``0``]` `=` `length`


`i` `+``=` `1`


`# Now we process the rest of the list.`


`while` `i <` `len``(lps):`


`# If they match, we advance both.`


`if` `needle[i]` `=``=` `needle[length]:`


`length` `+``=` `1`


`lps[i]` `=` `length`


`i` `+``=` `1`


`else``:`


`# If length is 0, advance i forward`


`if` `length` `=``=` `0``:`


`lps[i]` `=` `length`


`i` `+``=` `1`


`# Otherwise slide it back just as much as`


`# we need.`


`else``:`


`length` `=` `lps[length` `-` `1``]`


`return` `lps`


`# Process the lists, by keeping pointers for both.`


`i` `=` `0`


`j` `=` `0`


`lps` `=` `preprocessing(needle)`


`while` `i <` `len``(haystack):` `# Advance the pointers if they match.         if haystack[i] == needle[j]:             i += 1             j += 1             if j == len(needle):                 return True         # Otherwise move it back just as much as we need.         elif j > 0:`


`j` `=` `lps[j` `-` `1``]`


`# Worst case we move it forward`


`else``:`


`i` `+``=` `1`


`return` `False`


|


My comments explain it well in my opinion, so I'll leave it to them.


### 29. Divide Two Integers


Problem: Name says it all


The most basic way is to use the Euclidean algorithm, if not, experiment with bit shifting. TBH don't feel like explaining this problem.


### 30. Substring Concatenation Of All Words


Problem: You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.


Implement with a sliding window and a hash table.


### 31. Next Permutation


Problem: Given a string, and a comparator, return the next permutation


From the back of the number, proceed backwards while it's still increasing. If it's increasing all the way (seen backwards), return the number reversed. However, if you reach a point where the number became smaller, then find the smallest number in the tail of the string that is larger than this, and swap the two. Then reverse the tail, and you're good. All of it done in ![O(n)](img/latex-php) time.


### 32. Longest Valid Parantheses


Problem:  Given a string containing just the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.


For `"(()"`, the longest valid parentheses substring is `"()"`, which has length = 2.


Another example is `")()())"`, where the longest valid parentheses substring is `"()()"`, which has length = 4.


`def` `longestValidParentheses(``self``, s):`


`"""`


`:type s: str`


`:rtype: int`


`"""`


`# If its empty string, we simply return 0`


`if` `s` `=``=` `"":`


`return` `0`


`# dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]`


`dp` `=` `[``0` `for` `\_` `in` `s]`


`for` `i,c` `in` `enumerate``(s):`


`# if c == '(', obviously we will have dp[i] = 0, so we skip that.`


`if` `c` `=``=` `")"``:`


`# First case is when it ends with '.....()'`


`if` `i` `-` `1` `>``=` `0` `and` `s[i]` `=``=` `"("``:`


`dp[i]` `=` `2`


`if` `i` `-` `2` `>``=` `0``:`


`dp[i]` `+``=` `dp[i` `-` `2``]`


`# Second case is when we have '....(|..VALID...|)' where the`


`# string in between the "|...|" is a valid paranthetical`


`# expression.`


`elif` `i` `-` `dp[i` `-` `1``]` `-` `1` `>``=` `0` `and` `s[i` `-` `dp[i` `-` `1``]` `-` `1``]` `=``=` `"("``:`


`dp[i]` `=` `2` `+` `dp[i` `-` `1``]`


`if` `i` `-` `dp[i` `-` `1``]` `-` `2` `>``=` `0``:`


`dp[i]` `+``=` `dp[i` `-` `dp[i` `-` `1``]` `-` `2``]`


`return` `max``(dp)`


|


The comments should explain my work.


### 33. Search In A Rotated Array


Problem: Name says it all


We can do binary search. When we examine the ![mid](img/latex-php) element, if it is the element we want, we return it. If not, we first check whether ![nums[low:mid]](img/latex-php) is in the increasing section of the array, or not. We do this check by comparing ![nums[low]](img/latex-php) with ![nums[mid]](img/latex-php).


For the first case, pretend we are in the increasing section. If we have ![nums[low] <= target <= nums[mid]](img/latex-php) then we move left, and if not, we move right. Simple enough.


Now for the second case. If we have ![nums[mid] <= target <= nums[high]](img/latex-php), then we move right, and if not, we move left.


### 34. Search For A Range


Problem: Name says it all


We're going to do binary search twice, first for the lower index then the higher index. Basic rules of update you can figure it out.


### 35. Search For Insert Position


Problem: Name says it all. 


Do binary search, and at the end of the loop, just return ![mid](img/latex-php) or ![mid + 1](img/latex-php) it will be one of those two.


### 36. Valid Sudoku


Problem: Name says it all


Keep hashmaps for boxes, columns, and rows, and return False if it is ever present, otherwise return true.


### 37. Sudoku Solver


Problem: Name says it all


Do some form of DFS, and keep increasing the number until it is valid. If you get to 9, have a back pointer to the last number.


### 38. Count and Say


Problem: Name says it all


The next function is pretty trivial, just call it as many times as necessary.


### 39. Combination Sum


Problem: Find all unique combinations that sum up to some target. 


Simple DFS, passing in ![path, currentTarget](img/latex-php) to each call. Adding to a global array as we go along.


### 40. Combination Sum II


Problem: Same as previous problem but now there are duplicates. 


First we sort the list, then we pass in ![path, start, currentTarget](img/latex-php) to each call. Add to a global array as we go along.


We will call on the ![start](img/latex-php) index no matter what. After, we don't call it on indices that are the same before, and we pass ![i + 1](img/latex-php) as the ![start](img/latex-php) argument for those.


### 41. First Missing Positive


Problem: Name says it all


First of all, 0 all of the numbers that are negative or exceed the max size possible. Then on a second pass, put them all in the index specified by their value. On the third pass, go forward till you see a mismatch, and then return that number.


### 42. Trapping Rain Water


Problem: Given height of lists, return how much water has been trapped. 


The obvious way will be ![O(n)](img/latex-php) time and ![O(n)](img/latex-php) space. Have two arrays, ![left](img/latex-php) and ![right](img/latex-php), where ![left[i]](img/latex-php) is the tallest bar to the left of index ![i](img/latex-php), including ![arr[i]](img/latex-php). ![right](img/latex-php) is defined similarly. Now, we simply have to keep adding ![min(left[i], right[i]) - arr[i])](img/latex-php).\
Start with ![minHeight = 0](img/latex-php). Have a ![left](img/latex-php) and ![right](img/latex-php) pointers at both ends of the list. Now, run a loop while ![left < right](img/latex-php). This condition is important, note that its not ![left <= right](img/latex-php). Advance ![left](img/latex-php) or decrement ![right](img/latex-php) while it's greater than ![minHeight](img/latex-php) on each iteration, while adding the respective amount of extra water. Then, let ![minHeight = min(left, right)](img/latex-php). Return the total amount of water.  


### 43. Multiply Strings


Problem: Name says it all 


Implement it how you would implement grade school multiplication.


### 44. Wildcard Matching


Problem: Classic wildcard matching


`def` `isMatch(s, p):`


`"""`


`:type s: str`


`:type p: str`


`:rtype: bool`


`"""`


`pointer\_s` `=` `0`


`pointer\_p` `=` `0`


`star\_index` `=` `-``1`


`match` `=` `0`


`while` `pointer\_s <` `len``(s):`


`if` `(pointer\_p <` `len``(p))` `and` `(s[pointer\_s]` `=``=` `p[pointer\_p]` `or` `p[pointer\_p]` `=``=` `'?'``):`


`pointer\_s` `+``=` `1`


`pointer\_p` `+``=` `1`


`elif` `pointer\_p <` `len``(p)` `and` `p[pointer\_p]` `=``=` `'*'``:`


`star\_index` `=` `pointer\_p`


`pointer\_p` `+``=` `1`


`match` `=` `pointer\_s`


`elif` `star\_index !``=` `-``1``:`


`pointer\_p` `=` `star\_index` `+` `1`


`match` `+``=` `1`


`pointer\_s` `=` `match`


`else``:`


`return` `False`


`while` `pointer\_p <` `len``(p):`


`if` `p[pointer\_p]` `=``=` `'*'``:`


`pointer\_p` `+``=` `1`


`else``:`


`break`


`return` `(pointer\_p` `=``=` `len``(p))`


|


### 45. Jump Game II


Problem:


Given an array of non-negative integers, you are initially positioned at the first index of the array.


Each element in the array represents your maximum jump length at that position.


Your goal is to reach the last index in the minimum number of jumps.


For example:\
Given array A = `[2,3,1,1,4]`


Keep a window for each step, and try and expand that window as much as possible by jumping from that window, and increment the step you're on.


![Screen Shot 2017-10-13 at 7.24.25 PM](img/screen-shot-2017-10-13-at-7-24-25-pm-png)


### 46. Permutations


Problem: Return all permutations of an array in lexicographic order.


Write a next permutation function, and do it from sorted to reverse sorted.


Or there's also a smarter way to do this.


`void` `recursion(vector<``int``> num,` `int` `i,` `int` `j, vector<vector<``int``> > &res) {`


`if` `(i == j-1) {`


`res.push\_back(num);`


`return``;`


`}`


`for` `(``int` `k = i; k < j; k++) {`


`if` `(i != k && num[i] == num[k])` `continue``;`


`swap(num[i], num[k]);`


`recursion(num, i+1, j, res);`


`}`


`}`


`vector<vector<``int``> > permuteUnique(vector<``int``> &num) {`


`sort(num.begin(), num.end());`


`vector<vector<``int``> >res;`


`recursion(num, 0, num.size(), res);`


`return` `res;`


`}`


|


### 47. Permutations II


Problem: Return all permutations of an array in lexicographic order, this time, list may have repetitions. 


See the previous problem.


### 48. Rotate Image


Problem: Rotate n x n array. 


Do it by layer, kind of a bitchy problem but you got it.


### 49. Group Anagrams


Problem: Given a list of strings, group the strings that are anagrams of each other.


Hashing based off prime numbers, or perhaps sort them.


### 50. Pow(x,n)


Problem: Raise a number to the nth power.  


Do it based off the binary representation of ![n](img/latex-php) and keep squaring the numbers.


### 51. N -- Queens


Problem: Where to put N Queens on a chess board so that none of them are intersecting each other?


DFS, but keep pass in the path, difference, and sum arrays as you go along. Append to a global array.


### 52. N -- Queens II


Problem: How many solutions exist?


Same thing, just increment a counter.


### 53. Maximum Subarray


Problem: Which subarray has the greatest sum? 


Keep adding the numbers, and let ![currentSum = \max (currentSum, 0)](img/latex-php). Return the largest sum so far.


My boy Kadane's algorithm. The largest subarray up to a point either has the current point, or starts with it. Done.


### 54. Spiral Matrix


Problem: Print out a matrix in spiral form 


Set ![i,j = 0,0](img/latex-php). Initialize ![di, dj = 0, 1](img/latex-php). Loop through all the length of the matrix, and then increment ![i](img/latex-php) by ![di](img/latex-php) each time and ![j](img/latex-php) by ![dj](img/latex-php) each time and if we reach a corner, do ![di, dj = dj, -1* di](img/latex-php). This requires space however, you can do it more intelligently if you're more careful.


`def` `spiralOrder(``self``, matrix):`


`if` `not` `matrix:`


`return` `matrix`


`ans` `=` `[]`


`num\_layers` `=` `(``min``(``len``(matrix),``len``(matrix[``0``]))` `+` `1``)``/``2`


`row\_begin,row\_end, col\_begin, col\_end` `=` `0``,``len``(matrix)` `-` `1``,` `0``,` `len``(matrix[``0``])` `-` `1`


`for` `t` `in` `range``(num\_layers):`


`if` `row\_begin <``=` `row\_end:`


`for` `j` `in` `range``(col\_begin, col\_end` `+` `1``):`


`ans.append(matrix[row\_begin][j])`


`row\_begin` `+``=` `1`


`if` `col\_begin <``=` `col\_end:`


`for` `j` `in` `range``(row\_begin, row\_end` `+` `1``):`


`ans.append(matrix[j][col\_end])`


`col\_end` `-``=` `1`


`if` `row\_begin <``=` `row\_end:`


`for` `j` `in` `range``(col\_end,col\_begin` `-` `1``,` `-``1``):`


`ans.append(matrix[row\_end][j])`


`row\_end` `-``=``1`


`if` `col\_begin <``=` `col\_end:`


`for` `j` `in` `range``(row\_end, row\_begin` `-` `1``,` `-``1``):`


`ans.append(matrix[j][col\_begin])`


`col\_begin` `+``=` `1`


`return` `ans`


|


### 55. Jump Game


Problem: Can you get to the end? By jumping at most the number indicated by the number stored at an index. 


`def` `canJump(``self``, nums):`


`m` `=` `0`


`for` `i, n` `in` `enumerate``(nums):`


`if` `i > m:`


`return` `False`


`m` `=` `max``(m, i``+``n)`


`return` `True`


|


### 56. Merge Intervals


Problem: Given a bunch of intervals, merge them all.


`def` `merge(``self``, intervals):`


`"""`


`:type intervals: List[Interval]`


`:rtype: List[Interval]`


`"""`


`ans` `=` `[]`


`for` `i` `in` `sorted``(intervals, key` `=` `lambda` `a: a.start):`


`if` `ans` `and` `ans[``-``1``].end >``=` `i.start:`


`ans[``-``1``].end` `=` `max``(i.end, ans[``-``1``].end)`


`else``:`


`ans.append(i)`


`return` `ans`


|


### 57. Insert Intervals


Problem: Add in an interval and simplify


Just use the previous solution and add in the interval.


### 58. Length Of Last Word


Problem: Name says it all.


lol


### 59. Spiral Matrix II


Problem: Same as spiral matrix I


See Spiral Matrix I


### 60. Permutation Sequence


Problem: Output all permutations 


Use next permutation function.


### 61. Rotate List


Problem: Given A Linked List, rotate it K places.


Reverse first ![n - k](img/latex-php) elements, rotate last ![k](img/latex-php) elements, rotate entire list.


### 62. Unique Paths


Problem: How many paths down are there?


Simple DP. Or, you can also just do a math solution, combinatorial argument.


### 63. Unique Paths II


Problem: Something trivial


Simple DP


### 64. Minimum Path Sum


Problem: Given a m x n grid, best path from top left corner to top right corner. T


Simple DP, bottom up fill in. (top down works too)


### 65. Valid Number


Problem: Given A String, is it a number or not?


State diagram. Maybe regular expressions?


### 66. Plus One


Problem: Add 1 To A Number Represented By List/Linked List


Simple logic, for loop and have a carry.  Reverse the array in the beginning. You can also do it recursively quite easily.


`def` `plusOne(``self``, digits):`


`"""`


`:type digits: List[int]`


`:rtype: List[int]`


`"""`


`if` `digits` `=``=` `[]:`


`return` `[``1``]`


`if` `digits[``-``1``]` `=``=` `9``:`


`return` `self``.plusOne(digits[:``-``1``])` `+` `[``0``]`


`else``:`


`return` `digits[:``-``1``]` `+` `[digits[``-``1``]` `+` `1``]`


|


### 67. Add Binary


Problem: Given two binary strings given by strings, add them. 


Very easy recursive solution.


### 68. Text Justification


Problem: Given a bunch of lines of text, center them. 


This question is pretty freaking hard I won't sugercoat it.


I'll eventually come to explain this question, as well as the pretty printing problem which is quite similar to this.


### 69. Square Root X


Problem: Name says it all


I think this is a good time to recall Newton's method. Start with some guess ![a_0](img/latex-php) as a guess to the root of ![f(x)](img/latex-php). Then periodically do ![a_{i + 1} = a_{i} - \frac{f(a)}{f](img/latex-php).


### 70. Climbing Stairs


Problem: You can either skip 1 step or skip 2 steps, how many ways to get to the top?


One answer would be simple DP. But since you only need to keep track of ![dp[i - 1], dp[i - 1]](img/latex-php), we can simply do this with the use of constants.


### 81. Search In Rotated Sorted Array II


Problem: Name says it all


If duplicates are allowed, the best you can do is ![O(n)](img/latex-php).


### 82. Remove Duplicates From A Sorted List II


Problem: Name Says it all


Obvious


### 83. Remove Duplicates From A Sorted List


Problem: Name says it all


Obvious


### 84. Largest Rectangle In A Histogram


Problem: Name says it all


`def` `largestRectangleArea(``self``, height):`


`height.append(``0``)`


`stack` `=` `[``-``1``]`


`ans` `=` `0`


`for` `i` `in` `xrange``(``len``(height)):`


`while` `height[i] &lt; height[stack[``-``1``]]:`


`h` `=` `height[stack.pop()]`


`w` `=` `i` `-` `stack[``-``1``]` `-` `1`


`ans` `=` `max``(ans, h` `*` `w)`


`stack.append(i)`


`height.pop()`


`return` `ans`


|


Come back to this guy.


### 85. Maximal Rectangle


Problem: Name says it all


Just do this using maximum histogram, and you're good.


### 86. Partition List


Problem: Name says it all


`def` `partition(``self``, head, x):`


`h1` `=` `l1` `=` `ListNode(``0``)`


`h2` `=` `l2` `=` `ListNode(``0``)`


`while` `head:`


`if` `head.val &lt; x:`


`l1.``next` `=` `head`


`l1` `=` `l1.``next`


`else``:`


`l2.``next` `=` `head`


`l2` `=` `l2.``next`


`head` `=` `head.``next`


`l2.``next` `=` `None`


`l1.``next` `=` `h2.``next`


`return` `h1.``next`


|


### 87. Scramble String


Problem: 


Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.


Below is one possible representation of s1 = "great":


great\
/ \
gr eat\
/ \ / \
g r e at\
/ \
a t


To scramble the string, we may choose any non-leaf node and swap its two children.


For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".


rgeat\
/ \
rg eat\
/ \ / \
r g e at\
/ \
a t


We say that "rgeat" is a scrambled string of "great".


Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".


rgtae\
/ \
rg tae\
/ \ / \
r g ta e\
/ \
t a


We say that "rgtae" is a scrambled string of "great".


Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.


If they are equal to each other, then its True. If they have different length, it's False. If they are not anagrams, return False. After that, loop through the length of the strings. If isScramble(l1[:i], l2[:i]) && isScramble(l1[i:], l2[i:]) then return True. Also, if isScramble(l1[:i], l2[i:]) && isScramble(l1[i:], l2[:i]) then return True. Otherwise return False.


### 88. Merge Sorted Array


Problem: Name says it all


lol


### 89. Gray Code


Problem: Successive numbers differ by exactly one bit.


Start with the gray code of for ![n = 1](img/latex-php) being 0, 1. Now, when you want to increase, reverse the list, and add a ![1](img/latex-php) bit at the front for the reversed list, then concatenate both the straight list and the reversed modified list. So for ![n = 3](img/latex-php), this transforms to 00, 01, 11, 10.


### 90. Subsets II


Problem: Find all subsets, except with duplicates


Have a dictionary storing how many times each of the characters appeared. Then you can do the reduce technique again, except keep adding it ![n](img/latex-php) times.


### 91. Decode Ways


Problem: Number of ways to decode a number to strings. For example, "121" can be read as "ABA" or "LA" or "AU".


Trivial DP, but since you just need last two numbers, you can just keep track of those instead.


### 92. Reverse Linked List II


Problem: Reverse a linked list between two nodes


Just an exercise in coding. You got this.


### 93. Restore IP Addresses


Problem: Given a string of numbers, find all possible IP addresses it can correspond to.


Basic DFS, pretty sure you can do this one too.


### 94. Binary Tree Inorder Traversal


Problem: Name says it all


`def` `inorderTraversal(``self``, root):`


`"""`


`:type root: TreeNode`


`:rtype: List[int]`


`"""`


`if` `not` `root:`


`return` `[]`


`current` `=` `root`


`ans` `=` `[]`


`stack` `=` `[]`


`done` `=` `False`


`while` `not` `done:`


`if` `current:`


`stack.append(current)`


`current` `=` `current.left`


`else``:`


`if` `len``(stack)` `=``=` `0``:`


`done` `=` `True`


`else``:`


`current` `=` `stack.pop()`


`ans.append(current.val)`


`current` `=` `current.right`


`return` `ans`


|


### 95. Unique Binary Search Trees II


Problem: Name says it all


Same as the DP approach, but hold the trees now instead.


### 96. Unique Binary Search Trees


Problem: Name says it all


Easy DP. Hold the root fixed, then you want some number of nodes on the left and some number of nodes on the right. Very straightforward.


`def generateTrees(self, n):`


`if n == 0:`


`return []`


`def node(val, left, right):`


`node = TreeNode(val)`


`node.left = left`


`node.right = right`


`return node`


`def trees(first, last):`


`return [node(root, left, right)`


`for root in range(first, last+1)`


`for left in trees(first, root-1)`


`for right in trees(root+1, last)] or [None]`


`return trees(1, n)`


|


Or do it this way, your call.


### 97. Interleaving String


Problem: Find if a third string can be made by interleaving two given strings.


Trivial DP. Lol this is "hard" on LQ


### 98. Validate Binary Search Tree


Problem: Validate if a tree is a binary search tree. 


In order traversal, check if everything is increasing. This is a super super cool problem because you can do this in ![O(1)](img/latex-php) space using Morris Traversal. I'll leave you to figure out the answer to this problem, but ill leave the Morris Traversal code right here.


`def` `find\_pred(current):`


`tmp` `=` `current.left`


`while` `tmp.right` `and` `tmp.right !``=` `current:`


`tmp` `=` `tmp.right`


`return` `tmp`


`def` `MorrisTraversal(root):`


`current` `=` `root`


`ans` `=` `[]`


`while` `current:`


`if` `not` `current.left:`


`ans.append(current.val)`


`current` `=` `current.right`


`else``:`


`pred` `=` `find\_pred(current)`


`if` `not` `pred.right:`


`pred.right` `=` `current`


`current` `=` `current.left`


`else``:`


`pred.right` `=` `None`


`ans.append(current.val)`


`current` `=` `current.right`


`return` `ans`


|


### 99. Recover Binary Search Tree


Problem: Somebody switched two nodes, find and fix.


Morris Traversal, but you'll see one spike and one well. Switch those two, and you're done.


### 100. Same Tree


Problem: Check if two trees are the same or not. 


Recursion, any type of traversal, whatever you want tbh.


### 101. Symmetric Tree


Problem: Is a tree symmetric?


Trivial recursive solution.


### 102. Level Order Traversal


Problem: Name says it all. 


`def` `levelOrder(``self``, root):`


`"""`


`:type root: TreeNode`


`:rtype: List[List[int]]`


`"""`


`if` `not` `root:`


`return` `[]`


`q` `=` `deque()`


`q.append(root)`


`ans` `=` `[]`


`level` `=` `[]`


`curr\_level` `=` `1`


`next\_level` `=` `0`


`while` `q:`


`curr` `=` `q.popleft()`


`level.append(curr.val)`


`curr\_level` `-``=` `1`


`if` `curr.left:`


`next\_level` `+``=` `1`


`q.append(curr.left)`


`if` `curr.right:`


`next\_level` `+``=` `1`


`q.append(curr.right)`


`if` `curr\_level` `=``=` `0``:`


`curr\_level` `=` `next\_level`


`next\_level` `=` `0`


`ans.append(level)`


`level` `=` `[]`


`return` `ans`


|


### 103. Binary Tree Zigzag Level Order


Problem: Name says it all


Easy from the last problem.


### 104. Maximum Depth Of Binary Tree


Problem: Name says it all


Easy recursion.


### 105. Construct Binary Tree From Preorder And Inorder Traversal


Problem: Name says it all


`def` `buildTree(``self``, preorder, inorder):`


`"""`


`:type preorder: List[int]`


`:type inorder: List[int]`


`:rtype: TreeNode`


`"""`


`preorder` `=` `deque(preorder)`


`def` `recur(preorder, inorder):`


`if` `len``(preorder)` `=``=` `0` `or` `len``(inorder)` `=``=` `0``:`


`return` `None`


`root` `=` `TreeNode(preorder[``0``])`


`preorder.popleft()`


`i\_in\_order` `=` `inorder.index(root.val)`


`root.left` `=` `recur(preorder, inorder[:i\_in\_order])`


`root.right` `=` `recur(preorder, inorder[i\_in\_order` `+` `1``:])`


`return` `root`


`return` `recur(preorder, inorder)`


|


### 106. Construct Binary Tree From Postorder And Inorder Traversal


Problem: Name says it all


`def` `buildTree(``self``, inorder, postorder):`


`"""`


`:type inorder: List[int]`


`:type postorder: List[int]`


`:rtype: TreeNode`


`"""`


`def` `recur(inorder, postorder):`


`if` `len``(inorder)` `=``=` `0` `or` `len``(postorder)` `=``=` `0``:`


`return` `None`


`root\_val` `=` `postorder.pop()`


`root` `=` `TreeNode(root\_val)`


`index\_of\_root` `=` `inorder.index(root\_val)`


`root.right` `=` `recur(inorder[index\_of\_root` `+` `1``:], postorder)`


`root.left` `=` `recur(inorder[:index\_of\_root], postorder)`


`return` `root`


`return` `recur(inorder, postorder)`


|


### 107. Binary Tree Level Order Traversal II


Problem: Name says it all


Easy, just reverse it.


### 108. Convert Sorted Array To Binary Search Tree


Problem: Name says it all


Make the middle node the root, recur on left and right sides.


### 109. Convert Sorted List To Binary Search Tree


Problem: Name says it all


You can do this recursively pretty easily. Not the best solution.


`private` `ListNode node;`


`public` `TreeNode sortedListToBST(ListNode head) {`


`if``(head ==` `null``){`


`return` `null``;`


`}`


`int` `size =` `0``;`


`ListNode runner = head;`


`node = head;`


`while``(runner !=` `null``){`


`runner = runner.next;`


`size ++;`


`}`


`return` `inorderHelper(``0``, size -` `1``);`


`}`


`public` `TreeNode inorderHelper(``int` `start,` `int` `end){`


`if``(start > end){`


`return` `null``;`


`}`


`int` `mid = start + (end - start) /` `2``;`


`TreeNode left = inorderHelper(start, mid -` `1``);`


`TreeNode treenode =` `new` `TreeNode(node.val);`


`treenode.left = left;`


`node = node.next;`


`TreeNode right = inorderHelper(mid +` `1``, end);`


`treenode.right = right;`


`return` `treenode;`


`}`


|


### 110. Balanced Binary Tree


Problem: Name says it all


Recursion, very easy.


### 111. Minimum Depth Of Binary Tree


Problem: Name says it all


Easy recursion


### 112. Path Sum


Problem: Name says it all


Recursion solution is very easy.


### 113. Path Sum II


Problem: Name says it all


Basically do backtracking, its pretty easy.


### 114. Flatten Binary Tree To Linked List


Problem: Name says it all


`def` `flatten(``self``, root):`


`if` `not` `root:`


`return`


`# using Morris Traversal of BT`


`curr` `=` `root`


`while` `curr:`


`if` `curr.left:`


`pre` `=` `curr.left`


`while` `pre.right:`


`pre` `=` `pre.right`


`pre.right` `=` `curr.right`


`curr.right` `=` `curr.left`


`curr.left` `=` `None`


`curr` `=` `curr.right`


|


Yet another application of Morris travel.


### 115. Distinct Subsequences


Problem: Count the number of distinct subsequences of one string that equal the other string.


This simple DP. If ![s[i] == t[j]](img/latex-php) then ![dp[i][j] = dp[i - 1][j - 1] + dp [i][j - 1]](img/latex-php).


`def` `numDistinct(``self``, s, t):`


`"""`


`:type s: str`


`:type t: str`


`:rtype: int`


`"""`


`if` `not` `s` `and` `not` `t:`


`return` `1`


`if` `not` `s:`


`return` `0`


`dp` `=` `[[``0` `for` `\_` `in` `range``((``len``(t)` `+` `1``))]` `for` `\_` `in` `range``((``len``(s)` `+` `1``))]`


`#dp[i][j] answers the question for numDistinct(s[:i], t[:j])`


`#dp[i][0] will be 1 because anything matches with empty string`


`for` `i` `in` `range``(``len``(dp)):`


`dp[i][``0``]` `=` `1`


`# dp[0][j] will be 0, because empty string cant contain anything`


`# Already initialized so we gucci.`


`for` `i` `in` `range``(``1``,` `len``(s)` `+` `1``):`


`for` `j` `in` `range``(``1``,` `len``(t)` `+` `1``):`


`if` `s[i` `-` `1``]` `=``=` `t[j` `-` `1``]:`


`dp[i][j]` `=` `dp[i` `-` `1``][j` `-` `1``]` `+` `dp[i` `-` `1``][j]`


`else``:`


`dp[i][j]` `=` `dp[i` `-` `1``][j]`


`return` `dp[``-``1``][``-``1``]`


|


### 116. Populating Next Right Pointers In Each Node


Problem: Name says it all


Simple level order traversal


### 117. Populating Next Right Pointers In Each Node II


Problem: Name says it all


Simple level order traversal again.


### 118. Pascal's Triangle


Problem: Name says it all


lol


### 119. Pascal's Triangle II


Problem: Name says it all


lol


### 120. Triangle


Problem: Find the minimum path down the tree


Bottom up DP, taking the minimum each time.


### 121. Best Time To Buy And Sell A Stock, One Purchase


Problem: Name says it all


If we have ![arr[0] = 0](img/latex-php) and each other index we have ![arr[i] = arr[i] - arr[i - 1]](img/latex-php). Then, this just simplifies to Kadane's maximum subarray algorithm.


### 122. Best Time To Buy And Sell A Stock, Unlimited Purchase


Problem: Name says it all


On every adjacent pair of days where we can make a profit, buy for that day.


### 123. Best Time To Buy And Sell A Stock, K Transactions


Problem: Name says it all


I've devoted an entire post to just this. Check that out it has more than enough details.


### 124. Binary Tree Maximum Path Sum


Problem: Name says it all


Given a binary tree, find the maximum path sum, a path goes through the parent to child edges. This is easy recursion. Any maximum path has the shape of an upside down ![V](img/latex-php). So, initialize the answer to be negative infinity. The following code should be easy enough to understand. ![self.ans](img/latex-php) is initialized to negative infinity.


|


`def` `maxPathSum(``self``, root):`


`"""`


`:type root: TreeNode`


`:rtype: int`


`"""`


`def` `best\_at\_root(root):`


`if` `root` `=``=` `None``:`


`return` `0`


`else``:`


`left` `=` `max``(best\_at\_root(root.left),``0``)`


`right` `=` `max``(best\_at\_root(root.right),``0``)`


`self``.ans` `=` `max``(``self``.ans, left` `+` `right` `+` `root.val)`


`return` `max``(left,right)` `+` `root.val`


`best\_at\_root(root)`


`return` `self``.ans`


|


### 125. Valid Palindrome


Problem: Name says it all


Check if a string is a palindrome, pretty easy.


### 126. Word Ladder II


Problem: Shortest transformation from begin word to end word such that only one letter can be changed at a time.


Create a graph, do BFS.


### 127. Word Ladder


Problem: Same as before, except return number now.


Trivial


### 128. Longest Consecutive Sequence


Problem: 


Given an unsorted array of integers, find the length of the longest consecutive elements sequence.


For example,\
Given `[100, 4, 200, 1, 3, 2]`,\
The longest consecutive elements sequence is `[1, 2, 3, 4]`. Return its length: `4`.


Your algorithm should run in O(*n*) complexity.


Easy do this with a dictionary keep tracking of the end as you go. If the number is already in the dictionary, skip and moving ahead. If it's not, check if i + 1 or i -- 1 are in the dictionary, and if they are, update accordingly. Then, simply return the maximum number in the dictionary.


### 129. Sum Root To Leaf Numbers


Problem: Sum of all the numbers created by going from the root to the leaf.


It's trivial depth first search.


### 130. Surrounded Regions


Problem: Connected components question


Do BFS from the O's at the corner, and then X out all of the non selected O's. Or, use a Union Find Data Structure. Create a dummy node, and then attach all the corners to this, and then attach all touching O's together.


### 131. Palindrome Partitioning


Problem: Partition a string into only palindromes, and return all possibilities


First we find out all ![n^2](img/latex-php) substrings are palindromes are not. Create nodes between adjacent palindromes. Then do DFS. The only new part of this is how to find all the palindromes in ![n^2](img/latex-php) time. This is easily done with DP.


`def` `get\_dp\_table\_method\_1(``self``, s):`


`dp` `=` `[[``False` `for` `\_` `in` `range``(``len``(s)` `+` `1``)]` `for` `\_` `in` `range``(``len``(s))]`


`# Empty strings are obviously palindromes`


`for` `i` `in` `range``(``len``(s)):`


`dp[i][i]` `=` `True`


`# Single strings are obviously palindromes`


`for` `i` `in` `range``(``len``(s)):`


`dp[i][i` `+` `1``]` `=` `True`


`# Now we do the rest`


`for` `length` `in` `range``(``2``,``len``(s)` `+` `1``):`


`for` `i` `in` `range``(``len``(s)` `-` `length` `+` `1``):`


`j` `=` `i` `+` `length`


`if` `dp[i``+``1``][j``-``1``]` `and` `s[i]` `=``=` `s[j` `-` `1``]:`


`dp[i][j]` `=` `True`


`return` `dp`


`def` `get\_dp\_table\_method\_2(``self``, s):`


`dp` `=` `[[``False` `for` `\_` `in` `range``(``len``(s)` `+` `1``)]` `for` `\_` `in` `range``(``len``(s))]`


`#for i in range(len(s)):`


`#    dp[i][i + 1] = True`


`for` `i` `in` `range``(``len``(s)):`


`tmp\_start` `=` `i`


`tmp\_end` `=` `i`


`# We'll first deal with the odd case`


`while` `tmp\_start >``=` `0` `and` `tmp\_end <` `len``(s)` `and` `s[tmp\_start]` `=``=` `s[tmp\_end]:             dp[tmp\_start][tmp\_end` `+` `1``]` `=` `True`             `tmp\_start` `-``=` `1`             `tmp\_end` `+``=` `1`         `# We'll first deal with the even case         tmp\_start = i         tmp\_end = i + 1         while tmp\_start >= 0 and tmp\_end < len(s) and s[tmp\_start] == s[tmp\_end]:`


`dp[tmp\_start][tmp\_end` `+` `1``]` `=` `True`


`tmp\_start` `-``=` `1`


`tmp\_end` `+``=` `1`


`return` `dp`


|


### 132. Palindrome Partitioning II


Problem: Same as before, now shortest partitioning


Same idea as before, except minimum partitioning now.


### 133. Clone Graph


Problem: Clone a graph


Simple recursion.


### 134. Gas Station


Problem: There are *N* gas stations along a circular route, where the amount of gas at station *i* is `gas[i]`.


You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from station *i* to its next station (*i*+1). You begin the journey with an empty tank at one of the gas stations.


Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.


First of all, make sure that sum(cost) > sum(gas). Now if this is true, we are guaranteed to have a solution. Next, let m be the minimum index cumulative array of (gas -- cost), we will want to return m + 1. Leave as an exercise to the reader to prove.


### 135. Candy


Problem: Kid's have preferences, give them candy so that it's respected and minimum candy is given out.


We can do this in two passes. Set up a DP table the size of the array. Then we iterate through, left to right, and we let ![dp[i] = dp[i - 1] + 1](img/latex-php) if the rating is higher for kid ![i](img/latex-php). Next we loop from right to left, and we let ![dp[i] = max(dp[i], dp[i + 1] + 1)](img/latex-php). Then, the answer is simply the sum of all the elements in dp.


### 136. Single Number


Problem: Every element appears twice except one, find it.


Every element appears twice except one, find it. XOR everything.


### 137. Single Number II


Problem; Every element appears three times except one. Find it.\
I have a detailed post about the general version. You can simply use that for this.


### 138. Copy List With Random Pointer


Problem: Copy a linked list with random pointers


Copy the lists, then interweave the two, use that to copy the random pointer. Then unweave it and we should be done.


### 139. Wordbreak


Problem: Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.


`def` `wordBreak(``self``, s, words):`


`d` `=` `[``False``]` `*` `len``(s)`


`for` `i` `in` `range``(``len``(s)):`


`for` `w` `in` `words:`


`if` `w` `=``=` `s[i``-``len``(w)``+``1``:i``+``1``]` `and` `(d[i``-``len``(w)]` `or` `i``-``len``(w)` `=``=` `-``1``):`


`d[i]` `=` `True`


`return` `d[``-``1``]`


|


You can reduce the runtime by running KMP before hand and then saving all substring occurrences.


### 140. Wordbreak II


Problem: Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.\
Simple KMP and DFS.


### 141. Linked List Cycle


Problem: Find a cycle in a linked list


Trivial


### 142. Linked List Cycle Meeting Point


Problem: Find the meeting point.


Also trivial. We know that ![L + 2k](img/latex-php) is congruent to $k$. So we know that $L$ is congruent to $-k$. So we just advance another $L$ forward and we're good.


### 143. Reorder List


Problem: Given a singly linked list *L*: *L*0?*L*1?...?*L**n*-1?*L*n,\
reorder it to: *L*0?*L**n*?*L*1?*L**n*-1?*L*2?*L**n*-2?...


Split the list, reverse second half, merge them both.


### 144. Binary Tree Preorder Traversal


Problem: Name says it all


Use a stack, and append the right node first if you want to do it iteratively. Doing it recursively is absolutely trivial.


### 145. Binary Tree Postorder Traversal


Problem: Name says it all


Use a stack, and append the left node first if you want to do it iteratively. Then reverse the resultant list. Doing it recursively is absolutely trivial.


### 146. LRU Cache


Problem: Design and implement a data structure for [Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU). It should support the following operations: `get` and `put`.


`get(key)` -- Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.\
`put(key, value)` -- Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.


Use a mixture of a hashmap and a linked list. Pretty straight forward, but hard to code up.


`class` `Node:`


`def` `\_\_init\_\_(``self``, key, value):`


`self``.k` `=` `key`


`self``.v` `=` `value`


`self``.forward` `=` `None`


`self``.back` `=` `None`


`class` `LRUCache:`


`def` `\_\_init\_\_(``self``, capacity):`


`self``.c` `=` `capacity`


`self``.hashmap` `=` `{}`


`self``.head` `=` `Node(``0``,``0``)`


`self``.tail` `=` `Node(``0``,``0``)`


`self``.head.forward` `=` `self``.tail`


`self``.tail.back` `=` `self``.head`


`def` `add\_node\_end(``self``, node):`


`prev\_last` `=` `self``.tail.back`


`prev\_last.forward` `=` `node`


`node.back` `=` `prev\_last`


`node.forward` `=` `self``.tail`


`self``.tail.back` `=` `node`


`def` `remove\_node(``self``, node):`


`p` `=` `node.back`


`f` `=` `node.forward`


`p.forward` `=` `f`


`f.back` `=` `p`


`def` `put(``self``, key,value):`


`if` `key` `in` `self``.hashmap:`


`n` `=` `self``.hashmap[key]`


`self``.remove\_node(n)`


`n` `=` `Node(key,value)`


`self``.add\_node\_end(n)`


`self``.hashmap[key]` `=` `n`


`if` `len``(``self``.hashmap) >` `self``.c:`


`n` `=` `self``.head.forward`


`self``.remove\_node(n)`


`del``(``self``.hashmap[n.k])`


`def` `get(``self``, key):`


`if` `key` `in` `self``.hashmap:`


`n` `=` `self``.hashmap[key]`


`self``.remove\_node(n)`


`self``.add\_node\_end(n)`


`return` `n.v`


`return` `-``1`


`# Your LRUCache object will be instantiated and called as such:`


`# obj = LRUCache(capacity)`


`# param\_1 = obj.get(key)`


`# obj.put(key,value)`


|


### 147. Insertion Sort List


Problem: Name says it all


I don't know why this would ever be asked. But it's easy to do. Doing merge sort is a little harder, so just know that well.


### 148. Sort List


Problem: Name says it all


Trivial question.


### 149. Max Points On A Line


Problem: Name says it all


Hash based off slope and y intercept.


### 150. Evaluate Reverse Polish Notation


Problem: Name says it all


The obvious answer is process as a stack. The more complicated question is how to design this in a clever object oriented design fashion. I'll probably make a most on this in the design patterns section.


### 151. Reverse Words In A String


Problem: Name says it all


Reverse the entire string, then reverse each word at a time.


### 152. Maximum Product Subarray


Problem: Name says it all


This is very similar to Kadane's algorithm. However, we're going to keep track of the lowest we've seen so far and the highest we've seen so far. Now the new low is the minimum of the new number, the old low times the new number, and the old high times the new number. The new high is the maximum of the new number, the old low times the new number, and the old high times the new number. Then we simply return the last element in the highest array.


### 153. Find Minimum In Rotated Sorted Array


Problem: Name says it all


`def` `findMin(``self``, nums):`


`"""`


`:type nums: List[int]`


`:rtype: int`


`"""`


`# binary search for pivot`


`lo` `=` `0`


`hi` `=` `len``(nums)` `-` `1`


`while` `lo &lt; hi:`


`if` `nums[lo] &lt; nums[hi]:`


`return` `nums[lo]`


`mid` `=` `(lo` `+` `hi)``/``2`


`if` `(nums[mid] &gt;``=` `nums[lo]):`


`lo` `=` `mid` `+` `1`


`else``:`


`hi` `=` `mid`


`return` `nums[lo]`


|


### 154. Find Minimum Rotated Sorted Array II


Problem: Name says it all


If all of the elements aren't distinct, this isn't possible.


### 155. Min Stack


Problem: Name says it all


Initialize the stack to be an empty array. Initialize the minimum to be infinity.


Now, when you push something to the stack, if the number is less than the minimum, push the minimum to the stack and let the minimum now be equal to the thing being pushed.


When popping something from the stack, if the number is equal to the minimum, we pop again and let the second popped element be the minimum element now.


### 156 -- 159 Locked


### 160. Intersection Of Two Linked Lists


Problem: Name says it all


Easy, get the lengths then all you need to do is subtract.


### 161. One Edit Distance


Problem: Check if two words are one edit distance away.


Easy enough, if they're off by one letter (one delete operation) you know how to handle it.


### 162. Find Peak Element


Problem: Find peak element in rotated sorted array


You can do this with binary search.


`def` `findPeakElement(``self``, nums):`


`"""`


`:type nums: List[int]`


`:rtype: int`


`"""`


`start` `=` `0`


`end` `=` `len``(nums)` `-` `1`


`while` `start &lt; end:`


`mid` `=` `(start` `+` `end)``/``2`


`mid2` `=` `mid` `+` `1`


`if` `nums[mid] &lt; nums[mid2]:`


`start` `=` `mid2`


`else``:`


`end` `=` `mid`


`return` `start`


|


### 163. Missing Ranges


Problem: Find missing ranges


Easy, implement through the range and create intervals by checking if the number is in the array or not.


### 164. Maximum Gap


Problem: Find the maximum gap in between two numbers


Radix Sort seems like a good option right here.


### 165. Compare Version Numbers


Problem: Compare two version numbers


### 166. Fraction To Recurring Decimal


Problem: Do it until you have a remainder that's the same


Do this like normal fraction to decimal conversion.


### 167. Two Sum II Array Is Sorted


Problem: Name says it all


Left and right pointers, update as necessary.


### 168. Excel Sheet To Column Number


Problem: Name says it all


Although this question is trivial, it serves as a good way to convert numbers to other bases.


`def` `convertToTitle(``self``, num):`


`"""`


`:type n: int`


`:rtype: str`


`"""`


`return` `""` `if` `num` `=``=` `0` `else` `self``.convertToTitle((num` `-` `1``)` `/` `26``)` `+` `chr``((num` `-` `1``)` `%` `26` `+` `ord``(``'A'``))`


|


### 169. Majority Element


Problem: Name says it all


Moore's voting algorithm.


![Screen Shot 2017-09-14 at 8.00.02 PM](img/screen-shot-2017-09-14-at-8-00-02-pm-png)


### 170. Two Sum III Data Structure Design


Problem: Name says it all 


Space and time complexity tradeoff.


### 171. Excel Sheet Column To Column Number


Problem: Name says it all


This is trivial


### 172. Factorial Trailing Zeroes


Problem: Number of trailing 0's in a number's factorial.


Count the number of 5's. Then the number of 25's. Etc.


### 173. Binary Search Tree Iterator


Problem: Name says it all


Morris traversal, or maybe have a stack. Your call either way.


### 174. Dungeon Game


Problem: 


The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.


The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.


Some of the rooms are guarded by demons, so the knight loses health (*negative* integers) upon entering these rooms; other rooms are either empty (*0's*) or contain magic orbs that increase the knight's health (*positive* integers).


In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Bottom up DP.


### 175 -- 186 SQL Questions.


### 186. Locked Question


### 187. Repeated DNA Sequences


Problem: Find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.


Rolling Hash, Rabin Karp.


### 188. Best Time To Buy & Sell A Stock IV


Problem: See other post


I've devoted an entire post just to this question.


### 189. Rotate Array


Problem: Gone over before


Easy


### 190. Reverse Bits


Problem: Reverse the bits of a number


You can do this in ![O(1)](img/latex-php) if you do it intelligently. First reverse the halves, then recurse on those.


### 191. Number Of 1 Bits


Problem: Name says it all


Cool little trick is that ![(n AND n - 1)](img/latex-php) drops the lowest set bit.


### 192. Word Frequency


Problem: Count word frequency


Easy to do with a python script, but idk how to do this with a bash script.


### 193. Valid Phone Numbers


Problem: Find valid phone numbers


Idk how to do it with a bash script.


### 194 -- 197 -- Bash/SQL


### 198. House Robber


Problem: No adjacent houses can be robbed.


Simple dynamic programming


### 199. Binary Tree Right Side View


Problem: Name says it all


Level order traversal.


### 200. Number Of Islands


Problem: Count connected components. 


Union find data structure used here.


### 201. Bitwise AND Of Numbers Range


Problem: Name says it all


If there's an add or even number in the range, the lowest bit will be 0. So, let's not worry about that bit and look at the rest.


### 202. Happy Number


Problem: Is a number a happy number?


Trivial


### 203. Remove Linked List Elements


Problem: Remove everything with a certain value.


Trivial


### 204. Count Primes


Problem: Name says it all


Sieve of Erasthosthenes


### 205. Isomorphic Strings


Problem: Are two strings isomorphic?


Trivial hashing


### 206. Reverse Linked List


Problem: Name says it all


As easy as it sounds


### 207. Course Schedule


Problem: Can you take all the classes? Basically cycle detection. 


![Screen Shot 2017-10-17 at 1.05.07 AM](img/screen-shot-2017-10-17-at-1-05-07-am-png)


### 208. Implement Trie


Problem: Name says it all


Described in Data Structures & Algorithms page.


### 209. Minimum Size Subarray Sum


Problem: Find size of minimum size subarray whose sum is >= target


Two pointers, keep updating them


### 210. Course Schedule II


Problem: Find the order of which to take it.


See Course Schedule I, again implementation of Kahn's algorithm


### 211. Add And Search For Word Data Structure Design


Problem: Name says it all


Use a trie.


### 212. Word Search II


Problem: Find all words in a crossword puzzle


DFS + Trie


### 213. House Robber II


Problem: Circular houses, house robber I.


He other robs the first house or he doesn't.


### 214. Shortest Palindrome


Problem: Return shortest palindrome by adding characters to the front of it.


Reverse the string, now it becomes the problem of adding to the back of it. From now, make the string separated by "#" or something like that. Add string to reversed string. Find longest suffix that's also a proper prefix. Add that to the string.


### 215. K^th Largest Element In An Array


Problem: Name says it all


Quickselect!


### 216. Combination Sum III


