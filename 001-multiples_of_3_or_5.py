def old_way():
    multiples = []
    for number in range(1000):
        if number % 3 == 0 or number % 5 == 0:
            multiples.append(number)

    print(sum(multiples))


print(sum([i for i in range(1000) if i % 5 == 0 or i % 3 == 0]))
