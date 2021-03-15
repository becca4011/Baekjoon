# = or - or j 가 나왔을 때 검사

ca = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
sv = []
st = input()

cnt = 0
fi = 0
for s in st:
    sv.append(s)
    #print("".join(sv))
    if s == '=' or s == '-' or s == 'j':
        while(len(sv) != 0):
            if "".join(sv) in ca:
                cnt += 1
                #print("A", cnt)
                sv.clear()
            else:
                cnt += 1
                #print("B", cnt)
                del sv[0]
                
    elif fi == len(st)- 1 and len(sv) != 0:
        cnt += len(sv)
        #print("C", cnt)
        
    fi += 1
            
print(cnt)
