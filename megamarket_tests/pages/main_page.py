from selene import browser, be, have
from megamarket_tests.data.data_cards import Texts

import allure
import time


class MainPage:
    def __init__(self):
        self.search_input = browser.element('[class*=search-field-input]')
        self.basket = browser.element('[class*=cart__info]')

    def open_url(self):
        with allure.step("Открываем главную страницу"):
            browser.open('/')
        time.sleep(2)

    def search(self, value):
        with allure.step(f"Ищем товар {value}"):
            self.search_input.type(value).press_enter()

    def result_by_name(self, card_name, brand_name, card_article):
        with allure.step(f"Отображается товар с наименованием {card_name}"):
            browser.element(f'[data-product-id="{card_article}"] a').should(
                have.attribute('aria-label', f'{card_name} {brand_name}'))

    def result_by_article(self, card_article):
        with allure.step(f"Отображается товар с артикулом {card_article}"):
            browser.element('#data-product-id').should(have.text(card_article))

    def no_result(self):
        with allure.step(f"Отображается строка {Texts.nothing_found}"):
            browser.element('.not-found-search__text').should(have.text(Texts.nothing_found))

    def add_item_to_cart(self, card_article):
        with allure.step("Наводим курсор на товар"):
            browser.element(f'[data-product-id="{card_article}"]').hover()
        with allure.step("Нажимаем 'Купить'"):
            browser.element(f'[data-product-id="{card_article}"] [class*="catalog-buy-button__button btn sm"]').click()
        with allure.step("Счётчик корзины увеличился"):
            browser.element('//*[@id="page-header"]/div/div[1]/div/div/div/div/div[7]/div/div/a/div/div/span').should(be.visible)

    def open_basket(self):
        with allure.step("Нажимаем 'Корзина'"):
            self.basket.click()

    def check_cart(self, card_name, brand_name):
        self.open_basket()
        with allure.step(f"В корзине отображается товар с наименованием {card_name} {brand_name}"):
            browser.all('[class="good-info__title j-product-popup"] span').should(have.texts(card_name, brand_name))

    def remove_from_cart(self):
        self.open_basket()
        with allure.step("Удаляем товар"):
            browser.element('[class*=item-del]').click()
        with allure.step(f"Отображается текст {Texts.empty_cart}"):
            browser.element('[class*="basket-empty__title"]').should(have.text(Texts.empty_cart))
