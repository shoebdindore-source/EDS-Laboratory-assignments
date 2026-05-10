#question1)
import numpy as np

# Input matrices
print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])


# Addition
print("Addition (A + B):")
print(matrix_a + matrix_b)
# Subtraction
print("Subtraction (A - B):")
print(matrix_a - matrix_b)
# Multiplication (element-wise)
print("Element-wise Multiplication (A * B):")
print(matrix_a*matrix_b)
# Matrix multiplication (dot product)
print("A dot B:")
print(np.dot(matrix_a,matrix_b))
# Transpose
print("Transpose of A:")
print(matrix_a.T)

#question2)
import numpy as np

# Input matrices
print("Enter Array1:")
arr1 = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Array2:")
arr2 = np.array([list(map(int, input().split())) for i in range(3)])

# Perform horizontal stacking (hstack)

print("Horizontal Stack:")
print(np.hstack((arr1,arr2)))

# Perform vertical stacking (vstack)
print("Vertical Stack:")
print(np.vstack((arr1,arr2)))

#question3)
import numpy as np

# Take user input for the start, stop, and step of the sequence
start = int(input())
stop = int(input())
step = int(input())

sequence= np.arange(start,stop,step)
# Generate the sequence using np.arange()
print(sequence)
# Print the generated sequence


#question4)
import numpy as np

def array_operations(A, B):
   
	arr_A=np.array(A)
	arr_B=np.array(B)
	# Arithmetic Operations
	sum_result = arr_A +arr_B
	diff_result = arr_A-arr_B
	prod_result = arr_A*arr_B

	# Statistical Operations
	mean_A = np.mean(arr_A)
	median_A = np.median(arr_A)
	std_dev_A = np.std(arr_A)

	# Bitwise Operations
	and_result = arr_A & arr_B
	or_result = arr_A | arr_B
	xor_result = arr_A ^ arr_B

    # Output results with one space between each element
	print("Element-wise Sum:", ' '.join(map(str, sum_result)))
	print("Element-wise Difference:", ' '.join(map(str, diff_result)))
	print("Element-wise Product:", ' '.join(map(str, prod_result)))
    
	print(f"Mean of A: {mean_A}")
	print(f"Median of A: {median_A}")
	print(f"Standard Deviation of A: {std_dev_A}")
    
	print("Bitwise AND:", ' '.join(map(str, and_result)))
	print("Bitwise OR:", ' '.join(map(str, or_result)))
	print("Bitwise XOR:", ' '.join(map(str, xor_result)))

A = list(map(int, input().split()))  # Elements of array A
B = list(map(int, input().split()))  # Elements of array B
array_operations(A, B)

#question5)
import numpy as np

inputlist = list(map(int,input().split(" ")))

# Original array
original_array = np.array(inputlist)

# Create a view
view_array =original_array.view()

# Create a copy
copy_array = original_array.copy()

# Modify the view
view_array[0] = 99
print("Original array after modifying view:", original_array)
print("View array:", view_array)

# Modify the copy
copy_array[1] = 88
print("Original array after modifying copy:", original_array)
print("Copy array:", copy_array)


#question6)
import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Find indices where value matches in array1
indices=np.where(array1==search_value)[0]
print(indices)
# Count occurrences in array1
count=np.count_nonzero(array1==count_value)
print(count)
# Broadcasting addition
broadcasted_array=array1+broadcast_value
print(broadcasted_array)
# Sort the first array
sorted_array=np.sort(array1)
print(sorted_array)
