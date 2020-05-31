#include<iostream>
    #include<vector>
    #include<queue>
    #include<algorithm>
     
    using namespace std;
     
    vector<int>G[100];
     
    bool visit[100];
    int dis[100], par[100];
     
    void bfs(int s)
    {
        queue<int>Q;
        Q.push(s);
     
        visit[s] = 1;
        dis[s] = 0;
     
        while(!Q.empty())
        {
            int u = Q.front();
     
            for(int i=0; i<G[u].size(); i++)
            {
                int v=G[u][i];
     
                if(!visit[v])
                {
                    visit[v] = 1;
                    dis[v] = dis[u] + 1;
                    par[v] = u;
                    Q.push(v);
                }
            }
            Q.pop();
        }
    }
     
    int main()
    {
        int v, e;
        cin>>v>>e;
        int a, b;
        for(int i=0; i<e; i++)
        {
            cin>>a>>b;
            G[a].push_back(b);
        }
     
        cout<<endl<<"Graph:"<<endl;
        for(int i=1; i<=v; i++)
        {
            if(G[i].size() == 0)
                cout<<0;
            for(int j=0; j<G[i].size(); j++)
                cout<<G[i][j]<<" ";
            cout<<endl;
        }
     
        int s,d;
        cout<<"\nEnter source and destination:"<<endl;
        cin>>s>>d;
     
        bfs(s);
     
        cout<<"The distance of "<<s<<" and "<<d<<" is: "<<dis[d]<<endl;
     
        return 0;
    }
