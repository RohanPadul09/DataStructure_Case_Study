# Case Study: ZIP/GZIP File Compression Using Huffman Tree

## 1. Introduction

File compression reduces the number of bits required to represent data. Huffman coding is a lossless compression technique that assigns shorter binary codes to frequently occurring characters and longer codes to less frequent characters.

Huffman coding is an important concept in data compression and is used in compression formats such as DEFLATE, which is used by ZIP and GZIP.

## 2. Problem Statement

To implement frequency-based encoding using a Huffman tree, generate binary codes for characters, encode the input text, and decode it to verify that the original text is recovered.

## 3. Objectives

- Calculate character frequencies.
- Construct a Huffman tree using a priority queue.
- Generate variable-length binary codes.
- Encode and decode text.
- Analyze the compression payload size and algorithm complexity.

## 4. Huffman Tree

A Huffman tree is a binary tree constructed using character frequencies.

The algorithm repeatedly selects the two nodes with the smallest frequencies and combines them into a parent node. This continues until a single root node remains.

During traversal:
- Left edges represent `0`.
- Right edges represent `1`.
- Each character's path from the root forms its Huffman code.

## 5. Algorithm

1. Read the input text.
2. Count the frequency of each character.
3. Insert the characters into a min-priority queue.
4. Remove the two nodes with the smallest frequencies.
5. Combine them into a parent node and insert the parent into the queue.
6. Repeat until one tree remains.
7. Traverse the tree to generate character codes.
8. Encode the input text using those codes.
9. Decode the encoded bits and verify the original text.

## 6. Sample Execution

Example input:

`banana`

One valid set of Huffman codes is:

| Character | Frequency | Example code |
|---|---:|---|
| a | 3 | 0 |
| n | 2 | 11 |
| b | 1 | 10 |

The encoded payload is:

`100110110`

The decoded output is:

`banana`

When frequencies are tied, another valid tree and code assignment may be produced.

## 7. Complexity Analysis

Let n be the number of characters in the input and k be the number of distinct characters.

- Frequency counting: O(n) average time.
- Huffman tree construction: O(k log k).
- Code generation: O(k).
- Encoding and decoding: O(n) time for a fixed-size character alphabet.
- Space complexity: O(n + k), including the encoded output and tree.

## 8. Advantages

- Lossless compression.
- Frequently occurring characters receive shorter codes.
- Prefix-free codes allow unambiguous decoding.
- Useful for understanding compression algorithms.

## 9. Applications

- ZIP and GZIP compression concepts.
- Data transmission.
- File compression utilities.
- Storage optimization.

## 10. Important Limitation

This program demonstrates Huffman coding in memory. It does **not** create an actual ZIP or GZIP archive. Real ZIP/GZIP files require a defined file format, headers, metadata, and additional processing. ZIP and GZIP commonly use the DEFLATE algorithm, which combines LZ77 compression with Huffman coding.

## 11. Conclusion

This case study demonstrates how a Huffman tree uses character frequencies to generate variable-length binary codes. It shows how text can be encoded and decoded without losing information and explains the role of Huffman coding in modern compression systems.
