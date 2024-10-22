class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)

        return h % self.MAX

    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def delete(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

    # Overriding
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
t.add("march 6", 130)
print(t.get("march 6"))

# Overriding example
t["march 7"] = 157
t["march 8"] = 146
print(t["march 7"])
print(t.arr)
del t["march 7"]
t.delete("march 6")
print(t.arr)
