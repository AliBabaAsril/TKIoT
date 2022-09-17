from ctypes import c_double
# a = 10 berarti variabel a bernilai 10

# tipe data : angka nominal (integer)
from operator import truediv


data_integer = 1
print("data :", data_integer, ", Bertipe : ", type(data_integer))

# type data : angka dengan koma (float)
data_float = 1.5
print("data:", data_float, ", Bertipe : ", type(data_float))

#tipe data : karakter (string)
data_string = "Ali"
print("data:", data_string, ", Bertipe : ", type(data_string))

# type data : biner atau true/false (boolean)
data_bool = True
print("data:", data_bool, ", Bertipe : ", type(data_bool))

## tipe data khusus
# tipe data : kompleks

data_complex = complex(5, 6)
print("data:", data_complex, ", Bertipe : ", type(data_complex))

# tipe data bahasa C

data_c_double = c_double(10.5)
print("data:", data_c_double, ", Bertipe : ", type(data_c_double))