class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> res;
        int n = s.size();
        if(n == 0 || n >12) return res;
        vector<string> hash(12, "NULL");
        string ss(1, s[n-1]);
        hash[n-1] = ss;
        makeIp(0, hash, n, s);
        stringToArray(hash[0], res);
        filterArray(res);
        return res;
    }
    
    string makeIp(int left, vector<string>& hash, int n, string& s){
        if(hash[left] != "NULL"){
            return hash[left];
        }
        int upper = min(n-1, left + 3);
        vector<string> res;
        for(int k = left+1; k<= upper; k++){
            if(isIP(s, left, k-1)){
                string solution = makeIp(k, hash, n, s);
                vector<string> choices;
                stringToArray(solution, choices);
                int len = choices[0].size();
                string& substr = s.substr(left, k-left);
                if(isIP(s, left, k + len - 1)){
                   res.push_back(substr + solution);   
                }
                for(int i=0; i<choices.size(); i++){
                    string& tmp = choices[i];
                    int j = 0; int sz = tmp.size();
                    int count = 1;
                    while(j<sz){
                        if(tmp[j] == '.') count++;
                        j++;
                    }
                    if((count + 1) > 4){
                        continue;
                    }
                    res.push_back(substr + "." + choices[i]);
                }
            }
        }
        string r;
        arrayToString(res, r);
        hash[left] = r;
        return r;
    }
    
    void stringToArray(string& s, vector<string>& res){
        int n = s.size();
        int j=0;
        while(j<n && s[j]!='-')j++;
        if(j == n){
            res.push_back(s);
            return;
        }
        int i=0;
        if(i>=j) return;
        string str;
        while(i<n){
          str.clear();
          while(i<j)str.push_back(s[i++]);
          res.push_back(str);
          j++;
          i=j;
          while(j<n && s[j]!='-')j++;
        }
    }
    
    void arrayToString(vector<string>& array, string& res){
        int n = array.size();
        for(int i=0; i<n; i++){
            res += array[i];
            if(i != n-1) res += "-";
        }
    }
    
    void filterArray(vector<string>& array){
        vector<string> res;
        int n = array.size();
        for(int i=0; i<n; i++){
            string& s = array[i];
            int j=0; int sz = s.size();
            int count = 1;
            while(j<sz){
                if(s[j] == '.')count++;
                j++;
            }
            if(count == 4){
                res.push_back(array[i]);
            }
        }
        if(res.size() < n){
            array = res;
        }
    }
    
    bool isIP(string& s, int left, int right){
        int n = s.size();
        if(s[left] == '0' && left < right) return false;
        int k = left;
        int res = 0;
        while(k<=right){
            res *= 10;
            res += s[k] - '0';
            k++;
        }
        if(res>=0 && res <= 255) return true;
        return false;
    }
};