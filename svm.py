import numpy as np

from sklearn import svm
from sklearn import metrics
import matplotlib.pyplot as plt
x_train = np.load('hog_train_L2_Hys.npy')

y_train = np.zeros(len(x_train))
y_train[0:1100] = 1 # indicates that the pair of images goes for the same person


x_test = np.load('hog_test_L2_Hys.npy')
y_test = np.zeros(len(x_test))
y_test[0:500] = 1


clf = svm.SVC(kernel='linear', C=10)

#Train the model using the training sets
clf.fit(x_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(x_test)

#print(classification_report(y_test,y_pred))
#print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

#Calculate the distance to the decision boundary(Only for linear kernels)
y = clf.decision_function(x_test)
w_norm = np.linalg.norm(clf.coef_)
dist = y / w_norm

#Write distances to text file
dist_str = [str(d) for d in dist]
with open("distances_svm.txt", 'w') as b:
   b.write('\n'.join(dist_str))