#include <iostream>
#include <vector>

using namespace std;

int numberOfSides(int n);

int main() {
    vector <int> sides;
    int side;
    while( side != 0) {
        cin>>side;
        sides.push_back(side);
    }
    for(int i = 0; i < sides.size()-1; i++) {
        cout<<numberOfSides(sides[i])<<endl;
    }
}

int numberOfSides(int n) {
    return n*(n+1)*(2*n+1)/6;
}

