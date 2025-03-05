totalbottles = 0
counter = 0
todaybottles = 0
totalpayout = 0
keepGoing = "y"  


while keepGoing == 'y':
    while counter < 7:
        totalbottles_1 = int(input('sold bottles today'))
        todaybottles += totalbottles_1
        totalpayout_1 = totalbottles_1 * 0.1
        totalpayout += totalpayout_1
        counter += 1
        print('total bottles sold today #',counter, totalbottles_1)
    print("The total number of bottles collected", todaybottles )
    print("The total paid out is $", totalpayout)
    print("Do you want to enter another week’s worth of data?")
    keepGoing = input("Enter y or n")
    if keepGoing == 'y':
        totalbottles = 0
        counter = 0
        todaybottles = 0
        totalpayout = 0
