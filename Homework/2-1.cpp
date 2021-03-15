#include <bits/stdc++.h>
using namespace std;

const double e = 0.0005;
double f(double x) { return x * x * x - 2 * x - 5; }
double divide(double a, double b){
    double mid = (a + b) / 2;
    double fmid = f(mid);
    cout << a << " " << mid << " " << b << " " << fmid << endl;
    if(mid - a <= e) return mid;
    if(fmid == 0) return mid;
    if(fmid * f(a) > 0) return divide(mid, b);
    else return divide(a, mid);
}
int main() {
    cout << divide(2.0, 3.0) << endl;
    return 0;
}
