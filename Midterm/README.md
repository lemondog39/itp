

## fail 1

function setup() {
  createCanvas(400, 400); // Set the size of canvas
  noStroke(); // Disable drawing the stroke
}

function drawObject(x, y, s) {
  push();
  translate(x, y);
  scale(0.5,0.5);
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

let y = 0.0 
function draw() {
  drawObject(0, y, 0, y);
   y +=4;
}



## Fail 2

function setup() {
  createCanvas(400, 400); // Set the size of canvas
  noStroke(); // Disable drawing the stroke
}

function drawObject(x, y, s) {
  push();
  translate(x, y);
  scale(1,1);
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

let y = 0.0 
let x = 0.0 
function draw() {
  drawObject(x, y, x, y);
  x +=5; 
  y +=4;
}


## fail 3 

function setup() {
  createCanvas(400, 400); // Set the size of canvas
  noStroke(); // Disable drawing the stroke
}

function drawObject(x, y, s) {
  push();
  translate(x, y);
  scale(1,1);
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

let y = 0.0 
let x = 0.0 
function draw() {
  drawObject(x, y, x, y);
  x +=100; 
  y +=4;
}


## final


function setup() {
  createCanvas(800, 800); // Set the size of canvas
  noStroke(); // Disable drawing the stroke
}

function drawObject(x, y, s) {
  push();
  translate(x, y);
  scale(1,1);
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
  for (y = 0; y < 800; y += 100) {
  for (x = 0; x < 800; x += 100){
 drawObject(x, y, x, y);   
  }
} 
