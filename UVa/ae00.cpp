#include<bits/stdc++.h>

using namespace std;

int main() {
    int n, i, j;
    long long int cnt;
    cnt = 0;
    cin>>n;
    for(i = 1; i <= n; i++) {
        for(j = 1; j*j <= i; ++j) {
            if(i%j == 0) ++cnt;
        }
    }
    cout<<cnt<<endl;
}
