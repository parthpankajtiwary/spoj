#include<bits/stdc++.h>

using namespace std;

int main() {
    int t, k;
    long long int s = 0;
    cin>>t;
    for(int i = 0; i < t; i++) {
        cin>>k;
        if(k >= 0) s += k;
    }
    cout<<s;
}
