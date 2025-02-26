<h2>Sorting Algorithms</h2>
<h3><ol>Selection sort:</ol>ol></h3>
Time Complexity = O(n<sup>2</sup>)

<h4>Advantages:</h4>
<li>Requires only a constant O(1) extra memory space.</li>
<li>It requires less number of swaps (or memory writes) compared to many other standard algorithms. It can be simple algorithm choice when memory writes are costly.</li>

<h4> Disadvantages:</h4>
<li>Selection sort has a time complexity of O(n^2) makes it slower compared to algorithms like Quick Sort or Merge Sort.</li>
<li>Does not maintain the relative order of equal elements which means it is not stable.</li>

<h4>Applications:</h4>
<li>Suitable for small lists.</li>
<li>Heap Sort algorithm is based on Selection Sort.</li>

<h3><ol>Bubble sort:</h3></ol>
Time Complexity = O(n<sup>2</sup>)

<h4>Advantages:</h4>
<li>It does not require any additional memory space.</li>
<li>It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.</li>

<h4>Disadvantages:</h4>
<li>Bubble sort has a time complexity of O(n2) which makes it very slow for large data sets.</li>
<li>Bubble sort has almost no or limited real world applications.</li>

<h3><ol>Insertion sort:</h3></ol>
Time Complexity = O(n<sup>2</sup>)

<h4>Advantages:</h4>
<li>It does not require any additional memory space.</li>
<li>It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.</li>

<h4>Disadvantages:</h4>
<li>Bubble sort has a time complexity of O(n2) which makes it very slow for large data sets.</li>
<li>Bubble sort has almost no or limited real world applications.</li>

<h3><ol>Merge sort:</h3></ol>
Time Complexity = O(n log n)

<h4>Advantages:</h4>
<li>Stability : Merge sort is a stable sorting algorithm, which means it maintains the relative order of equal elements in the input array.</li>
<li>Guaranteed worst-case performance: Merge sort has a worst-case time complexity of O(N logN) , which means it performs well even on large datasets.</li>
<li>Simple to implement: The divide-and-conquer approach is straightforward.</li>
<li>Naturally Parallel : We independently merge subarrays that makes it suitable for parallel processing.</li>

<h4>Disadvantages:</h4>
<li>Space complexity: Merge sort requires additional memory to store the merged sub-arrays during the sorting process.</li>
<li>Not in-place: Merge sort is not an in-place sorting algorithm, which means it requires additional memory to store the sorted data. This can be a disadvantage in applications where memory usage is a concern.</li>
<li>Merge Sort is Slower than QuickSort in general as QuickSort is more cache friendly because it works in-place.</li>

<h4>Applications:</h4>
<li>Sorting large datasets</li>
<li>Merge Sort and its variations are used in library methods of programming languages.</li>
<li>It is a preferred algorithm for sorting Linked lists.</li>
<li>It can be easily parallelized as we can independently sort subarrays and then merge.</li>
<li>The merge function of merge sort to efficiently solve the problems like union and intersection of two sorted arrays.</li>

