# 使用 `kMeans聚类` 算法实现日志分类v1.0
- 处理步骤：
1. 加载及提取数据模块：
    >首先提取出每条日志中 `content` 的内容，然后以使用求出`content中的第一个词所含的字符的ASCII码的数值和` 和 `content所有字符的ASCII码的数值和`，以此构建出一个 `n×2` 的二维数组（array）（n为日志条数）
2. 使用 `kMeans聚类` 算法处理模块：
    >对应不同的日志信息，可以将聚类的质心 `k` 设为对应于该种日志的模板数，然后使用上诉二元组进行欧氏距离计算并更新质心和数据的标签值，直到每条数据不再改变其所属类别为止。
3. 使用 `matplotlib` 绘制数据分类图
- 所选取特征：
1. `content` 中的第一个词所含的字符的ASCII码的数值和
2. `content` 所有字符的ASCII码的数值和
    - eg. instruction cache parity error corrected
        1. featur1: instruction ——> 1218
        2. feature2: instruction cache parity error corrected ——> 3892
- 聚类结果图如下：（使用BGL_2k.log作为加载文件，由其模板文件知共120中日志类型，这里即将 `kMeans算法` 的质心设为120个）
![1ONsPO.png](https://s2.ax1x.com/2020/02/13/1ONsPO.png)
部分细节图：
![1OUrmn.png](https://s2.ax1x.com/2020/02/13/1OUrmn.png)

- Reference
1. > [Python-画图（散点图scatter、保存savefig）及颜色大全](https://blog.csdn.net/w576233728/article/details/86538060)

