import io.Source.stdin

object Solution {
    def main(args: Array[String]): Unit = {
        println("Please enter two numbers on separate lines")
        val sum = stdin.getLines().take(2).map(_.toInt).sum
        println(sum)
    }
}