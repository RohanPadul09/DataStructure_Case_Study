"""Social network friendship representation using an adjacency matrix."""

users = ["Alice", "Bob", "Charlie", "Diana"]
n = len(users)

# Start with an n x n matrix filled with zeros.
matrix = [[0 for _ in range(n)] for _ in range(n)]

# Each friendship is mutual (an undirected graph).
friendships = [
    ("Alice", "Bob"),
    ("Alice", "Charlie"),
    ("Bob", "Diana"),
]

# Store each user's position in the list for quick lookup.
index = {user: i for i, user in enumerate(users)}

# Add every friendship to the matrix.
for user1, user2 in friendships:
    i = index[user1]
    j = index[user2]
    matrix[i][j] = 1
    matrix[j][i] = 1

print("Social Network Adjacency Matrix")
print()
print("       " + " ".join(f"{user:<8}" for user in users))

for i, user in enumerate(users):
    row = " ".join(f"{value:<8}" for value in matrix[i])
    print(f"{user:<8}{row}")


def are_friends(user1, user2):
    """Return True if two users have a direct friendship."""
    return matrix[index[user1]][index[user2]] == 1


print()
print("Are Alice and Bob friends?", are_friends("Alice", "Bob"))
print("Are Alice and Diana friends?", are_friends("Alice", "Diana"))
