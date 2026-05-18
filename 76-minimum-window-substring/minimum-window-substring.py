class Solution:
    def minWindow(self, s, t):

        if len(t) > len(s):
            return ""

        target = {}
        for ch in t:
            target[ch] = target.get(ch, 0) + 1

        window = {}

        required = len(target)
        formed = 0

        left = 0

        min_len = float('inf')
        ans = ""

        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in target and window[char] == target[char]:
                formed += 1

            while left <= right and formed == required:

                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    ans = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in target and window[left_char] < target[left_char]:
                    formed -= 1

                left += 1

        return ans