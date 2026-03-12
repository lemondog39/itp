# Midterm

## What I did


## Problems I faced
- The first three phases were actually quite easy. 
- Phases 1 and 3 in particular were quite simply, because phase 1 just involved drawing out each component of my image, while for phase 3 I directly referenced the example phase 3 code from the class repository. 
- While the code I submitted is basically identital to the class code (in terms of getting the image to function in a particular way) I did try messing around with it and shifting the two images around by changing the coordinate numbers in the drawObject(x, y, s) command line at the end.
- Phase 2 was a bit more complicated in that I had to figure out what each number (e.g. in ellipse(x1, y1, x2, y2)) meant and how they would affect the printed image, but that was also quite easy to get a hang of. It was a bit more difficult to get the triangles printed the way I wanted since I was dealing with 3 points (so basically like (x1, y1, x2, y2, x3, y3)), but I also managed to get that figured out pretty quickly. 

- The biggest problem I faced was for Phase 4, when tessalating the image. 
- For this code, I heavily referenced codes from the class repository, specifically the codealong.js file from the Control Flow lecture folder. 

### Fail 1

```
function setup() {
  createCanvas(400, 400);
  noStroke();
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

```

- This would just continuously and endlessly print my object in a vertical straight line. 

![Failed code 1](img/failedcode1.png)


### Fail 2

```

function setup() {
  createCanvas(400, 400);
  noStroke();
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

```

- I made the image a bit bigger by increasing the scale by 100%, but this code would print my image in a diagonal, consecutive and eternal line. 

![Failed code 2](img/failedcode2.png)

### Fail 3 

```

function setup() {
  createCanvas(400, 400);
  noStroke();
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

```

- This one resulted in something a bit closer to what I needed to get, though it only showed singular horizontal line of my image repeated 4 times.
- I assume the image is actually repeated eternally, but I only saw it appear 4 times because my canvas is set to dimensions of 400x400 while my image scales 100x100. 

![Failed code 3](img/failedcode3.png)

### Final

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
}

- I increased my canvas dimensions to 800x800 so that I could see more. Since this code worked, I also tried changing the canvas size a few times (200x100, 400x600, etc.) to see if it would change the number of times I saw the image. (it worked)

![Completed tessellation](img/phase4.png)
