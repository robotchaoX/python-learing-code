from distutils.core import setup

setup(name="message_pkg",  # 包名
      version="1.0",  # 版本
      description="itheima's 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="itheima",  # 作者
      author_email="itheima@itheima.com",  # 作者邮箱
      url="www.itheima.com",  # 主页
      py_modules=["message_pkg.send_message",
                  "message_pkg.receive_message"])

"""
# build 
python3 setup.py build

# distribute
python3 setup.py sdist

# install 
sudo python3 setup install

"""
