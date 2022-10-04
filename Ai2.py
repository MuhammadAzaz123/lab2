##mylist=[]
##print("enter objects of first list")
##for i in range(5):
##    val=input("enter a value:")
##    n=int(val)
##    mylist.append
##
##mylist2=[]
##print("enter objects of second list...")
##for i in range(5):
##      val=input("enter a value:")
##      mylist2.append
##
##list3=mylist+mylist2;
##print(list3)


##def isPalindrome(word):
##    temp=word[::-1]
##    if temp.capitalize()==word.capitalize():
##        return True
##    else:
##        return False
##
##print(isPalindrome("deed"))


##for indrow in range(3):
##    c.append([])
##    for indcol in range(3):
##        c[indrow].append(0)
##        for indaux in range(3):
##            c[indrow][indcol]+=a[indrow][indaux]*b[indcol][indrow]

##def perimeter(listing):
##    leng=len(listing)
##    perimeter=0
##    for i in range(0,leng-1):
##        dist=(((listing[i][0]-listing[i+1][0]**2)+
##               ((listing[i][1]-listing[i+1][1])*2))*0.5
##              
##        perimeter = perimeter+dist
##    perimeter=perimeter+(((listing[0][0]-listing[leng-1][0])*2)+((listing[0][1]-listing[leng-1])2))*0.5
##    return perimeter
##L=[(1,3),(2,7),(3,9),(-1,0)]
##print(perimeter(L))

##def symmDiff(a,b):
##    e=set()
##    for i in a:
##        if i in a:
##            if i not in b:
##                e.add(i)
##    for i in b:
##        if i not in a:
##            e.add(i)
##    return e
##set1={0,1,2,4,5}
##set2={4,5,7,8,9}
##print(symmDiff(set1,set2))
##print(set1.symmetric_difference(set2))
##print(set2.symmetric_difference(set1))
##print(set1^set2)
##print(set2^set1)

##sample={("shoaib","ali"):"09373643636",("aib","li"):"847373737",("sib","ai"):"43874874387",}
##firstname=input("enter first name")
##lastname=input("enter last name")
##
##searchTuple=(firstname,lastname)
##if searchTuple in sample:
##        print(sample[searchTuple])
##else:
        print("name not found")
