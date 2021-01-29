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

![](https://github.com/GiottoFrean/Small-Python-Projects/blob/main/NaiveBayes/PGM.png =250x)

<img src="https://github.com/GiottoFrean/Small-Python-Projects/blob/main/NaiveBayes/PGM.png" alt="PGM" width="200"/>

<br>
Using the above model data is generated, and a Naive Bayes classifier trained with it.<br>
