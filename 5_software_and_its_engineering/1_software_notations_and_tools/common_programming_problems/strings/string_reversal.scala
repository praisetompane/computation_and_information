import io.Source.stdin

/*
    Constraints:
        0 <= T <= 10
        0 <= n <= 10^2
    Performance:
        Time:
            T = number of test cases
            n = length of each string
            O(T * n)

 */
object Solution {
  def main(args: Array[String]): Unit = {
    val incomingStrings = stdin.getLines().takeWhile(_.nonEmpty).toList
    incomingStrings.drop(1).foreach { input =>
      val output = new StringBuilder()
      var rotated = input 
      val totalRotations = input.length()
      (0 until totalRotations).foreach { _ =>
        rotated = rotated.appended(rotated(0)).drop(1)
        output.append(rotated)
        output.append(" ")
      }
      println(output)
    }
  }
}
