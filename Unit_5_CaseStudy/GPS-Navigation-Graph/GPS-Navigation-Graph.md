# Case Study: GPS / Navigation System Using Weighted Graphs

## 1. Introduction

A GPS navigation system helps users find routes between locations. A city map can be represented using a weighted graph, where vertices represent locations, edges represent roads, and edge weights represent distances.

## 2. Problem Statement

To implement a navigation system that represents a city map as a weighted graph and calculates the shortest route between two locations using a graph algorithm.

## 3. Objectives

- Understand weighted graphs and adjacency lists.
- Represent locations and roads using a graph.
- Apply Dijkstra's shortest-path algorithm.
- Display the shortest route and total distance.

## 4. Data Structure and Algorithm

The program uses an adjacency list to store the road network. Each location stores its neighboring locations and the distance to each neighbor.

Dijkstra's algorithm calculates the minimum distance from a starting location to other reachable locations. A priority queue helps process the closest unvisited location first.

## 5. Operations

1. Add roads and their distances.
2. Accept a starting location and destination.
3. Calculate the shortest path.
4. Display the route and total distance.
5. Report an error for invalid or unreachable locations.

## 6. Sample Input and Output

Input:
- Starting location: A
- Destination: E

Output:

```text
Shortest route: A -> C -> B -> D -> E
Total distance: 10 km
```

## 7. Complexity Analysis

For V vertices and E edges, Dijkstra's algorithm using an adjacency list and a binary heap takes O((V + E) log V) time and O(V + E) space.

## 8. Applications

- GPS navigation and route planning.
- Road network analysis.
- Delivery route planning.
- Network routing.

## 9. Conclusion

This case study demonstrates how weighted graphs and Dijkstra's algorithm can be used to calculate shortest routes between locations. The sample program uses fictional locations and distances for demonstration.
