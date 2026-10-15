# Case Study: Dictionary Application Using Hash Tables

## 1. Introduction

A dictionary is an application that stores words and their meanings. It allows users to add new words, search for meanings, delete words, and display stored entries.

A Hash Table is a data structure that stores data using keys and values. In this application, the word is the key and its meaning is the value. A hash function converts each word into an index in the hash table.

## 2. Problem Statement

To implement a dictionary application using a hash table that stores words and meanings and supports insertion, searching, deletion, and display operations. The application must handle hash collisions using a collision-resolution technique.

## 3. Objectives

- Understand the working of hash tables.
- Store words and meanings as key-value pairs.
- Implement a hash function to calculate table indexes.
- Resolve collisions using separate chaining.
- Perform insertion, searching, deletion, and display operations.
- Analyze the time and space complexity of the application.

## 4. Data Structure Used

### Hash Table

A hash table is an array of buckets. Each bucket stores entries that map to the same index.

### Hash Function

The program calculates an index using the following formula:

`index = sum(ASCII values of characters in the word) % table_size`

For example, if the table size is 10, the word `cat` produces:

- ASCII value of `c` = 99
- ASCII value of `a` = 97
- ASCII value of `t` = 116
- Sum = 312
- Index = 312 % 10 = 2

Therefore, the word `cat` is stored in bucket 2.

## 5. Collision Resolution

A collision occurs when two different words produce the same hash-table index.

This application uses **Separate Chaining**. Each index contains a list of entries. If multiple words map to the same index, they are stored in that list.

For example, with a table size of 10:

- `cat` produces index 2.
- `act` also produces index 2.

Both words can be stored in bucket 2 without overwriting each other.

## 6. Operations

### 6.1 Insert

The application calculates the hash index for a word. If the word already exists, its meaning is updated. Otherwise, the word and meaning are added to the corresponding bucket.

### 6.2 Search

The hash function calculates the index of the requested word. The application searches the corresponding bucket and displays the meaning if the word is found.

### 6.3 Delete

The application calculates the word's index, searches the corresponding bucket, and removes the matching entry.

### 6.4 Display

The application traverses the hash table and displays all stored words and their meanings.

## 7. Algorithm

1. Create a hash table with a fixed number of buckets.
2. Accept the user's choice.
3. For insertion, calculate the hash index and store the word and meaning.
4. For searching, calculate the index and look for the word in its bucket.
5. For deletion, locate the word and remove it from the bucket.
6. For display, print all non-empty buckets.
7. Repeat until the user selects Exit.

## 8. Sample Execution

```text
===== DICTIONARY APPLICATION =====
1. Add word and meaning
2. Search word
3. Delete word
4. Display dictionary
5. Exit

Enter your choice: 1
Enter word: cat
Enter meaning: A small domesticated animal
Word added successfully.

Enter your choice: 2
Enter word to search: cat
Word: cat
Meaning: A small domesticated animal
```

## 9. Time Complexity

Let `n` be the number of stored words and `m` be the number of buckets.

| Operation | Average Case | Worst Case |
|---|---|---|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Display | O(n + m) | O(n + m) |

The average-case performance assumes a reasonably distributed hash function and a controlled load factor. In the worst case, all words may map to the same bucket.

## 10. Space Complexity

The space complexity is **O(n + m)**, where `n` is the number of stored words and `m` is the number of hash-table buckets.

## 11. Applications

- English dictionaries and vocabulary applications.
- Contact lookup systems.
- Symbol tables in compilers.
- Caching systems.
- Database indexing and fast key-value lookup.

## 12. Advantages

- Fast average-case searching.
- Efficient insertion and deletion.
- Collision handling through separate chaining.
- Supports dynamic updates to word meanings.

## 13. Conclusion

This case study demonstrates a dictionary application implemented using a hash table. Words act as keys and meanings act as values. Separate chaining resolves collisions by storing multiple entries in the same bucket. The application supports insertion, searching, deletion, and display operations and demonstrates the practical use of hashing in dictionary lookup systems.
# Case Study: Dictionary Application Using Hash Tables

## 1. Introduction

A dictionary is an application that stores words and their meanings. It allows users to add new words, search for meanings, delete words, and display stored entries.

A Hash Table is a data structure that stores data using keys and values. In this application, the word is the key and its meaning is the value. A hash function converts each word into an index in the hash table.

## 2. Problem Statement

To implement a dictionary application using a hash table that stores words and meanings and supports insertion, searching, deletion, and display operations. The application must handle hash collisions using a collision-resolution technique.

## 3. Objectives

- Understand the working of hash tables.
- Store words and meanings as key-value pairs.
- Implement a hash function to calculate table indexes.
- Resolve collisions using separate chaining.
- Perform insertion, searching, deletion, and display operations.
- Analyze the time and space complexity of the application.

## 4. Data Structure Used

### Hash Table

A hash table is an array of buckets. Each bucket stores entries that map to the same index.

### Hash Function

The program calculates an index using the following formula:

`index = sum(ASCII values of characters in the word) % table_size`

For example, if the table size is 10, the word `cat` produces:

- ASCII value of `c` = 99
- ASCII value of `a` = 97
- ASCII value of `t` = 116
- Sum = 312
- Index = 312 % 10 = 2

Therefore, the word `cat` is stored in bucket 2.

## 5. Collision Resolution

A collision occurs when two different words produce the same hash-table index.

This application uses **Separate Chaining**. Each index contains a list of entries. If multiple words map to the same index, they are stored in that list.

For example, with a table size of 10:

- `cat` produces index 2.
- `act` also produces index 2.

Both words can be stored in bucket 2 without overwriting each other.

## 6. Operations

### 6.1 Insert

The application calculates the hash index for a word. If the word already exists, its meaning is updated. Otherwise, the word and meaning are added to the corresponding bucket.

### 6.2 Search

The hash function calculates the index of the requested word. The application searches the corresponding bucket and displays the meaning if the word is found.

### 6.3 Delete

The application calculates the word's index, searches the corresponding bucket, and removes the matching entry.

### 6.4 Display

The application traverses the hash table and displays all stored words and their meanings.

## 7. Algorithm

1. Create a hash table with a fixed number of buckets.
2. Accept the user's choice.
3. For insertion, calculate the hash index and store the word and meaning.
4. For searching, calculate the index and look for the word in its bucket.
5. For deletion, locate the word and remove it from the bucket.
6. For display, print all non-empty buckets.
7. Repeat until the user selects Exit.

## 8. Sample Execution

```text
===== DICTIONARY APPLICATION =====
1. Add word and meaning
2. Search word
3. Delete word
4. Display dictionary
5. Exit

Enter your choice: 1
Enter word: cat
Enter meaning: A small domesticated animal
Word added successfully.

Enter your choice: 2
Enter word to search: cat
Word: cat
Meaning: A small domesticated animal
```

## 9. Time Complexity

Let `n` be the number of stored words and `m` be the number of buckets.

| Operation | Average Case | Worst Case |
|---|---|---|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Display | O(n + m) | O(n + m) |

The average-case performance assumes a reasonably distributed hash function and a controlled load factor. In the worst case, all words may map to the same bucket.

## 10. Space Complexity

The space complexity is **O(n + m)**, where `n` is the number of stored words and `m` is the number of hash-table buckets.

## 11. Applications

- English dictionaries and vocabulary applications.
- Contact lookup systems.
- Symbol tables in compilers.
- Caching systems.
- Database indexing and fast key-value lookup.

## 12. Advantages

- Fast average-case searching.
- Efficient insertion and deletion.
- Collision handling through separate chaining.
- Supports dynamic updates to word meanings.

## 13. Conclusion

This case study demonstrates a dictionary application implemented using a hash table. Words act as keys and meanings act as values. Separate chaining resolves collisions by storing multiple entries in the same bucket. The application supports insertion, searching, deletion, and display operations and demonstrates the practical use of hashing in dictionary lookup systems.
