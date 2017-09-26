#!/usr/bin/python
# -*- coding: utf-8 -*-

#对于两个方程 
#x≡c1(modm1) 
#x≡c2(modm2) 
#将其合并成一个方程，有解条件为(m1,m2)|(c2−c1) 
#m=m1m2/(m1,m2) 
#c=(inv(m1/(m1,m2),m2/(m1,m2))∗(c2−c1)/(m1,m2))%m2/(m1,m2)∗m1+c1 
#最终得出一个式子x≡c(modm1) 
#x=c%m即为原问题的一个解

import sys

#扩展的欧几里得算法求逆元和gcd
def gcd_inv( a , b ):
     if (b == 0):
         return 1, 0, a
     else:
         x , y , q = gcd_inv( b , a % b )
         x , y = y, ( x - (a // b) * y )
         return x,y,q

def do(N=1000000, NN=1005000, gcd_inv=gcd_inv):
    
    #筛法求euler'totient
    #φ(n)=n*（1-1/p1)(1-1/p2)....(1-1/pk),其中p1、p2…pk为n的所有素因子。
    #比如：φ(12)=12*(1-1/2)(1-1/3)=4。
    #利用这个就比较好求了，可以用类似求素数的筛法。
    #先筛出N以内的所有素数，再以素数筛每个数的φ值。
    #比如求10以内所有数的φ值：
    #设一数组phi[11]，赋初值phi[1]=1,phi[2]=2...phi[10]=10；
    #然后从2开始循环，把2的倍数的φ值*(1-1/2)，则phi[2]=2*1/2=1,phi[4]=4*1/2=2,phi[6]=6*1/2=3....；
    #再是3，3的倍数的φ值*(1-1/3)，则phi[3]=3*2/3=2,phi[6]=3*2/3=2，phi[9]=.....；
    #再5，再7...因为对每个素数都进行如此操作，因此任何一个n都得到了φ(n)=n*（1-1/p1)(1-1/p2)....(1-1/pk)的运算
    #觉得这个“筛”还是比较好用的，以前求数的所有因子之和也是用的它
    
    phi = list(xrange(NN)); phi[0:2] = [-1, -1]
    for n, p in enumerate(phi):
        if p == n: #they are prime
            for i in xrange(p, NN, p): #p的倍数
                phi[i] -= phi[i] // p#divides evenly
    ans = 0
    for n in xrange(N, NN):
        for m in xrange(n + 1, NN):
            a = phi[n]; b = phi[m]
            inv,x,g = gcd_inv(m, n)
            if (a - b) % g: 
                continue
            ans += m * (((inv * (a - b)) % n) // g) + b
    return ans

print(do())

#slightly faster: ans += m * ((inv * ((a - b) // g)) % (n // g)) + b
#Also faster to simply return (m, d) in gcd_inv