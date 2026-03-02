# FizzBuzz javaScript Assignment

## What I did 

- Writing this code actually took me 4 tries to get correct.
- I ran each one through [p5.js](https://editor.p5js.org/)
- I referenced 2 codes from the class repository:

``` for (let i = 1500; i <= 2700; i++) {
  if (i % 7 === 0 && i % 5 === 0) {
    console.log(i);
  }
} ```

``` let mmMIDI = 64;
if (mmMIDI === 12) {
  console.log("MIDI is 12.");
} else if (mmMIDI === 13) {
  console.log("MIDI is 13.");
} else if (mmMIDI > 64) {
  console.log("MIDI is greater than 64.");
} else {
  console.log("MIDI is less than 64 but not 12 or 13.");
} ```

- The first code was to help with the divisibles, so that I could single out numbers divisible by 3, 5 and 3 AND 5. 
- The second code was to help with the "else if" commands. 
- This resulted below program: 

``` for (let i = 1; i <= 100; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
  console.log("FizzBuzz");
} else if (i % 5 === 0)  {
  console.log("Buzz");
} else if (i % 3 === 0 ) {
  console.log("Fizz");
} else {
  console.log(i)
}
} ```

## Problems I faced

- As I mentioned earlier, I had to rewrite this program 4 times before it finally worked, and 


### Initial Program

``` for (let i = 1500; i <= 2700; i++) {
  if (i % 3 === 0) {
  console.log("Fizz");
} else if (i % 3 === 0)  {
  console.log("Buzz");
} else if (i % 7 === 0 && i % 5 === 0) {
  console.log("FizzBuzz");
}
}
console.log(i) ```
​

- This was obviously stupid because I copy and pasted my reference code but forgot to change the two defining values in the first line. 
- (i % 3 === 0) appears twice because I forgot to change the 3 to a 5
- I also didn't have a closing "else" line, and also the extra console.log(i) at the end also screwed up the program. 
- I actually didn't know the console.log(i) was wrong for quite a while (you will see soon) and so I thought the issue was really just that I defined the range of numbers wrong and either way this whole initial program was just messy and careless and very bad overall so it's not surprising that it was faulty. 
- Anyway it gave me the below result: 

``` ReferenceError: i is not defined
2
Fizz 
FizzBuzz 
12
Fizz 
FizzBuzz 
23
Fizz 
FizzBuzz 
12
Fizz 
FizzBuzz 
23
Fizz 
FizzBuzz ```

- And so on

### Second Program

``` for (let i = 0; i <= 100; i++) {
  if (i % 3 === 0) {
  console.log("Fizz");
} else if (i % 5 === 0)  {
  console.log("Buzz");
} else if (i % 3 === 0 && i % 5 === 0) {
  console.log("FizzBuzz");
}
}
console.log(i) ```

- Resulted in this:

``` ReferenceError: i is not defined
2
Fizz 
Buzz 
2
Fizz 
Buzz 
3
Fizz 
Buzz ```

- I think it was that I didn't have a final "else" line as well as the fact that the console.log(i) appeared OUTSIDE the braces that contained the conditions of the program. 
- For the next program, I moved the console.log(i) inside the braces instead and wrote it as "else console.log(i)" as shown below.


### Third Program
``` for (let i = 0; i <= 100; i++) {
  if (i % 3 === 0) {
  console.log("Fizz");
} else if (i % 5 === 0)  {
  console.log("Buzz");
} else if (i % 3 === 0 && i % 5 === 0) {
  console.log("FizzBuzz");
} else {
  console.log(i)
}
} ```

- Resulted in this:

``` Fizz 
1
2
Fizz 
4
Buzz 
Fizz 
7
8
Fizz 
Buzz 
11
Fizz 
13
14
Fizz 
16 ```

- This was the closest I got to printing the correct results, but for the numbers that were divisible by 3 and 5 (in this case, 15), the word printed was just Fizz instead of FizzBuzz.
- I assume it is because I wrote the ``` else if (i % 3 === 0 && i % 5 === 0) {console.log("FizzBuzz"); ``` as the last line, so whenever the program was run to print a number, it would just follow through and see ```if (i % 3 === 0) {console.log("Fizz");``` and immediately print Fizz for numbers divisible by 3 and ignore the rest of the code, regardless if it was also divisible by 5 or not. 
- I forgot that computers read things line by line and not as a whole. 
- To avoid this, for the next and final version of the program, I just shifted the last line all the way to the top to give it priority and let it be the first command to be run/eliminated when the program is run. 

## LAST PROGRAM!!

``` for (let i = 1; i <= 100; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
  console.log("FizzBuzz");
} else if (i % 5 === 0)  {
  console.log("Buzz");
} else if (i % 3 === 0 ) {
  console.log("Fizz");
} else {
  console.log(i)
}
} ```
 
- Resulted in the correct sequence! Yay!


``` 1
2
Fizz 
4
Buzz 
Fizz 
7
8
Fizz 
Buzz 
11
Fizz 
13
14
FizzBuzz 
16 ```

- And so on
