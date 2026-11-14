a = "A"
print(ord(a)) #This will print 65 because the variable 'a' is a string and ord() returns the Unicode code point for a given character.

b = "😊"
print(ord(b)) #This will print 128522 because the variable 'b' is a string and ord() returns the Unicode code point for a given character.

c = 65
print(chr(c)) #This will print 'A' because the variable 'c' is an integer and chr() returns the character for a given Unicode code point.

d = "hello brother"
print(len(d)) #This will print 13 because the variable 'd' is a string with 13 characters.

e = "SHER"
print(e[1]) #This will print 'H' because the variable 'e' is a string and e[1] accesses the character at index 1.

f = "SHER"
print(f[-1], f[3]) #This will print 'R R' because the variable 'f' is a string and f[-1] accesses the last character while f[3] accesses the character at index 3.

g = "SHER CODER"
print(g[0:4:1]) #This will print 'SHE' because the variable 'g' is a string and g[0:3:1] slices the string from index 0 to 2 (3 is exclusive) with a step of 1.

h = "SHER CODER"
print(h[5::1]) #This will print 'CODER' because the variable 'h' is a string and h[5::1] slices the string from index 5 to the end with a step of 1.