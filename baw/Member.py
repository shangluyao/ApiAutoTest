'''
用户模块的接口（注册、登录、充值、用户列表、取现……）
'''

def register(url, baserequests, data):
    '''
    发送注册请求
    :param url:  http://jy001:8081/ ，是从环境文件中读取的。
    :param baserequests: 是BaseRequests的一个实例
    :param data: 注册接口的参数
    :return: 响应信息
    '''
    url = url + "futureloan/mvc/api/member/register"
    r = baserequests.post(url,data=data)
    return r

# 获取用户列表
def getList(url,baserequests):
    url = url + "futureloan/mvc/api/member/list"
    r = baserequests.get(url)
    return r

# 登录账号
def login(url,baserequests,data):
    url = url + "futureloan/mvc/api/member/login"
    r = baserequests.post(url,data=data)
    return r



# 测试代码，用完删除
if __name__ == '__main__':
    from ZongHe.caw.BaseRequests import BaseRequests

    aaa = BaseRequests()
    canshu = {"mobilephone":12323123, "pwd":132}
    r = register("http://jy001:8081/", aaa, canshu)
    print(r.json())