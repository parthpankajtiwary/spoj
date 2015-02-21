#include<iostream>
#include<vector>
using namespace std;

int main() {
    vector <long long int> numbers;
    int t;
    cin>>t;
    for(int i = 0; i < t; i++) {
        long long int temp;
        cin>>temp;
        numbers.push_back(temp);
    }
    for(int i = 0; i < numbers.size(); i++) {
        cout<<((numbers[i]-1)*250)+192<<endl;
    }
}
