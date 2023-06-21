fun main() {
    while (true) {
        var ans: String = readln()
        if (ans == "#") break
        println(ans.count{ it == 'a' || it == 'e' || it == 'i' || it == 'o' || it == 'u' || it == 'A' || it == 'E' || it == 'I' || it == 'O' || it == 'U' })
    }
}
