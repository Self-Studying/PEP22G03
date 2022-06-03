# break

print("Thr break instruction: ")
for i in range(1, 7):
    if i == 3:
        break
    print("Inside the loop!", i)

# continuing the example

print("\nThe continued instruction: ")
for i in range(1, 7):
    if i == 3:
        continue
    print("Inside the loop!", i)
print("Outside the loop!")
