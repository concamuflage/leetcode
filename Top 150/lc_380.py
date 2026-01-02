import random


class RandomizedSet:

    def __init__(self):
        self.storage = []
        self.dict = {}

    def insert(self, val: int) -> bool:

        if val not in self.dict:
            self.storage.append(val)
            self.dict[val] = len(self.storage) - 1
            return True
        else:
            return False


    def remove(self, val: int) -> bool:
        if val in self.dict:
            index = self.dict[val]
            # swap with the last element
            value = self.storage[-1]
            self.storage[index] = value
            self.storage.pop()
            # update the dictionary
            self.dict[value] = index
            # remove the record of the deleted value
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.storage)

randomizedSet = RandomizedSet()
print(randomizedSet.insert(0))
print(randomizedSet.remove(0))
print(randomizedSet.insert(0))
print(randomizedSet.getRandom())
print(randomizedSet.remove(0))
print(randomizedSet.insert(0))
print(randomizedSet.getRandom())