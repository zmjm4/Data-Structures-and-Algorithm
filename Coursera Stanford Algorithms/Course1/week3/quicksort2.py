# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 23:12:56 2018

@author: Administrator
"""
#更换pivot
a=open('data.txt')
b=[]
for i in a.readlines():
	b.append(int(i.strip()))


def quicksort(A,l,r):
    #比较次数
    if l>=r:
        #return
        return 0
    else:
        #交换A[l-1],A[r-1]
        p=A[l-1]
        A[l-1]=A[r-1]
        A[r-1]=p
        i=l
        for j in range(l,r):
            if A[j]<p:
                #交换A[j]和A[i]
                x=A[j]
                A[j]=A[i]
                A[i]=x
                i+=1
        #交换A[l-1]和A[i-1]
        y=A[i-1]
        A[i-1]=p
        A[l-1]=y
        '''
        快速排序
        quicksort(A,1,i-1)
        quicksort(A,i+1,r)
        '''
        return quicksort(A,1,i-1)+quicksort(A,i+1,r)+r-l        
print len(b)
print quicksort(b,1,10000)
'''
c=b[:20]
print c
quicksort(c,1,20)
print c
'''

    