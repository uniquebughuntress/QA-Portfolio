# utils/constants.py
# Erstellt: 22.07.26 um 14:03
# Autor: natalya
# Projekt: QA-Portfolio
# -*- coding: utf-8 -*-
"""Test data and application constants."""

from selenium.webdriver.common.by import By

# ==================== URLS ====================

URL_GROCERY_MATE = "https://grocerymate.masterschool.com/"
URL_LOGIN = "https://grocerymate.masterschool.com/auth"
URL_SHOP = "https://grocerymate.masterschool.com/store"


# ==================== TEST USER ====================

TEST_USER_1_EMAIL = "test1@test.de"
TEST_USER_1_PASSWORD = "AdminTest!"
TEST_USER_1_NAME = "Testina1"

TEST_USER_2_EMAIL = "test2@test.de"
TEST_USER_2_PASSWORD = "Admin123!"
TEST_USER_2_NAME = "Jenny Doe"


# ==================== TIMEOUTS ====================

DEFAULT_TIMEOUT = 10
SHORT_TIMEOUT = 3


# ==================== PRODUCT URLS ====================

PRODUCT_GALA_APPLES_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47998"
)

PRODUCT_PINK_LADY_APPLES_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4799b"
)

PRODUCT_LOOSE_PEARS_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47990"
)

PRODUCT_CHERRIES_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47991"
)

PRODUCT_BEN_BRACKEN_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a91"
)

PRODUCT_BALMUIR_WHISKY_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a9b"
)

PRODUCT_PINK_GIN_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a8d"
)

PRODUCT_NECTARINES_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47992"
)

PRODUCT_GALIA_MELON_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47993"
)

PRODUCT_SIMPLY_PEPPERONI_PIZZA_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a50"
)

PRODUCT_OCEAN_SEA_KING_PRAWNS_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a4e"
)

PRODUCT_TRATTORIA_ALFREDO_PIZZA_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a4f"
)


# Bereits von Jenny Doe bewertet.

PRODUCT_PLUMS_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47994"
)

PRODUCT_LOOSE_MANGO_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47997"
)

PRODUCT_CELERY_URL = (
    "https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a1"
)


# ==================== LOCATORS ====================


class StorePageLocators:
    """Locators for the store page."""

    # ====== PRODUKTLISTE ======

    PRODUCT_GRID = (By.CSS_SELECTOR, ".product-grid")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".product-card")
    PRODUCT_CARD_BY_NAME = (
        By.XPATH,
        "//div[contains(@class, 'product-card')]"
        "[.//p[contains(@class, 'lead') and "
        "normalize-space()='{product_name}']]",
    )

    PRODUCT_QUANTITY = (
        By.CSS_SELECTOR,
        ".quantity",
    )

    PRODUCT_ADD_TO_CART = (
        By.CSS_SELECTOR,
        ".btn-cart",
    )

    # ====== PRODUKTTITEL ======

    PRODUCT_TITLE = (By.CSS_SELECTOR, ".card-header .lead")

    # ====== ERSTES PRODUKT ======

    FIRST_PRODUCT_CARD = (
        By.CSS_SELECTOR,
        ".product-card:first-child",
    )

    FIRST_PRODUCT_TITLE = (
        By.CSS_SELECTOR,
        ".product-card:first-child .card-header .lead",
    )

    FIRST_PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        ".product-card:first-child .discount-price",
    )

    FIRST_PRODUCT_ADD_TO_CART = (
        By.CSS_SELECTOR,
        ".product-card:first-child .btn-cart",
    )

    FIRST_PRODUCT_QUANTITY = (
        By.CSS_SELECTOR,
        ".product-card:first-child .quantity",
    )

    # ====== SUCHE ======

    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='Search Products']",
    )

    SEARCH_SUGGESTION = (
        By.CSS_SELECTOR,
        ".suggestion-item",
    )

    SEARCH_SUGGESTION_BY_NAME = (
        By.XPATH,
        "//div[contains(@class, 'suggestion-item')]"
        "//strong[normalize-space()='{product_name}']",
    )

    # ====== KATEGORIEN ======

    CATEGORY_BY_NAME = (
        By.XPATH,
        "//div[contains(@class, 'widget-menu')]"
        "//li//a[normalize-space()='{category_name}']",
    )

    CATEGORY_ALCOHOL = (
        By.XPATH,
        "//div[@class='widget-menu']//li//a[text()='Alocohol']",
    )

    # ====== PAGINATION ======

    NEXT_PAGE_BTN = (
        By.XPATH,
        "//li[contains(@class, 'pagination-item')]" "//button[text()='Next']",
    )

    PREV_PAGE_BTN = (
        By.XPATH,
        "//li[contains(@class, 'pagination-item')]" "//button[text()='Previous']",
    )

    ACTIVE_PAGE = (
        By.CSS_SELECTOR,
        ".pagination-item.active button",
    )

    MODAL_OVERLAY = (
        By.CSS_SELECTOR,
        "div.modal-overlay",
    )

    MODAL_CONTENT = (
        By.CSS_SELECTOR,
        "div.modal-content",
    )

    MODAL_INPUT = (
        By.CSS_SELECTOR,
        ".modal-content input[type='text']",
    )

    MODAL_CONFIRM_BTN = (
        By.XPATH,
        "//div[@class='modal-content']//button[text()='Confirm']",
    )

    MODAL_TITLE = (
        By.CSS_SELECTOR,
        ".modal-content h2",
    )

    MODAL_TEXT = (
        By.CSS_SELECTOR,
        ".modal-content p",
    )


class LoginPageLocators:
    """Locators for the login page."""

    EMAIL_INPUT = (
        By.CSS_SELECTOR,
        "input[type='email']",
    )

    PASSWORD_INPUT = (
        By.CSS_SELECTOR,
        "input[type='password']",
    )

    SUBMIT_BTN = (
        By.CSS_SELECTOR,
        "button.submit-btn",
    )

    LOGIN_ERROR = (
        By.CSS_SELECTOR,
        ".error-message, .alert-danger",
    )


class HomePageLocators:
    """Locators for the home page."""

    # ====== NAVIGATION ======

    CART_ICON = (
        By.CSS_SELECTOR,
        ".social-icon-cont .headerIcon:nth-child(3)",
    )

    NAV_HOME = (
        By.XPATH,
        "//ul[@class='anim-nav']//a[text()='Home']",
    )

    NAV_SHOP = (
        By.XPATH,
        "//ul[@class='anim-nav']//a[text()='Shop']",
    )

    NAV_FAVORITES = (
        By.XPATH,
        "//ul[@class='anim-nav']//a[text()='Favorites']",
    )

    NAV_CONTACT = (
        By.XPATH,
        "//ul[@class='anim-nav']//a[text()='Contact']",
    )

    # ====== LOGO ======

    LOGO = (
        By.CSS_SELECTOR,
        "img[alt='Logo']",
    )

    # ====== SEARCH ======

    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        ".search-cont input[type='text']",
    )


class ProductPageLocators:
    """Locators for product details, age verification and reviews."""

    # ==================== REVIEW UI ====================
    REVIEW_STARS = (
        By.CSS_SELECTOR,
        "div.interactive-rating span.star",
    )
    REVIEW_TEXTAREA = (
        By.CSS_SELECTOR,
        "textarea.new-review-form-control",
    )
    REVIEW_SEND_BTN = (
        By.CSS_SELECTOR,
        "button.new-review-btn-send",
    )
    REVIEW_CHAR_COUNTER = (
        By.CSS_SELECTOR,
        ".new-review-char-counter span",
    )
    REVIEWS_COUNT = (
        By.CSS_SELECTOR,
        ".ratingContainer p.reviews",
    )

    # ====== PRODUKTLISTE ======

    PRODUCT_GRID = (
        By.CSS_SELECTOR,
        ".product-grid",
    )

    PRODUCT_CARDS = (
        By.CSS_SELECTOR,
        ".product-card",
    )

    PRODUCT_TITLE = (
        By.CSS_SELECTOR,
        ".card-header .lead",
    )

    # ====== PAGINATION ======

    PAGINATION = (
        By.CSS_SELECTOR,
        ".pagination",
    )

    PAGE_NUMBERS = (
        By.CSS_SELECTOR,
        ".page-numbers",
    )

    PAGE_LINK = (
        By.CSS_SELECTOR,
        ".page-numbers .pagination-item button",
    )

    NEXT_PAGE_BTN = (
        By.XPATH,
        "//li[contains(@class, 'pagination-item')]" "//button[text()='Next']",
    )

    PREV_PAGE_BTN = (
        By.XPATH,
        "//li[contains(@class, 'pagination-item')]" "//button[text()='Previous']",
    )

    ACTIVE_PAGE = (
        By.CSS_SELECTOR,
        ".pagination-item.active button",
    )

    # ====== ERSTES PRODUKT ======

    FIRST_PRODUCT_CARD = (
        By.CSS_SELECTOR,
        ".product-card:first-child",
    )

    FIRST_PRODUCT_TITLE = (
        By.CSS_SELECTOR,
        ".product-card:first-child .card-header .lead",
    )

    FIRST_PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        ".product-card:first-child .discount-price",
    )

    FIRST_PRODUCT_ADD_TO_CART = (
        By.CSS_SELECTOR,
        ".product-card:first-child .btn-cart",
    )

    FIRST_PRODUCT_QUANTITY = (
        By.CSS_SELECTOR,
        ".product-card:first-child .quantity",
    )

    # ====== KATEGORIEN ======

    CATEGORY_ALCOHOL = (
        By.XPATH,
        "//div[@class='widget-menu']//li//a[text()='Alocohol']",
    )

    # ====== ALCOHOL MODAL ======

    MODAL_OVERLAY = (
        By.CSS_SELECTOR,
        "div.modal-overlay",
    )

    MODAL_CONTENT = (
        By.CSS_SELECTOR,
        "div.modal-content",
    )

    MODAL_INPUT = (
        By.CSS_SELECTOR,
        ".modal-content input[type='text']",
    )

    MODAL_CONFIRM_BTN = (
        By.XPATH,
        "//div[@class='modal-content']//button[text()='Confirm']",
    )

    MODAL_TITLE = (
        By.CSS_SELECTOR,
        ".modal-content h2",
    )

    MODAL_TEXT = (
        By.CSS_SELECTOR,
        ".modal-content p",
    )

    # ====== PRODUKTDETAILS ======

    PRODUCT_TITLE = (
        By.CSS_SELECTOR,
        ".descriptionContainer h2",
    )

    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        ".descriptionContainer p.price",
    )

    # ====== CART ======

    ADD_TO_CART_BTN = (
        By.CSS_SELECTOR,
        "button.btn-cart",
    )

    QUANTITY_INPUT = (
        By.CSS_SELECTOR,
        "input.quantity",
    )

    # ====== REVIEW UI ======

    REVIEW_STARS = (
        By.CSS_SELECTOR,
        "div.interactive-rating span.star",
    )

    REVIEW_TEXTAREA = (
        By.CSS_SELECTOR,
        "textarea.new-review-form-control",
    )

    REVIEW_SEND_BTN = (
        By.CSS_SELECTOR,
        "button.new-review-btn-send",
    )

    REVIEW_CHAR_COUNTER = (
        By.CSS_SELECTOR,
        ".new-review-char-counter span",
    )

    # ====== REVIEW RESTRICTION ======

    REVIEW_RESTRICTION = (
        By.CSS_SELECTOR,
        ".reviewRestriction",
    )

    REVIEW_RESTRICTION_TEXT = (
        By.CSS_SELECTOR,
        ".reviewRestriction p",
    )

    # ====== COMMENTS ======

    COMMENTS_CONTAINER = (
        By.CSS_SELECTOR,
        ".comments-container",
    )

    ALL_COMMENTS = (
        By.CSS_SELECTOR,
        "div.comment",
    )

    FIRST_COMMENT = (
        By.CSS_SELECTOR,
        "div.comment:first-child",
    )

    FIRST_COMMENT_HEADER = (
        By.CSS_SELECTOR,
        "div.comment:first-child .comment-header h5 strong",
    )

    FIRST_COMMENT_TEXT = (
        By.CSS_SELECTOR,
        "div.comment:first-child p",
    )

    FIRST_COMMENT_RATING_STARS = (
        By.CSS_SELECTOR,
        "div.comment:first-child .custom-rating .star",
    )

    # ====== COMMENT MENU ======

    FIRST_COMMENT_MENU_ICON = (
        By.CSS_SELECTOR,
        "div.comment:first-child .menu-icon",
    )

    DROPDOWN_EDIT_BTN = (
        By.XPATH,
        "//div[@class='dropdown-menu']//button[text()='Edit']",
    )

    DROPDOWN_DELETE_BTN = (
        By.XPATH,
        "//div[@class='dropdown-menu']//button[text()='Delete']",
    )
