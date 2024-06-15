class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        temp = []
        for i in range(len(s)):
            if s[i] in vowels:
                temp.append(s[i])
        slist = list(s)
        for i in range(len(slist)):
            if slist[i] in vowels:
                slist[i] = temp.pop()

        return "".join(slist)