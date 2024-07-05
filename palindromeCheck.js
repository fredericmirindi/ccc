function isPalindrome(num) {
  let reversedNum = 0;
  let originalNum = num;

  while (num !== 0) {
    let remainder = num % 10;
    reversedNum = reversedNum * 10 + remainder;
    num = Math.floor(num / 10);
  }

  return originalNum === reversedNum;
}

// Example usage
console.log(isPalindrome(121)); // Output: true
console.log(isPalindrome(123)); // Output: false
