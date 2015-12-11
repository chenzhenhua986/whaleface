import caffe
import numpy as np

net = caffe.Net('/u/chen478/whaleface/test.prototxt','/u/chen478/whaleface/finetune_whaleface_iter_25000.caffemodel', caffe.TEST)
net.forward()
scores = net.blobs['prob'].data
np.savetxt('predictions.txt', scores, delimiter=' ', newline='\n')
print scores.shape


