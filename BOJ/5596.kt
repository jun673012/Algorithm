fun main() {
    var inkook:Int = 0
    var manse:Int = 0
    var (a1, b1, c1, d1) = readln().split(' ').map { it.toInt() }
    var (a2, b2, c2, d2) = readln().split(' ').map { it.toInt() }
    inkook += a1 + b1 + c1 + d1
    manse += a2 + b2 + c2 + d2
    if (inkook > manse)
        println(inkook)
    else
        println(manse)
}
