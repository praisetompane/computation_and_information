import scala.annotation.tailrec

/*
    Given:
        x: nᵗʰ fibonacci number required
    Flow
        1 1 2 3 ... (n-1 + n-2)

    Example:
        n = 5
               value terms    values_index  values_index_relative_to_curret_index
        fib₀ = 0
        fib₁ = 1
        fib₂ = 1 =   1 + 0  = fib₁ + fib₀ = fib₂₋₁ + fib₂₋₂
        fib₃ = 2 =   1 + 1  = fib₂ + fib₁ = fib₃₋₁ + fib₃₋₂
        fib₄ = 3 =   2 + 1  = fib₃ + fib₂ = fib₄₋₁ + fib₄₋₂
        fib₅ = 5 =   3 + 2  = fib₄ + fib₃ = fib₅₋₁ + fib₅₋₂

        fibₙ = fibₙ₋₁ + fibₙ₋₂

        NB: n is an index to a value in the sequence(i.e. the Fibonacci sequence).
            i.e. - fibₙ means get the value of the sequence
                    at index n.
                 - that value is the sum of n - 1 and n - 2
                    i.e. the value of the sequence
                        at index n - 1 and
                                 n - 2
 */
def fibonacci(n: Int): Int = {
  def _fibonacci(n: Int): Int = {
    if (n == 0) n
    else if (n == 1) n
    else _fibonacci(n - 1) + _fibonacci(n - 2)
  }
  _fibonacci(n)
}

@main def main(): Unit = {
  println(fibonacci(7))
  println(fibonacci(10))
  println(fibonacci(17))
  println(fibonacci(19))
}
