# def removeduplicates(input_list):
#     """Remove duplicates from a list while preserving order."""
#     seen = set()
#     output_list = []
#     for item in input_list:
#         if item not in seen:
#             seen.add(item)
#             output_list.append(item)
#     return output_list
# # Example usage
# if __name__ == "__main__":
#     sample_list = [1, 2, 2, 3, 4, 4, 5]
#     print("Original list:", sample_list)
#     print("List after removing duplicates:", removeduplicates(sample_list))
# a = 10
# b= 20
# def lcm(a,b):
#     greater = max(a,b)    
#     while True:
#         if greater % a == 0 and greater % b ==0 :
#             lcm = greater
#             break
#     greater +=1
#     return lcm    
# print("LCM of",a,"and",b,"is",lcm(a,b))

# def my_generator():
#     for i in range (5):
#         yield i
# gen = my_generator()
# print(next (gen)) 

# def prime_checker(num):
#     if num > 1:
#         for i in range(2, int(num**0.5) + 1):
#             if (num % i) == 0:
#                 return False
#         return True
#     else:
#         return False
    
# num = 29
# if prime_checker(num):
#     print(num, "is a prime number")

# def is_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)


# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")

# if is_anagram(s1, s2):
#     print("Anagram")
# else:
#     print("Not an Anagram")

# def fibonacci(n):
#     a, b = 0,1
#     for _ in range (n):
#         print(a, end=' ')
#         a,b = b, a+b

# fibonacci(10)  

# def factorial(n):
#     fact =1
#     for i in range (1, n+1):
#         fact*=i
#     return fact
# num = 5
# print("Factorial of", num, "is", factorial(num))

# arr = list (map (int, input("Enter numbers separated by space: ").split()))
# max_val = arr[0]
# for num in arr:
#     if num > max_val:
#         max_val = num
# print("Maximum value in the array is:", max_val)


# arr = list(map(int, input("Enter values separated by space ").split()))
# unique = []
# for num in arr:
#     if num not in unique:
#         unique.append(num)
# print("Array after removing duplicates:", unique)


s = input()
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


s = input("Enter a string: ").split()
count = {}
for word in s :
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)  

def removeduplicates(input_list):
    seen = set()
    output_list  = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            output_list.append(item)
    print( output_list)
input_list = list(map(int, input("Enter numbers separated by space: ").split()))
