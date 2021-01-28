# Project Demonstrating In-Place Merge Sort

Packages required: Numpy <br>
How to run: $ python main.py <br>

Expected output: <br>
/[3 6 3 1 6 8 3 6 5 3/]   <- original array <br> <br>

/[3 6/]/[3 1/]/[6 8/]/[3 6/]/[5 3/] <br>
/[3 6/]/[1 3/]/[6 8/]/[3 6/]/[3 5/] <br>
/[3 6 1 3/]/[6 8 3 6/]/[3 5/] <br>
/[1 3 3 6/]/[3 6 6 8/]/[3 5/] <br>
/[1 3 3 6 3 6 6 8/]/[3 5/] <br>
/[1 3 3 3 6 6 6 8/]/[3 5/] <br>
/[1 3 3 3 6 6 6 8 3 5/] <br>
/[1 3 3 3 3 5 6 6 6 8/] <br>
/[1 3 3 3 3 5 6 6 6 8/]   <- final sorted array

