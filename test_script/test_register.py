'''
注册的测试脚本（pytest）
'''
import pytest
from ZongHe.baw import Member,DbOp
from ZongHe.caw import DataRead

# 测试前置：获取测试数据，数据是列表，通过readyaml读取来的
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_fail.yaml"))
def fail_data(request):  # 固定写法
    return request.param


# 注册失败
def test_register_fail(fail_data,url,baserequests):
    print(f"测试数据为：{fail_data['casedata']}")
    print(f"预期结果为：{fail_data['expect']}")
    r = Member.register(url,baserequests,fail_data['casedata'])
    # 检查结果
    assert r.json()['msg'] == fail_data['expect']['msg']
    assert r.json()['status'] == fail_data['expect']['status']
    assert str(r.json()['code']) == fail_data['expect']['code']


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_pass.yaml"))
def pass_data(request):  # 固定写法
    return request.param
# 注册成功
def test_register_pass(pass_data,url,db,baserequests):
    # print(f"测试数据为：{pass_data['casedata']}")
    # print(f"预测结果为：{pass_data['expect']}")
    phone = pass_data['casedata']['mobilephone']
    # 初始化环境，确保环境中没有影响本次执行的数据
    DbOp.deleteUser(db,phone)

    # 发送请求
    r = Member.register(url,baserequests,pass_data['casedata'])
    # 1.检查响应结果
    assert r.json()['msg'] == pass_data['expect']['msg']
    assert r.json()['status'] == pass_data['expect']['status']
    assert str(r.json()['code']) == pass_data['expect']['code']
   #检查实际有没有注册成功（1.查数据库 2.获取用户列表 3.用注册用户的登录

    r = Member.getList(url,baserequests)#获取用户列表
    assert phone in str(r.json())
    assert str(phone) in r.text #断言电话在用户列表中(同上）
    #清理环境，根据手机号删除注册用户
    DbOp.deleteUser(db,phone)


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_repeat.yaml"))
def repeat_data(request):  # 固定写法
    return request.param
# 重复注册
def test_register_repeat(repeat_data,url,db,baserequests):

    phone = repeat_data['casedata']['mobilephone']
    DbOp.deleteUser(db, phone)
    # 发送请求
    r = Member.register(url,baserequests,repeat_data['casedata'])
    # 再次发送请求
    r = Member.register(url, baserequests, repeat_data['casedata'])

    # 1.检查响应结果
    assert r.json()['msg'] == repeat_data['expect']['msg']
    assert r.json()['status'] == repeat_data['expect']['status']
    assert str(r.json()['code']) == repeat_data['expect']['code']
    DbOp.deleteUser(db, phone)







