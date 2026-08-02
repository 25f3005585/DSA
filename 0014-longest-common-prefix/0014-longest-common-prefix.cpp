class Solution {
public:
    // string longestCommonPrefix(vector<string>& strs) {
    //     int n = strs.size();
    //     if (n == 1) {
    //         return strs[0];
    //     }
    //     string initial = strs[0];
    //     string result = "";
    //     int i = 0;

    //     while (i < initial.size()) {
    //         char value = initial[i];
    //         for (int index = 1; index < n; index++) {
    //             string valueString = strs[index];
    //             char valueOfString = valueString[i];
    //             if(value!=valueOfString){
    //                 return result;
    //             }
    //         }
    //         result+=value;
    //         i++;
    //     }
    //     return result;
    // }
    
    string findCommonPrefix(string first, string last) {
        string result = "";
        int n = first.size();

        for (int i = 0; i < n; i++) {
            if (first[i] != last[i]) {
                return result;
            } else {
                result += first[i];
            }
        }
        return result;
    }

    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        if (n == 1) {
            return strs[0];
        }
        sort(strs.begin(), strs.end());
        string result = "";
        string first = strs[0];
        string last = strs[strs.size() - 1];

        if (first.size() < last.size()) {
            result = findCommonPrefix(first, last);
        } else {
            result = findCommonPrefix(last, first);
        }
        return result;
    }
};