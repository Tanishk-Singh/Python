def highest_even(li):
 highest_quot = 0
 for i in li :
        if i%2 == 0:
          if i//2 > highest_quot:
            highest_quot = i//2
  
 return 2*highest_quot

print(highest_even([1,2,16,11,4]))
      

