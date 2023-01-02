# MapReduce

assignment of Big Data System course in Taiwan, NDHU

----
report written with Hackmd.io and markdown  
[Report](https://hackmd.io/NKgyYJfTRKaNGQZw6vB7hw)
implementation using Python


## wordcount
trying basic Word Count with mapper and reducer

## sorting algorithm
input:
* a file of values to sort, one value per line
* Mapper key is file ID, line number
* Mapper value is the contects of the line

ps. Takes advantages of reducer properties: (key, value) pairs are processed in order by key;
reducers are themselves ordered

* Mapper: Identity function for value: (k,v) -> (v, _)

* Reducer: Identity function: (k',_) -> (k', "")

## searching algorithm
Given a set of `files` containing lines of text and a search `pattern` to find.
Determine the `files` that matches the pattern.
Can be easily generalized into determining (file, [l1, l2, …]), i.e. all lines that match the pattern.

* Mapper: Given (fileID, some text) and “pattern”, if “text” matches “pattern” output (filename, _)
* Reducer: Identity function


## tf-idf
Term Frequency – Inverse Document Frequency

Job 1: Word Frequency in Doc
* Mapper
  * Input: (docname, contents)
  * Output: ((word, docname), 1)
* Reducer
  * Sums counts for each word in document
  * Outputs ((word, docname), n)  
  
// Combiner is the same as Reducer

Job 2: Total Word Counts For Docs
* Mapper
  * Input: ((word, docname), n)
  * Output: (docname, (word, n))
* Reducer
  * Sums frequency of individual n’s in same doc
  * Feeds original data through
  * Outputs ((word, docname), (n, N))

Job 3: Word Frequency In Corpus
* Mapper
  * Input: ((word, docname), (n, N))
  * Output: (word, (docname, n, N, 1))
* Reducer
  * Sums counts for word in corpus
  * Outputs ((word, docname), (n, N, m))

Job 4: Calculate TF-IDF
* Mapper
  * Input: ((word, docname), (n, N, m))
  * Assume D is known (or, easy MR to find it, exercise!)
  * Output ((word, docname), TF*IDF)
* Reducer
  * Just the identity function


## sequential pattern mining (a.k.a activity pattern mining v1, in short apm)

Job1: Large-1 activity set generation.
* Mapper: given (TID, Behavior_Items), generate all possibnle (item, 1).
* Reducer: for each item, sum the count and emit all ((item), n) for items with n >= support.

Job2: Large-2 ~ n activity set generation.
* Mapper: Given a (activityset, count) pair (A, n), emit (prefix of A except the last item, last item).
* Reducer: Given (prefix, [m1, m2, …]), emit all possible ((prefix, mi, mj), _) as candidates.

Job3: Given each candidate pattern, count frequency in TDB and keep only those with enough support.

The final result is the union of the output of all reducers that generate (ActivitySet, count)


## sequential pattern mining verison2 -- One pass (a.k.a activity pattern mining v2, in short apm)
One pass MapReduce algorithm
* Mapper: Given (TID, Behavior_Items), generate all possible (pattern, 1).
* Reducer: Sum the count for the same pattern and emit (pattern, n) if n >= support.  

That’s it !!
