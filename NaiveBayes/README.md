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

Expected output: <br>
Generating Data (up to 10 rows): <br>
weather: clear      temp: 16.481     raincoats: few <br>
weather: sun        temp: 15.834     raincoats: none <br>
weather: clear      temp: 22.002     raincoats: none <br>
weather: rain       temp: 14.784     raincoats: lots <br>
weather: sun        temp: 17.916     raincoats: none <br>
weather: sun        temp: 20.456     raincoats: few <br>
weather: sun        temp: 16.528     raincoats: none <br>
weather: sun        temp: 17.38      raincoats: none <br>
weather: clear      temp: 16.731     raincoats: none <br>
weather: rain       temp: 18.822     raincoats: lots <br>
