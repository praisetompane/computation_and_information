import io.StdIn

/*
    Given:
        string of length N

    Objective: 
        remove characters that have already appeared
        i.e. remove duplicate characters    

    Constraints
        1 <= N <= 30000
*/
object Solution {
    def main(args: Array[String]) = {
        val input = StdIn.readLine()
        println(input.distinct)
    }
}