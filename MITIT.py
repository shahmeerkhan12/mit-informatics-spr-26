def solve(name):
    # MITIT
    # need in [A][B][B]
    
    n = len(name)

    # at max how many chars
    boundary = n // 2
    if n % 2 == 0: # if n is even, need at least 1 for [A]
        boundary -= 1 

    for i in range(1, boundary + 1):
        p1 = name[-i:]
        p2 = name[-i*2:-i]
        
        if p1 == p2:
            print("YES")
            return

    print("NO")
    return


if __name__ == "__main__":
    Q = int(input())

    for _ in range(Q):
        name = input()
        solve(name)