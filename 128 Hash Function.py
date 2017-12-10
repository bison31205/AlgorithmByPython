# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 19:59:35 2017

@author: KangziLi
@source: lintcode - 128. Hash Function
"""

class Solution:
    """
    In data structure Hash, hash function is used to convert a string(or any other type) into an integer smaller than hash size and bigger or equal to zero. The objective of designing a hash function is to "hash" the key as unreasonable as possible. A good hash function can avoid collision as less as possible. A widely used hash function algorithm is using a magic number 33, consider any string as a 33 based big integer like follow:
    hashcode("abcd") = (ascii(a) * 333 + ascii(b) * 332 + ascii(c) *33 + ascii(d)) % HASH_SIZE 
                     = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE
                     = 3595978 % HASH_SIZE
    here HASH_SIZE is the capacity of the hash table (you can assume a hash table is like an array with index 0 ~ HASH_SIZE-1).
    Given a string as a key and the size of hash table, return the hash value of this key.  
    @param: key: A string you should hash
    @param: HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        ans = 0
        for x in key:
            ans = (ans * 33 + ord(x)) % HASH_SIZE
        return ans
