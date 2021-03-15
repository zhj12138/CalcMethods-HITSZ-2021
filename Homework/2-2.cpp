//
// Created by 15502 on 2021/3/15.
//
#include<bits/stdc++.h>
using namespace std;
const double a = 115;
const double e = 1e-7;
double iter(double x){
    return 1.5 * x - 1 / (2 * a) * x * x * x;
}
int main() {
    double x1 = 10, x2;
    cout << setprecision(10);
    while(true){
        x2 = iter(x1);
        cout << x2 << endl;
//        cout << abs(x2 - x1) << endl;
        if(abs(x2 - x1) < e) break;
        x1 = x2;
    }
    cout << "ans: " << x2 << endl;
    return 0;
}
