import caffe
import lmdb
import os
import caffe.proto.caffe_pb2
from caffe.io import datum_to_array
import numpy as np

lmdb_env = lmdb.open('/u/chen478/whaleface/features')
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
datum = caffe.proto.caffe_pb2.Datum()

j=0
f = open("predictions.csv", "r+")
for key, value in lmdb_cursor:
    print key
    s = ''
    datum.ParseFromString(value)
#    label = datum.label
    data = caffe.io.datum_to_array(datum)
    for i in range(447):
        s += str(data[i][0][0]) + ','
    s += '\n'
#    data = ' '.join(str(i) for i in data)
    f.write(s)
#    np.savetxt('predictions.txt', data, delimiter=' ', newline='\n')
#    for d in data:
#            print
f.close()
