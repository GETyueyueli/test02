from unittest import TestCase
from requests import Response
import app
import json
import logging

app.init_logging()


def assert_utils(self, response, status_code, success, code, message):
    """
    @type self:TestCase
    @type response: Response
    """
    jsonData = response.json()  # type: dict
    # 断言
    # HTTP相应状态吗
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(success, jsonData.get("success"))
    self.assertEqual(code, jsonData.get("code"))
    self.assertIn(message, jsonData.get("message"))


def read_login_data():
    # 读取登陆数据
    data_path = app.BASE_DIR + "/data/login_data.json"
    with open(data_path, encoding='utf-8') as f:
        jsonData = json.load(f)
        login_data_list = []
        for login_data in jsonData:
            # logging.info("登陆数据为：{}".format(login_data))
            mobile = login_data.get("mobile")
            password = login_data.get("password")
            status_code = login_data.get("status_code")
            success = login_data.get("success")
            code = login_data.get("code")
            message = login_data.get("message")
            login_data_list.append((mobile, password, status_code, success, code, message))
        logging.info("读取后，返回的登陆数据列表为： {}".format(login_data_list))

    return login_data_list


def read_emp_add():
    # 读取添加员工的数据
    data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(data_path, encoding='utf-8') as f:
        jsonData = json.load(f)
        logging.info("jsonData {}".format(jsonData))
        add_emp_data = jsonData.get("emp_add")
        add_emp_data_list = []
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        status_code = add_emp_data.get("status_code")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        add_emp_data_list.append((username, mobile, status_code, success, code, message))
    logging.info("读取到的添加员工的数据为：{}".format(add_emp_data_list))
    return add_emp_data_list


if __name__ == '__main__':
    # read_login_data()
    read_emp_add()
