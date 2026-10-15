# Case Study 1: E-commerce Product Sorting Using Divide and Conquer

## 1. Introduction

E-commerce applications contain many products. Customers often sort products by price, rating, discount, or popularity. An efficient sorting algorithm helps organize products so customers can compare them easily.

Divide and Conquer is an algorithm design strategy that divides a problem into smaller subproblems, solves them, and combines their results. Merge Sort is a common example.

## 2. Problem statement

Sort a list of product prices in ascending order using Merge Sort.

## 3. Objectives

- Understand the Divide and Conquer strategy.
- Sort product prices efficiently.
- Demonstrate the divide, conquer, and combine steps.
- Analyze the algorithm's time and space complexity.

## 4. Algorithm: Merge Sort

1. If the list contains zero or one item, it is already sorted.
2. Divide the list into two halves.
3. Recursively sort each half.
4. Merge the two sorted halves in ascending order.
5. Return the sorted list.

## 5. Example

Input product prices:

`[500, 200, 800, 100, 400, 300, 700, 600]`

Divide into two halves:

- Left: `[500, 200, 800, 100]`
- Right: `[400, 300, 700, 600]`

After recursively sorting:

- Left sorted: `[100, 200, 500, 800]`
- Right sorted: `[300, 400, 600, 700]`

Final sorted list:

`[100, 200, 300, 400, 500, 600, 700, 800]`

## 6. Python implementation

See [`merge_sort.py`](merge_sort.py).

## 7. Complexity analysis

| Case | Time complexity |
|---|---|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |
| Auxiliary space | O(n) for this implementation |

Here, `n` is the number of products.

## 8. Advantages

- Efficient for large lists.
- Predictable O(n log n) running time.
- Can sort by different product attributes by changing the comparison rule.
- Illustrates the Divide and Conquer strategy clearly.

## 9. Conclusion

Merge Sort applies Divide and Conquer to sort product prices efficiently. It divides the list into smaller parts, sorts them recursively, and merges the results into a single sorted list.
