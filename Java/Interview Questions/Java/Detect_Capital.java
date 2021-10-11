package main.cp.leetcode.august;

public class Day_01_Detect_Capital {
    // 1. Counting
    class Solution {
        public boolean detectCapitalUse(String word) {
            int small = 0;
            int capital = 0;
            for(char letter : word.toCharArray()) {
                if(letter >= 'A' && letter <= 'Z')
                    capital++;
                else small++;
            }

            return capital == word.length() || capital == 0 || capital == 1 && word.charAt(0) >= 'A' && word.charAt(0) <= 'Z';
        }
    }

    // 2. String Methods
    class Solution2 {
        public boolean detectCapitalUse(String word) {
            return word.toUpperCase().equals(word) || word.substring(1).toLowerCase().equals(word.substring(1));
        }
    }

    // 3. Regex
    class Solution3 {
        public boolean detectCapitalUse(String word) {
            return word.matches("[A-Z]*|.[a-z]*");
        }
    }
}
