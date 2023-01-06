weight = float(input("Enter the weight: "))
input_unit = input("lbs, kgs, ozs or grams? ")

x = weight / 2.2046
y = weight * 2.2046
z = x * 1000
q = weight * 16
r = y * 16
s = weight * 1000
t = weight / 16
u = t / 2.2046
w = u * 1000
a = weight / 1000
b = a * 2.2046
c = b * 16

if input_unit == "lbs":
    print(str(x) + " kgs")
    print(str(q) + " ozs")
    print(str(z) + " grams")
elif input_unit == "kgs":
    print(str(y) + " lbs")
    print(str(r) + " ozs")
    print(str(s) + " grams")
elif input_unit == "ozs":
    print(str(u) + " kgs")
    print(str(t) + " lbs")
    print(str(w) + " grams")
elif input_unit == "grams":
    print(str(a) + " kgs")
    print(str(b) + " lbs")
    print(str(c) + " ozs")
else:
    print("Invalid number or unit!!!")