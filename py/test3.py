import tensorflow as tf

a=tf.placeholder("float")
b=tf.placeholder("float")

x=tf.mod(a,b)
y=tf.mul(c,d)

result=tf.add(x,y)

sess=tf.Session()

print sess.run(x,feed_dict={a:7,b:3})
print sess.run(y,feed_dict2={c:3,d:3})

print sess.run(result,feed_dict={x,y})
