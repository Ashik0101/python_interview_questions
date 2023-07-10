def reverse(string):
    result = ""
    for char in string:
          result = char + result
    return result
 


print(reverse("Python is fun"))