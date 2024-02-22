# Belief Functions Converter

## I - Introduction
Dempster-Shafer theory is used to deal with uncertainty and imprecision while having connections
between hypothesis such as probability.

It represents a generalization of both probabilistic and possibilistic models.
That is why this theory is based on the idea of combining sets and probabilities.
The difference with probability is the key concept of `Mass function`.

A Mass function is defined on set and not on singletons and the belief degree is assigned exactly to the
hypothesis A and to none more specific hypothesis.

Sets A of $`\Omega`$ such that m(A) > 0 are called focal elements of m and m($`\Omega`$) represents the
degree of total ignorance.

Example : 
Let $`\Omega`$ = {Red, Yellow, Green} a finite set of answers
Here, a random mass is assigned to all the subsets out of $`\Omega`$ in the table below :

| Hypothesis                 | Mass    |
| -------------------------- |:-------:|
| None ($`\emptyset`$)       | 0       |
| {Red}                      | 0.35    |
| {Yellow}                   | 0.25    |
| {Green}                    | 0.15    |
| {Red $` \cup `$ Yellow}    | 0.06    |
| {Red $` \cup `$ Green}     | 0.05    |
| {Yellow $` \cup `$ Green}  | 0.04    |
| Any ($` \Omega `$)         | 0.1     |

Based on that, different Belief Functions have been created to represent the information from that mass values :

* **Belief Function `Bel`**
  $$Bel(A) = \sum_{B \subseteq A, B \neq \emptyset} m(B), \forall A \subseteq \Omega$$

  $$Bel(\Omega) = 1, Bel(\emptyset) = 0$$

* **Plausability Function `Pl`**
  $$Pl(A) = \sum_{(B \cap A) \neq \emptyset} m(B), \forall A \subseteq \Omega$$

  $$Pl(\Omega) = 1, Pl(\emptyset) = 0$$

These two are the most common functions used in the Dempster-Shafer theory but the two following,
despite they have no signification can still be useful.

* **Implicability Function `b`**
  $$b(A) = \sum_{B \subseteq A} m(B), \forall A \subseteq \Omega$$

  $$b(\Omega) = 1$$

* **Commonality Function `q`**
  $$Pl(A) = \sum_{B \supseteq A} m(B), \forall A \subseteq \Omega$$

  $$q(\emptyset) = 1$$

Knowing that, if we come back to ou previous example, we will be able to add 4 more columns to 
the table which will become the one below :

| Hypothesis                 | Mass    | Belief   | Plausibility   |Implicability   | Commonality   |
| -------------------------- |:-------:|:--------:|:--------------:|:--------------:|:-------------:|
| None ($`\emptyset`$)       | 0       | 0        | 0              | 0              | 1.0           |
| {Red}                      | 0.35    | 0.35     | 0.56           | 0.35           | 0.56          |
| {Yellow}                   | 0.25    | 0.25     | 0.45           | 0.25           | 0.45          |
| {Green}                    | 0.15    | 0.15     | 0.34           | 0.15           | 0.34          |
| {Red $` \cup `$ Yellow}    | 0.06    | 0.66     | 0.85           | 0.66           | 0.16          |
| {Red $` \cup `$ Green}     | 0.05    | 0.55     | 0.75           | 0.55           | 0.15          |
| {Yellow $` \cup `$ Green}  | 0.04    | 0.44     | 0.65           | 0.44           | 0.14          |
| Any ($` \Omega `$)         | 0.1     | 1.0      | 1.0            | 1.0            | 0.1           |

  
