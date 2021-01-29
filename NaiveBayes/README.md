# Simple Naive Bayes

Packages required: Numpy <br>
How to run: $ python main.py <br>
<br>
## Description:<br>

This is a simple naive bayes classifer, trained on a toy problem: <br>
* The weather (W) is either sunny (s), rainy (r) or cloudy (c).
* The temperature (T) is a continous normal distribution, defined by a mean and standard deviation.
* The rough frequency of people wearing raincoats (R) is recorded; none (n), few (f), lots (l) or all (a).
* T and R are conditionally independent given W.
This is represented by the diagram below, which has the "true" probabilities: <br>

<img src="https://github.com/GiottoFrean/Small-Python-Projects/blob/main/NaiveBayes/PGM.png" alt="PGM" width="600"/>

<br>
Using the above model data is generated, and a Naive Bayes classifier trained with it.<br>

**Example output:** <br>

1. Generating Data (printing up to 10 rows):
2. weather: clear      temp: 12.596     raincoats: few
3. weather: clear      temp: 17.905     raincoats: few
4. weather: rain       temp: 17.632     raincoats: lots
5. weather: clear      temp: 15.496     raincoats: few
6. weather: rain       temp: 13.49      raincoats: lots
7. weather: rain       temp: 15.139     raincoats: lots
8. weather: sun        temp: 25.383     raincoats: none
9. weather: clear      temp: 17.872     raincoats: few
10. weather: clear      temp: 16.022     raincoats: few
11. weather: rain       temp: 14.976     raincoats: few
12. 
13. \[22.96 15.83 17.1 \]   <- T mean|W
14. \[4.92 3.52 4.39 \]   <- T std|W
15. \[\[0.9  0.02 0.15 \]
16. \[0.06 0.09 0.63 \]
17. \[0.02 0.75 0.21 \]
18. \[0.02 0.14 0.01 \]\]   <- prob R|W, rounded to 2dp

total test accuracy: 82.0 %
accuracy on true sunny data: 85.71428571428571 %
accuracy on true rainy data: 92.85714285714286 %
accuracy on true cloudy data: 75.86206896551724 %

