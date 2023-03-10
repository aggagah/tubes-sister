# -*- coding: utf-8 -*-
"""[v2]HANSIPXTRUNO-TUBES SISTER-DOCUMENT SIMILARITY-PARALLEL-THREAD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mjt-st_7QynSxm4poWwf9-cNNftQqX2Y

### DOCUMENT SIMILARITY - PARALLEL
### KELOMPOK: HansipxTruno IF-44-01
### ANGGOTA :
- Adinda Arwa Salsabil - 1301204011

- Gagah Aji Gunadi - 1301204093

- Ihsani Hawa Arsytania - 1301204105

- Muhammad Raffif Haziq - 1301204146

- Syahdan Naufal Nur Ihsan - 1301204110

import libraries
"""

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
from threading import *
import os

path = "db"
dir_list = os.listdir(path)
listDatabase = []
for i in range(len(dir_list)):
  doc1 = []

  with open(f"db\{dir_list[i]}") as f:
    splitSentence = sent_tokenize(f.read())
    for sentence in splitSentence:
      doc1.append(sentence)
  # print("Number of sentences :", len(doc1))
  """split doc1 sentence into words"""

  splittedDoc1 = [[word.lower() for word in word_tokenize(text)] for text in doc1]
  doc1all = []
  for i in splittedDoc1:
    for j in i:
      doc1all.append(j)
  listDatabase.append(doc1all)

"""main algorithm"""
# dokumen yang akan dicek
doc = []
results = []

with open("check.txt") as f:
  splitSentence = sent_tokenize(f.read())
  for sentence in splitSentence:
    doc.append(sentence)
print("Number of sentences :", len(doc))
"""split doc sentence into words"""

splittedDoc = [[word.lower() for word in word_tokenize(text)] for text in doc]
docall = []
for i in splittedDoc:
  for j in i:
    docall.append(j)

class firstApp(Thread):
  def calculate(self, document1, document2, results):
    result = 0
    for word1 in document1:
      for word2 in document2:
        if word1 == word2 and (word1 != "." and word2 != "."):
          result+=1
          # print(f"{word1} is similar with {word2}")
        else:
          continue
    persentase = (result / (len(document1) + len(document2))) * 100
    results.append(persentase)
    print(f"Persentase kemiripan dokumen : {persentase}%")

app = firstApp()
# print("Kemiripan dokumen dengan dokumen 1 pada database")
thread1 = Thread(target=app.calculate, args=(docall, listDatabase[0], results))
thread1.start()
print()

# print("Kemiripan dokumen dengan dokumen 2 pada database")
thread2 = Thread(target=app.calculate, args=(docall, listDatabase[1], results))
thread2.start()
print()

# print("Kemiripan dokumen dengan dokumen 3 pada database")
thread3 = Thread(target=app.calculate, args=(docall, listDatabase[2], results))
thread3.start()
print()

# print("Kemiripan dokumen dengan dokumen 4 pada database")
thread4 = Thread(target=app.calculate, args=(docall, listDatabase[3], results))
thread4.start()
print()

# print("Kemiripan dokumen dengan dokumen 5 pada database")
thread5 = Thread(target=app.calculate, args=(docall, listDatabase[4], results))
thread5.start()
print()

# print("Kemiripan dokumen dengan dokumen 6 pada database")
thread6 = Thread(target=app.calculate, args=(docall, listDatabase[5], results))
thread6.start()
print()

# print("Kemiripan dokumen dengan dokumen 7 pada database")
thread7 = Thread(target=app.calculate, args=(docall, listDatabase[6], results))
thread7.start()
print()

# print("Kemiripan dokumen dengan dokumen 8 pada database")
thread8 = Thread(target=app.calculate, args=(docall, listDatabase[7], results))
thread8.start()
print()

# print("Kemiripan dokumen dengan dokumen 9 pada database")
thread9 = Thread(target=app.calculate, args=(docall, listDatabase[8], results))
thread9.start()
print()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
thread9.join()
print("Semua thread telah dieksekusi")

finalResult = 0
for value in results:
  finalResult += value
print(f"Kemiripan dokumen keseluruhan : {finalResult / len(results)}%")