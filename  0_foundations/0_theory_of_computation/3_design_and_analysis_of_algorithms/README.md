# 3_design_and_analysis_of_algorithms

objective:
    - unpack in layman's terms what algorithms & data structures are and their role in the humanity's current implementation of computation.
    - solve computational problems.
    - prove correctness of solutions.
    - argue efficiency.

## What is a Computational Problem?
def: a binary relation from problem inputs to correct outputs (Demaine, Ku, Solomon, 2020).
    for binary relation definition:
        see: https://github.com/praisetompane/mathematics/blob/master/0_foundations/relation.txt

# What is an Algorithm?
def¹: a finite procedure
        that maps
            an input
            to a **single** output (Demaine, Ku, Solomon, 2020).
        i.e.a function f: Input -> Output.
            a solution to a computational problem.

def²: a recipe for solving a specific problem by manipulating symbols (Wengrow, 2017:56).

def³: a computational procedure for solving a problem (Demaine, 2017)
    i.e. input -> algorithm -> output

plain english:
    - algorithms are just a sequence of steps "to do something"
        "to do something", you need:
            store and name things = variables/values(see point 2)
            decisions = if, else
            repeat = iteration constructs = loops, recursion
            
    - etymology: Why algorithms are called algorithms | BBC Ideas: https://m.youtube.com/watch?v=oRkNaF0QvnI
    
# What is a Data Structure?
def¹: how data is organised (Wengrow, 2017:27).

defᵖˡᵃⁱⁿ_ᵉⁿᵍˡⁱˢʰ: data structures are just how you store things
    to store something, you need:
        place to store it = array index, node in a list, leave in a tree etc
        a way to retrieve = access patterns = LIFO, FIFO etc


# References:
* Wengrow J. 2017. A Common-Sense Guide to Data Structures and Algorithms: Level Up Your Core Programming Skills.
* Demaine E. Ku J. Solomon J. Introduction To Algorithms. 2020. https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-1-algorithms-and-computation/
* Demaine E. Devadas S. Introduction To Algorithms. 2011. https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/lecture-4-heaps-and-heap-sort/.
