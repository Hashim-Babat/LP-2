#include <iostream>
#include <vector>
using namespace std;

// Print the board
void printBoard(vector<vector<int>>& board, int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            cout << board[i][j] << " ";
        cout << endl;
    }
}

// ----------- BACKTRACKING APPROACH -----------

bool isSafeBT(vector<vector<int>>& board, int row, int col, int N) {
    for (int i = 0; i < col; i++)
        if (board[row][i])
            return false;

    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;

    for (int i = row, j = col; j >= 0 && i < N; i++, j--)
        if (board[i][j])
            return false;

    return true;
}

bool solveNQueensBT(vector<vector<int>>& board, int col, int N) {
    if (col >= N)
        return true;

    for (int i = 0; i < N; i++) {
        if (isSafeBT(board, i, col, N)) {
            board[i][col] = 1;
            if (solveNQueensBT(board, col + 1, N))
                return true;
            board[i][col] = 0; // backtrack
        }
    }
    return false;
}

// ----------- BRANCH AND BOUND APPROACH -----------

bool solveNQueensBB(vector<vector<int>>& board, int col, int N, vector<bool>& leftRow, vector<bool>& upperDiag, vector<bool>& lowerDiag) {
    if (col >= N)
        return true;

    for (int row = 0; row < N; row++) {
        if (!leftRow[row] && !lowerDiag[row + col] && !upperDiag[N - 1 + col - row]) {
            board[row][col] = 1;
            leftRow[row] = lowerDiag[row + col] = upperDiag[N - 1 + col - row] = true;

            if (solveNQueensBB(board, col + 1, N, leftRow, upperDiag, lowerDiag))
                return true;

            // Backtrack
            board[row][col] = 0;
            leftRow[row] = lowerDiag[row + col] = upperDiag[N - 1 + col - row] = false;
        }
    }
    return false;
}

// ------------- MAIN DRIVER -------------
int main() {
    char c = 'y';
    while (c == 'y') {
        int N, choice;
        cout << "\nEnter value of N: ";
        cin >> N;

        vector<vector<int>> board(N, vector<int>(N, 0));

        cout << "Choose algorithm:\n1. Backtracking\n2. Branch and Bound\nEnter choice: ";
        cin >> choice;

        bool result = false;

        if (choice == 1) {
            result = solveNQueensBT(board, 0, N);
        } else if (choice == 2) {
            vector<bool> leftRow(N, false), upperDiag(2 * N - 1, false), lowerDiag(2 * N - 1, false);
            result = solveNQueensBB(board, 0, N, leftRow, upperDiag, lowerDiag);
        } else {
            cout << "Invalid choice!";
        }

        if (result)
            printBoard(board, N);
        else
            cout << "\nSolution does not exist" << endl;

        cout << "\nDo you want to continue (y/n): ";
        cin >> c;
    }

    return 0;
}
