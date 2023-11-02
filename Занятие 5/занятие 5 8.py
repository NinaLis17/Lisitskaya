def max():
    s = []
    n = int(input("Введите число: "))
    while n != 0:
        s.append(n)
        n = int(input("Введите число: "))

    max_length = 0
    length = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            length += 1
        else:
            if length > max_length:
                max_length = length

    if length > max_length:
        max_length = length

    print("Наибольшее число подряд идущих элементов, равных друг другу: ", max_length)
max()