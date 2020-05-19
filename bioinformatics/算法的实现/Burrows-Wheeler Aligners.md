# Burrows-Wheeler Aligners 算法实现



## Burrows-Wheeler Transformer

``` python 
def BMT(dna):
    matrix = []
   
    for i in range(len(dna)):
        t = -i-1
        out = dna[t:]+dna[:t]
        matrix.append(out)
    matrix = sorted(matrix) 
    return ''.join(i[-1] for i in matrix)
print(BMT('ATCGAA'))
```



## Burrows-Wheeler LF

算法的原理在之前的文章中有过讨论了，就不再介绍

下面对python代码进行解释

首先输入一个压缩后的序列`L`

随后对`L`进行重排列并变成一个字符串的格式 

```pyt
L = 'GC$AAAC'
F = ''.join(i for i in sorted(L))#sorted后得到的是一个列表，因而重新变成序列类型
print(L,F)


> TTCCTAACG$A $AAACCCGTTT
```

下一步生成L和F列中各个碱基在各自列中的位置编号

```python 
L_index = [(index,value) for index,value in enumerate(L)]
F_index = [(index,value) for index,value in enumerate(F)]
```

这个编号有什么用呢？ 这个编号是回溯的核心因为L列重新排列后获得的是F列但是这个时候L列和F列的碱基相同却有着不同的位置编码。因为我写的算法是从5端开始回溯！所以从重新排列后的L列开始

那么`L_index = sorted(L_index,key=lambda x:x[1])`后便可以获得L列与F列之间等价碱基之间的关系。结合下面的图，便可以理解回溯的核心。

```python 
 F_index:
([(0, '$'), (1, 'A'), (2, 'A'), (3, 'A'), (4, 'C'), (5, 'C'), (6, 'G')],
L_index:
 [(2, '$'), (3, 'A'), (4, 'A'), (5, 'A'), (1, 'C'), (6, 'C'), (0, 'G')])
```

<img src="https://file.upyun.biopy.cn/bed/20200519130642.png" alt="img" style="zoom: 50%;" />

从L_index[0]开始回溯，迭代`range(len(F_index))`

```python 
L = L_index[0]

def LF(L):
    out =''
    for i in range(len(F_index)):
        F = F_index[L[0]]# 获得传入的L列的碱基其前的碱基（即其在F列中对应的碱基）
        out+=F[1]#把这个碱基加入到序列的第一个位置中
        L = L_index[F[0]]#获取这个碱基在L列中的等价碱基。不断迭代获取原始的序列
        
    return out 

LF(L)
```

总代码如下：

```python 
def LF(L):
    out =''
    for i in range(len(F_index)):
        F = F_index[L[0]]# 获得传入的L列的碱基其前的碱基（即其在F列中对应的碱基）
        out+=F[1]#把这个碱基加入到序列的第一个位置中
        L = L_index[F[0]]#获取这个碱基在L列中的等价碱基。不断迭代获取原始的序列
        
    return out 

def BWLF(L):
    F = ''.join(i for i in sorted(L))
    L_index = [(index,value) for index,value in enumerate(L)]
    L_index = sorted(L_index,key=lambda x:x[1])
    F_index = [(index,value) for index,value in enumerate(F)]
    L = L_index[0]
    return LF(L)

BWLF('TTCCTAACG$A')
```

## Burrows-Wheeler Align 

### Get substring 

``` pyhon 
def BWA_substing(refBWT,dnaseq):
    L = refBWT
    F = ''.join(i for i in sorted(L))#sorted后得到的是一个列表，因而重新变成序列类型
    L_index = [(index,value) for index,value in enumerate(L)]
    F_index = [(index,value) for index,value in enumerate(F)]
    L_index = sorted(L_index,key=lambda x:x[1])


    #比对时，5端开始比对则从F列开始找
    result = []
    for F in F_index:
        if F[1] ==dnaseq[0]: 

            out =''
            for i in range(len(dnaseq)):
                L = L_index[F[0]]# 获得传入的L列的碱基其前的碱基（即其在F列中对应的碱基）
                if L[1] == '$':
                    out = None
                    break  
                else:
                    out+=L[1]#把这个碱基加入到序列的第一个位置中
                    F = F_index[L[0]]#获取这个碱基在L列中的等价碱基。不断迭代获取原始的序列
            if out:
                result.append(out)
    return result
    
    
 print(BWA_substing('GC$AAAC','ACC'))
```

