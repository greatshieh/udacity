![title](./rossmann_banner2.png
)
# Udacity MAND
# 毕业项目开题报告

谢伟
2018年3月14日

### Rossmann商店销量预测

## 项目背景
Rossmann在7个欧洲国家经营着3000多家药店。目前，Rossmann门店经理的任务是提前6周预测他们的日销量。商店的销售受到许多因素的影响，包括促销、竞争、学校和州假日、季节性和地点。由于成千上万的个人经理根据他们独特的情况预测销售，结果的准确性可能会非常不同。<br>
可靠的销售预测使商店经理能够制定有效的员工时间表，提高工作效率和积极性。通过帮助Rossmann创建一个健壮的预测模型，您将帮助商店经理专注于对他们来说最重要的事情:他们的客户和他们的团队!

## 问题描述
根据Rossmann给出的历史销售数据，提前6周预测他们的日销量，帮助门店经理制定更有效的员工时间表。
## 数据集
* 文件<br>
    - train.csv - 包含销售信息的历史数据，用于模型训练<br>
    - test.csv - 不包含销售信息的历史数据，用于模型测试<br>
    - store.csv - 有关商店的补充信息
* 数据描述
    - Id - 测试集中表示商店信息的id
    - store - 每个商店的唯一id
    - Sales - 指定日期的销售额
    - Customers - 指定日期中的顾客数量
    - Open - 商店是否营业，0=不营业，1=营业
    - StateHoliday - 是否为国家法定假期， a=公共假期， b=东部假期， c=圣诞节， 0=不是假期
    - SchoolHoliday - 附近的学校是否对商店有影响
    - StoreType - 一共有四种商店类型，分别是a，b，c，d
    - Assortment - 描述分类水平，包括a = basic, b = extra, c = extended
    - CompetitionDistance - 附近最近竞争对手商店的距离
    - CompetitionOpenSince[Month/Year] - 附近最近竞争对手的开业时间
    - Promo - 在给定日期中，商店是否有促销
    - Promo2 - 是否参与连续促销活动。0：没有参与，1：参与
    - Promo2Since[Year/Week] - 连续促销活动开始的时间
    - PromoInterval - 每轮连续促销活动开始的时间，比如"Feb,May,Aug,Nov"表示每一轮连续促销开始的时间是"Feb，May，Aug，Nov"

## 解决方案

## 基准模型

## 评估指标

## 项目设计
