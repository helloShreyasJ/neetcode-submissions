class Solution {
    public boolean isAnagram(String s, String t) {
        char[] c1 = s.toCharArray();
        char[] c2 = t.toCharArray();

        Map<Character,Integer> map = new HashMap<>();
        Map<Character,Integer> map2 = new HashMap<>();

        for(int i = 0; i < c1.length; i++) {
            map.put(c1[i], map.getOrDefault(c1[i],0) + 1);
        }
        for(int i = 0; i < c2.length; i++) {
            map2.put(c2[i], map2.getOrDefault(c2[i],0) + 1);
        }
        if(map.equals(map2)) {
            return true;
        } else {
            return false;
        }
    }
}
