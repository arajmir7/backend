class Solution:
    def replaceWords(self, dictionary, sentence: str) -> str:
        roots = set(dictionary)
        words = sentence.split()
        
        for i, word in enumerate(words):
            prefix = ""
            for ch in word:
                prefix += ch
                if prefix in roots:
                    words[i] = prefix
                    break
        
        return " ".join(words)
