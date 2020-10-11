#include<bits/stdc++.h>
using namespace std;

bool fillBoard(char board[3][3], int n){
  for(int i = 0; i < 3; i++){
    for(int j = 0; j < 3; j++){
      if(i*3 + j + 1 == n && board[i][j] == '_'){
        board[i][j] = 'x';
        return true;
      }
    }
  }
  return false;
}

void showBoard(char board[3][3]){
  for(int i = 0; i < 3; i++){
    for(int j = 0; j < 3; j++){
      cout<<board[i][j]<<" ";
    }
    cout<<endl;
  }
}

bool isFull(char board[3][3]){
  for(int i = 0; i < 3; i++){
    for(int j = 0; j < 3; j++){
      if(board[i][j] == '_') return false;
    }
  }

  return true;
}

bool isWin(char board[3][3], char ch){
  
  for(int i = 0; i < 3; i++){
    if(board[i][0] == ch && board[i][0] == board[i][1] && board[i][1] == board[i][2]) return true;
  }
  for(int j = 0; j < 3; j++){
    if(board[0][j] == ch && board[0][j] == board[1][j] && board[1][j] == board[2][j]) return true;
  }

  if(board[0][0] == ch && board[0][0] == board[1][1] && board[1][1] == board[2][2]) return true;

  if(board[2][0] == ch && board[2][0] == board[1][1] && board[1][1] == board[0][2]) return true;

  return false;
}


int evaluate(char board[3][3]){
  for(int i = 0; i < 3; i++){
    if(board[i][0] == board[i][1] && board[i][1] == board[i][2]){
      if(board[i][0] == 'o') return 10;
      if(board[i][0] == 'x') return -10;
    }
  }
  for(int j = 0; j < 3; j++){
    if(board[0][j] == board[1][j] && board[1][j] == board[2][j]){
      if(board[0][j] == 'o') return 10;
      if(board[0][j] == 'x') return -10;
    }
  }

  if(board[0][0] == board[1][1] && board[1][1] == board[2][2]){
    if(board[0][0] == 'o') return 10;
    if(board[0][0] == 'x') return -10;
  }

  if(board[2][0] == board[1][1] && board[1][1] == board[0][2]){
    if(board[2][0] == 'o') return 10;
    if(board[2][0] == 'x') return -10;
  }

  return 0;
}


int minimax(char board[3][3], bool isMax){
  int score;
  score = evaluate(board);
  if(score == 10 || score == -10) return score;
  if(isFull(board)) return 0; 

  if(isMax){
    int best = -10000;
    for(int i = 0; i < 3; i++){
      for(int j = 0; j < 3; j++){
        if(board[i][j] != '_') continue;
        board[i][j] = 'o';
        best = max(best, minimax(board, !isMax));
        board[i][j] = '_';
      }
    }

    return best;
  }

  else{
    int best = 1000;
    for(int i = 0; i < 3; i++){
      for(int j = 0; j < 3; j++){
        if(board[i][j] != '_') continue;
        board[i][j] = 'x';
        best = min(best, minimax(board, !isMax));
        board[i][j] = '_'; 
      }
    }

    return best;
  }

  return 0;

}

void computerMove(char board[3][3], int &x, int& y){
  int bestMove = -10000;

  for(int i = 0; i < 3; i++){
    for(int j = 0; j < 3; j++){
      if(board[i][j] != '_') continue;
      board[i][j] = 'o';
      int moveVal = max(bestMove, minimax(board, false));
      board[i][j] = '_';

      if(moveVal > bestMove){
        x = i;
        y = j;
        bestMove = moveVal;
      }
    }
  }

}


int main(){

  cout<<"Welcome to Tic Tac Toe"<<endl;
  cout<<"You have to chose a number from 1 to 9 to put your cross in that place"<<endl;
  for(int i = 0; i < 3; i++){
    for(int j = 1; j <= 3; j++){
      cout<<i*3 + j<<" ";
    }
    cout<<endl;
  }

  while(true){

    char board[3][3];
    for(int i = 0; i < 3; i++){
      for(int j = 0; j < 3; j++){
        board[i][j] = '_';
      }
    }
    cout<<"Coin toss for who goes first"<<endl;
    cout<<"Pick your side :\n 1. Heads\n 2. Tails"<<endl;
    int userNum;
    cin>>userNum;
    int randNumber = rand()%2;
    if(userNum == randNumber + 1){
      cout<<"you won the toss, Go first"<<endl;
      int moveIndex = 0;
      while(true){
        showBoard(board);
        int n;
        cin>>n;
        while(!fillBoard(board, n)){
          cout<<"invalid move. Try again"<<endl;
          cin>>n;
        }
        if(isWin(board, 'x')){
          showBoard(board);
          cout<<"Congrats!! you win"<<endl;
          break;
        }
        moveIndex++;
        if(moveIndex == 9) {
          showBoard(board);
          cout<<"It is a Draw"<<endl;
          break;
        }

        int x = -1, y = -1;
        computerMove(board, x, y);
        board[x][y] = 'o';
        if(isWin(board, 'o')){
          showBoard(board);
          cout<<"You Lost"<<endl;
          break;
        }
        moveIndex++;
        if(moveIndex == 9) {
          showBoard(board);
          cout<<"It is a Draw"<<endl;
          break;
        } 
      
      }

    }
    else{
      cout<<"you lost the toss"<<endl;
      int moveIndex = 0;
      while(true){

        int x = -1, y = -1;
        computerMove(board, x, y);
        board[x][y] = 'o';
        if(isWin(board, 'o')){
          showBoard(board);
          cout<<"You Lost"<<endl;
          break;
        }
        moveIndex++;
        if(moveIndex == 9) {
          showBoard(board);
          cout<<"It is a Draw"<<endl;
          break;
        } 

        showBoard(board);
        int n;
        cin>>n;
        while(!fillBoard(board, n)){
          cout<<"invalid move. Try again"<<endl;
          cin>>n;
        }
        if(isWin(board, 'x')){
          showBoard(board);
          cout<<"Congrats!! you win"<<endl;
          break;
        }
        moveIndex++;
        if(moveIndex == 9) {
          showBoard(board);
          cout<<"It is a Draw"<<endl;
          break;
        } 
      }

    }

    cout<<"want to play again? [y/n]"<<endl;
    char yesOrNo;
    cin>>yesOrNo;
    if(yesOrNo != 'y') break; 

  }

}