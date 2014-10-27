#!/usr/bin/env python

#Technique come from here: http://permalink.gmane.org/gmane.comp.file-systems.s3.s3tools/583
import hashlib
import sys
import os

def get_multipart(file, chunk_size):
    f = open(file, 'r')

    binary_hash_list = []

    while True:
        md5 = hashlib.md5()

        data = f.read(chunk_size)
        if not data:
            break
        md5.update(data)
        #Note that the digest() function, not hexdigest() is used for this stage
        binary_hash_list.append(md5.digest())

    md5 = hashlib.md5()
    md5.update(''.join(binary_hash_list))
    return str(md5.hexdigest()) + '-' + str(len(binary_hash_list))

def get_simple(file):
    f = open(file)
    md5 = hashlib.md5()
    while True:
        data = f.read(2**20)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()

def get(file, chunk_size):
    if chunk_size is None:
        return get_simple(file)
    else:
        size = os.path.getsize(file)

        if size > chunk_size:
            return get_multipart(file, chunk_size)
        else:
            return get_simple(file)

if __name__ == "__main__":
    file = sys.argv[1]
    if len(sys.argv) > 2 :
       chunk_size = int(sys.argv[2])
    else:
        chunk_size = None

    print get(file, chunk_size)