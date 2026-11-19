print("HELLO GYM FREAK!\n")

egg_count = int(input("Enter number of eggs taken: "))
egg_protein = 6 * egg_count
print(f"{egg_protein} grams\n")

soya_quantity = int(input("Enter grams of soya chunks taken: "))
soya_protein = (52 / 100) * soya_quantity
print(f"{soya_protein} grams\n")

green_gram_quantity = int(
    input("Enter grams of green gram/chana taken: ")
)
green_gram_protein = (24 / 100) * green_gram_quantity
print(f"{green_gram_protein} grams\n")

total_protein = egg_protein + soya_protein + green_gram_protein

print(f"Total estimated protein intake: {total_protein} grams\n")

if total_protein < 60:
    print("Low protein intake")
elif 60 <= total_protein <= 100:
    print("Good protein intake")
else:
    print("Excellent protein intake")