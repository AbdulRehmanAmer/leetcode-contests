# My Leetcode submission with detailed explanation:
# https://leetcode.com/problems/longest-absolute-file-path/solutions/3782578/monotonic-stack-with-the-detailed-understanding-python-easiest-solution/
class Solution:
    def lengthLongestPath(self, input: str) -> int:  
        self.stack = list()
        longest_path = 0
        i = 0
        while i < len(input):
            if input[i] == "\n":
                if "\t" * len(self.stack) == input[i + 1 : i + 1 + len(self.stack)]:
                    i += 1 + len(self.stack)
                else:
                    length = input[i + 1 : i + 1 + len(self.stack)].count("\t")
                    self.maintain_stack (length)

            else:
                i = self.push_item (i, input)
                if "." in self.stack[-1]: 
                    longest_path = max(longest_path, self.count_length ())
        
        return longest_path

    def maintain_stack (self, length):
        self.stack = self.stack[ : length]
    
    def push_item (self, i, input, s = ""): 
        while i < len(input) and input[i] != "\n":
            s += input[i]
            i += 1
        self.stack.append(s)
        return i

    def count_length (self, length = 0): 
        for x in self.stack:
            if x == "\t": length += 1
            else: length += len(x)
        length += len(self.stack) - 1
        self.stack.pop()
        return length