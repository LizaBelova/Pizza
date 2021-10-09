def greeting(username='Liza'):
    print('Hello '+username)
greeting(username='Hello!')
def makepizza(size,*toppings):
    print('Make pizza '+str(size)+'with toppings: ' )
    for i in toppings:
        print(i)

makepizza(20, 'onion','cheese','mionez', 'paprika')

        
    

