import time
class addtocart1():

    def __init__(self, driver):
        self.driver = driver

        # These are the three locators on this page
        self.Practice_site_button_xpath = "//a[contains(text(),'Practice Site')]"
        self.add_to_basket_xpath = "//li[contains(@class,'post-163 product type-product status-publish has-post-thumbnail product_cat-html product_tag-html has-post-title no-post-date has-post-category has-post-tag has-post-comment has-post-author first instock sale downloadable taxable shipping-taxable purchasable product-type-simple')]//a[contains(@class,'button product_type_simple add_to_cart_button ajax_add_to_cart')][contains(text(),'Add to basket')]"
        self.view_basket_xpath = "//a[contains(@class,'added_to_cart wc-forward')]"
        self.proceed_to_checkout_xpath = "//a[contains(@class,'checkout-button button alt wc-forward')]"



    def Practice_site(self):

        time.sleep(5)
        self.driver.find_element_by_xpath(self.Practice_site_button_xpath).click()
        time.sleep(5)

    def addtoCart(self):

        self.driver.find_element_by_xpath(self.add_to_basket_xpath).click()
        self.driver.find_element_by_xpath(self.view_basket_xpath).click()
        self.driver.find_element_by_xpath(self.proceed_to_checkout_xpath).click()

