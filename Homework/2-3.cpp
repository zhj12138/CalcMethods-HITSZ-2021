//
// Created by 15502 on 2021/3/15.
//
#include<bits/stdc++.h>
using namespace std;
const double e = 1e-5;
double iterp1(double x){
    double top = cos(x) - x * exp(x);
    double down = sin(x) + exp(x) * (1 + x);
    return x + top / down;
}
void p1(double x0){//牛顿迭代法
    double x1;
    while(true){
        x1 = iterp1(x0);
        if(abs(x1 - x0) < e) break;
        x0 = x1;
    }
    cout << "ans of p1: " << x1 << endl;
}
double fp2(double x){
    return cos(x) - x * exp(x);
}
double iterp2(double x1, double x2){
    return x2 - (x2 - x1) * fp2(x2) / (fp2(x2) - fp2(x1));
}
void p2(double x0, double x1){//割线法
    double x2;
    while(true){
        x2 = iterp2(x0, x1);
        if(abs(x2 - x1) < e) break;
        x0 = x1;
        x1 = x2;
    }
    cout << "ans of p2: " << x2 << endl;
}
int main() {
    cout << setprecision(10);
    p1(0);
    p2(0, 1);
    return 0;
}
