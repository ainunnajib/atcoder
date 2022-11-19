#include <iostream>
#include <map>
using namespace std;

typedef long long ll;

int main() {
	ll offset = 0;
	map<int, bool> isnotreset;
	int n, q, iq, x;
	cin >> n;
	ll a[n];
	for(int i=0;i<n;i++) {
		cin >> a[i];
		isnotreset[i] = true;
	}
	cin >> q;
	while(q--){
		int t; cin >> t;
		ll x;
		if(t==1){
			cin >> x;
			offset = x;
			isnotreset.clear();
		}
		else if(t==2){
			cin >> iq >> x; iq--;
			if(isnotreset[iq]){
				a[iq] += x;
			} else {
				a[iq] = offset + x;
				isnotreset[iq] = true;
			}
		}
		else {
			cin >> iq; iq--;
			if(isnotreset[iq])
				cout << a[iq] << endl;
			else
				cout << offset << endl;
		}
	}
}