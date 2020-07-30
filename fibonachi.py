# Create a new function fibonachi
gigi
def fibonachi(n):
    if n <= 1:
        return 1
    else:
        return n * fibonachi(n-1)
print(fibonachi(4))