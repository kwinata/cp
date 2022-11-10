// Input Output
#include <cstdio>
#include <cstdlib>
#include <iostream>
// Datastructures
#include <cstring>
#include <bitset>
#include <queue>
#include <map>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <stack>
#include <utility>
#include <queue>
// Others
#include <cmath>
#include <numeric>      // std::iota
#include <algorithm>
#include <time.h>
#include <atcoder/fenwicktree>
// Define
#define mp make_pair
#define ff first
#define fi first
#define ss second
#define se second
#define pb push_back
#define eb emplace_back
#define rep(x,a,b,c) for(int x=a;x<=b;x+=c)
#define repp(x,a,b) rep(x,a,b,1)
#define rev(x,a,b,c) for(int x=a;x>=b;x-=c)
#define revv(x,a,b) rev(x,a,b,1)

using namespace std;

// Typedef
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pii> vii;
typedef vector<vi> vvi;
typedef long long ll;
typedef unsigned long long ull;

// const
const double EPS = 1e-9;
const double PI = acos(-1);
const int OO = 2e9;
const ll INF = (ll)9e18;

// Additional typedef for long long
typedef vector<ll> vl;
typedef pair<ll,ll> pll;
typedef vector<pll> vll;
typedef vector<vector<pii>> vvii;

const ull mod=998244353;

ull powmod(ll z,ll a)
{
	if(a==0)return 1;
	if(a==1)return z;
	ll x=powmod(z,a/2);
	x=(x*x)%mod;
	if(a%2==1)x=(x*z)%mod;
	return x;
}

ull invmod(ll z)
{
	return powmod(z,mod-2);
}

const int N = 200005;
ull f1[N], f2[N];
ull query(ull *f, int n) {
	ull a = 0;
	for(int i= n ;i> 0; i-= (i& -i)) {
	    a += f[i];
		a%=mod;
	}
	return a;
}

void upd(ull *f, int i, ull v) {
	for( ; i<= N ; i+= (i& -i) ) {
	    f[i] += v;
		f[i]%=mod;
	}
}

int main() {
	int n;
	vi nums;
	scanf("%d",&n);
	nums.pb(0);
	repp(x,1,n) {
		int t;
		scanf("%d",&t);
		if(t>N) {
			return 1;
		}
		nums.pb(t);
	}
	fenwick_t
	vector<ull> sum(n+1,0);
	// f1 is counter 
	// f2 is prefix sum
	ull curmax=0;
	repp(y,1,n) {
		ull curval= nums[y];
		sum[y]=sum[y-1] + curval; // get prev sum + if both cards is the current card
		curmax=max(curmax,curval); // get global max
		ull smol = query(f1,curval);
		// printf("%d is on %llu th pos\n",curval,smol);
		sum[y]+=(((curval*smol)%mod)*2 )%mod;
		sum[y]+=(query(f2,curmax)-query(f2,curval))*2; // get suffix sum
		sum[y]%=mod; 

		// printf("sum[y] is %llu\n",sum[y]);
		upd(f1,curval,1);
		upd(f2,curval,curval);
	}
	// printf("test1\n");
	repp(y,1,n) {
		// cout<<((ulsl)sum[y]*invmod(y*y))%mod<<"\n";
		// printf("%llu\n",sum[y]);
		printf("%llu\n", (sum[y]*invmod(y*y))%mod);
	}
	
	return 0;
}
