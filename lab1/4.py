def calculate_pi(n=0):
    result = 3
    for i in range(n + 1):
        if i:
            delta = ((-1) ** (i + 1)) * 4 / (2 * i * (2 * i + 1) * (2 * i + 2))
            print(delta)
            result += delta
    return result


for i in range(5):
    print(calculate_pi(i))
