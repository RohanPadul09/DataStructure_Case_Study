# Case Study: Social Network Adjacency Matrix

## 1. Introduction

A social network allows users to connect with friends. In a graph, each user is represented by a **vertex (node)** and each friendship is represented by an **edge**.

An **adjacency matrix** is a two-dimensional table used to represent connections between nodes. If two users are friends, the corresponding matrix entry is `1`; otherwise, it is `0`.

This case study demonstrates the adjacency matrix using a small network. It also explains why a matrix may be inefficient for a very large network containing millions of users.

## 2. Problem Statement

Represent friendship connections between users using an adjacency matrix and determine whether two users are directly connected.

## 3. Objectives

- Understand graphs and adjacency matrices.
- Represent users and their friendships.
- Check whether two users are friends.
- Understand the memory and time complexity of this representation.
- Recognize the limitations of a matrix for networks with millions of users.

## 4. Example Network

Suppose there are four users: Alice, Bob, Charlie, and Diana.

Friendships:
- Alice is friends with Bob and Charlie.
- Bob is friends with Alice and Diana.
- Charlie is friends with Alice.
- Diana is friends with Bob.

Assume friendships are mutual. The graph is undirected.

## 5. Adjacency Matrix

Rows and columns represent the same users in this order: Alice, Bob, Charlie, Diana.

| User | Alice | Bob | Charlie | Diana |
|---|---:|---:|---:|---:|
| Alice | 0 | 1 | 1 | 0 |
| Bob | 1 | 0 | 0 | 1 |
| Charlie | 1 | 0 | 0 | 0 |
| Diana | 0 | 1 | 0 | 0 |

A value of `1` means the two users are friends. A value of `0` means there is no direct friendship. The diagonal is `0` because users are not considered friends with themselves in this example.

## 6. Algorithm

1. Create a list of users.
2. Create an `n × n` matrix filled with zeros, where `n` is the number of users.
3. For each friendship, find the indexes of both users.
4. Set both corresponding matrix entries to `1` because the friendship is mutual.
5. To check whether two users are friends, inspect the matrix entry for their row and column.

## 7. Python Implementation

See [`adjacency_matrix.py`](adjacency_matrix.py).

## 8. Sample Output

```text
Social Network Adjacency Matrix

       Alice    Bob      Charlie  Diana
Alice  0        1        1        0
Bob    1        0        0        1
Charlie1        0        0        0
Diana  0        1        0        0

Are Alice and Bob friends? True
Are Alice and Diana friends? False
```

## 9. Complexity Analysis

For `n` users:

- **Space complexity:** `O(n²)` because the matrix contains `n × n` entries.
- **Check a friendship:** `O(1)` when the users' indexes are known.
- **Initialize the matrix:** `O(n²)`.
- **Add a friendship:** `O(1)` when the users' indexes are known.

## 10. Representing Millions of Users

An adjacency matrix becomes impractical for a large social network because its memory requirement grows quadratically.

For example, a network of 1,000,000 users requires 1,000,000,000,000 matrix entries. Even if each entry used only one byte, this would require about 1 terabyte of storage (before overhead). A typical Python list-of-lists would use much more memory.

Real social networks are usually sparse: each user is connected to only a small fraction of all users. Adjacency lists, compressed sparse representations, and distributed graph storage are generally more memory-efficient for such networks. An adjacency matrix remains useful for small or dense graphs and for constant-time friendship checks when memory is available.

## 11. Advantages

- Simple and easy to understand.
- Checks whether two users are directly connected in `O(1)` time with known indexes.
- Useful for small or dense graphs.
- Represents mutual friendships clearly with a symmetric matrix.

## 12. Limitations

- Requires `O(n²)` memory.
- Adding many users requires expanding the matrix.
- Wastes space when most pairs of users are not connected.
- A full matrix is generally unsuitable for millions of users.

## 13. Conclusion

An adjacency matrix represents friendships by storing `1` for a connection and `0` for no connection. It is simple and provides fast friendship checks, but its quadratic memory requirement makes it unsuitable for very large, sparse social networks. Adjacency lists or sparse graph representations are often a better choice at that scale.
