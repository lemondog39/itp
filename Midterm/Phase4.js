function setup() {
  createCanvas(800, 800);
  noStroke();
}

function drawObject(x, y, s) {
  push();
  translate(x, y);
  scale(1,1);
   fill(0);
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
 for (y = 0; y < 800; y += 100) {
  for (x = 0; x < 800; x += 100){
 drawObject(x, y, x, y);   
  }
 }
}

