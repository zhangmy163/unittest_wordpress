from .page_objects import PageObject,PageElement
from selenium import webdriver

class DashboardPage(PageObject):
    name = PageElement(class_='display-name')