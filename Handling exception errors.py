## Handling exception errors: try-except
#new_list = [2,4,6, 'California']

#for element in new_list:
#    try:
#        print(element/2)

## Agar 'California' tidak terbaca
#    except:
#        print('the element is not number!')

## While-Break case 1:
#n = 4
#while n>0:
#    print(n)
##print('Massage')

## While-Break case 2:
n = 4
while n>0:
    print(n)
    n=n-1
    if n==2:
        break
print('loop ended')