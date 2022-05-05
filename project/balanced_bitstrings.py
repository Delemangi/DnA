def main():
    n = int(input())
    k = int(input())
    s = input()

    zeros = 0
    ones = 0

    for i in range(k):
        temp = -1

        for j in range(i, n, k):
            if s[j] != '?':
                if temp != -1 and int(s[j]) != temp:
                    return 'NO'

                temp = int(s[j])

        if temp == 0:
            zeros += 1
        elif temp == 1:
            ones += 1

    return 'YES' if max(zeros, ones) <= k // 2 else 'NO'

if __name__ == '__main__':
    print(main())
