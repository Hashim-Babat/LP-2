#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
class Graph
{
	int v;
	public:
	Graph(int n){
		this->v=n;
	}
	void print(vector<vector<int>>& mat){
		cout<<"\nWeighted Graph : ";
		cout<<endl;
		for(int i=0;i<mat.size();i++){
			for(int j=0;j<mat[0].size();j++){
				cout<<mat[i][j]<<"  ";
			}
			cout<<endl;
		}
		cout<<endl;
	}
	int index(vector<string>& cities,string city){
		int n = cities.size();
		for(int i=0;i<n;i++){
			if(cities[i]==city) return i;
		}
		return -1;
	}
    void kruskalMinCost(vector<vector<int>>& adjacencyMatrix,vector<string>& cities) {
        int V = adjacencyMatrix.size();
        int minCost = 0;
        // Initialize a vector to track parent vertices for union-find
        vector<int> parent(V, -1);
        // Number of edges to be included in the MST
        int edgeCount = 0;
        // Iterate through all edges in the graph
        while (edgeCount < V - 1) {
            int minWeight = 9999;
            int u, v;
            // Find the minimum weight edge that does not form a cycle
            for (int i = 0; i < V; ++i) {
                for (int j = 0; j < V; ++j) {
                    if (adjacencyMatrix[i][j] != 0) {
                        int uSet = i;
                        int vSet = j;
                        while (parent[uSet] != -1) uSet = parent[uSet];
                        while (parent[vSet] != -1) vSet = parent[vSet];
                        if (uSet != vSet && adjacencyMatrix[i][j] < minWeight) {
                            minWeight = adjacencyMatrix[i][j];
                            u = i;
                            v = j;
                        }
                    }
                }
            }
            // Operation to avoid cycles
            int uSet = u;
            int vSet = v;
            while (parent[uSet] != -1) uSet = parent[uSet];
            while (parent[vSet] != -1) vSet = parent[vSet];
            if (uSet != vSet){
                cout<<"\n"<<cities[u]<<" -> "<<cities[v]<<" : "<<minWeight<<endl;
                minCost += minWeight;
                parent[uSet] = vSet;
                edgeCount++;
            }
            // Mark the edge as visited
			adjacencyMatrix[u][v]=0;
        }
        cout<<"\nMinimum Cost : "<<minCost<<endl;
    }
    void primsMinCost(vector<vector<int>>& adjacencyMatrix, vector<string>& cities) {
        int V = adjacencyMatrix.size();
        vector<bool> visited(V, false);
        vector<int> key(V, 9999);  // Stores minimum weight to reach a node
        vector<int> parent(V, -1); // Stores parent node in MST
    
        key[0] = 0; // Start from the first vertex
    
        for (int count = 0; count < V - 1; count++) {
            int min = 9999, u = -1;
    
            // Find the vertex with the minimum key value from the unvisited set
            for (int i = 0; i < V; i++) {
                if (!visited[i] && key[i] < min) {
                    min = key[i];
                    u = i;
                }
            }
    
            visited[u] = true;
    
            // Update key values of adjacent vertices
            for (int v = 0; v < V; v++) {
                if (adjacencyMatrix[u][v] && !visited[v] && adjacencyMatrix[u][v] < key[v]) {
                    key[v] = adjacencyMatrix[u][v];
                    parent[v] = u;
                }
            }
        }
    
        // Print MST
        int minCost = 0;
        cout << "\nPrim's MST Edges:\n";
        for (int i = 1; i < V; i++) {
            cout << cities[parent[i]] << " -> " << cities[i] << " : " << adjacencyMatrix[parent[i]][i] << endl;
            minCost += adjacencyMatrix[parent[i]][i];
        }
        cout << "\nMinimum Cost : " << minCost << endl;
    }
    
};
int main() {
	cout<<"\nEnter total no of cities : ";
	int n;
	cin>>n;
	Graph g(n);
	vector<vector<int>> adjMatrix(n,vector<int>(n,0));
	vector<string> cities(n);
	for(int i=0;i<n;i++){
		cout<<"\nEnter city "<<i<<" : ";
		string str;
		cin>>str;
		cities[i]=str;
	}
	for(int i=0;i<n;i++){
		cout<<"\nEnter total no of cities which are connected to "<<cities[i]<<" : ";
		int e;
		cin>>e;
		if(e>=0 && e<n){
			for(int j=1;j<=e;j++){
				cout<<"\nEnter city name : ";
				string s;
				cin>>s;
				int ans = g.index(cities,s);
				if(ans!=-1){
					int wt;
					cout<<"\nEnter cost : ";
					cin>>wt;
					adjMatrix[i][ans]=wt;
				}
				else cout<<"\nCity doesnt exist";
			}
		}
		else cout<<"\nInavlid number !";
	}
    vector<vector<int>> adjMatrixCopy = adjMatrix; // for Kruskal
    vector<vector<int>> adjMatrixCopy2 = adjMatrix; // for Prim
	g.print(adjMatrix);
	g.kruskalMinCost(adjMatrixCopy,cities);
    g.primsMinCost(adjMatrixCopy2,cities);
}