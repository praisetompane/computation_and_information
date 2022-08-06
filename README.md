## What is computation?

This repo is an attempt at unpacking in layman's terms what computation is, and humanity's current implementation of computation.

**Disclaimer**: This is an ongoing and incomplete project to unpack these concepts.

def 1: the **transformation** of **sequences of symbols** by **precise rules**¹

* symbols = {1,0,\*,{,;,<,>,...}
* to be refined: precise rules
  * example sequences:
    * 11010
    * ;\*>{11}  
      i.e. any sequence of the valid symbols

def 2: The **evolution process** of some environment, by a **sequence of "simple, local" steps**. _Church-Turing thesis_

### Rough overview of computation and applications

* theory of computation
  * define a language(formal language theory = FLT) to express computations.
  * Know what you can and can't compute.  
  * Know how fast you can compute.
* algorithms and data structures
  * Know how to compute
* hardware
  * use FLT to ask machines to compute.
* operating systems
  * use FLT to create computations that manage the machine.
* networking
  * connect the machines.
* computer systems engineering
  * use machines to build systems.
  
# References

* 1 https://iopscience.iop.org/book/978-1-6817-4093-5/chapter/bk978-1-6817-4093-5ch1

* The Church-Turing Thesis, https://plato.stanford.edu/entries/church-turing/

* The early history of computing | Professor Ursula Martin (Lecture 1), https://youtu.be/moYxYEfxO7g

* Alan Turing, Grace Hopper, and the history of getting things right | Ursula Martin (Lecture 2), https://www.youtube.com/watch?v=FSlkwUMhoes

# Repository Maintenance
## update sub-modules

```bash
  git pull --recurse-submodules
```


