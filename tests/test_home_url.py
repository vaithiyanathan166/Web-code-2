URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@pytest.mark.usefixtures("driver")
class TestHomeURL:
    def test_home_url(self, driver):
        driver.get(URL)
        assert "OrangeHRM" in driver.title
