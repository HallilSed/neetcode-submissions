class Solution:

    def encode(self, strs: List[str]) -> str:


        encoded = ""

        for i in strs[0:]:
            encoded += str(len(i)) + "#" + i
    
        return encoded

    def decode(self, s: str) -> List[str]:
        
        decoded = []
        
        i = 0
        while i < len(s):
            j = i
            
            while s[j] != "#":
                
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = length + start
            
            decoded.append(s[start:end])
            
            i = end

        return decoded
