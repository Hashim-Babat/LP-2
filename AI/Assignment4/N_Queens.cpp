#include <iostream>
#include <vector>
using namespace std;


// Function to print the board
void printBoard(vector<vector<int>>& board,int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            cout << board[i][j] << " ";
        cout << endl;
    }
}

// Function to check if a queen can be placed safely
bool isSafe(vector<vector<int>>& board, int row, int col,int N) {
    // Check left side of this row
    for (int i = 0; i < col; i++)
        if (board[row][i])
            return false;

    // Check upper diagonal on left side
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;

    // Check lower diagonal on left side
    for (int i = row, j = col; j >= 0 && i < N; i++, j--)
        if (board[i][j])
            return false;

    return true;
}

// Recursive function to solve N-Queens problem
bool solveNQueens(vector<vector<int>>& board, int col,int N) {
    // Base case: If all queens are placed
    if (col >= N)
        return true;

    // Try placing a queen in all rows one by one
    for (int i = 0; i < N; i++) {
        if (isSafe(board, i, col,N)) {
            board[i][col] = 1; // Place queen

            if (solveNQueens(board, col + 1,N))
                return true; // Found a solution

            board[i][col] = 0; // Backtrack
        }
    }
    return false; // No solution found
}

// Driver function
int main() {
    char c='y';
    while(c=='y'){
        int N;
        cout<<"\nEnter value of n : ";
        cin>>N;
        vector<vector<int>> board(N, vector<int>(N, 0));

        if (solveNQueens(board, 0,N))
            printBoard(board,N);
        else cout << "\nSolution does not exist" << endl;
        cout<<"\nDo you want to continue (y/n) : ";
        cin>>c;
    }
    

    return 0;
}
