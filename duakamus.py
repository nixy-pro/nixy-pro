# Menggabungkan Dua Kamus
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}

# List Comprehension untuk Menghitung Kuadrat
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]

# Membalik String
original_string = "hello"
reversed_string = original_string[::-1]

# Mencari Substring dalam String
text = "Python programming"
if "programming" in text:
    print("Substring found!")

# Mengurutkan List of Dictionaries Berdasarkan Key Tertentu
from operator import itemgetter
list_of_dicts = [{'name': 'John', 'age': 45}, {'name': 'Doe', 'age': 30}]
sorted_list = sorted(list_of_dicts, key=itemgetter('age'))

# Mengecek Apakah File Ada
import os
file_path = 'my_file.txt'
if os.path.isfile(file_path):
    print(f"File {file_path} exists")

# Menghitung Jumlah Kata dalam Teks
from collections import Counter
text = "Python is awesome and Python is easy"
word_counts = Counter(text.split())

# Output dari potongan kode
print("Merged Dictionary:", merged_dict)
print("Squared Numbers:", squared)
print("Reversed String:", reversed_string)
print("Sorted List of Dictionaries:", sorted_list)
print("Word Counts:", word_counts)
