from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_invalid_password_shows_error(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("wrong_password")
    page.get_by_role("button", name="Login").click()

    error = page.locator('[data-test="error"]')
    expect(error).to_be_visible()
    expect(error).to_contain_text("Epic sadface")
    expect(page).to_have_url("https://www.saucedemo.com/")

    
