if __name__ == '__main__':
    N = int(input())
    lt=[]
    
    for i in range(N):
        h=input().split()

        if len(h)==2:
            h[1]=int(h[1])
        elif len(h)==3:
            h[2]=int(h[2])
            h[1]=int(h[1])

        if h[0]=='insert':
            lt.insert(h[1],h[2])
        elif h[0]=='print':
            print(lt)
        elif h[0]=='remove':
            lt.remove(h[1])
        elif h[0]=='append':
            lt.append(h[1])
        elif h[0]=='sort':
            lt.sort()
        elif h[0]=='pop':
            lt.pop()
        elif h[0]=='reverse':
            lt.reverse()