import collections 
import Bio
from Bio import SeqIO
import random 
import pandas as pd 

nucleotides =['A','C','G','T']

#生产随机的DNA序列
def randomDNA(lenth):
    return ''.join(random.choice(nucleotides) for i in range(lenth))

# 检查这个序列是否是一个DNA序列
def validateSeq(seq):
    dna_seq = seq.upper()
    for i in seq:
        if i not in nucleotides:
            return False

    return seq 
# 统计DNA序列中各个碱基的个数
def countNTFrequency(seq):
    tmpFreqDict = {'A':0,'C':0,'G':0,'T':0}
    for nt in seq:
        tmpFreqDict[nt] +=1 
        
    return tmpFreqDict
    # return dict(collections.Counter(seq))

#读入fasta格式的序列
def read_fasta(filename):
    return [i for i in SeqIO.parse(open(filename),'fasta')]

def profileMatrix(DNARecords):
    #输入Bio.SeqRecord.SeqRecord 的List


    #生产一个4xn，n为DNA序列的数目，4代表4种碱基,类型是一个pd.DataFrame
    if all(isinstance(dna,Bio.SeqRecord.SeqRecord) for dna in DNARecords ):
        # 首先转变成DNAStrings的样式
        DNAStrings = pd.DataFrame([pd.Series(list(i.seq),name=i.name)for i in DNARecords])
        Profile = DNAStrings.apply(lambda x:x.value_counts()).fillna(0)
        return Profile
 


def Consensus(profileMatrix):
    #Consensus是ProfileMatrix中每一个DNA序列出现频率最多的碱基的组合，
    # 也即每一个序列中频率最高的字符的合集组成的一个1xn的矩阵
    #输入的矩阵类型是pd.DataFrame
    if isinstance(profileMatrix,pd.DataFrame):
        #定义一个匿名函数
        def func(x):
            out= x[x.values == max(x)].index
            if len(out)  >1:
                print('{}有多个Consensu，这些分别是{}'.format(x.name,out.tolist()))
                out = random.choice(out)
            return out

        #Consensu = profileMatrix.apply(lambda x :x[x.values ==max(x)].index,axis=0)
        Consensu = profileMatrix.apply(lambda x :func(x),axis=0)
        return Consensu








# Bowtile wheeler Align 

#Bowtile wheeler Transform
def BMT(dna):
    matrix = []
   
    for i in range(len(dna)):
        t = -i-1
        out = dna[t:]+dna[:t]
        matrix.append(out)
    matrix = sorted(matrix) 
    return ''.join(i[-1] for i in matrix)

#BWLF回溯算法
def BWLF(L):
    F = ''.join(i for i in sorted(L))#sorted后得到的是一个列表，因而重新变成序列类型
    L_index = [(index,value) for index,value in enumerate(L)]
    L_index = sorted(L_index,key=lambda x:x[1])
    F_index = [(index,value) for index,value in enumerate(F)]
    L = L_index[0]
    out =''
    #LF过程
    for i in range(len(F_index)):
        F = F_index[L[0]]# 获得传入的L列的碱基其前的碱基（即其在F列中对应的碱基）
        out+=F[1]#把这个碱基加入到序列的第一个位置中
        L = L_index[F[0]]#获取这个碱基在L列中的等价碱基。不断迭代获取原始的序列
    return out 

    #LF回溯过程
def LF(L,L_index,F_index):
    """传入L列中的$所在的turple (num,$)
    通过从5端开始还原原始的序列
    
    若想从3端开始，BWA等算法的方式开始则只需要改写整个循环的开始过程 即是
    从F列开始
    """
    out =''
    for i in range(len(F_index)):
        F = F_index[L[0]]# 获得传入的L列的碱基其前的碱基（即其在F列中对应的碱基）
        out+=F[1]#把这个碱基加入到序列的第一个位置中
        L = L_index[F[0]]#获取这个碱基在L列中的等价碱基。不断迭代获取原始的序列
        
    return out 