# Closure.py

def analyse(U, x, F):
    """分析属性组合x关于函数依赖集F+的闭包，其中U为属性集合"""
    last_x = x

    tempWs = []
    for func in F:
        if func[0] in x:
            tempWs.append(func[1])

    # 以下处理是为了在每一层迭代中，连接找出来符合条件的属性集合
    Ws = ""
    for i in tempWs:
        if i not in x:
            Ws += i
    x+=Ws
    # x = standardizeAttrX(x)     # 每一次迭代相当于接受一次新的用户输入，也需要对X进行标准化
    x = removeRepetition(x)     # 每一次迭代都得到一个过程量，性质等同于结果，会出现重复属性字符情况，可以去除重复符号，该方法包括重新排列，所以可以略去前一步
    print(x)

    if x != last_x and x != U:
        x = analyse(U, x, F)

    return x


def removeRepetition(x_result):
    """考虑到算法处理可能会出现结果中有重复属性符号的情况（猜测），如‘ABCCDE’，该方法将去除其中（可能存在的）重复符号"""
    x_set = set(x_result)
    x_pureList = []
    for i in x_set:
        x_pureList.append(i)
    x_pureList.sort()

    x_pureResult = ""
    for item in x_pureList:
        x_pureResult += item

    return x_pureResult


def standardizeFuncLists(func_list):
    """考虑到函数依赖集的决定因素v可能存在顺序不一致问题，如AB属性组合有AB或是BA两种表示形式，利用standardizeFuncLists
    将函数依赖集F中所有的决定因素转换为标准形式，即属性集符号按ASCII码值排列"""
    for function in func_list:
        if len(function[0]) > 1:
            tempAttrs = []
            for attribute in function[0]:
                tempAttrs.append(attribute)
            tempAttrs.sort()
            function[0] = ""
            for tempAttr in tempAttrs:
                function[0] += tempAttr # 单独更改了相应函数依赖的决定因素

    return func_list


def standardizeAttrX(x):
    """考虑到用户输入可能存在属性组合顺序不一致问题，利用standardizeAttrX方法
    将用户输入的决定因素x转换为标准形式，即属性集符号按ASCII码值排列"""
    attrX = []
    for attr in x:
        attrX.append(attr)
    attrX.sort()

    str_attrX = ""
    for attr in attrX:
        str_attrX += attr

    return str_attrX


def stringU(U):
    """转换用户输入字符串的形式，接受参数-以逗号隔开的属性集合，返回属性符号直接连接的字符串形式
    U = stringU("A,B,C,D,E"),U将赋值为stringU()方法返回的'ABCDE'"""
    UList = U.split(",")
    stringU = ""
    for string in UList:
        stringU += string

    return stringU


def funcLists(F):
    """将函数依赖字符串，转换为列表，其中每个元素为一个长度为2的列表，列表第一个元素为决定因素X，第二个元素代表被决定属性Y
    主函数可以通过 func_lists = funcList("AB->C,B->D,C->E,EC->B,AC->B")调用函数，并将返回的函数依赖列表赋给func_lists。
    此时funcLists为[['AB', 'C'], ['B', 'D'], ['C', 'E'], ['EC', 'B'], ['AC', 'B']]"""
    attachList = F.split(",")
    func_lists = []
    for attach in attachList:
        temp = attach.split("->")
        func_lists.append(temp)
    return func_lists


def main():
    U = input("请参照'A,B,C,D,E',输入关系模式的属性集合U：")
    F = input("请参照格式'AB->C,B->D,C->E,EC->B,AC->B',输入关系模式的函数依赖集F: ")
    strU = stringU(U)                                   # 将用户输入的属性集合字符串，转换为程序所属的字符串形式
    func_list = funcLists(F)                            # 将用户输入的函数依赖集字符串，转换为以列表形式表示
    stdFunc_list = standardizeFuncLists(func_list)      # 进一步处理函数依赖集，使得以列表形式存储的函数依赖的决定因素v按照属性符号的顺序排列，如,将[['EC','D']]转化为[['CE','D']]

    x = standardizeAttrX(input("请输入决定因素属性x: "))               # 对用户输入的决定因素属性组合x进行标准化，如，将"BA"转化为"AB"
    result = removeRepetition(analyse(strU,x,stdFunc_list))         # 对于analyse()方法返回的结果，其中可能存在属性符号重复的情况，做去除处理，最终产生可靠、形式简明的结果

    print("\n对于R<U,F>，U=({0})，F=({1})".format(U,F))
    print("决定因素{0}关于函数依赖集F的闭包为{1}".format(x,result))


if __name__ == '__main__':
    main()

# A->B,A->C,CG->H,CG->I,B->H