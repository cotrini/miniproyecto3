# this function use cuadratic center method to make a direction on hash table
def hashFunction(number):
    cuadrado = number ** 2
    cuadrado=str(cuadrado)
    pos=len(cuadrado)//2
    num=cuadrado[pos-1:pos+1]
    num=int(num)
    return num 




    