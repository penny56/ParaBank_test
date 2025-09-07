from pages.base_page import BasePage

class HomePage:
    def __init__(self, page):
        self.page = page

    def goto(self, base_url: str):
        self.page.goto(base_url)

    def get_title(self):
        self.page.wait_for_load_state("domcontentloaded")
        return self.page.title()
    
    def go_to_register(self):
        from pages.register_page import RegisterPage

        self.page.click("a[href='register.htm']")
        self.page.wait_for_load_state("domcontentloaded")
        return RegisterPage(self.page)

    def go_to_about_us(self):
        self.page.click("text=About Us")
        self.page.wait_for_load_state("domcontentloaded")      
    
    def go_to_services(self):
        self.page.click("text=Services")
        self.page.wait_for_load_state("domcontentloaded")

    def go_to_products(self):
        self.page.click("text=Products")
        self.page.wait_for_load_state("domcontentloaded")

    def go_to_locations(self):
        self.page.click("text=Locations")
        self.page.wait_for_load_state("domcontentloaded")

    def go_to_admin_page(self):
        self.page.click("text=Admin Page")
        self.page.wait_for_load_state("domcontentloaded")
    
    def back_to_home(self):
        self.page.go_back()
        self.page.wait_for_selector("div#leftPanel")

