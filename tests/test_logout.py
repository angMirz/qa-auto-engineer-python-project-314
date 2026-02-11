def test_logout_redirect_to_login(logged_in):
    page = logged_in
    page.logout()

    assert "/login" in page.driver.current_url
