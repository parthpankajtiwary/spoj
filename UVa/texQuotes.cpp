#include<bits/stdc++.h>

using namespace std;

int main() {
    char str[100];
    cin.getline(str, sizeof(str));
    int flag = 0;
    while(cin) {
        for(int i = 0; str[i] != '\0'; i++) {
            if(str[i] == 34 && flag == 0) {
                cout<<"\`\`";
                flag = 1;
            }
            else if(str[i] == 34 && flag == 1) {
                cout<<"\'\'";
                flag = 0;
            }
            else {
                cout<<str[i];
            }
        }
        cout<<endl;
        cin.getline(str, sizeof(str));
    }
}
