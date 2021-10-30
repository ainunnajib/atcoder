#include <iostream>
using namespace std;

long long n, c = 0, xa, xb, ya, yb;

int main(){
    cin >> n;
    long long x[n], y[n];
    for (int i=0;i<n;i++) cin >> x[i] >> y[i];
    for (int i=0;i<n;i++){
        for (int j=i+1;j<n;j++){
            for (int k=j+1;k<n;k++){
                xa = x[j] - x[i];
                xb = x[k] - x[i];
                ya = y[j] - y[i];
                yb = y[k] - y[i];
                if (xa * yb != xb * ya) c++;
            }
        }
    }
    cout << c;
}