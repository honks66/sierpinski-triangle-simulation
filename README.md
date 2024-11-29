The Sierpinski Triangle

This project produces an animated Sierpinski fractal as an output. You can read more about the Sierpinski fractal in here: https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle

The fractal is generated by simulation: 
  1) choose a first xy-point randomly inside an equilateral triangle
  2) choose the xy-point of one of the three triangle vertices randomly (1/3 chance each)
  3) calculate distance to the vertex and create a new xy-point at the half way
  4) repeat N times

You can tune the location of the outer triangle by choosing the coordinate of its left vertex, and the size of the triangle by choosing the length of its side. The triangle is created by the function generateSierpinskiPoints(num_of_points, triangle_left, size).
You can tune the "speed" of the resulting .gif by changing the value of speed_Multiplier variable (basically it determines the amount of points generated per frame).
