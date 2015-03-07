
#include<bits/stdc++.h>
long long int maxLength(long long int a, long long int b);
long long int cycleLength(long long int n);

using namespace std;

int main() {
    long long int a, b;
    cin>>a>>b;
    while(cin) {
        maxLength(a, b);
        cin>>a>>b;
    }
}

long long int maxLength(long long int a, long long int b) {
        long long int maximum = -99999;
        if(a < b) {
            for(long long int n = a; n <= b; n++) {
                long long int cL;
                cL = cycleLength(n);
                if(cL > maximum) maximum = cL;
            }
            cout<<a<<" "<<b<<" "<<maximum<<endl;
        }
        else {
            for(long long int n = b; n <= a; n++) {
                long long int cL;
                cL = cycleLength(n);
                if(cL > maximum) maximum = cL;
            }
            cout<<a<<" "<<b<<" "<<maximum<<endl;
        }

}


long long int cycleLength(long long int n) {
            long long int cnt = 0;
            while(n != 1) {
                if(n%2 != 0) {
                    n = 3*n+1;
                }
                else {
                    n /= 2;
                }
                cnt++;
            }
            ++cnt;
            return cnt;
}
