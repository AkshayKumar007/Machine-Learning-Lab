```bash
    $ python prgm2.py
```

## Output

```
 The Given Training Dataset 

['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes']
['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes']
['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No']
['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']

 The initial Value of hypothesis: 

 The most specific hypothesis S0 : [0,0,0,0,0,0]


 The most general hypothesis G0 : [?,?,?,?,?,?]


Candidate Elimination Algorithm Hypothesis Version Space Computation

-------------------------------------------
For Training Example No : 1 the hypothesis is S1  ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same']
For Training Example No : 1 the hypothesis is G1  ['?', '?', '?', '?', '?', '?']
-------------------------------------------
For Training Example No : 2 the hypothesis is S2  ['Sunny', 'Warm', '?', 'Strong', 'Warm', 'Same']
For Training Example No : 2 the hypothesis is G2  ['?', '?', '?', '?', '?', '?']
-------------------------------------------
For Training Example No :3 the hypothesis is S3  ['Sunny', 'Warm', '?', 'Strong', 'Warm', 'Same']
For Training Example No :3 the hypothesis is G3  [['Sunny', '?', '?', '?', '?', '?'], ['?', 'Warm', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', 'Same']]
-------------------------------------------
For Training Example No : 4 the hypothesis is S4  ['Sunny', 'Warm', '?', 'Strong', '?', '?']
For Training Example No : 4,the hypothesis is G4  [['Sunny', '?', '?', '?', '?', '?'], ['?', 'Warm', '?', '?', '?', '?']]
```
