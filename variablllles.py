# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Za4iS2JccDHSTqQlPnorkzi7xRtZQJlh
"""

#variable allows us to a trainable parameters to our graph
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

w=tf.Variable([.3],tf.float32) #storing value .32
b=tf.Variable([-.3],tf.float32)

x=tf.placeholder(tf.float32)

##then we crate a linear model
model=w*x + b

##then we need to initialize all the variables in tensorflow program for that we must explicitly call a special operation which is tf.global...
init=tf.global_variables_initializer()
sess=tf.compat.v1.Session()
sess.run(init)
print(sess.run(model,{x:[1,2,3,4]}))