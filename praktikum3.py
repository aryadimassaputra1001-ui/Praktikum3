 def cari_terbesar(a, b, c):
   """Mencari bilangan terbesar dari tiga input.
   Args:
   a: Bilangan pertama.
   b: Bilangan kedua.
   c: Bilangan ketiga.
 Return:
  Bilangan terbesar dari a, b, c.
 """
 if a >= b and a >= c:
   return a
 elif b >= a and b >= c:
   return b
 else:
   return c
# Contoh penggunaan
bil1 = 10
bil2 = 5
bil3 = 20
terbesar = cari_terbesar(bil1, bil2, bil3)
print("Bilangan terbesar adalah:", terbesar) # Output: Bilangan terbesar adalah: 20
