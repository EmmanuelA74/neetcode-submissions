class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.map[key]
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2

            if values[mid][0] <= timestamp:
                l = mid + 1
                res = values[mid][1]
            else:
                r = mid - 1
        
        return res
