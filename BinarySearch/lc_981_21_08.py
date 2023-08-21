class TimeMap:

    def __init__(self):
        self.store = {}
    def set(self, key: str, value: str, timestamp: int):
        if key not in self.store:
            self.store[key] = []

obj=TimeMap()
x=["TimeMap", "set", "get", "get", "set", "get", "get"]
y=[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]


        
