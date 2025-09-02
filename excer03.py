import random, itertools
from collections import Counter

def nhapvao():
    return list(map(int, input("Nhập vào các số (cách nhau bởi khoảng trắng): ").split()))

def bai_1(): return sum(nhapvao())
def bai_2():
    m=1
    for i in nhapvao(): m*=i
    return m
def bai_3(): return max(nhapvao())
def bai_4(): return min(nhapvao())
def bai_5():
    lst=input().split();return sum(1 for s in lst if len(s)>0 and s[0]==s[-1])
def bai_6(): return sorted(input().split(),key=lambda x:x[-1])
def bai_7(): return list(set(input().split()))
def bai_8():
    lst=input().split()
    return "Danh sách rỗng." if not lst else lst
def bai_9():
    import copy
    lst=input().split();return list(copy.deepcopy(lst))
def bai_10():
    lst=input().split();n=int(input())
    return [x for x in lst if len(x)>n]
def bai_11():
    lst1=input().split();lst2=input().split()
    chung=[x for x in lst1 if x in lst2]
    return chung if chung else "Hai danh sách không có phần tử chung."
def bai_12():
    lst=input().split()
    for i in [0,4,5]:
        if i<len(lst): lst.pop(i)
    return lst
def bai_13(): return [[["*" for _ in range(6)]for _ in range(4)]for _ in range(3)]
def bai_14():
    a=list(map(int,input().split()))
    return [x for x in a if x%2!=0]
def bai_15():
    a=list(input());random.shuffle(a);return ''.join(a)
def bai_16():
    sq=[i**2 for i in range(1,31) if i**2<=30]
    return sq[:5],sq[-5:]
def bai_17():
    lst=list(map(int,input().split()))
    def is_prime(n):
        if n<2:return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:return False
        return True
    return all(is_prime(x) for x in lst)
def bai_18(): return list(itertools.permutations(input().split()))
def bai_19():
    a=set(input());b=set(input())
    return list(a-b),list(b-a)
def bai_20():
    a=input()
    return [(i,v) for i,v in enumerate(a)]
def bai_21(): return str(input())
def bai_22():
    lst=input().split();item=input()
    return f"Vị trí: {lst.index(item)}" if item in lst else "Không tìm thấy."
def bai_23(): return [j for i in eval(input()) for j in i]
def bai_24(): a=input().split();b=input().split();a.extend(b);return a
def bai_25(): return random.choice(input().split())
def bai_26():
    a=input().split();b=input().split()
    return len(a)==len(b) and any(b==a[i:]+a[:i] for i in range(len(a)))
def bai_27(): a=sorted(set(map(int,input().split())));return a[1] if len(a)>1 else None
def bai_28(): a=sorted(set(map(int,input().split())));return a[-2] if len(a)>1 else None
def bai_29(): return list(set(input().split()))
def bai_30(): return dict(Counter(input().split()))
def bai_31():
    a=list(map(int,input().split()));l,h=map(int,input().split())
    return sum(l<=x<=h for x in a)
def bai_32():
    a=input().split();b=input().split()
    return any(a[i:i+len(b)]==b for i in range(len(a)-len(b)+1))
def bai_33():
    a=input().split()
    return [a[i:j] for i in range(len(a)+1) for j in range(i+1,len(a)+1)]
def bai_34():
    n=int(input());s=[1]*(n+1);s[0]=s[1]=0
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i:n+1:i]=[0]*len(range(i*i,n+1,i))
    return [i for i in range(n+1) if s[i]]
def bai_35():
    a=input().split();n=int(input())
    return [f"{x}{i}" for i in range(1,n+1) for x in a]
def bai_36(): return id(input())
def bai_37(): return list(set(input().split())&set(input().split()))
def bai_38():
    a=input().split()
    for i in range(0,len(a)-1,2):a[i],a[i+1]=a[i+1],a[i]
    return a
def bai_39(): return int("".join(input().split()))
def bai_40():
    a=input().split();d={}
    for w in a:d.setdefault(w[0],[]).append(w)
    return d
def bai_41(): return [[] for _ in range(int(input()))]
def bai_42():
    a=input().split();b=input().split()
    return {"Missing":[x for x in a if x not in b],"Additional":[x for x in b if x not in a]}
def bai_43(): return tuple(input().split())
def bai_44():
    n=int(input());a=list(range(1,n+1))
    return [a[i:i+5] for i in range(0,len(a),5)]
def bai_45(): return sorted(set(input().split())|set(input().split()))
def bai_46(): return input().split()[1::2]
def bai_47():
    a=input().split();e=input();r=[]
    for x in a:r+=[e,x]
    return r
def bai_48():
    for s in eval(input()):print(s)
def bai_49():
    c=input().split();d=input().split()
    return [{"màu":x,"mã màu":y} for x,y in zip(c,d)]
def bai_50():
    a=eval(input());k=input()
    return sorted(a,key=lambda x:x[k])

def main():
    while True:
        print("\n===== MENU =====")
        for i in range(1,51): print(f"{i}. Bài {i}")
        print("0. Thoát")
        chon=input("Chọn bài: ").strip()
        if chon=="0":break
        try: print(globals()[f"bai_{chon}"]())
        except: print("Lỗi hoặc lựa chọn không hợp lệ.")

if __name__=="__main__": main()
