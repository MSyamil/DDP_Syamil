# Tugas 3
#Pyramid
a = int(input("masukkan angka : "))
for x in range(1, a + 1):
    for y in range(1,a-x+1):
        print(" ", end="")
    for y in range(1,2*x):
        print("*", end="")
    print()

print()
print("===========================================")
print()
for b in range(a):
    for c in range(b+1):
        print("*", end="")
        c+=1
    print()
    b+=1