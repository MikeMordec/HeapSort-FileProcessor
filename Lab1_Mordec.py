def heapify(arr, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2
	if l < n and arr[i] < arr[l]:
		largest = l
	if r < n and arr[largest] < arr[r]:
		largest = r
	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i]) 
		heapify(arr, n, largest)

def heapSort(arr):
	n = len(arr)
	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)
	for i in range(n - 1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i]) 
		heapify(arr, i, 0)

for num in range(1,6):
    input_filename = "in"+str(num)+".txt"
    output_filename = "out"+str(num)+"_sample_actual.txt"
    print(input_filename)
    print(output_filename)
    file = open(input_filename)
    file_out = open(output_filename,'w')
    linesRaw = file.readlines()
    if(len(linesRaw)>=3):
        lines = []
        for line in linesRaw:
            lines.append(line.strip())
        target = int(lines[1])
        words = lines[2].split()
        nums = []
        for word in words:
            nums.append(int(word))
        file_out.write(str(target)+"\r\n")
        file_out.write("Before sorting\r\n")
        file_out.write("SumOfK\r\n")
        for num in nums:
            file_out.write(str(num)+" ")
        file_out.write("\r\n")
        heapSort(nums)
        file_out.write("After sorting\r\n")
        file_out.write("SumOfK\r\n")
        for num in nums:
            file_out.write(str(num)+" ")
        file_out.write("\r\n")    
        file_out.write("Calculation O(N) in Lab1 after sorting\r\n")    
        dub="No"
        for num in nums:
            if(int(target)>1):
                dub="Yes"        
        file_out.write(dub+"\r\n")
        p1 = 0
        p2 = len(nums)-1
        while(p1!=p2 and nums[p1]+nums[p2]!=target):
            if(nums[p2]>target):
                p2=p2-1
            else:
                p1=p1+1
        if(nums[p1]+nums[p2]==target):
            file_out.write(str(nums[p1])+"+"+str(nums[p2])+"="+str(target)+"\r\n")
            print("FOUND")  