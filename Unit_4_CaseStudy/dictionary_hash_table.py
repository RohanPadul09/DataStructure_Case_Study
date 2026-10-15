
# Case Study: Dictionary Application Using Hash Tables
# Collision Resolution Technique: Separate Chaining

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, word):
        # Convert word into a hash-table index
        return sum(ord(char.lower()) for char in word) % self.size

    def insert(self, word, meaning):
        index = self.hash_function(word)
        bucket = self.table[index]

        # Update meaning if the word already exists
        for item in bucket:
            if item[0].lower() == word.lower():
                item[1] = meaning
                print("Meaning updated successfully.")
                return

        # Add a new word and meaning
        bucket.append([word, meaning])
        print("Word added successfully.")

    def search(self, word):
        index = self.hash_function(word)

        for stored_word, meaning in self.table[index]:
            if stored_word.lower() == word.lower():
                print(f"Word: {stored_word}")
                print(f"Meaning: {meaning}")
                return meaning

        print("Word not found.")
        return None

    def delete(self, word):
        index = self.hash_function(word)
        bucket = self.table[index]

        for item in bucket:
            if item[0].lower() == word.lower():
                bucket.remove(item)
                print("Word deleted successfully.")
                return

        print("Word not found.")

    def display(self):
        print("\n--- Dictionary Contents ---")
        for index, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {index}: ", end="")
                for word, meaning in bucket:
                    print(f"[{word}: {meaning}]", end=" ")
                print()


def main():
    dictionary = HashTable()

    while True:
        print("\n===== DICTIONARY APPLICATION =====")
        print("1. Add word and meaning")
        print("2. Search word")
        print("3. Delete word")
        print("4. Display dictionary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            word = input("Enter word: ").strip()
            meaning = input("Enter meaning: ").strip()

            if word and meaning:
                dictionary.insert(word, meaning)
            else:
                print("Word and meaning cannot be empty.")

        elif choice == "2":
            word = input("Enter word to search: ").strip()
            dictionary.search(word)

        elif choice == "3":
            word = input("Enter word to delete: ").strip()
            dictionary.delete(word)

        elif choice == "4":
            dictionary.display()

        elif choice == "5":
            print("Exiting Dictionary Application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
