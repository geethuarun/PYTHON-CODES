# for row in range (1,5):
#     for col in range (1,row+1):
#         print(col,end=" ")
#     print()





# t=1
# while(t<=5):
#     print(t)
#     t+=1
# for row in range (4,0,-1):
#      for col in range (row):
#          print("#",end=" ")
#      print()



# n=3
# for i in range(1,n+1):
#      print(str(n)*i ,end="+")





# n=1
# while(n<=3):
#      print("k")
#      n+=1

#square
# for row in range(5):
#      for col in range(5):
#           print("*",end=" ")
#      print()
    
# #increasing triangle pattern
# for row in range(1,5):
#      for col in range(row):
#           print("*",end=" ")
#      print()


#decreasing triangle pattern
# for row in range(4,0,-1):
#      for col in range(row):
#           print("*",end=" ")
#      print()




for row in range(1,6):
     for col in range(1,6):
          if row==5 or col==5 or row+col==8 :
               print("*",end="")
          else:
               print(end=" ")
     print()

    