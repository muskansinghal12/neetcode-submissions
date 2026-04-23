class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hm = new HashMap<>();
        List<List<String>> l = new ArrayList<>();
        for(int i = 0;i<strs.length;i++){
            String s = strs[i];
            char[] chs = s.toCharArray();
            Arrays.sort(chs);
            String sorted = new String(chs);
            if(!hm.containsKey(sorted)){
                hm.put(sorted,new ArrayList<>());
            }
            hm.get(sorted).add(s);
        }
        for(Map.Entry<String,List<String>> entry:hm.entrySet()){
            l.add(entry.getValue());
        }
        return l;
    }
}
