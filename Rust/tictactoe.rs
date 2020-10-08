use std::fmt;
#[macro_use] extern crate itertools;
use itertools::Itertools;

//#[allow(dead_code)]

// struct CaseAlreadyMarkedError;
// impl fmt::Display for CaseAlreadyMarkedError {
//     fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
//         write!(f, "The case has already been marked!") // user-facing output
//     }
// }

#[derive(Debug, Copy, Clone, PartialEq)]
enum TickType {
    Cross,
    Nought,
    Nil,
}

impl fmt::Display for TickType {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            TickType::Cross  => write!(f, "X"),
            TickType::Nought => write!(f, "O"),
            TickType::Nil    => write!(f, "."),
        }
    }
}

#[derive(Debug, Copy, Clone)]
enum Player {
    Crosses,
    Noughts,
}

impl Player {
    fn mark(&self) -> TickType {
        match self {
            Player::Crosses => TickType::Cross,
            Player::Noughts => TickType::Nought,
        }
    }

    fn other(&self) -> Player {
        match self {
            Player::Crosses => Player::Noughts,
            Player::Noughts => Player::Crosses,
        }
    }
}


#[derive(Debug)]
struct TicTacToe {
    turn: u8,
    player_turn: Player,
    board: [[TickType; 3]; 3],
    winner: Option<Player>,
}

impl TicTacToe {
    fn get_player(&self) {
        println!("{:?}", self.player_turn);
    }

    fn new() -> TicTacToe {
        TicTacToe {
            turn: 0,
            player_turn: Player::Crosses,
            board: [[TickType::Nil; 3]; 3],
            winner: None,
        }
    }

    fn place_mark(&mut self, x: usize, y: usize) {
        let current_player = self.player_turn;
        assert_eq!(self.board[x][y], TickType::Nil);
        self.board[x][y] = current_player.other().mark();
        self.player_turn = current_player.other();
        self.turn += 1;
    }

    fn win_condition(&self) -> bool{
        if self.turn < 5 {
            return false;
        }
        for i in 0..3 {
            if TicTacToe::check_all_same(&self.board[i]) == true {
                return true;
            }
            if TicTacToe::check_all_same(&self.board[..][i]) == true {
                return true;
            }
        }
        if TicTacToe::check_all_same(&[self.board[0][0], self.board[1][1], self.board[2][2]]) == true {
            return true;
        }
        if TicTacToe::check_all_same(&[self.board[0][2], self.board[1][1], self.board[2][0]]) == true {
            return true;
        }
        return false;
    }

    fn check_all_same(slice: &[TickType;3]) -> bool {
        let nil_present = slice.iter().any(|&x| x == TickType::Nil);
        if nil_present == true {
            return false;
        }
        return slice[0] == slice[1] && slice[1] == slice[2];
    }
}

impl fmt::Display for TicTacToe {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        for row in self.board.iter() {
            let row_string = itertools::join(row, " | ");
            write!(f, "{}\n", row_string);
        }
        return write!(f, "");
    }
}


fn main() {
    let mut game = TicTacToe::new();
    println!("{:}", game);

    let player = Player::Crosses;
    println!("{:?}", player);
    let player_2 = player.other();
    println!("{:?}", player);
    println!("{:?}", player_2);

    game.place_mark(0,0);
    game.place_mark(0,1);
    game.place_mark(1,1);
    game.place_mark(1,2);
    game.place_mark(2,2);
    println!("{:}", game);

    // game.place_mark(0,0);
    // println!("{:}", game);

    println!("{:?}", game.board[..][0]);

    println!("{:?}", game.win_condition());
}
