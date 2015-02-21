#include<iostream>
#include<vector>

using namespace std;

int main() {
    float input;
    cin>>input;
    while(input > 0.00) {
        int n = 1;
        float hang = 0.0;
        while(hang < input) {
            hang += 1.0/(n+1);
            n += 1;
        }
            cout<<n-1<<" card(s)"<<endl;
            cin>>input;
    }
}

