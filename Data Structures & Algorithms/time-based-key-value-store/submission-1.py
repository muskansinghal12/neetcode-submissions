class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        moods = self.keys[key]
        low = 0
        high = len(moods)-1
        ans = ""
        while low <= high:
            mid = (low+high) // 2
            value, t = moods[mid]
            if t == timestamp:
                return value
            elif t < timestamp:
                ans = value
                low = mid+1
            else:
                high = mid-1
        return ans
        

