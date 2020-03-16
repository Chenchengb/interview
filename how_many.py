#此程序可输入纯数字或者字符串


def how_many_ways(digitarray):
    #将数字转化为字符串
    digitarray = str(digitarray)
    #如果第一位为0则去掉
    digitarray = digitarray.lstrip('0')
    #得到字符串长度
    length = len(digitarray)
    #如果长度为0或1则直接返回1
    if length == 0 or length == 1:
        return 1
    #按照数字长度创建一个列表,第一位改为1
    li = list(range(length+1))
    li[0] = 1
    #循环判断此数字的每个值
    for i in range(length+1):
        #使循环在i=0时正常往下运行
        if i == 0:
            continue
        #前一个数值不为0,则至少等于li[i-1]
        if digitarray[i-1] == '0':
            li[i] = 1
        else:
            li[i] = li[i-1]
        #判断当i>1时,当前数跟前一个数能否组成一个字母对应值
        num = int(digitarray[i-2])*10 + int(digitarray[i-1])
        if i > 1 and 10 <= num <=25:
            li[i] += li[i-2]
    return li[length]
print(how_many_ways('21199'))
#共计用时16分钟
