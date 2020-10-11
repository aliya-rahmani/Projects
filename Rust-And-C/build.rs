extern crate cc;

fn main() {
    cc::Build::new()
        .file("src/c_code/main.c")
        .file("src/c_code/stdio_usage.c")
        .compile("libctorust.a");
}