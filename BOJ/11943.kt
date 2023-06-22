import kotlin.math.min

fun main() {
    var (a, b) = readln().split(" ").map{it.toInt()}
    var (c, d) = readln().split(" ").map{it.toInt()}
    print(min(a+d, b+c))
}
