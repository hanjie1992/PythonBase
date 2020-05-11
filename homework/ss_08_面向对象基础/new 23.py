def knn_iris():
    """
    K-近邻算法
     鸢尾花数据集
    含有3个特征、150条记录、目标值为0、1、2
    :return:
    """
    #导包
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    #导入数据
    data_iris = load_iris()
    #将数据集划分为训练集和测试集
    x_train,x_test,y_train,y_test = train_test_split(
        data_iris.data,data_iris.target,test_size=0.25)
    #数据标准化处理
    stdScaler = StandardScaler().fit(x_train)
    x_trainStd = stdScaler.transform(x_train)
    x_testStd = stdScaler.transform(x_test)
    #使用KNeighborsClassifier函数构建knn模型
    knn_model = KNeighborsClassifier()
    knn_model.fit(x_trainStd,y_train)
    print("测试集准确率为：",knn_model.score(x_testStd,y_test))
    print("预测测试集前5个结果为：",knn_model.predict(x_testStd)[:5])
    
    
    