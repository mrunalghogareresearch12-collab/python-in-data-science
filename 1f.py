numbers = [12, 45, 7, 23, 56, 89, 34, 67, 10, 90]

print("List:", numbers)
print("Maximum =", max(numbers))
print("Minimum =", min(numbers))
print("Average =", sum(numbers) / len(numbers))

ascending = sorted(numbers)
print("Ascending Order =", ascending)

descending = sorted(numbers, reverse=True)
print("Descending Order =", descending)

numbers.append(100)
print("After Adding 100 =", numbers)

numbers.pop(0)
print("After Removing First Item =", numbers)
