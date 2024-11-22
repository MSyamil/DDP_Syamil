def bilangan(angka):
    i = 1
    while i <= angka:
        if i % 2 == 1:
            if i == 19:
                print(i)
            else:
                print(f"{i}, ", end="")
        i += 1

bilangan(20)