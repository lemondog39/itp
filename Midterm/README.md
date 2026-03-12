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


### fail 3 

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