#pictoblox
# import numpy
# print(numpy.__version__)

# import numpy
# arr = numpy.array([1, 2, 3, 4, 5]) #numpy burda sınıf
# print(arr)
# print(type(arr))

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))

###veri türleri--------------------
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# xxx = np.array([1, 2, 3, 4, 5],np.int8)
# print(arr)
# print(type(arr))
# print(type(xxx))
# print(arr.dtype)
# print(xxx.dtype)


#düzenli olma---------

# import numpy as np
# arr= np.array([[1,2,5],[7,8,9]]) #eğer np.array([[1,2],[7,8,9]]) olsaydı hata verirdi.
# arr1 = np.arange(5,15,2)
# print(arr1)

#zeros ve ones--------------
# import numpy as np
# arr1 = np.zeros((3,4))
# print(arr1)

# arr2 = np.ones((3,5,2))
# print(arr2)

# arr3 = np.ones((3,5))*4
# print(arr3)


# arange ile aralık------------------
# import numpy as np

# arr1 = np.arange(10)
# print(arr1)

# arr2 = np.arange(7,30,5)
# print(arr2)

# Birim matris------------------
# import numpy as np

# arr1 = np.eye(5)
# print(arr1)

# bir dizinin tersi
# import numpy as np

# arr1 = np.arange(1,11)
# print("Dizi :\n",arr1)
# arr1 = arr1.reshape(5,2) #diziyi yeniden şelille
# print("Dizi :\n",arr1)


# tersi = arr1[::-1]          #diziyi tersine  çevirdi
# print("Tersi:\n",tersi) 

# numpy satırlar ve sütünlar---------------------------
# import numpy as np

# arr1 = np.arange(1,21).reshape(5,4)
# print (arr1)

# print("\nBirinci satır => arr1[0]   : ",arr1[0])
# print("\nİkinci satır  => arr1[1]   : ",arr1[1])
# print("\nİlk iki satır => arr1[0:2] : \n",arr1[0:2])
# print("\nBirinci sütun => arr1[:,0] : ",arr1[:,0])
# print("\nİkinci sütun  => arr1[:,1] : ",arr1[:,1]) 
# print("\nEleman        => arr1[2,1] : ",arr1[2,1])  


# split (bölme)------------------------------
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 2)
# print("\n3'e bölünen yeni dizi :",newarr)

#search(dizide arama)-----------------
# import numpy as np
# arr = np.array([3, 2, 0, 1])
# print(np.sort(arr)) # numerik sıralama

# arr = np.array(['muz','elma','armut'])
# print(np.sort(arr)) # string sıralama

# arr = np.array([True, False, True])
# print(np.sort(arr)) # bolean sıralama

# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr)) # 2D array sıralama


# filreleme-------------------


# numpy ve OpenCV ile Resim oluşturma-----------------
import cv2
import numpy as np

r1 =np.full((5,5,3),[255,255,255],dtype=np.uint8)
print(r1)

dtype=np.uint8

cv2.imshow("Olusan resim", r1)

cv2.waitKey(0)
 
cv2.destroyAllWindows()
