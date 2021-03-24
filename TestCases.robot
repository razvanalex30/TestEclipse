*** Variables ***
${browser}    chrome
${url}    https://www.python.org/
${menu}    Downloads
${submenu}    All releases
${search_string}    decorator
${result_string}    PEP 318 -- Decorators for Functions and Methods


*** Settings ***
Library           SeleniumLibrary
Library           downloads_page.DownloadPage
Library           primary_page.PrimaryPage
Library           result_page.ResultPage
library           decorator_page.DecoratorPage

*** Keywords ***
Open Browser Page
    Open Browser    ${url}    ${browser}


*** Test Cases ***
firstTest
    [Tags]    debug
    Open Browser Page   
    Navigate Menu Submenu    ${menu}    ${submenu}
    Retrieve Version
    Close Browser
    
secondTest
    [Tags]    debug
    Open Browser Page
    Search    ${search_string}
    Get First Result    ${result_string}
    Verify Example Count
    Close Browser
       
