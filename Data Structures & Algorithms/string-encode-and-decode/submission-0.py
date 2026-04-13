class Solution:
    def encode(self, strs):
        key = 65
        encoded_string = []
        
        for i in strs:
            encoded_word = ""
            for j in i:
                base = ord('A') if j.isupper() else ord('a')
                ch = chr((ord(j) - base + key) % 26 + base)
                encoded_word += ch
            encoded_string.append(encoded_word)
        
        return " ".join(encoded_string)

    def decode(self, s):
        key = 65
        decode_string = []
        
        for i in s.split(" "):
            decoded_word = ""    
            for j in i:
                base = ord('A') if j.isupper() else ord('a')
                ch = chr((ord(j) - base - key) % 26 + base)
                decoded_word += ch
            decode_string.append(decoded_word)
        
        return decode_string