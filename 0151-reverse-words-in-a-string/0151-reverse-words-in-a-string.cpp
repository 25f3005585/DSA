class Solution {
public:
    string reverseWords(string s) {
        int n = s.size();
        int j = n - 1;

        while (j >= 0 && s[j] == ' ')
            j--;

        int start = j;

        j = 0;

        while (j < n && s[j] == ' ')
            j++;

        int end = j;

        if (start < end)
            return "";

        string ans = "";
        vector<char> word;

        for (int i = start; i >= end; i--) {
            if (s[i] != ' ') {
                word.push_back(s[i]);
            } else {
                if (s[i] == s[i + 1])
                    continue;

                while (!word.empty()) {
                    ans += word.back();
                    word.pop_back();
                }

                ans += ' ';
            }
        }

        while (!word.empty()) {
            ans += word.back();
            word.pop_back();
        }

        return ans;
    }
};