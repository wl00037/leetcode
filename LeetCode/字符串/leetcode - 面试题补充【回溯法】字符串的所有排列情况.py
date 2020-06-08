#   leetcode中该类型题目有两道：
#   1、面试题 08.07. 无重复字符串的排列组合
#   2、面试题 08.08. 有重复字符串的排列组合

#   示例：
#   给出字符串 s = "abc"，得到所有的排列情况如下：['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

#   先分析一下全排列题目中对于回溯法三个重点的解析：
#   1、当前递归层可选则的内容：从上层传入的，上层剩下未选择的元素，就是本层可选的；
#   2、当前递归层次已选择的内容：从上层未传入的元素每一个都可以作为本层已选择的元素，然后再传入下一层递归
#   3、递归的出口：当上层传入的上层未选择的字符串为空，也就是说都选了，那么就可以跳出递归了；


def backtrack(S, path):        #   从当前的S中进行选择，path是当前已经选了的；
    if S == '':             #   结束条件，可以将全路径放到res中了
        res.append(path)
        return
    for i in range(len(S)):
        backtrack(S[:i] + S[i + 1:], path+S[i])

S = 'abc'
path = ''
res = []
backtrack(S, path)
print(res)