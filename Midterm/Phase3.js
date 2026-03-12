function setup() {
  createCanvas(400, 400); // Set the size of canvas
  noStroke(); // Disable drawing the stroke
}

function drawObject(x, y, s) {
  push();
  translate(x, y);
  scale(s);
   fill(0); // Fill in with black color
  square(10, 20, 60, 20);
  fill(300)
 ellipse(25, 50, 10, 10)
 ellipse(55, 50, 10, 10)
 ellipse(40, 65, 30, 20)
  fill(0)
 ellipse(40, 60, 10, 5) 
 triangle(15, 35, 15, 5, 50, 35)
 triangle(66, 35, 66, 5, 30, 35)
  fill(300)
  triangle(18, 23, 16.5, 8, 20, 21)
  triangle(63, 20, 65, 8, 60, 21)
  pop();
}


function draw() {
  drawObject(0, 0, 1);
  drawObject(0, 200, 1);
}