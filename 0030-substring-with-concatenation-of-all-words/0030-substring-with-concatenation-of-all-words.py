class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_freq = defaultdict(int)
        for word in words:
            word_freq[word] += 1

        word_len = len(words[0])
        # words of the same length
        window = len(words) * word_len
        ans = []

        for i in range(len(s) - window + 1):
            substr_freq = defaultdict(int)
            j = i

            while j < i + window:
                current = s[j : j + word_len]
                if current not in word_freq:
                    break

                substr_freq[current] += 1
                if substr_freq[current] > word_freq[current]:
                    break

                j += word_len
            
            if j == i + window:
                ans.append(i)

        return ans
        