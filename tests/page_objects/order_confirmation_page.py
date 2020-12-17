order_confirmation_header = '//*[@id="post-8"]/header/h1'


def verify_order_confirmation_displayed(driver_instance):
    elem = driver_instance.find_element_by_xpath(order_confirmation_header)
    elem.is_displayed()