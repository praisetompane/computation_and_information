def f[T](arr:List[T]):List[T] = arr
                                .zipWithIndex
                                .sortWith{_._2 > _._2}
                                .map{case(value, index) => value}

@main def main() = {
    val numbers = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    println(f(numbers))
}