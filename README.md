HeapSort-FileProcessor
Description

A Python script that sorts numbers using the Heap Sort algorithm and identifies pairs of numbers that sum up to a specified target. The script processes data from input files, performing sorting and sum calculations, and outputs the results to corresponding files.
Features

    Heap Sort Algorithm: Efficiently sorts an array of numbers.
    Target Sum Finder: Identifies if two numbers in the sorted array sum up to a specified target.
    File Processing: Reads input data from files and writes sorted data and results to output files.

Getting Started
Prerequisites

    Python 3.x

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/HeapSort-FileProcessor.git

Navigate to the project directory:

bash

    cd HeapSort-FileProcessor

Usage

    Prepare your input files named as in1.txt, in2.txt, ..., containing the following format:

    arduino

<line 1: any content>
<line 2: target sum>
<line 3: space-separated list of integers>

Example:

mathematica

Example Input File
10
4 15 6 3 8 10

Run the script:

bash

python heap_sort_processor.py

The output files out1_sample_actual.txt, out2_sample_actual.txt, ..., will be generated with the following format:

mathematica

    <target sum>
    Before sorting
    SumOfK
    <original list of integers>

    After sorting
    SumOfK
    <sorted list of integers>

    Calculation O(N) in Lab1 after sorting
    <Yes/No based on whether two numbers sum up to the target>

    <if a pair is found>

Example Output

If the target is 10 and the input list is 4 15 6 3 8 10, the output might look like:

mathematica

10
Before sorting
SumOfK
4 15 6 3 8 10 

After sorting
SumOfK
3 4 6 8 10 15 

Calculation O(N) in Lab1 after sorting
Yes
4+6=10
