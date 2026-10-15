

def merge_sort(items):
    
    if len(items) <= 1:
        return items[:]

    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
  
    prices = [500, 200, 800, 100, 400, 300, 700, 600]

    print("E-commerce Product Sorting")
    print("Original prices:", prices)
    print("Sorted prices:  ", merge_sort(prices))
