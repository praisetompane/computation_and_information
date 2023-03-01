import scala.annotation.tailrec
def count(arr:List[Int]):Int = {
    @tailrec
    def _count(total: Int, objects:List[Int]): Int = objects match {
        case List() => total
        case head :: tail => _count(total + 1, tail)
    }
    _count(0, arr)
}


@main def main(): Unit = {
    println(count((0 until 10).toList))
}