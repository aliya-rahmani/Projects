impl Solution {
    pub fn k_concatenation_max_sum(arr: Vec<i32>, k: i32) -> i32 {
        let MOD = 1_000_000_007_i64;
        let copy = arr.iter().map(|c| *c as i64).collect::<Vec<i64>>();
        let mut best = 0_i64;
        let mut cur = 0_i64;
        let sum_i64: i64 = copy.iter().sum();
        let k = k as usize;
        
        for i in 0..min(k, 2) * copy.len() {
            let a = copy[i % arr.len()]; 
            cur = max(a, cur+a) % MOD;
            best = max(best, cur) % MOD;
        }
        let res = if k > 1 { max(best, best + (k as i64 - 2) * max(sum_i64, 0)) % MOD } else {best % MOD};
        res as i32
    }
}
