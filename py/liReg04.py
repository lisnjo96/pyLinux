import tensorflow as tf

W=tf.Variable(tf.random_uniform([1],-1.0,1.0)
b=tf.Variable(tf.zeros([1]))
y=W*x_data+b

loss=tf.reduce_mean(tf.square(y-y_data))

optimizer=tf.train.GradientDescentOptimizer(0.5)
train=optimizer.minimize(loss)
