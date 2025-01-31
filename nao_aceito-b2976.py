from itertools import combinations

def max_non_consecutive_triangle_subsequence(arr):
    n = len(arr)
    max_len = 0

    for size in range(3, n + 1):
        for subset in combinations(arr, size):
            valid = all(sorted(triple)[0] + sorted(triple)[1] > sorted(triple)[2]
                        for triple in combinations(subset, 3))
            if valid:
                max_len = max(max_len, len(subset))
    return max_len


def max_consecutive_triangle_subsequence(arr):
    max_len = 0
    current_len = 0

    for i in range(len(arr) - 2):
        a, b, c = sorted(arr[i:i + 3])  
        if a + b > c:  
            current_len += 1 if current_len else 3  
        else:
            max_len = max(max_len, current_len)
            current_len = 0

    max_len = max(max_len, current_len)
    return max_len

def main():
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    max_consecutive = max_consecutive_triangle_subsequence(arr)
    max_non_consecutive = max_non_consecutive_triangle_subsequence(arr)

    print(max_consecutive)
    print(max_non_consecutive)

main()

