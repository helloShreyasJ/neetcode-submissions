class Solution {
    public boolean isPalindrome(String s) {
    	String cleanedString = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String reversedString = "";
        for(int i = 0; i < cleanedString.length(); i++) {
            reversedString = cleanedString.charAt(i) + reversedString;
        }
        if(reversedString.equals(cleanedString)) {
            return true;
        }
        return false;
    }
}
