#include<bits/stdc++.h>

long long int coins(long long int n);

using namespace std;

map<long long int, long long int> dp;
int main() {
    long long int n;
    while(cin>>n) {
        cout<<coins(n)<<endl;
    }
}

long long int coins(long long int n) {
    if(n < 12) return n;
    if(dp.count(n)) return dp[n];
    dp[n] = max(n, coins(n/2)+coins(n/3)+coins(n/4));
    return dp[n];
}

