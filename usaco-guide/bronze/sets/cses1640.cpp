#include<bits/stdc++.h>

#define ll long long

using namespace std;

int main(){
	ll n, x, cur;
	cin >> n >> x;
	map<ll, ll> a;
	for(ll i = 0; i<n; i++){
		cin >> cur;
		if (a.count(x-cur)){
			cout << a[x-cur] << ' ' << i+1 << endl;
			return 0;
		}
		a[cur] = i+1;
	}
	cout << "IMPOSSIBLE" << endl;
}

