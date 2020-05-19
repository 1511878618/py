
def BWLF(L):
    F = ''.join(i for i in sorted(L))#sorted后得到的是一个列表，因而重新变成序列类型
    L_index = [(index,value) for index,value in enumerate(L)]
    L_index = sorted(L_index,key=lambda x:x[1])
    F_index = [(index,value) for index,value in enumerate(F)]
    L = L_index[0]
    out =''
    for i in range(len(F_index)):
        F = F_index[L[0]]# 获得传入的L列的碱基其前的碱基（即其在F列中对应的碱基）
        out+=F[1]#把这个碱基加入到序列的第一个位置中
        L = L_index[F[0]]#获取这个碱基在L列中的等价碱基。不断迭代获取原始的序列
    return out 

print(BWLF('TTCCTAACG$A'))