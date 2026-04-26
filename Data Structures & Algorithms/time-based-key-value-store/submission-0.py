class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        i = 0
        if key not in self.key_store:
            return ""
        res = ""
        for t,v in self.key_store[key]:
            if t <= timestamp:
                res = v
            else:
                break
        return res
            

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)