def int_to_bin(numb:int) ->str:

    binary = ""
    i = 128
    a = numb

    while i >= 1:
        binary += str(a//i)
        a = a%i
        i = i//2


    return (int(binary)) 
