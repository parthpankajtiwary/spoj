#include<bits/stdc++.h>

using namespace std;

int main() {
    int n, m, idx;
    while(cin>>n) {
        idx = 0;
        string cipher;
        cin>>cipher;
        if(n != 0) {
            m = cipher.length()/n;
        }
        char arr[m][n];
        int flag = 0;
        for(int i = 0; i < m; i++) {
            if(flag == 0) {
                for(int j = 0; j < n; j++) {
                    arr[i][j] = cipher[idx];
                    idx++;
                }
                flag = 1;
            }
            else {
                for(int k = n-1; k >= 0; k--) {
                    arr[i][k] = cipher[idx];
                    idx++;
                }
                flag = 0;
            }
        }
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                cout<<arr[j][i];
            }
        }
        cout<<endl;
    }
}
