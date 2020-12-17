import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, cart_page, order_page, order_confirmation_page


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(TestSettings.WEBDRIVER_CHROME_PATH)
        self.url = TestSettings.PAGE_URL
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_process(self):
        self.assertTrue(main_page.taps_logo_visible(self.driver))
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.approve_cart(self.driver)
        order_page.proper_fill_all_form_areas(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_confirmation_page.verify_order_confirmation_displayed(self.driver))


if __name__ == '__main__':
    unittest.main()