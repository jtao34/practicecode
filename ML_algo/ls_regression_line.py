# Enter your code here. Read input from STDIN. Print output to STDOUT
#y_hat = be_1 * x + be_0
L = [ list( map( float, input().strip().split(" ") ) ) for i in range(5) ]
xs = [i[0] for i in L]
ys = [i[1] for i in L]
xs_mean = sum(xs)/len(xs)
ys_mean = sum(ys)/len(ys)
var = 0
for i in range(len(xs)):
    var += (xs[i] - xs_mean)**2
b1 = 0
for i in range(len(xs)):
    b1 += (xs[i] - xs_mean)*(ys[i] - ys_mean)/var
b0 = ys_mean - b1*xs_mean
#print('%.3f' % (b1*80 + b0))
print("{:.3f}".format(b1*80 + b0))
#print(round(b1*80 + b0, 3))