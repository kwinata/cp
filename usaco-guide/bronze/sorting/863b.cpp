#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin >> n;
	vector<int> weights(2*n);
	int x;
	for(int i=0; i<2*n; i++){
		cin >> x;
		weights[i] = x;
	}
	sort(weights.begin(), weights.end());
	int i, j;
	vector<int> other_weights(2*n-2);
	int sum;
	int min_sum = 1e9;
	for(i=0; i<2*n; i++)
		for(j=i+1; j<2*n; j++){
			other_weights.clear();
			for(int k=0; k<2*n; k++)
				if(k != i && k != j)
					other_weights.push_back(weights[k]);
//			for(auto i: other_weights)
//				cout << i << ' ';
//			cout << " = ";
			sum = 0;
			for(int i=0;i<2*n-2; i+=2){
				sum += other_weights[i+1]-other_weights[i];
			}
//			cout << sum << endl;
			min_sum = min(min_sum, sum);
		}
	cout << min_sum;
}
