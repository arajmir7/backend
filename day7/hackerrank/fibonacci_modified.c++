#include <bits/stdc++.h>
using namespace std;

// We're scaling up! Using long long chunks to dodge that TLE (Time Limit Exceeded)
typedef vector<long long> BigInt;
const long long BASE = 1e9; 

BigInt stringToBigInt(string s) {
    BigInt res;
    for (int i = s.size(); i > 0; i -= 9) {
        if (i < 9) res.push_back(stoll(s.substr(0, i)));
        else res.push_back(stoll(s.substr(i - 9, 9)));
    }
    return res;
}

BigInt add(const BigInt &a, const BigInt &b) {
    BigInt res;
    long long carry = 0;
    for (size_t i = 0; i < max(a.size(), b.size()) || carry; ++i) {
        long long sum = carry + (i < a.size() ? a[i] : 0) + (i < b.size() ? b[i] : 0);
        res.push_back(sum % BASE);
        carry = sum / BASE;
    }
    return res;
}

BigInt multiply(const BigInt &a, const BigInt &b) {
    BigInt res(a.size() + b.size(), 0);
    for (size_t i = 0; i < a.size(); ++i) {
        long long carry = 0;
        for (size_t j = 0; j < b.size() || carry; ++j) {
            long long cur = res[i + j] + a[i] * (j < b.size() ? b[j] : 0) + carry;
            res[i + j] = cur % BASE;
            carry = cur / BASE;
        }
    }
    while (res.size() > 1 && res.back() == 0) res.pop_back();
    return res;
}

string bigIntToString(const BigInt &a) {
    if (a.empty()) return "0";
    string res = to_string(a.back());
    for (int i = (int)a.size() - 2; i >= 0; --i) {
        string temp = to_string(a[i]);
        res += string(9 - temp.size(), '0') + temp; 
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t1, t2, n;
    if (!(cin >> t1 >> t2 >> n)) return 0;

    BigInt a = stringToBigInt(to_string(t1));
    BigInt b = stringToBigInt(to_string(t2));

    for (int i = 3; i <= n; i++) {
        BigInt bSquared = multiply(b, b);
        BigInt nextTerm = add(a, bSquared);
        a = b;
        b = nextTerm;
    }

    cout << bigIntToString(b) << endl;
    return 0;
}