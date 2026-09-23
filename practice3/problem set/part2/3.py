def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    return rabbits, chickens


rabbits, chickens = solve(35, 94)

print("Rabbits:", rabbits)
print("Chickens:", chickens)
