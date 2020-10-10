extern crate libc;

extern {
    fn square(input: libc::c_int) -> libc::c_int;
    fn cube(input: libc::c_int) -> libc::c_int;
    fn hello_world();
}

fn main() {
    let num = 4; // Number we input to C functions
    let sq_of_num = unsafe { square(num) }; // C functions aren't safe.
    let cb_of_num = unsafe { cube(num) }; // C functions aren't safe.
    println!("{} square = {}", num, sq_of_num);
    println!("{} cube   = {}", num, cb_of_num);
    unsafe {
        hello_world()
    };
}