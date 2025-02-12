import time, sys
start = time.time()
squares = [x ** 2 for x in range(1,20)]
end = time.time()
print("List comprehension time:",end - start)
print(sys.getsizeof(squares))
squares = []
for x in range(1, 20):
    squares.append(x ** 2)
print("For loop time:", end -start)
print(sys.getsizeof(squares))
