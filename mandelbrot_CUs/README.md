Mandelbrot Y-axis
=================

This module takes the parameters of the Mandelbrot fractal and decompose
    the image into y  diferent parts, where  is the number of y-axis dimension. 
    Then it runs for every part the mandelbrot Generator Code 
    which is the mandel_lines.py. The mandel_lines.py creates y Images and
    then we compose the y images into one. The whole fractal Image.
    For every part of the image we create one Compute Unit.

The parameters are the following:
	imgX, imgY: the dimensions of the mandelbrot image, e.g. 1024, 1024
    xBeg, xEnd: the x-axis portion of the (sub-)image to calculate
    yBeg, yEnd: the y-axis portion of the (sub-)image to calculate

You can run this code via command list:
	python mandelbrot_pilot.py imgX imgY xBeg xEnd yBeg yEnd

<h2>You can give a test drive: </h2>

Make sure you have your virtualenv activated and everything installed:

[Readme_Installation](https://github.com/georgeha/mandelbrot/blob/master/README.md)

Download the two required executables:
```
curl --insecure -Os https://raw.githubusercontent.com/georgeha/mandelbrot/master/mandelbrot_CUs/mandel_lines.py 
curl --insecure -Os https://raw.githubusercontent.com/georgeha/mandelbrot/master/mandelbrot_CUs/mandelbrot_pilot.py
```
Run:
```
python mandelbrot_pilot.py 50 50 0 50 0 50
```
When you finish the execution you may find the image in your working directory: mandelbrot_full.gif