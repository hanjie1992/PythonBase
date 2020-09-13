
"""
在一个软件村里,有一名资深「面向过程」程序员——老过,和一名「面向对象」信徒——阿对
同时受雇于一家店
有一天老板突发奇想,决定让这两名程序员进行一次比赛
"""
import random
LOVERS_DAY = "七夕节"  # 七夕节
MIDDLE_AUTUMN = "中秋节"  # 中秋节
NATIONAL_DAY = "国庆节"  # 国庆节

"""
1.写一个店里的收银程序，根据客人购买的商品单价和数量，生成
所购商品的价格

不一会，他俩都写出了几乎相同的代码
"""
class Bill():
    def getPrice(self,number,unit):
        price = number * unit
        return price

# a = Bill()
# print(a.getPrice(12,2))


"""
2.快七夕了，我们店要在七夕节对商品搞活动，所有商品打77折

老过看到新需求，微微一笑
"""
class GuoBill():
    def getPrice(self,number,unit,type):
        if (type == LOVERS_DAY):
            price = number * unit * 0.77
        else:
            price = number * unit
        return price
g = GuoBill()
print(g.getPrice(12,2,"七夕节"))
# 阿对决定让新的收银方式继承 Bill 类，先在 Bill 类中新增 discount 方法
# 普通的收费方式在 discount,​函数中直接返回价格,七夕节的收费方式则继承此类,
# 在 discount 函数中实现打 77折
class DuiBill():

    def discount(self,price):
        return price

    def getPrice(self, number, unit):
        price = number * unit
        return self.discount(price)

# a = DuiBill()
# print(a.getPrice(12,2))

class LoversDayPrice(DuiBill):
    def discount(self,price):
        return price * 0.77

a = LoversDayPrice()
print(a.getPrice(12,2))

"""
3. 现在我们需求增加，中秋节：购物满399减100
国庆节：购物总价100元以内1/10概率免单
吐槽归吐槽，老过在 getPrice 函数中，再次增加了条件判断
"""
class GuoBill():
    def getPrice(self,number,unit,type):
        price = number * unit
        if (type == LOVERS_DAY):
            return price * 0.77
        if ((type == MIDDLE_AUTUMN) & price >399):
            return price - 100
        if ((type == NATIONAL_DAY)& price < 100):
            free = random.randrange(9)
            if (free == 0):
                return 0.0
            return price
a = GuoBill()
print(a.getPrice(12,2,"国庆节"))

"""
看着越来越复杂的,Bill 类和 getPrice 方法,老过眉头紧锁,他深知事情远没有结束.
中秋和国庆一过,他还需要到这个复杂的类中,删掉打折的方法,天知道老板还会再提,什么天马行空的需求。
"""

"""
阿对收到新需求时,先是新增了中秋节支付类,再增加了国庆节支付类：
"""
class DuiBill():

    def discount(self,price):
        return price

    def getPrice(self, number, unit):
        price = number * unit
        return self.discount(price)

# a = DuiBill()
# print(a.getPrice(12,2))

class LoversDayPrice(DuiBill):
    def discount(self,price):
        return price * 0.77

class MiddleAutumePrice(DuiBill):
    def discount(self,price):
        if (price > 399):
            return price - 100
        return price

class NationalDayPrice(DuiBill):
    def discount(self,price):
        if (price < 100):
            free = random.randrange(9)
            if (free == 0):
                return 0.0
        return price

"""
4. 有一个好消息要告诉大家！当老板兴高采烈地说出这句话时。
老过和阿对都露出了心惊胆战的表情，这句话往往意味着要更改需求

在七夕节当天，凡是到本店来购物的情侣慢99元及以上的订单
随机附赠精美礼品一份[鲜花，巧克力，9.9元抵扣券]之前打77折的
活动也修改为仅限情侣参加
"""
gifts = ["flower","chocolate","9.9 discount"]
class GuoBill():
    def getPrice(self,number,unit,type,isCouple):
        price = number * unit
        if ((type == LOVERS_DAY) & (isCouple==1)):
            if (price >= 99):
                luck = random.randrange(len(gifts))
                print("恭喜获得",gifts[luck],"礼物一份")
            return price * 0.77
        return price
        if ((type == MIDDLE_AUTUMN) & price >399):
            return price - 100
        if ((type == NATIONAL_DAY)& price < 100):
            free = random.randrange(9)
            if (free == 0):
                return 0.0
            return price
a = GuoBill()
print(a.getPrice(120,2,"七夕节",1))

# 阿对打开了 LoversDayPrice 类
# 将其修改如下
class DuiBill():

    def discount(self,price):
        return price

    def getPrice(self, number, unit):
        price = number * unit
        return self.discount(price)

# a = DuiBill()
# print(a.getPrice(12,2))

class LoversDayPrice(DuiBill):
    gifts = ["flower", "chocolate", "9.9 discount"]
    def discount(self,price,isCouple):
        if (isCouple != 1):
            return price
        if (price > 99):
            luck = random.randrange(len(gifts))
            print("恭喜获得",gifts[luck],"礼物一份")
        return price * 0.77

class MiddleAutumePrice(DuiBill):
    def discount(self,price):
        if (price > 399):
            return price - 100
        return price

class NationalDayPrice(DuiBill):
    def discount(self,price):
        if (price < 100):
            free = random.randrange(9)
            if (free == 0):
                return 0.0
        return price