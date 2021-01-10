```

['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'heartdisease']
Few examples from the dataset are given below- 
    age  sex   cp  trestbps   chol  ...  oldpeak  slope   ca  thal  heartdisease
0   age  sex   cp  trestbps   chol  ...  oldpeak  slope   ca  thal  heartdisease
1  63.0  1.0  1.0     145.0  233.0  ...      2.3    3.0  0.0   6.0             0
2  67.0  1.0  4.0     160.0  286.0  ...      1.5    2.0  3.0   3.0             2
3  67.0  1.0  4.0     120.0  229.0  ...      2.6    2.0  2.0   7.0             1
4  37.0  1.0  3.0     130.0  250.0  ...      3.5    3.0  0.0   3.0             0

[5 rows x 14 columns]

Learning CPDs using Maximum Likelihood Estimators...

Inferencing with Bayesian Network:

1.Probability of HeartDisease given Age = 20

+----------------------------+---------------------+
| heartdisease               |   phi(heartdisease) |
+============================+=====================+
| heartdisease(0)            |              0.4924 |
+----------------------------+---------------------+
| heartdisease(1)            |              0.2722 |
+----------------------------+---------------------+
| heartdisease(2)            |              0.0673 |
+----------------------------+---------------------+
| heartdisease(3)            |              0.1333 |
+----------------------------+---------------------+
| heartdisease(4)            |              0.0321 |
+----------------------------+---------------------+
| heartdisease(heartdisease) |              0.0027 |
+----------------------------+---------------------+

```
