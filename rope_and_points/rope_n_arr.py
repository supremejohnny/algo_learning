# 给出一个有序arr和一个绳长l，找到这根绳子能cover住多少个arr上的点
# 比如arr是[1,4,5,7,8,10,15],那ans就是[4,5,7,8],4个点
import random


# 随机生成list的方程，用于随机测试
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


# 代码核心
def find_pts(arr, rl):
    ans = 0

    # 这里的核心想法是从arr中遍历，以那个点为绳子末端，然后向前找l个数，生成一个辅助数组arr_aux去
    # 遍历，arr_aux里的element如果在arr中那就是绳子cover到了这个点，ans+1

    # uncomment 2个print即可看到遍历过程
    for ele in arr:
        ans_tmp = 0
        arr_tmp = range((ele - rl), ele + 1)
        # print(arr_tmp)
        for ele2 in arr_tmp:
            if ele2 in arr:
                ans_tmp += 1
                # print(ele,ele2,ans_tmp)
        if ans_tmp >= ans:
            ans = ans_tmp

    return ans


# 测试数组和随机数组
arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [1, 4, 5, 7, 8, 10, 15]
arr3 = [3]
l1 = 3
l2 = 4
l3 = 10
arr_rand = random_int_list(10, 1000, random.randint(10, 300))
l_rand = random.randint(10, 800)
print("The test array is ", arr1, "the rope length is ", l1, " and the most points the rope could cover is",
      find_pts(arr1, l1))
print("The test array is ", arr2, "the rope length is ", l2, " and the most points the rope could cover is",
      find_pts(arr2, l2))
print("The test array is ", arr3, "the rope length is ", l3, " and the most points the rope could cover is",
      find_pts(arr3, l3))
print("The random test array is ", arr_rand, "the rope length is ", l_rand,
      " and the most points the rope could cover is", find_pts(arr_rand, l_rand))
print("All done!")
