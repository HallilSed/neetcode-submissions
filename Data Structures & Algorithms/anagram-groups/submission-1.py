class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        if not strs:
            return []
        
        cache = {}


        for val in strs:
            
            key = "".join(sorted(val))

            if key not in cache:
                cache[key] = []
            cache[key].append(val)

        
        return list(cache.values())