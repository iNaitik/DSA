class Solution:
    def encode(self, strs):
        key = 65
        encoded_string = []
        if strs == []:
            return "#EMPTY_LIST#"
        if strs == [""]:
            return "#EMPTY_STRING#"
        for i in strs:
            encoded_word = ""
            for j in i:
                if j.isalpha():
                    base = ord('A') if j.isupper() else ord('a')
                    ch = chr((ord(j) - base + key) % 26 + base)
                else:
                    ch = j
                encoded_word += ch
            encoded_string.append(encoded_word)
        
        return " ".join(encoded_string)

    def decode(self, s):
        key = 65
        decode_string = []
        if s == "#EMPTY_LIST#":
            return []

        if s == "#EMPTY_STRING#":
            return [""]
        for i in s.split(" "):
            decoded_word = ""    
            for j in i:
                if j.isalpha():  
                    base = ord('A') if j.isupper() else ord('a')
                    ch = chr((ord(j) - base - key) % 26 + base)
                else:
                    ch = j
                decoded_word += ch
            decode_string.append(decoded_word)
        
        return decode_string