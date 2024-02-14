from megamarket_tests.data.data_cards import card
from megamarket_tests.pages.main_page import MainPage
import pytest


def test_search_by_name():
    main_page = MainPage()

    main_page.open_url()
    main_page.search(card.card_name)
    main_page.result_by_name(card.card_name, card.brand_name, card.card_article)


def test_search_by_article():
    main_page = MainPage()

    main_page.open_url()
    main_page.search(card.card_article)
    main_page.result_by_article(card.card_article)


def test_search_without_result():
    main_page = MainPage()

    main_page.open_url()
    main_page.search(card.non_existent_article)
    main_page.no_result()
