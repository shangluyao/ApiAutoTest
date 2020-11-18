'''
数据库操作
1.数据卡从mysql换成sqlite，脚本不用改动，只需要改动caw里面的mysql。py以及这个文件
2.这部分访问到业务的数据库了，所以放在bow
'''
from ZongHe.caw import MySqlOp

def deleteUser(db,phone):
    '''
    根据手机号删除用户
    :param db: 一个字典存储数据库信息
    :param phone: 手机号
    :return:
    '''
    conn = MySqlOp.connect(db)  #链接数据库
    MySqlOp.execute(conn,f"delete from Member where MobilePhone= {phone};") #执行sql语句
    MySqlOp.disconnect(conn) #关闭数据库