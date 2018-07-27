import numpy as np

num_points=1000
vectors_set=[]

for i in xrange(num_points):
    x1=np.random.normal(0.0, 0.55)
    y1=x1*0.1+0.3+np.random.normal(0.0,0.03)
    vectors_set.append([x1,y1])

x_data=[v[0] for v in vectors_set]
y_data=[v[0] for v in vectors_set]
