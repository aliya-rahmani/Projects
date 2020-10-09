use std::fs;
extern crate cc;

fn main() {
    cc::Build::new()
        .file("src/c_code/main.c")
        .compile("libctorust.a");
}