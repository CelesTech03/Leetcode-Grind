class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        letters_to_words = defaultdict(list)
        
        for word in strs:
            key = "".join(sorted(list(word)))
            letters_to_words[key].append(word)
            
        result = []
        
        for i in letters_to_words.values():
            result.append(i)
        
        return result