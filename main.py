'''
this is the judging program
author:JingChen
email:jingchen23@tongji.edu.cn
copyright 2016
'''

import time
import threading
import com_detect as Com_detect


def isTOK(new_transaction):    #this function is used to judge whether a transaction is safe or not

'''
把新交易的双方拎出来，直接到数据库里去查找他们的信任值，看是否大于阈值。
然后返回结果
'''


    result = 1
    
    return result

def update():                  #this function is used to update the graph and community information
    print ("this is 2")
    

t = time.time()

a = 0

t1 = threading.Thread(target = isTOK, args= a )
t2 = threading.Thread(target = update )

t1.start()
t2.start()

t1.join()
t2.join()

print ("done in :", time.time()-t)
'''
主函数应该包括两个函数，
g = load("F:\onedrive\工行项目\RandomGraph.gml",format="gml")
读取银行数据库
第一步
判断结果
第二步
看结果
返回是否通过信号

如果满足一定条件
重新计算第一步和第二步，更新文件

这个程序将一直循环，永不停息。
'''
