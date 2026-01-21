def merge_the_tools(string, k):
    n = len(string)

    for i in range(0, n, k):
        chunk = string[i:i+k]
        seen = set()
        result = []

        for ch in chunk:
            if ch not in seen:
                seen.add(ch)
                result.append(ch)

        print("".join(result))


if __name__ == "__main__":
    string = input().strip()
    k = int(input().strip())
    merge_the_tools(string, k)
