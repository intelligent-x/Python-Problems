"""
题目背景
输入三个自然数N，i，j （1<=i<=N，1<=j<=N），输出在一个N * N格的棋盘中（行列均从1开始编号），与格子（i，j）同行、同列、同一对角线的所有格子的位置。如： =4，i=2，j=3表示了棋盘中的第二行第三列的格子，如下图：

第一列	第二列	第三列	第四列
第一行			
(2,3)	第二行		
第三行			
第四行			
当n=4，i=2，j=3时，输出的结果是：
(2,1) (2,2) (2,3) (2,4)                        同一行上格子的位置
(1,3) (2,3) (3,3) (4,3)                        同一列上格子的位置
(1,2) (2,3) (3,4)                               左上到右下对角线上的格子的位置
(4,1) (3,2) (2,3) (1,4)                        左下到右上对角线上的格子的位置

输入输出格式
输入格式

一行，三个自然数N，i，j，相邻两个数之间用单个空格隔开。1 <= N <= 10。

输出格式

四行： 第一行：从左到右输出同一行格子位置；
第二行：从上到下输出同一列格子位置；
第三行：从左上到右下输出同一对角线格子位置；
第四行：从左下到右上输出同一对角线格子位置。

其中每个格子位置用如下格式输出：(x,y)，x为行号，y为列号，采用英文标点，中间无空格。相邻两个格子位置之间用单个空格隔开。
"""

info = input("请输入信息: ").split(" ")
n = int( info[0] )
i = int( info[1] )
j = int( info[2] )

print( n, i, j )

line1, line2, line3, line4 = "", "", "", ""

for x in range( 0, n ):
    line1 += "(" + format( i ) + "," + format( x + 1 ) + ") "

for y in range( 0, n ):
    line2 += "(" + format( y + 1 ) + "," + format( j ) + ") "

if i > j:
    for x in range( 0, n ):
        if 1 + x > n or i - j - 1 + x > n:
            break
        line3 += "(" + format( i - j + x + 1 ) + "," + format( 1 + x ) + ") "

elif i == j:
    for x in range( 0, n ):
        line3 += "(" + format( x + 1 ) + "," + format( x + 1 ) + ") "

else:
    for x in range( 0, n ):
        if 1 + x > n or j - i + x + 1 > n:
            break
        line3 += "(" + format( 1 + x ) + "," + format( j - i + x + 1 )+ ") "

print( line1, line2, line3, sep="\n" )