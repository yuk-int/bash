a = 0x654321
b = a & 0x0000FFFF
c = a & 0xFFFF0000

print ('(hex)a= ', hex(a))
print ('(hex)b= ', hex(b))
print ('(hex)c= ', hex(c))
#remove 4 bytes
d = c >>16
print (hex(d))

#Other methods
#method1
e = a % 16**4
print (hex(e))

f = a // 16**4
print (hex(f))

c = a & 0xFFFF0000
print (hex(c))

d = c >>16
print (hex(d))

#method2
e = a % 16**4
print (hex(e))

f = a // 16**4
print (hex(f))