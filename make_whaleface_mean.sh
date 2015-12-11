#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

DATA=/u/chen478/whaleface
TOOLS=/u/chen478/caffe/build/tools

$TOOLS/compute_image_mean /u/chen478/whaleface/whaleface_train_lmdb \
  $DATA/whaleface_mean.binaryproto

echo "Done."
