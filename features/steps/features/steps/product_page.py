from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_NOTICE = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")


@given('Open Amazon T&C page')
def open_amazon_TC_page(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/'))
    context.driver.refresh()


@given('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handler
    print('Original:', context.original_window)
    print('All windows:', context.driver.window_handles)

    @when('Click on Amazon Privacy Notice link')
    def click_on_amazon_privacy_notice_link(context):
        context.driver.find_element(*PRIVACY_NOTICE).click()

        @when('Switch to the newly opened window')
        def switch_newly_opened_window(context):
            context.driver.wait.until(EC.new_window_is_opened)
            all_windows = context.driver.windows_handle
            print('After window opened, all windows:', all_windows)
            context.driver.switch_to.window(all_windows[1])

            @when('Verify Amazon Privacy Notice page is opened')
            def verify_privacy_notice_opened(context):
                context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/'))

                @then('User can close new window')
                def close_new_window(context):
                    context.driver.close()
                    print('After window closed, all windows:', all_windows)

                    @then('switch back to original')
                    def switch_back_to_original(context):
                        context.driver.switch_to.window(context.original_window)
