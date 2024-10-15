class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        len_p = len(p)
        len_s = len(s)
        counts = defaultdict(int)

        if len_p > len_s:
            return indices

        for character in p:
            counts[character] += 1
        print(counts)

        for i in range(len_s):
            if s[i] in counts:
                counts[s[i]] -= 1
            if i-len_p >= 0:
                if s[i-len_p] in counts:
                    counts[s[i-len_p]] += 1
            if not any (counts.values()):
                indices.append(i-len_p+1)
        
        return indices

         
