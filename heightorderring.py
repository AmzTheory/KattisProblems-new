#https://open.kattis.com/problems/height


'''
5 6 2 1 7 3

0  5
0  5 6
2  2 5 6
3  1 2 5 6
0  1 2 5 6 7
3  1 2 3 5 6 7
=8 
'''


def main():
    p=int(input())
    dic=dict()
    for i in range(p):
        inp=input().split(" ")
        dic[int(inp[0])]=calculateNumberOfSteps(inp[1:])
    for (k,v) in dic.items():
         print(k,v)

def calculateNumberOfSteps(order):
    currentOrder=[]
    totalSteps=0
    for i in order:
            totalSteps+=insert(currentOrder,int(i))
    return totalSteps
        


def insert(ls,v):
    sum=0
    for i in range(len(ls)-1,-1,-1):
        if(v<=ls[i]):
            sum+=1
        else:
            temp=((ls[0:(i+1)]+[v])+ls[i+1:])##reordering the list
            ls.clear()
            ls.extend(temp)
            return sum
    ls.insert(0,v)
   
    return sum


main()
