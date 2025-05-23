from time import sleep

for contador in range(1, 11):
    print(contador, end=' ')
    sleep(1)

print("FIM")


for x in range(1, 11):
    for y in range(1, 11):
        print(f"{x} x  {y} = {x*y}")

