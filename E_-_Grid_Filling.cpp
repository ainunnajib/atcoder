#include <iostream>
#include <map>
#include <set>
using namespace std;

int main(){
    int H, W, N, h, w;
    cin >> H >> W >> N >> h >> w;
    int a[H][W];
    set<int> s;
    for(int i=0;i<H;i++)
        for(int j=0;j<W;j++) {
            cin >> a[i][j];
            s.insert(a[i][j]);
        }
    
    map<int, int> minx, maxx, miny, maxy;
    for(int i=0;i<H;i++)
        for(int j=0;j<W;j++) {
            if(!minx.count(a[i][j])) minx[a[i][j]] = i;
            else minx[a[i][j]] = min(i, minx[a[i][j]]);
            if(!miny.count(a[i][j])) miny[a[i][j]] = j;
            else miny[a[i][j]] = min(j, miny[a[i][j]]);
            if(!maxx.count(a[i][j])) maxx[a[i][j]] = i;
            else maxx[a[i][j]] = max(i, maxx[a[i][j]]);
            if(!maxy.count(a[i][j])) maxy[a[i][j]] = j;
            else maxy[a[i][j]] = max(j, maxy[a[i][j]]);
        }

    for(int i=0;i<=H-h;i++) {
        for(int j=0;j<=W-w;j++) {
            int ans = 0;
            for(auto x : s)
                if( minx[x] < i or maxx[x] > i+h-1 or miny[x] < j or maxy[x] > j+w-1 )
                    ans++;
            cout << ans << ' ';
        }
        cout << endl;
    }
}