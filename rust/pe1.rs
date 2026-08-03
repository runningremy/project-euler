fn main() {
    let mut i = 1;
    let mut j = 0;
    while i < 1000 {
        if i % 3 == 0 || i % 5 == 0 {
            j = j + i;
            i += 1;
        } else {
            i += 1;
        }
    }
    println!("{}", j);
}
