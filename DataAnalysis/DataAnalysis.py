import numpy

#Goal: Calculate how close each of our metrics gets to the "ground truth"
#Reference: Crypto-code from CIS331 HW2 Written by David Cahn
def chi_squared(a,b):
    if (len(a) != len(b)):
        return -1
    diff = 0.0
    for i in range (0,len(a)):
        squared_diff = numpy.square((a[i] - b[i]))
        my_diff = float(squared_diff) / b[i] 
        diff = diff + my_diff
    return diff

#From my EXCEL Spreadsheet -- Actual data values for each Test
arr1 = [0.571428571, 0.785714286, 0.714285714, 0.607142857, 0.571428571, 0.678571429, 0.535714286, 0.5, 0.571428571, 0.714285714, 0.607142857, 0.535714286, 0.5, 0.571428571, 0.607142857, 0.678571429, 0.571428571, 0.571428571, 0.642857143, 0.535714286, 0.607142857, 0.5, 0.714285714, 0.535714286, 0.5, 0.75, 0.5, 0.714285714, 0.75, 0.571428571]
arr2 = [0.578947368, 0.9, 0.5, 0.5, 0.45, 0.45,0.25, 0.55, 0.5, 0.75, 0.65, 0.7, 0.35, 0.35, 0.75, 0.75, 0.7, 0.75, 0.6, 0.55, 0.5, 0.25, 0.8, 0.5, 0.6, 0.85, 0.35, 0.5, 0.45, 0.45]
arr3 = [0.5, 0.7, 0.6, 0.5, 0.6, 0.5, 0.4, 0.2, 0.5, 0.6, 0.6, 0.8, 0.5, 0.6, 0.7, 0.9, 0.7, 0.5, 0.2, 0.4, 0.5, 0.2, 0.6, 0.6, 0.5, 0.9, 0.5, 0.9, 0.9,0.2]
arr4 = [0.7, 0.9, 0.65, 0.45, 0.368421053, 0.65, 0.4, 0.65, 0.5, 0.8, 0.45, 0.65, 0.5, 0.65, 0.75,0.75,0.5,0.421052632,0.45,0.35,0.45, 0.3, 0.75,0.45, 0.4, 0.85, 0.4, 0.6, 0.55, 0.45]
arr5 = [0.5, 1, 0.631578947, 0.277777778, 0.421052632, 0.647058824, 0.3125, 0.6, 0.4, 0.736842105, 0.526315789, 0.263157895, 0.470588235, 0.529411765, 0.666666667, 0.722222222, 0.777777778, 0.473684211, 0.4, 0.352941176, 0.555555556, 0.3, 0.6875, 0.315789474, 0.294117647, 0.875, 0.588235294, 0.75, 0.588235294, 0.4]
arr6 = [0.727272727, 0.727272727, 1, 0.555555556, 0.1, 0.6, 0.2, 0.4, 0.3, 0.8, 0.5, 0.5, 0.3, 0.333333333, 0.333333333, 0.8, 0.4, 0.7, 0.7, 0.444444444, 0.555555556, 0.5, 0.555555556, 0.5, 0.333333333, 0.8, 0.333333333, 0.666666667, 0.3, 0.666666667]

#For Column Chart
print ('TEST 1')
print chi_squared(arr1,arr1)
print ('TEST 2')
print chi_squared(arr1,arr2)
print ('TEST 3')
print chi_squared(arr1,arr3)
print ('TEST 4')
print chi_squared(arr1,arr4)
print ('TEST 5')
print chi_squared(arr1,arr5)
print ('TEST 6')
print chi_squared(arr1,arr6)

#For Line Chart
for i in range (0,len(arr1)):
	print "[" + str(i) + "," + str(arr1 [i]) + "," + str(arr4[i])+ "]"