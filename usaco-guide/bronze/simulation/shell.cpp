#include<bits/stdc++.h>
using namespace std;
void setIn(string s) { freopen(s.c_str(),"r",stdin); }
void setOut(string s) { freopen(s.c_str(),"w",stdout); }
int main(){
	setIn("shell.in");
	setOut("shell.out");
	int n;
	cin >> n;
	vector<tuple<int, int, int>> v;
	int a,b,c;
	for(int i=0; i<n; i++){
		cin >> a >> b >> c;
		v.push_back(make_tuple(a-1, b-1, c-1));
	}
	int max_point = 0;
	for(int start=0; start<3; start++){
		vector<int> loc {0, 0, 0};
		loc[start] = 1;
		int point = 0;
		for(auto el: v) {
 			iter_swap(loc.begin() + get<0>(el), loc.begin() + get<1>(el));
		
			if (loc[get<2>(el)]){
				point += 1;
			}
		}
		max_point = max(max_point, point);
	}
	cout << max_point;
}
