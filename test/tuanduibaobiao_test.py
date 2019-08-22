#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-21 下午5:08

# print(" ")执行后,默认换行,光标停留在下一行.
#
# 要让print(" ")执行输出后不换行,方法:print("XXXXX ",end=" ")
#
# 原因:print(" ")之所以换行是因为print里的字符串""的最后一个end为/n,即换行,要使其不换行,只需改变end即可


phone_data =[
    {
        "recharge": 170038.0,
        "withdraw": 126656.19,
        "consume": 2257196.75,
        "bonus": 2156669.26,
        "rebate": 593.33,
        "activity": 25190.44,
        "fee": 0.0,
        "profit": -74710.14,
        "balance": 3617.674,
        "field": "总计"
    },
    {
        "recharge": 0.0,
        "withdraw": 47414.0,
        "bonus": 0.0,
        "rebate": 592.21,
        "consume": 0.0,
        "activity": 25190.44,
        "fee": 0.0,
        "profit": 25799.54,
        "dividend": 10762.73,
        "balance": 1954.477,
        "field": "yatou1992",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 10.927,
        "field": "deng1215",
        "type": "agent",
        "member_level": 1920,
        "member_rebate": 6.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.248,
        "field": "ZQL6666",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 4000.0,
        "withdraw": 0.0,
        "bonus": 58783.46,
        "rebate": 1.12,
        "consume": 62791.4,
        "activity": 0.0,
        "fee": 0.0,
        "profit": -4006.82,
        "dividend": 0.0,
        "balance": 144.776,
        "field": "py0918",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 2.969,
        "field": "mzr888",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 7.15,
        "field": "lili568",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.004,
        "field": "h519519",
        "type": "agent",
        "member_level": 1970,
        "member_rebate": 8.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 6.461,
        "field": "WM1117",
        "type": "agent",
        "member_level": 1960,
        "member_rebate": 8.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 3.123,
        "field": "a438181076",
        "type": "agent",
        "member_level": 1960,
        "member_rebate": 8.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 1.368,
        "field": "jeep520",
        "type": "agent",
        "member_level": 1956,
        "member_rebate": 7.8
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 14.527,
        "field": "xj8898",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.471,
        "field": "qwm888",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.024,
        "field": "LXY6666",
        "type": "agent",
        "member_level": 1976,
        "member_rebate": 8.8
    },
    {
        "recharge": 900.0,
        "withdraw": 0.0,
        "bonus": 14454.92,
        "rebate": 0.0,
        "consume": 15354.95,
        "activity": 0.0,
        "fee": 0.0,
        "profit": -900.03,
        "dividend": 0.0,
        "balance": 0.018,
        "field": "ct9999",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.88,
        "field": "qqww168",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 18.88,
        "field": "lt17888",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 1.227,
        "field": "ww7890",
        "type": "agent",
        "member_level": 1986,
        "member_rebate": 9.3
    },
    {
        "recharge": 3200.0,
        "withdraw": 700.0,
        "bonus": 8602.69,
        "rebate": 0.0,
        "consume": 11113.2,
        "activity": 0.0,
        "fee": 0.0,
        "profit": -2510.51,
        "dividend": 0.0,
        "balance": 502.451,
        "field": "zhang520",
        "type": "agent",
        "member_level": 1956,
        "member_rebate": 7.8
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 679.157,
        "field": "jyh1314",
        "type": "agent",
        "member_level": 1950,
        "member_rebate": 7.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 22.426,
        "field": "yin4139",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 12.463,
        "field": "jyh668",
        "type": "agent",
        "member_level": 1950,
        "member_rebate": 7.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 162.486,
        "field": "yl0701",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 1000.0,
        "withdraw": 1852.19,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 16.69,
        "dividend": 0.0,
        "balance": 68.087,
        "field": "dandan888",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 400.0,
        "withdraw": 1000.0,
        "bonus": 3112.48,
        "rebate": 0.0,
        "consume": 2512.4,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 600.08,
        "dividend": 0.0,
        "balance": 0.817,
        "field": "a26233",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 160538.0,
        "withdraw": 75690.0,
        "bonus": 2071715.71,
        "rebate": 0.0,
        "consume": 2165424.8,
        "activity": 0.0,
        "fee": 0.0,
        "profit": -93709.09,
        "dividend": 0.0,
        "balance": 2.257,
        "field": "wushen666",
        "type": "agent",
        "member_level": 1970,
        "member_rebate": 8.5
    }
]


phone_data1 = [
    {
        "recharge": 170038.0,
        "withdraw": 126656.19,
        "consume": 2257196.75,
        "bonus": 2156669.26,
        "rebate": 593.33,
        "activity": 25190.44,
        "fee": 0.0,
        "profit": -74710.14,
        "balance": 3617.674,
        "field": "总计"
    },
    {
        "recharge": 0.0,
        "withdraw": 47414.0,
        "bonus": 0.0,
        "rebate": 592.21,
        "consume": 0.0,
        "activity": 25190.44,
        "fee": 0.0,
        "profit": 25799.54,
        "dividend": 10762.73,
        "balance": 1954.477,
        "field": "yatou1992",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 10.927,
        "field": "deng1215",
        "type": "agent",
        "member_level": 1920,
        "member_rebate": 6.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.248,
        "field": "ZQL6666",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 4000.0,
        "withdraw": 0.0,
        "bonus": 58783.46,
        "rebate": 1.12,
        "consume": 62791.4,
        "activity": 0.0,
        "fee": 0.0,
        "profit": -4006.82,
        "dividend": 0.0,
        "balance": 144.776,
        "field": "py0918",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 2.969,
        "field": "mzr888",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 7.15,
        "field": "lili568",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.004,
        "field": "h519519",
        "type": "agent",
        "member_level": 1970,
        "member_rebate": 8.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 6.461,
        "field": "WM1117",
        "type": "agent",
        "member_level": 1960,
        "member_rebate": 8.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 3.123,
        "field": "a438181076",
        "type": "agent",
        "member_level": 1960,
        "member_rebate": 8.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 1.368,
        "field": "jeep520",
        "type": "agent",
        "member_level": 1956,
        "member_rebate": 7.8
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 14.527,
        "field": "xj8898",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.471,
        "field": "qwm888",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.024,
        "field": "LXY6666",
        "type": "agent",
        "member_level": 1976,
        "member_rebate": 8.8
    },
    {
        "recharge": 900.0,
        "withdraw": 0.0,
        "bonus": 14454.92,
        "rebate": 0.0,
        "consume": 15354.95,
        "activity": 0.0,
        "fee": 0.0,
        "profit": -900.03,
        "dividend": 0.0,
        "balance": 0.018,
        "field": "ct9999",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.88,
        "field": "qqww168",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 18.88,
        "field": "lt17888",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 1.227,
        "field": "ww7890",
        "type": "agent",
        "member_level": 1986,
        "member_rebate": 9.3
    },
    {
        "recharge": 3200.0,
        "withdraw": 700.0,
        "bonus": 8602.69,
        "rebate": 0.0,
        "consume": 11113.2,
        "activity": 0.0,
        "fee": 0.0,
        "profit": -2510.51,
        "dividend": 0.0,
        "balance": 502.451,
        "field": "zhang520",
        "type": "agent",
        "member_level": 1956,
        "member_rebate": 7.8
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 679.157,
        "field": "jyh1314",
        "type": "agent",
        "member_level": 1950,
        "member_rebate": 7.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 22.426,
        "field": "yin4139",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 12.463,
        "field": "jyh668",
        "type": "agent",
        "member_level": 1950,
        "member_rebate": 7.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 162.486,
        "field": "yl0701",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 1000.0,
        "withdraw": 1852.19,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 16.69,
        "dividend": 0.0,
        "balance": 68.087,
        "field": "dandan888",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 400.0,
        "withdraw": 1000.0,
        "bonus": 3112.48,
        "rebate": 0.0,
        "consume": 2512.4,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 600.08,
        "dividend": 0.0,
        "balance": 0.817,
        "field": "a26233",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 160538.0,
        "withdraw": 75690.0,
        "bonus": 2071715.71,
        "rebate": 0.0,
        "consume": 2165424.8,
        "activity": 0.0,
        "fee": 0.0,
        "profit": -93709.09,
        "dividend": 0.0,
        "balance": 2.257,
        "field": "wushen666",
        "type": "agent",
        "member_level": 1970,
        "member_rebate": 8.5
    }
]

phone_data2 =[
    {
        "recharge": 170038.0,
        "withdraw": 126656.19,
        "consume": 2257196.75,
        "bonus": 2156669.26,
        "rebate": 593.33,
        "activity": 25190.44,
        "fee": 0.0,
        "profit": -74710.14,
        "balance": 3617.674,
        "field": "总计"
    },
    {
        "recharge": 0.0,
        "withdraw": 47414.0,
        "bonus": 0.0,
        "rebate": 592.21,
        "consume": 0.0,
        "activity": 25190.44,
        "fee": 0.0,
        "profit": 25799.54,
        "dividend": 10762.73,
        "balance": 1954.477,
        "field": "yatou1992",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 10.927,
        "field": "deng1215",
        "type": "agent",
        "member_level": 1920,
        "member_rebate": 6.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.248,
        "field": "ZQL6666",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 4000.0,
        "withdraw": 0.0,
        "bonus": 58783.46,
        "rebate": 1.12,
        "consume": 62791.4,
        "activity": 0.0,
        "fee": 0.0,
        "profit": -4006.82,
        "dividend": 0.0,
        "balance": 144.776,
        "field": "py0918",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 2.969,
        "field": "mzr888",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 7.15,
        "field": "lili568",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.004,
        "field": "h519519",
        "type": "agent",
        "member_level": 1970,
        "member_rebate": 8.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 6.461,
        "field": "WM1117",
        "type": "agent",
        "member_level": 1960,
        "member_rebate": 8.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 3.123,
        "field": "a438181076",
        "type": "agent",
        "member_level": 1960,
        "member_rebate": 8.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 1.368,
        "field": "jeep520",
        "type": "agent",
        "member_level": 1956,
        "member_rebate": 7.8
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 14.527,
        "field": "xj8898",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.471,
        "field": "qwm888",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.024,
        "field": "LXY6666",
        "type": "agent",
        "member_level": 1976,
        "member_rebate": 8.8
    },
    {
        "recharge": 900.0,
        "withdraw": 0.0,
        "bonus": 14454.92,
        "rebate": 0.0,
        "consume": 15354.95,
        "activity": 0.0,
        "fee": 0.0,
        "profit": -900.03,
        "dividend": 0.0,
        "balance": 0.018,
        "field": "ct9999",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 0.88,
        "field": "qqww168",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 18.88,
        "field": "lt17888",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 1.227,
        "field": "ww7890",
        "type": "agent",
        "member_level": 1986,
        "member_rebate": 9.3
    },
    {
        "recharge": 3200.0,
        "withdraw": 700.0,
        "bonus": 8602.69,
        "rebate": 0.0,
        "consume": 11113.2,
        "activity": 0.0,
        "fee": 0.0,
        "profit": -2510.51,
        "dividend": 0.0,
        "balance": 502.451,
        "field": "zhang520",
        "type": "agent",
        "member_level": 1956,
        "member_rebate": 7.8
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 679.157,
        "field": "jyh1314",
        "type": "agent",
        "member_level": 1950,
        "member_rebate": 7.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 22.426,
        "field": "yin4139",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 12.463,
        "field": "jyh668",
        "type": "agent",
        "member_level": 1950,
        "member_rebate": 7.5
    },
    {
        "recharge": 0.0,
        "withdraw": 0.0,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 0.0,
        "dividend": 0.0,
        "balance": 162.486,
        "field": "yl0701",
        "type": "agent",
        "member_level": 1990,
        "member_rebate": 9.5
    },
    {
        "recharge": 1000.0,
        "withdraw": 1852.19,
        "bonus": 0.0,
        "rebate": 0.0,
        "consume": 0.0,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 16.69,
        "dividend": 0.0,
        "balance": 68.087,
        "field": "dandan888",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 400.0,
        "withdraw": 1000.0,
        "bonus": 3112.48,
        "rebate": 0.0,
        "consume": 2512.4,
        "activity": 0.0,
        "fee": 0.0,
        "profit": 600.08,
        "dividend": 0.0,
        "balance": 0.817,
        "field": "a26233",
        "type": "agent",
        "member_level": 1980,
        "member_rebate": 9.0
    },
    {
        "recharge": 160538.0,
        "withdraw": 75690.0,
        "bonus": 2071715.71,
        "rebate": 0.0,
        "consume": 2165424.8,
        "activity": 0.0,
        "fee": 0.0,
        "profit": -93709.09,
        "dividend": 0.0,
        "balance": 2.257,
        "field": "wushen666",
        "type": "agent",
        "member_level": 1970,
        "member_rebate": 8.5
    }
]

# for item in phone_data:
#     print("profit=%s,recharge=%s,field=%s,bonus=%s,consume=%s"%(item["profit"],item["recharge"],item["field"],item["bonus"],item["consume"]))
i=0
consume = 0
bonus = 0
profit=0
for item in phone_data2:
    i=i+1

    print("number:%s---field=%s,recharge=%s,profit=%s,bonus=%s,consume=%s" % (i,
    item["field"], item["recharge"], item["profit"], item["bonus"], item["consume"]))
    if i>1:
        profit = profit+item["profit"]
        consume=consume+item["consume"]
        bonus=bonus+item["bonus"]

print("profit",profit,"consume",consume,"bonus",bonus)