<h2><ol>Sorting Algorithms</ol></h2>
<h3>Selection sort:</h3>
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

<h3>Bubble sort:</h3>
Time Complexity = O(n<sup>2</sup>)

<h4>Advantages:</h4>
<li>It does not require any additional memory space.</li>
<li>It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.</li>

<h4>Disadvantages:</h4>
<li>Bubble sort has a time complexity of O(n2) which makes it very slow for large data sets.</li>
<li>Bubble sort has almost no or limited real world applications.</li>

<h3>Insertion sort:</h3>
Time Complexity:
<li>Best case: O(n), If the list is already sorted, where n is the number of elements in the list.</li>
<li>Average case: O(n2), If the list is randomly ordered.</li>
<li>Worst case: O(n2), If the list is in reverse order.</li>

<h4>Advantages:</h4>
<li>Stable sorting algorithm.</li>
<li>Efficient for small lists and nearly sorted lists.</li>
<li>Space-efficient as it is an in-place algorithm.</li>
<li>Adoptive. the number of inversions is directly proportional to number of swaps. For example, no swapping happens for a sorted array and it takes O(n) time only.</li>

<h4>Disadvantages: </h4>
<li>Inefficient for large lists.</li>
<li>Not as efficient as other sorting algorithms (e.g., merge sort, quick sort) for most cases.</li>

<h4>Applications:</h4>
<li>The list is small or nearly sorted.</li>
<li>Simplicity and stability are important. </li>
<li>Used as a subroutine in Bucket Sort. </li>
<li>Can be useful when array is already almost sorted (very few inversions)</li>
