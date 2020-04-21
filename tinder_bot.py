from random import randint
from time import sleep

from goto import with_goto
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TinderAutoSwipeBot():
    def __init__(self):
        self.driver = webdriver.Firefox()

    # Open New Browser window with Tinder Web
    def login(self):
        self.driver.get('https://tinder.com')
        # executor_url = self.driver.command_executor._url
        # session_id = self.driver.session_id
        # print(executor_url)
        # print(session_id)

    # Stop the Bot
    def stop(self):
        print('Stopping Bot')
        self.driver.close()

    # Like Profile
    def like(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
        print('Liking....')

    # Dislike Profile
    def dislike(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_LEFT)
        print('Disliking....')

    # Auto Swiping Functionality
    def auto_swipe(self):
        print('Auto Swiping Starts')
        random = randint(0, 5)
        likes = 0
        dislikes = 0
        while True:
            sleep(0.5)
            if random > 0:
                self.like()
                sleep(2)
                likes = likes + 1
                print('Liked - {}'.format(likes))
                random = random - 1
            else:
                self.dislike()
                sleep(2)
                dislikes = dislikes + 1
                print('Disliked - {}'.format(dislikes))
                random = randint(0, 5)


@with_goto
def main():
    # Call the Bot
    bot = TinderAutoSwipeBot()
    # Start Login Process
    bot.login()

    print('---------------------------------------------------------------------------------------')
    print('STEP 1: Kindly login to your Tinder account manually in newly open browser screen. '
          'Allow all required permission location, notification etc')
    print('STEP 2: One You done with login. Input Yes or 1 and Hit Enter Key')
    print('STEP 3: Enjoy! Auto Swiping :)')
    print('---------------------------------------------------------------------------------------')

    # Start the Auto Liking / Disliking
    label.begin
    answer = input("Have you logged in? (Yes | 1): ")
    if answer.lower() == '1' or answer.lower() == 'yes':
        bot.auto_swipe()
    else:
        print("Enter Correct Value: Yes or 1")
        goto.begin


if __name__ == '__main__':
    main()
