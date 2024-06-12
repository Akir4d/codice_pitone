

x = 0

while (x <= 20):
    x = int (input ("\nInserisci un numero inferiore a 20: "))
    if (x == 20):
        print ("Ho detto inferiore a 20! Sei al limite questo e' un avvertimento")
    elif (x > 10):
        print ("il numero e' maggiore di 10")
    elif (x == 10):
        print ("il numero e' uguale a 10")
    else:
        print ("il numero e' minore di 10")
print ("Mi spiace hai sballato!")