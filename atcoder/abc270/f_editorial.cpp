#include <bits/stdc++.h>
#include <atcoder/dsu>

using namespace std;
using namespace atcoder;

#define INF (long long)3e+18

int n,m;
vector<tuple<long long,int,int> >e;

long long solve(void){
	long long ret=0;
	sort(e.begin(),e.end());
	int sz=e.size();
	
	dsu d(n+3);
	for(int i=0;i<sz;i++){
		if(!d.same(get<1>(e[i]),get<2>(e[i]))){
			d.merge(get<1>(e[i]),get<2>(e[i]));
	 		ret+=get<0>(e[i]);
        	}
    }
   
	if(d.size(1)<n)return INF;
	return ret;
}



int main(void) {

    cin>>n>>m;

    vector<int> a(m),b(m);
    vector<long long> x(n),y(n),z(m);

	for(int i=0;i<n;i++)cin>>x[i];
	for(int i=0;i<n;i++)cin>>y[i];
	for(int i=0;i<m;i++){
		cin>>a[i]>>b[i]>>z[i];
	}

	long long ans=INF;
	for(int k=0;k<4;k++){
		e.clear();
		if(k&1)for(int i=0;i<n;i++)e.push_back({x[i],i+1,n+1});
		if(k&2)for(int i=0;i<n;i++)e.push_back({y[i],i+1,n+2});
		for(int i=0;i<m;i++)e.push_back({z[i],a[i],b[i]});
		ans=min(ans,solve());
	}
	cout<<ans<<endl;
	return 0;

}
