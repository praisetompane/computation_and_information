
def contain_all_unique_characters(string: String): Boolean = {
    string.distinct.length() == string.length()
}

@main def main(): Unit = {
    val s1 = "gofreetech"  // false
    println(contain_all_unique_characters(s1))

    val s2 = "python"  // true
    println(contain_all_unique_characters(s2))

    val s3 = "p"  // true
    println(contain_all_unique_characters(s3))

    val s4 = ""  // true
    println(contain_all_unique_characters(s4))
}