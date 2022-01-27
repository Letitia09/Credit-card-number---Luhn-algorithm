# Credit-card-number:Luhn-algorithm
Use Luhn algorithm to validate a credit card number.<br>

A credit card number has 16 digits, the last digit being the check digit. A credit card number can be validated using Luhn algorithm as follows:<br>

Step 1a: From the second last digit (inclusive), double the value of every second digit.<br>
Suppose the credit card number is 1456734512345698.<br>
Take the double of 9,5,3,1,4,7,5 and 1<br>
i.e., 18, 10, 6, 2, 8, 14, 10 and 2<br>

Note: If any number is greater than 9, then sum the digits of that number.<br>
i.e., 9, 1, 6, 2, 8, 5 ,1 and 2<br>

Step 1b: Sum the numbers obtained in Step 1a.<br>
i.e., 34<br>

Step 2: Sum the remaining digits in the credit card and add it with the sum from Step 1b.<br>
i.e., 34 + (8+6+4+2+5+3+6+4) = 72<br>

Step 3: If the total is divisible by 10 then the number is valid else it is not valid.<br>

Write a function, validate_credit_card_number(), which accepts a 16 digit credit card number and returns true if it is valid as per Luhn’s algorithm or false, if it is invalid. <br>
<pre>
<b>Input                        Output</b>
card_number-5239512608615007	  True
card_number-3245627890761450    False
</pre>
