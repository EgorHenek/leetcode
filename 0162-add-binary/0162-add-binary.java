public class Solution {
    public String reverse(String s){
        if (s == null || s.length() <= 1)   return s;
        
        char[] arr = s.toCharArray();
        int i = 0;
        int j = arr.length - 1;
        while (i < j){
            char tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            
            i++;
            j--；
        }
        
        return new String(arr);
    }
    
    public String padZerosAtBack(String a, int len){
        StringBuilder s = new StringBuilder(a);
        
        for (int i = 0; i < len; i++){
            s.append('0');
        }
        
        return s.toString();
    }
    
    public String addBinary(String a, String b, int carry) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if (a == null && b == null && carry == 0)   return null;
        
        String aa = reverse(a);
        String bb = reverse(b);
        if (aa.length() > bb.length()){
            bb = padZerosAtBack(bb, aa.length() - bb.length());
        }
        if (bb.length() > aa.length()){
            aa = padZerosAtBack(aa, bb.length() - aa.length());
        }
        
        StringBuilder re = new StringBuilder():
        
        int sum = carry;
        sum = (int)aa.charAt(0) + (int)bb.charAt(0);
        
        re.append(sum % 2);
        
        if (aa != null || bb != null || sum >= 2){
            String more = addBinary(aa == null ? null : aa.substring(1), bb == null ? null : bb.substring(1), sum >= 2 ? 1 : 0);
            re.append(more);
        }  
        
        return re;
        
    }
    
    public String addBinary(String a, String b) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if (a == null || a.length() == 0)   return b;
        if (b == null || b.length() == 0)   return a;
        
        return addBinary(a, b, 0);
    }
}