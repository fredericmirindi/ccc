public class PalindromeCheck {
    public static void main(String[] args) {
        int number = 121;
        
        if (isPalindrome(number)) {
            System.out.println(number + " is a palindrome.");
        } else {
            System.out.println(number + " is not a palindrome.");
        }
    }
    
    private static boolean isPalindrome(int number) {
        int reversedNumber = 0;
        int originalNumber = number;
        
        while (number != 0) {
            int remainder = number % 10;
            reversedNumber = reversedNumber * 10 + remainder;
            number /= 10;
        }
        
        return originalNumber == reversedNumber;
    }
}
