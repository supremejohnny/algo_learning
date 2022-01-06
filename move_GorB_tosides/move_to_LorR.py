# BBGGBBBG变成GGGBBBBB或者BBBBBGGG,看左B移动次数少还是左G移动次数少
# 这里移动只能相邻的两个字母移动

# 核心代码部分，想法是比如BBGGBBBG,我们把每个G的位置记下来，就是[0,0,2,3,0,0,0,7]，然后
# 我们知道这三个G只能在0,1,2的位置出现，因为只能相邻移动，那就把[2,3,7]-[0,1,2]算出来便是
# 最少的移动次数。同理，把移动B的次数也算出来，对比两个值，小者为先。
def move_char(strr):
    # 计算移动G的最少次数
    ans = 0

    # 这一整步是为了找到G的出现位置并打点
    str_aux = [0] * len(strr)
    cnt = 0
    while cnt < len(strr):
        if strr[cnt] == "G":
            tmp = cnt + 1
            str_aux[cnt] = tmp
        cnt += 1

    # 因为G的位置打过点了，那B是str_aux里面的0，其余的便为G
    b_show = str_aux.count(0)
    g_show = len(strr) - str_aux.count(0)

    # 为了对位相减，把所有的不相关内容删除(删掉0)
    n = 0
    while n < b_show:
        str_aux.remove(0)
        n += 1

    # pyhton不能list - list，所以写一个forloop对位相减
    for ele in range(0, g_show):
        ans += (str_aux[ele] - ele - 1)

    # 这一步开始计算B的最少移动次数
    ans2 = 0

    str_aux2 = [0] * len(strr)
    cnt2 = 0
    while cnt2 < len(strr):
        if strr[cnt2] == "B":
            tmp = cnt2 + 1
            str_aux2[cnt2] = tmp
        cnt2 += 1

    g_show2 = str_aux2.count(0)
    b_show2 = len(strr) - str_aux2.count(0)

    n2 = 0
    while n2 < g_show2:
        str_aux2.remove(0)
        n2 += 1

    for ele2 in range(0, b_show2):
        ans2 += (str_aux2[ele2] - ele2 - 1)

    # 最后带一次对比，判断哪种情况可以更好的fit
    if ans > ans2:
        return (ans2, "B")
    else:
        return (ans, "G")

# 测试方案5种，extreme，normal和side cases
test1 = "BGB"
test2 = "BGBB"
test3 = "BBGGBBBG"
test4 = "BBG"
test5 = ""
print("For case ", test1, " we want to swap all ", move_char(test1)[1], " to one side, we need at least move ", move_char(test1)[0], " time(s)")
print("For case ", test2, " we want to swap all ", move_char(test2)[1], " to one side, we need at least move ", move_char(test2)[0], " time(s)")
print("For case ", test3, " we want to swap all ", move_char(test3)[1], " to one side, we need at least move ", move_char(test3)[0], " time(s)")
print("For case ", test4, " we want to swap all ", move_char(test4)[1], " to one side, we need at least move ", move_char(test4)[0], " time(s)")
print("For case ", test5, " we want to swap all ", move_char(test5)[1], " to one side, we need at least move ", move_char(test5)[0], " time(s)")
print("All done!")
