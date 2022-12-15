scores_id = fopen('mera_podobnosti.txt');
labels_id = fopen('oznake_ujemanje.txt');
scores = fscanf(scores_id, '%f');
labels = fscanf(labels_id, '%d');
x = [0 1];
y = [0 1];
y_reverse = [1 0];
[X,Y,T,AUC] = perfcurve(labels,scores,1);
figure
plot(X,Y,'k');
grid on
xlabel('False positive rate');
ylabel('True positive rate');
title('ROC 4SF');
hold on 
plot(x,y, 'b');
plot(x, y_reverse,'b');
hold off

scores_svm = fopen('distances_svm.txt');
scores_svm_real = fscanf(scores_svm, '%f');
[X_svm,Y_svm,T_svm,AUC_svm] = perfcurve(labels,scores_svm_real,1);
figure
plot(X_svm,Y_svm,'k');
grid on
xlabel('False positive rate');
ylabel('True positive rate');
title('ROC SVM');
hold on 
plot(x,y, 'b');
plot(x, y_reverse,'b');
hold off


