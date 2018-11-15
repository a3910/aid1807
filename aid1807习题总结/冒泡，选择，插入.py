#Python 冒泡，选择，插入排序使用实例
#选择排序
def selection_sort(list2):
    for i in range(0, len(list2)-1):
        min_ = i
        for j in range(i + 1, len(list2)):
            if list2[j] < list2[min_]:
                min_ = j
        list2[i], list2[min_] = list2[min_], list2[i]  # swap
    return list2


list2 = [1, 2, 4, 7, 6, 999, 233, 666, 5, 3]
print(selection_sort(list2))

list2 = [1, 3, 2, 4, 5, 7, 9, 8, 6, 888, 123]
print(selection_sort(list2))

list2 = [1, 2, 4, 5, 3]
print(selection_sort(list2))

list2 = [1, 2, 4, 3, 5]
print(selection_sort(list2))


def selection_sort(seq):
    for i in range(len(seq)):
        position = i
        for j in range(i,len(seq)):
            if seq[position] > seq[j]:
                position = j
        if position != i:
                tmp = seq[position]
                seq[position] = seq[i]
                seq[i] = tmp
    return seq


seq=[1,3,2,5,6,4,7,0]
print(selection_sort(seq))


#插入排序
def insertion_sort(seq1):
    if len(seq1) > 1:
        for i in range(1,len(seq1)):
            while i > 0 and seq1[i] < seq1[i-1]:
                tmp = seq1[i]
                seq1[i] = seq1[i-1]
                seq1[i-1] = tmp
                i = i - 1
        return seq1
if __name__ == '__main__':
    seq1=[1,3,2,5,6,4,7,0]
    selection_sort(seq1)

#冒泡排序
def bubble(bubbleList):
    listLength = len(bubbleList)
    while listLength > 0:
        for i in range(listLength - 1):
            if bubbleList[i] > bubbleList[i+1]:
                bubbleList[i] = bubbleList[i] + bubbleList[i+1]
                bubbleList[i+1] = bubbleList[i] - bubbleList[i+1]
                bubbleList[i] = bubbleList[i] - bubbleList[i+1]
        listLength -= 1
    print(bubbleList)
 
if __name__ == '__main__':
    bubbleList = [1,3,2,5,6,4,7,0]
    bubble(bubbleList)
