#include<bits/stdc++.h>

using namespace std;

int operations(string a, string b);

int main() {
    int n;
    cin>>n;
    for(int i = 0; i < n; i++) {
        string a, b;
        cin>>a>>b;
        cout<<operations(a, b)<<endl;
    }
}

int operations(string a, string b) {
    int cnt = 0;
    if(a.length() <= b.length()) {
        cnt = abs(b.length()-a.length());
        for(int i = 0; i < a.length(); i++) {
            if(a[i] != b[i]) cnt++;
        }
    }
    else {
        cnt = abs(a.length()-b.length());
        for(int i; i < b.length(); i++) {
            if(a[i] != b[i]) cnt++;
        }
    }
    return cnt;
}
