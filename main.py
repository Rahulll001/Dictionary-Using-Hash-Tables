
class Dictionary:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, word):
        return sum(ord(ch) for ch in word) % self.size

    def insert(self, word, meaning):
        index = self.hash_function(word)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.table[pos] is None:
                self.table[pos] = (word, meaning)
                print("Word added successfully!")
                return

            if self.table[pos][0] == word:
                self.table[pos] = (word, meaning)
                print("Meaning updated successfully!")
                return

        print("Dictionary is full!")

    def search(self, word):
        index = self.hash_function(word)

        for i in range(self.size):
            pos = (index + i) % self.size
            item = self.table[pos]

            if item is None:
                break

            if item[0] == word:
                print("Meaning:", item[1])
                return

        print("Word not found!")

    def display(self):
        print("\nDictionary Contents:")
        for item in self.table:
            if item is not None:
                print(item[0], ":", item[1])


d = Dictionary()

d.insert("apple", "A fruit")
d.insert("book", "A set of written pages")
d.insert("cat", "A small domestic animal")

d.search("apple")
d.display()
