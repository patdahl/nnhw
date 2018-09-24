#Parse MNIST data into usable data

import struct

#takes filepath to data returns data in array
def idxParse(path):

    #define idx type coding
    formdict = {8:'B',9:'b','B':'h','C':'i','D':'f','E':'d'}

    #open
    f = open(path,'rb')
    toc = f.read(4) #gets info first
    magic = struct.unpack_from('>BBBB',toc)
    frmt = formdict[magic[2]] #format of array data
    ndims = magic[3] #number of dimensions

    dim_data = f.read((ndims)*4)

    #size of each dimension
    d = [struct.unpack_from('>I',dim_data,(ii*4))[0] for ii in range(ndims)]

    raw = f.read()
    data = [x[0] for x in struct.iter_unpack('>'+frmt,raw)]

    return data,d
