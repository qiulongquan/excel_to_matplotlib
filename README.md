```
这个世界从古至今一直是一个看颜值的世界。对于我们作报告，写文章时使用的图片，也是一样的。
一图胜千言，一张制作精美的图片，不仅能展示大量的信息，更能体现绘图者的水平、审美、与态度。
国内外多家 SCI ， EI 文章的审稿人，甚至说，一篇文章拿到手里，一眼扫过去，看看数据和图片，
就知道这篇文章值不值得发表，水平如何。由此观之，制作一张精美图片的意义，实在重大。

本程序使用 python 从 excel 读取数据，并使用 matplotlib 绘制成二维图像。
这一过程中，将通过一系列操作来美化图像对于需要书写实验报告，学位论文，发表文章，做PPT报告的学员具有较大价值。

实验知识点
使用xlrd扩展包读取excel数据
使用matplotlib绘制二维图像
美化图像，添加标注，注释，显示Latex风格公式，坐标点处透明化处理等技巧

实验环境
python3.6
numpy-1.14.5
matplotlib-2.2.2
xlrd-1.1.0

xlrd顾名思义，就是excel文件的后缀名.xl文件read的扩展包。这个包只能读取文件，不能写入。写入需要使用另外一个包。
但是这个包，其实也能读取.xlsx文件。 从excel中读取数据的过程比较简单，首先从xlrd包导入open_workbook，然后打开excel文件，
把每个sheet里的每一行每一列数据都读取出来即可。很明显，这是个循环过程。

from xlrd import open_workbook
x_data1=[]
y_data1=[]
wb = open_workbook('phase_detector.xlsx')
for s in wb.sheets():
    print('Sheet:',s.name)
    for row in range(s.nrows):
        print('the row is:',row)
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print(values)
        x_data1.append(values[0])
        y_data1.append(values[1])

打开excel文件后，首先对文件内的sheet进行循环，这是最外层循环；在每个sheet内，进行第二次循环，行循环；在每行内，进行列循环，这是第三层循环。
在最内层列循环内，取出行列值，复制到新建的values列表内，很明显，源数据有几列，values列表就有几个元素。我们例子中的excel文件有两列，
分别对应角度和DC值。所以在列循环结束后，我们将取得的数据保存到x_data1和y_data1这两个列表中。

```