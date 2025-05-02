#include<bits/stdc++.h>
#include<iostream>
#include<queue>
#include<vector>
using namespace std;
#define N 3

// movement positions : (1,0) -->down, (0,-1) --> left, (-1,0) -->up (0,1) -->right
int drow[] = {1,0,-1,0};
int dcol[] = {0,-1,0,1};
 
struct Node{
    Node *parent; 
    int mat[N][N];
    int g; 
    int h; 
    int x,y;  
};

void printMatrix(int mat[N][N],int g,int h){ //here pass g and h
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }

    cout << "\ng : " <<  g
         << " h : " <<  h
         << " f : " << g+h << endl;
    
}

Node* newNode(int start[N][N],int x,int y,int nx,int ny,int g,Node *parent){
    Node *node = new Node;
    node->parent = parent;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            node->mat[i][j] = start[i][j];
        }
        
    }

    swap(node->mat[x][y],node->mat[nx][ny]);

    node->h = INT_MAX;
    node->g = g;
    node->x = nx;
    node->y = ny;

    return node;
}

int heuristic(int initial[N][N], int final[N][N]){
    int count = 0;
    for(int i = 0; i < N; i++){
        for (int j = 0; j < N; j++)
        {
            if(initial[i][j] && initial[i][j] != final[i][j]) count++;
        }
    }
    return count;
}

bool isSafe(int x,int y){
    return (x >= 0 && x < N && y >= 0 && y < N);
}

void printPath(Node *root){
    if(root == NULL) return;
    printPath(root->parent);
    printMatrix(root->mat, root->g, root->h);
    cout << endl;
}

struct comp{
    bool operator()(Node* lhs, Node *rhs){ // here operator() (...) remember syntax
        return (lhs->g + lhs->h) > (rhs->g + rhs->h); 
    }
};

void solve(int start[N][N],int x,int y,int goal[N][N]){
    int cnt = 0;
    priority_queue<Node *,vector<Node*>,comp> pq;

    Node *root = newNode(start,x,y,x,y,0,NULL);
    root->h = heuristic(start,goal);

    pq.push(root);

    while(!pq.empty()){
        Node *m = pq.top();
        pq.pop();

        if(m->h == 0){
            printPath(m);
            cout << "\nReached goal in " << m->g << " steps\n";
            return;
        }

        cnt++;
        for (int i = 0; i < 4; i++)
        {
            int dx = m->x + drow[i];
            int dy = m->y + dcol[i];

            if(isSafe(dx,dy)){
                Node *child = newNode(m->mat,m->x,m->y,dx,dy,m->g + 1,m);
                child->h = heuristic(child->mat,goal);
                pq.push(child);
            }
        }
        
    }
}

int main(){
    int start[N][N];
    int goal[N][N];

    int x = -1;
    int y = -1;

    cout << "Enter the inital state : " << endl;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> start[i][j];
            if(start[i][j] == 0){
                x = i;
                y = j;
            }
        }   
    }

    cout << "Enter the final state : " << endl;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> goal[i][j];
        }
    }
    cout << endl;
    solve(start,x,y,goal);

    return 0;
}