
row=int(input("Enter your matrix rows:"))

col=int(input("Enetr your second matrix colomns:"))


mat=[]

for i in range(row):

 a=[]
  
 for j in range(col):

         a.append(0)

         mat.append(a)



for k in range(len(mat)):

        for l in range(len(mat[0])):

                mat[k][l] == int(input("Enter elements:"))
                #[k][l]=row[i][j] + col[i][j]

print("Your matrix is :")
for j in range(len(mat)):
        for i in range(len(mat[0])):

                print(mat[k][l])
         

        






 



