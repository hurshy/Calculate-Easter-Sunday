#Easter Sunday
#Tyler Hegewald
#Input
y = int(input("Enter a year "))
a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32
if n == 4 and y <= 2015:
    print("In", y, "Easter Sunday fell on April", p)
elif n == 4 and y > 2015:
    print("In",y, "Easter Sunday will fall on April",p)
elif n == 3 and y <= 2015:
    print("In",y, "Easter Sunday fell on March",p)
elif n == 3 and y > 2015:
    print("In",y, "Easter Sunday will fall on March",p)
