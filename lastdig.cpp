#include<bits/stdc++.h>

int lastDig(int a, long long int b);
using namespace std;

int main() {
    int t;
    cin>>t;
    for(int i = 0; i < t; i++) {
        int a, b;
        cin>>a>>b;
        lastDig(a, b);
    }
}

int lastDig(int a, long long int b) {
    if(b == 0) {
        cout<<1;
    }
    if(b%4 == 0) {
        cout<<(int)pow(a, 4)%10<<endl;
    }
    if(b%2 == 0 && b%4 != 0) {
        cout<<(int)pow(a, 2)%10<<endl;
    }
    if(b%4 == 1) {
        cout<<(int)pow(a, 1)%10<<endl;
    }
    if(b%4 == 3) {
        cout<<(int)pow(a, 3)%10<<endl;
    }
}

