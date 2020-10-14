#include <stdio.h>
#define N 8

int is_valid(int i, int j, int sol[N+1][N+1]) {
  if (i>=1 && i<=N && j>=1 && j<=N && sol[i][j]==-1)
    return 1;
  return 0;
}

int knight_tour(int sol[N+1][N+1], int i, int j, int step_count, int X_move[], int Y_move[]) {
  if (step_count == N*N)
    return 1;

  int k;
  for(k=0; k<8; k++) {
    int next_i = i+X_move[k];
    int next_j = j+Y_move[k];

    if(is_valid(i+X_move[k], j+Y_move[k], sol)) {
      sol[next_i][next_j] = step_count;
      if (knight_tour(sol, next_i, next_j, step_count+1, X_move, Y_move))
        return 1;
      sol[i+X_move[k]][j+Y_move[k]] = -1; 
    }
  }

  return 0;
}

int start_knight_tour() {
  int sol[N+1][N+1];

  int i, j;
  for(i=1; i<=N; i++) {
    for(j=1; j<=N; j++) {
      sol[i][j] = -1;
    }
  }

  int X_move[] = {2, 1, -1, -2, -2, -1, 1, 2};
  int Y_move[] = {1, 2, 2, 1, -1, -2, -2, -1};

  sol[1][1] = 0; 

  if (knight_tour(sol, 1, 1, 1, X_move, Y_move)) {
    for(i=1; i<=N; i++) {
      for(j=1; j<=N; j++) {
        printf("%d\t",sol[i][j]);
      }
      printf("\n");
    }
    return 1;
  }
  return 0;
}

int main() {
  printf("%d\n",start_knight_tour());
  return 0;
}
