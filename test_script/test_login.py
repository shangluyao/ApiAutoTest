'''
登录测试脚本
'''
import pytest
from ZongHe.caw import DataRead
from ZongHe.baw import Member,DbOp



# @pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_pass.yaml"))
# def pass_data(request):
#     return request.param

@pytest.fixture(scope='module')
def a(url,db,baserequests):
    pass_data = {'mobilephone': 18686820596, 'pwd': 123456}

    phone = pass_data['mobilephone']
    # 初始化环境，确保环境中没有影响本次执行的数据
    DbOp.deleteUser(db,phone)
     # 发送请求
    r = Member.register(url,baserequests,{'mobilephone': 18686820596, 'pwd': 123456})

    yield
    DbOp.deleteUser(db, phone)


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_fail.yaml"))
def fail_data(request):
    return request.param
# 登录失败
def test_login_fail(fail_data,baserequests,url,a):
    # 发送登录请求
    r = Member.login(url,baserequests,fail_data['casedata'])
    assert r.json()['msg'] == fail_data['expect']['msg']
    assert r.json()['status'] == fail_data['expect']['status']
    assert str(r.json()['code']) == fail_data['expect']['code']

# 登录成功
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_pass.yaml"))
def pass_data(request):
    return request.param

def test_login_pass(pass_data,baserequests,url,a):
    # 发送登录请求
    r = Member.login(url,baserequests,pass_data['casedata'])
    assert r.json()['msg'] == pass_data['expect']['msg']
    assert r.json()['status'] == pass_data['expect']['status']
    assert str(r.json()['code']) == pass_data['expect']['code']






