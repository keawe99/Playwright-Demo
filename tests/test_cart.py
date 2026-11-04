import os

import pytest
from playwright.sync_api import Page, expect


CART_URL = os.getenv("CART_URL", "https://www.saucedemo.com/cart.html")


@pytest.fixture
def cart_page(page: Page) -> Page:
	page.goto(CART_URL)
	return page


def test_cart_page_loads(cart_page: Page) -> None:
	expect(cart_page.get_by_role("heading", name="Cart")).to_be_visible()


def test_cart_shows_items_or_empty_state(cart_page: Page) -> None:
	items = cart_page.data-testid("cart-item")
	if items.count() > 0:
		expect(items.first).to_be_visible()
		expect(cart_page.data-testid("cart-subtotal")).to_be_visible()
	else:
		expect(cart_page.data-testid("cart-empty")).to_be_visible()


def test_cart_item_can_be_removed(cart_page: Page) -> None:
	items = cart_page.data-testid("cart-item")
	if items.count() == 0:
		pytest.skip("Cart has no items to remove")

	initial_count = items.count()
	items.first.get_by_role("button", name="Remove").click()
	expect(items).to_have_count(initial_count - 1)
