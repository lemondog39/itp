#  FotC javaScript Assignment

## What I did:
### Program 1
- Wrote a program in JavaScript converting 99 Fahrenheit into Celsius, as shown below:

```let f = 99;
const c = ((f - 32)* (5/9));
console.log(c);```

- Running this program gave me the result of 37.22222222222222 (degrees Celsius). 

### Program 2 
- Wrote a program in JavaScript to convert any value of Fahrenheit into Celsius, as shown below:

```let f = prompt("What is the temperature in Fahrenheit?");
const c = ((f - 32)* (5/9)); 
console.log(c);```

## How I did it:
### Program 1 
- I borrowed the below code from the class repository:

```const pi = 3.14;
let radius = 11;
const area = pi * (radius ** 2);
console.log(area);```

- And basically changed the names of the variables to match f (for Fahrenheit) and c (for Celsius), as well as changed the formula for calculating area to reflect the formula for converting Fahrenheit to Celsius. 
- To check whether the program would run and give me the correct answer, I typed the statements into the Eloquent JavaScript Code Sandbox. 

### Program 2
- I borrowed the below code from the class repository:

```let height = prompt("What is your height in inches?");
const canRide = (height > 48) ? "Yes, you may ride." : "Sorry, you may not ride.";
console.log(canRide);```

- And changed the values and variables to reflect Fahrenheit and Celsius, like I did for the first program. 
- To check if it would work properly, I ran the code through Google Chrome's JavaScript Console in Developer View.
- It worked perfectly! Running the code results in Chrome showing a pop-up prompt asking "What is the temperature in Fahrenheit?", which I then typed in a random value, which then generates the converted temperature in Celsius. 
- To double check if it was accurate, I used a regular converter app on my phone. 

## Problems faced:
### Program 1 
- At first I tried to make things too complicated and wrote the program as:

```let f = "Fahrenheit", c = "Celsius";
let f = 99;
const c = ((f - 32)* (5/9));
console.log(c);```

- This resulted in the message "SyntaxError: Identifier 'f' has already been declared". 
- To fix this, I deleted the line ```let f = "Fahrenheit", c = "Celsius";``` and ran the code again in the Code Sandbox.
- This fixed the code to give me the correct answer. 

### Program 2
- No problems at all! (Since I kind of just stole the code from the class repository codealong js file and substituted the relevant variables...)