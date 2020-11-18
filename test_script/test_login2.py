'''
测试登录功能
'''
import pytest
from  ZongHe.caw  import DataRead
from ZongHe.baw import Member,DbOp

@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_data.yaml"))
def login_data(request):
    return request.param
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_setup.yaml"))
def setup_data(request):
    return request.param
#测试前置和后置
@pytest.fixture()
def register(setup_data,url,db,baserequests):
    # 注册
    phone = setup_data['casedata']['mobilephone']
    # 初始化环境，确保环境中没有影响本次执行的数据
    DbOp.deleteUser(db, phone)
    # 发送请求
    Member.register(url, baserequests,setup_data['casedata'])
    yield
    DbOp.deleteUser(db, phone)


def test_login(login_data,url,baserequests,register):
    # 登录
    # 检查登录结果
    r = Member.login(url,baserequests,login_data['casedata'])
    assert r.json()['msg'] == login_data['expect']['msg']
    assert r.json()['status'] == login_data['expect']['status']
    assert str(r.json()['code']) == login_data['expect']['code']


