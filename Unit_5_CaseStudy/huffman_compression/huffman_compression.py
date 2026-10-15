
import heapq
from collections import Counter
from itertools import count


class Node:
    def __init__(self, char, frequency, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_huffman_tree(text):
    frequencies = Counter(text)
    if not frequencies:
        return None, frequencies

    # Counter avoids comparing Node objects when frequencies tie.
    unique_id = count()
    heap = [
        (freq, next(unique_id), Node(char, freq))
        for char, freq in frequencies.items()
    ]
    heapq.heapify(heap)

    while len(heap) > 1:
        freq1, _, left = heapq.heappop(heap)
        freq2, _, right = heapq.heappop(heap)

        parent = Node(None, freq1 + freq2, left, right)
        heapq.heappush(heap, (parent.frequency, next(unique_id), parent))

    return heap[0][2], frequencies


def generate_codes(root):
    codes = {}

    def traverse(node, code):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = code or "0"
            return

        traverse(node.left, code + "0")
        traverse(node.right, code + "1")

    traverse(root, "")
    return codes


def encode(text, codes):
    return "".join(codes[char] for char in text)


def decode(bits, root):
    if root is None:
        return ""

    # Special case: text containing only one unique character.
    if root.char is not None:
        if any(bit != "0" for bit in bits):
            raise ValueError("Invalid encoded bits")
        return root.char * len(bits)

    result = []
    node = root

    for bit in bits:
        if bit not in "01":
            raise ValueError("Encoded data must contain only 0 and 1")

        node = node.left if bit == "0" else node.right

        if node is None:
            raise ValueError("Invalid encoded data")

        if node.char is not None:
            result.append(node.char)
            node = root

    if node is not root:
        raise ValueError("Incomplete encoded data")

    return "".join(result)


def main():
    text = input("Enter text to compress: ")

    if not text:
        print("Please enter some text.")
        return

    root, frequencies = build_huffman_tree(text)
    codes = generate_codes(root)
    encoded = encode(text, codes)
    decoded = decode(encoded, root)

    print("\nCharacter Frequencies:")
    for char, frequency in frequencies.items():
        print(repr(char), ":", frequency)

    print("\nHuffman Codes:")
    for char, code in sorted(codes.items()):
        print(repr(char), ":", code)

    print("\nEncoded bits:", encoded)
    print("Original text:", text)
    print("Decoded text:", decoded)
    print("Original size (8-bit characters):", len(text) * 8, "bits")
    print("Encoded payload size:", len(encoded), "bits")

    if decoded == text:
        print("Verification: Successful")


if __name__ == "__main__":
    main()
