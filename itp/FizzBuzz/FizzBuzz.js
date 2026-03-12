// To print numbers 1-100, printing "Fizz" when divisible by 3, "Buzz" when divisible by 5, and "FizzBuzz" when divisible by both. 

for (let i = 1; i <= 100; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
  console.log("FizzBuzz");
} else if (i % 5 === 0)  {
  console.log("Buzz");
} else if (i % 3 === 0 ) {
  console.log("Fizz");
} else {
  console.log(i)
}
} 