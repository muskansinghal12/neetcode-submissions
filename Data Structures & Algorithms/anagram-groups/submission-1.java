class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hm = new HashMap<>();
        // List<List<String>> l = new ArrayList<>();
        for(int i = 0;i<strs.length;i++){
            int freq[] = new int[26];
            for(char ch: strs[i].toCharArray()){
                freq[ch-'a']++;
            }
            String key = Arrays.toString(freq);
            hm.putIfAbsent(key, new ArrayList<>());
            hm.get(key).add(strs[i]);
        }
        // for(Map.Entry<String,List<String>> entry:hm.entrySet()){
        //     l.add(entry.getValue());
        // }
        return new ArrayList<>(hm.values());
    }
}
