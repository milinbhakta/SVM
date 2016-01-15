from sklearn.svm import SVC
import numpy as np
X = np.array([[0, 90], [91, 180], [181,270], [271,360]])
y = np.array([1,2,3,4])
clf = SVC(kernel='linear')
clf.fit(X, y)
a = input("Enter The Angle")
if a > 360:
    b = a/360
    b = a - (b * 360)
else:
    b = a

#b = input("Enter Maximum Angle")
p = clf.predict([[b,b]])
print '%d is lies in quadrant %d' %(a,p[0])
#print '%d is lies in quadrant %d' %(a,p[0])
