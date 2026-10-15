
import heapq

class CityMap:
    def __init__(self):
        self.graph = {}

    def add_road(self, source, destination, distance):
        self.graph.setdefault(source, [])
        self.graph.setdefault(destination, [])
        self.graph[source].append((destination, distance))
        self.graph[destination].append((source, distance))

    def shortest_path(self, start, end):
        distances = {city: float("inf") for city in self.graph}
        previous = {}
        distances[start] = 0
        queue = [(0, start)]

        while queue:
            current_distance, city = heapq.heappop(queue)

            if current_distance != distances[city]:
                continue

            if city == end:
                break

            for neighbor, distance in self.graph[city]:
                new_distance = current_distance + distance

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = city
                    heapq.heappush(queue, (new_distance, neighbor))

        if end not in distances or distances[end] == float("inf"):
            return None, float("inf")

        path = []
        current = end

        while current != start:
            path.append(current)
            current = previous[current]

        path.append(start)
        path.reverse()
        return path, distances[end]


def main():
    city = CityMap()

    city.add_road("A", "B", 4)
    city.add_road("A", "C", 2)
    city.add_road("C", "B", 1)
    city.add_road("B", "D", 5)
    city.add_road("C", "D", 8)
    city.add_road("D", "E", 2)
    city.add_road("B", "E", 10)

    print("GPS Navigation System")
    start = input("Enter starting location (A-E): ").strip().upper()
    end = input("Enter destination (A-E): ").strip().upper()

    if start not in city.graph or end not in city.graph:
        print("Invalid location.")
        return

    path, distance = city.shortest_path(start, end)

    if path is None:
        print("No route available.")
    else:
        print("Shortest route:", " -> ".join(path))
        print("Total distance:", distance, "km")


if __name__ == "__main__":
    main()
