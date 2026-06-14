class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grouped_anagrams = {}

        # for each word
        for word in strs:
            # create frequency dict 
            word_freq_map = [0] * 26
            for letter in word:
                letter_index = (ord(letter) - ord('a'))
                word_freq_map[letter_index] = word_freq_map[letter_index] + 1
            # create f tuple
            word_freq_tuple = tuple(word_freq_map)
            print(word_freq_tuple)
            # use f tuple as key & add word to main dict array
            print(grouped_anagrams)
            anagrams = grouped_anagrams.get(word_freq_tuple, [])
            anagrams.append(word)
            grouped_anagrams[word_freq_tuple] = anagrams
        
        ans = []
        for key in grouped_anagrams:
            ans.append(grouped_anagrams[key])
        
        return ans