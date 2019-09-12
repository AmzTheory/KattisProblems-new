#https://open.kattis.com/problems/whatdoesthefoxsay

def main():
    n=int(input())
    sounds=set()
    for i in range(n):
        rec=input().split(" ")
        cont=True
        while cont:
            line=input()
            if(line.startswith("what does")):
                break
            words=line.split(" ")
            sounds.add(words[2])
        
        for s in rec:
            inter=({s}).intersection(sounds)
            if(inter==set()):
                print (s,end=" ")
main()

