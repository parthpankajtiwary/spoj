#include<bits/stdc++.h>

int eORn(char a, char b);
using namespace std;

int min(int x,int y,int z)
{
    int k=(x>y)?y:x;
    k=(k>z)?z:k;
    return k;
}

int main() {
    string a, b;
    short m, n, t;
    cin>>t;
    while(t--) {
        cin>>a>>b;
        m = a.length();
        n = b.length();
        short dp[m+1][n+1];

        for(int i = 0; i <= m; i++) dp[i][0] = i;
        for(int j = 1; j <= m; j++) dp[0][j] = j;

        for(int i = 1; i <= m; i++) {
            for(int j = 1; j <= n; j++) {
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + eORn(a[i-1], b[j-1]));
            }
        }
        cout<<dp[m][n]<<endl;
    }
}


int eORn(char a, char b) {
    if(a == b) return 0;
    return 1;
}
