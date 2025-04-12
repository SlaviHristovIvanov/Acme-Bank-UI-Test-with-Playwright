import pytest
import re

from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.acme_bank
def test_acme_bank_login(page: Page):

    # Arrange
    page.goto('https://demo.applitools.com')  # This will load the page

    # Act
    page.locator('id=username').fill('dsds')  # page.locator will select, interaction is fill('dsds')
    page.locator('id=password').fill('dsds')  # the element wich is username & pass
    page.locator('id=log-in').click()         # then it will click log-in

    # Assert      # we need to che if the page loads correctly
    # expect in playwright is like assert in python
    expect(page.locator('div.logo-w')).to_be_visible()
    expect(page.locator('ul.main-menu')).to_be_visible()
    expect(page.get_by_text('Add Account')).to_be_visible()
    expect(page.get_by_text('Make Payment')).to_be_visible()
    expect(page.get_by_text('View Statement')).to_be_visible()
    expect(page.get_by_text('Request Increase')).to_be_visible()
    expect(page.get_by_text('Pay Now')).to_be_visible()

