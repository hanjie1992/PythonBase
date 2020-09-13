import random
LOVERS_DAY = "七夕节"  # 七夕节
MIDDLE_AUTUMN = "中秋节"  # 中秋节
NATIONAL_DAY = "国庆节"  # 国庆节

gifts = ["flower","chocolate","9.9 discount"]
class WangBill():
    def getPrice(self,number,unit,type,isCouple):
        price = number * unit
        if ((type == LOVERS_DAY) & (isCouple==1)):
            if (price >= 99):
                luck = random.randrange(len(gifts))
                print("恭喜获得",gifts[luck],"礼物一份")
            return price * 0.77
        if ((type == MIDDLE_AUTUMN) & price >399):
            return price - 100
        if ((type == NATIONAL_DAY)& price < 100):
            free = random.randrange(9)
            if (free == 0):
                return 0.0
            return price
a = WangBill()
print(a.getPrice(120,2,"七夕节",1))