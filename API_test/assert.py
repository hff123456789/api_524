class Assert():
    self.pass_result = {
        'code': 0,
        'response_code': self.response_data.status_code,
        'response_reason': self.response_data.reason,
        'response_headers': self.response_data.headers,
        'response_body': self.response_data.text,
        'message': '测试用例执行通过',
        'check_result': True
    }
    self.fail_result = {
            'code': 2,
            'response_code': self.response_data.status_code,
            'response_reason': self.response_data.reason,
            'response_headers': self.response_data.headers,
            'response_body': self.response_data.text,
            'message': '测试用例断言失败，测试用例执行不通过',
            'check_result': False
        }
    self.pass_result

    def __none_check(self):
        logger.info("断言类型[none]-->不进行断言操作，本次断言操作通过")
        return self.pass_result

    def __key_check(self, check_data):
        """
        检查json类型的响应body中是否包含一个或多个key
        :param check_data: 检查数据字符串
        :return:都包含则返回True； 有一个不包含就返回False
        """
        key_list = check_data.split(',')
        tmp_result = []
        for check_key in key_list:
            if check_key in self.response_data.json().keys():
                tmp_result.append(True)
            else:
                tmp_result.append(False)
        if False in tmp_result:
            error_message = '断言类型[json_key]-->实际结果：%s ；期望结果：%s 不相符，断言失败' % (self.response_data.text, check_data)
            logger.error(error_message)
            self.fail_result["message"] = error_message
            return self.fail_result
        else:
            pass_message = '断言类型[json_key]-->实际结果：%s ；期望结果：%s 相符，断言通过' % (self.response_data.text, check_data)
            logger.info(pass_message)
            self.pass_result["message"] = pass_message
            return self.pass_result

        def __key_value_check(self, check_data):
            """
            检查json类型的响应body中是否包含一个或多个键值对
            :param check_data:检查数据字符串
            :return:都包含则返回True； 有一个不包含就返回False
            """
            key_value_dict = json.loads(check_data)
            tmp_result = []
            for key_value in key_value_dict.items():
                if key_value in self.response_data.json().items():
                    tmp_result.append(True)
                else:
                    tmp_result.append(False)
            if False in tmp_result:
                error_message = '断言类型[json_key_value]-->实际结果：%s ；期望结果：%s 不相符，断言失败' % (
                self.response_data.text, check_data)
                logger.error(error_message)
                self.fail_result["message"] = error_message
                return self.fail_result
            else:
                pass_message = '断言类型[json_key_value]-->实际结果：%s ；期望结果：%s 相符，断言通过' % (self.response_data.text, check_data)
                logger.info(pass_message)
                self.pass_result["message"] = pass_message
                return self.pass_result

        def __body_regexp_check(self, check_data):
            if re.findall(check_data, self.response_data.text):
                pass_message = '断言类型[body_regexp]-->实际结果：%s ；期望结果：%s 相符，断言通过' % (self.response_data.text, check_data)
                logger.info(pass_message)
                self.pass_result["message"] = pass_message
                return self.pass_result
            else:
                error_message = '断言类型[body_regexp]-->实际结果：%s ；期望结果：%s 不相符，断言失败' % (self.response_data.text, check_data)
                logger.error(error_message)
                self.fail_result["message"] = error_message
                return self.fail_result

            def __response_code_check(self, check_data):
                if self.response_data.status_code == int(check_data):
                    pass_message = '断言类型[response_code]-->实际结果：%s ；期望结果：%s 相符，断言通过'
                    logger.info(pass_message)
                    self.pass_result["message"] = pass_message
                    return self.pass_result
                else:
                    error_message = '断言类型[response_code]-->实际结果：%s ；期望结果：%s 不相符，断言失败'
                    logger.error(error_message)
                    self.fail_result["message"] = error_message
                    return self.fail_result