# _*_ coding : utf-8 _*_
# @Time : 2022/5/20 22:55
# @Author : Cosmica
# @File : eat
# @Project : Food
import random


def init_food_list():
    food_list = ["西区食堂 大可鱼酸菜鱼 鸡肉酸菜配饭 12.8元", "西区食堂 大可鱼酸菜鱼 海鲜蛋饺配饭 11.9元",
                 "西区食堂 大可鱼酸菜鱼 牛肉丸配饭 11.9元", "西区食堂 淇轩便当 干捞酱香拌面 11.9元",
                 "西区食堂 淇轩便当 干捞炸酱面 11.9元", "西区食堂 淇轩便当 酱香卤鸭肠 11.9元",
                 "西区食堂 淇轩便当 卤肉荷包蛋 11.9元", "西区食堂 淇轩便当 油炸香酥大猪排 12.8元",
                 "西区食堂 淇轩便当 青瓜炒火腿肠片 11.9元",
                 "西区食堂 淇轩便当 椒盐小酥肉 12.9元", "西区食堂 淇轩便当 奥尔良大鸡扒 12.8元",
                 "西区食堂 淇轩便当 冲量套餐 11.9元", "西区食堂 淇轩便当 (小份)香辣酸菜鸡配饭 11.9元",
                 "西区食堂 淇轩便当 (小份)番茄酸菜鸡配饭 11.9元", "西区食堂 自选特色套餐 绿色食饭 10.8元",
                 "西区食堂 自选特色套餐 套餐A 12.88元", "西区食堂 潮汕猪杂汤饭 牛肉丸+螃排配饭 11.9元",
                 "西区食堂 潮汕猪杂汤饭 黑椒脆皮肠 11.9元", "西区食堂 潮汕猪杂汤饭 炸香葱鱼羹 11.9元",
                 "西区食堂 卤友记 广式烧鸭饭 11.9元", "西区食堂 卤友记 红焖鸭肉饭 11.9元",
                 "西区食堂 卤友记 五香卤肉饭 11.9元", "西区食堂 卤友记 奥尔良鸡排饭 11.9元",
                 "西区食堂 麻辣香锅 鸡翅尖 11.9元", "西区食堂 麻辣香锅 精选牛肉 11.9元",
                 "西区食堂 麻辣香锅 精选瘦肉 11.9元", "西区食堂 麻辣香锅 精选牛肉+炸腐竹 11.9元",
                 "西区食堂 麻辣香锅 精选牛肉+波波肠 11.9元", "西区食堂 美极川湘菜馆 特惠双拼 11.99元",
                 "西区食堂 美极川湘菜馆 啤酒鸭 12.99元", "西区食堂 美极川湘菜馆 笋肉 12.99元",
                 "西区食堂 美极川湘菜馆 肉末茄子 11.9元", "西区食堂 美极川湘菜馆 手撕包菜肉丝饭 11.9元",
                 "西区食堂 港式烧腊 烧鸭饭 11.9元", "西区食堂 港式烧腊 卤水肉卷饭 10.8元",
                 "西区食堂 港式烧腊 奥尔良鸡排饭 11.0元", "西区食堂 港式烧腊 奥尔良烤鸡饭 11.9元",
                 "西区食堂 港式烧腊 蜜汁烤鸡翅饭 12.0元", "中区食堂 广州荷叶饭 黑椒鸡柳 11.9元",
                 "中区食堂 北京麻辣香锅",
                 "中区食堂 五谷渔粉 鲜香玉米粉 12.0元", "中区食堂 捌味芳麻辣烫 牛肉丸 11.8元",
                 "中区食堂 捌味芳麻辣烫 蟹排 12.8元", "中区食堂 捌味芳麻辣烫 香菇肠 11.8元",
                 "中区食堂 捌味芳麻辣烫 鸡肉丸 12.8元", "中区食堂 捌味芳麻辣烫 墨鱼丸 11.8元",
                 "中区食堂 F+牛肉饭 鸡扒滑蛋饭 12.0元",
                 "中区食堂 F+牛肉饭 鸡肉滑蛋饭 12.0元", "中区食堂 F+牛肉饭 腊味滑蛋饭 12.0元",
                 "东区食堂 汕头裸条汤 牛筋丸 11.9元", "东区食堂 汕头裸条汤 墨鱼丸 11.9元",
                 "东区食堂 汕头裸条汤 虾迷饺 11.9元", "东区食堂 汕头裸条汤 小猪肉丸 12.8元",
                 "东区食堂 汕头裸条汤 牛筋丸+潮汕肉卷 12.8元", "东区食堂 周记关东煮 鱼籽包 11.8元",
                 "东区食堂 周记关东煮 牛筋丸 11.8元", "东区食堂 周记关东煮 紫菜 12.8元",
                 "东区食堂 超级便当 美味鸡排 11.9元", "东区食堂 超级便当 土豆爆炒鸡肉丁 11.9元",
                 "东区食堂 超级便当 番茄滑蛋 11.9元", "东区食堂 超级便当 秘制鸡扒 11.9元",
                 "东区食堂 超级便当 香辣土豆片 11.9元", "东区食堂 超级便当 芝士爆浆鸡排 11.9元",
                 "东区食堂 魔饭 咖喱鸡肉饭 11.99元", "东区食堂 魔饭 孜然鸡肉饭 12.99元",
                 "东区食堂 魔饭 粤式手撕鸡套餐 12.99元", "东区食堂 魔饭 宫爆鸡丁套餐 12.99元",
                 "东区食堂 魔饭 肉末红烧茄子 11.99元", "美食城 五谷鱼粉 鸡蛋炒米粉 11.9元",
                 "美食城 五谷鱼粉 素五谷杂粮粉 11.9元", "美食城 五谷鱼粉 金汤五谷杂粮粉 11.9元",
                 "美食城 师姐石磨肠粉 鸡蛋蒸米粉 11.9元", "美食城 师姐石磨肠粉 蛋肉蒸米粉 11.9元",
                 "美食城 师姐石磨肠粉 鸡蛋蒸米粉 11.9元", "美食城 丼炙食堂 桂林香辣干捞米粉 11.99元",
                 "美食城 丼炙食堂 开心新鲜猪杂汤米粉 11.9元", "美食城 丼炙食堂 烧肉汁油豆腐肉末拌饭 11.9元",
                 "美食城 丼炙食堂 开心潮汕肉饼汤米粉 11.9元", "云餐厅 一日三餐 香菇肉酱盖饭 12.88元",
                 "云餐厅 一日三餐 土豆鸡丁盖饭 12.88元", "云餐厅 一日三餐 招牌大块卤肉饭 11.9元",
                 "云餐厅 一日三餐 卤汁鸡饭 11.9元", "云餐厅 沙县小吃 鸡蛋炒河粉 12.0元",
                 "云餐厅 明记肥肠鸡饭 明记卤肉卷饭 11.99元", "云餐厅 明记肥肠鸡饭 明记土豆排骨饭 11.99元",
                 "云餐厅 明记肥肠鸡饭 咖喱鸡饭 11.99元", "云餐厅 明记肥肠鸡饭 香菇炒肉饭 11.99元",
                 "云餐厅 明记肥肠鸡饭 卤猪头肉饭 11.99元", "云餐厅 美乐佳炸鸡汉堡 盲盒 12.88元",
                 "云餐厅 阿姨便当 自选双拼 11.99元", "云餐厅 粗茶淡饭 主食+副食 12.88元",
                 "云餐厅 舌尖上的炒粉 蛋+黑椒热狗 11.99元", "云餐厅 舌尖上的炒粉 蛋+自选配料 12.8元",
                 "云餐厅 最高鸡密 网红鸡排饭 12.88元", "云餐厅 日式拉面 日式杂菇拉面 12.8元",
                 "云餐厅 日式拉面 日式冬菇拉面 11.8元", "云餐厅 塔塔先生 香菇滑鸡 11.9元",
                 "云餐厅 塔塔先生 红烧茄子 11.9元", "云餐厅 塔塔先生 巴西炒肉片 11.9元"
                 ]
    return food_list


if __name__ == '__main__':
    print(init_food_list()[random.randint(0, len(init_food_list()) - 1)])
    print("Test")
    print("你好，世界！")
