class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        if (n == 1) {
            return s;
        }
        string result(1, s[0]);
        for (int i = 1; i < n; i++) {
            int low = i;
            int high = i;

            while (low >= 0 && high < n && s[low] == s[high]) {
                low--;
                high++;
            }
            string check = s.substr(low + 1, high - low - 1);
            if (check.size() > result.size()) {
                result = check;
            }

            low = i - 1;
            high = i;

            while (low >= 0 && high < n && s[low] == s[high]) {
                low--;
                high++;
            }
            check = s.substr(low + 1, high - low - 1);
            if (check.size() > result.size()) {
                result = check;
            }
        }
        return result;
    }
};