fn main() {

    let mut found: i64 = 0;                                     
    for count in 1i64..10_000_000 {                             
        if count % 2 != 0 {                                     
            if check_prime(&count) {                            
                found = add(found,1);                           
                println!("{},{}",&count,&found);                
            }
        }
    }

    fn check_prime(count: &i64) -> bool {                       
        let mut stop = ((*count as f64).sqrt() + 1.0) as i64;   
        for i in 3..stop {                                      
            if i % 2 != 0 {                                     
                if count % i == 0 {                             
                    return false                                
                }
            }
        }
        return true                                             
    }

    fn add(number: i64, add: i64) -> i64 {                      
        number + add                                            
    }
}
