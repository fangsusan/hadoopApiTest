import string
import random

def random_name(slen=10):
    """ 随机生成数字与字母的最多20位数字符串"""
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(slen):
      sa.append(random.choice(seed))
    return ''.join(sa)

def random_phone(slen=11):
    """ 随机生成数字11位手机号"""
    seed = "1234567890"
    sa = []
    for i in range(slen):
      sa.append(random.choice(seed))
    return ''.join(sa)

def random_password(slen=12):
    """ 随机生成数字,字母组合的最多12位密码"""
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(slen):
      sa.append(random.choice(seed))
    return ''.join(sa)





