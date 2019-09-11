# nomor 1 

def calculate_years(principal, interest, tax, desired) :
    year = 0

    while principal < desired :
        principal = principal + (principal * interest) - (tax*(principal * interest))

        year += 1

    return year

print(calculate_years(1200,0.17,0.05,2000))

# nomor2

def expandedform(num):
     a = num
     aa= (a[-1])
    

     a = num
     ab= (a[-2])
     bb=str(ab)+"0"
  


     a = num
     ac=(a[-3])
     bc=str(ac)+"00"

     a = num
     ad=(a[-4])
     bd=str(ad)+"000"

     a = num
     ae=(a[-5])
     be=str(ae)+"0000"


     print(str(be)+"+"+str(bd)+"+"+str(bc)+"+"+str(bb)+"+"+str(aa))

     

num=([7,0,3,0,4])
expandedform(num)

# nomor3

def tower_builder(n_floors, block_size ) :
w,h = block_size

z= ''

for i in range (0,n_floors,1):
    for j in range (0, 2):
        if j >= 10-i and j <= 10+i:
            z += ' * '
        else: 
            z += '   '    
    z += '\n'
print (z) 


print tower_builder(10, (2,3))