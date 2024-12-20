*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create user And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register
    Register Should Fail With Message  Username needs to be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Submit Register
    Register Should Fail With Message  Password needs to be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kallekas
    Set Password Confirmation  kallekas
    Submit Register
    Register Should Fail With Message  Password needs to have numbers or symbols

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle124
    Submit Register
    Register Should Fail With Message  Passwords need to match

Register With Username That Is Already In Use
    Set Username  ville
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register
    Register Should Fail With Message  This username is already in use

Login After Successful Registration
    Set Username  jussi
    Set Password  jussi123
    Set Password Confirmation  jussi123
    Submit Register
    Go To Ohtu Page
    Click Button  Logout
    Go To Login Page
    Set Username  jussi
    Set Password  jussi123
    Submit Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  jussi
    Set Password  jussi12
    Set Password Confirmation  jussi12
    Submit Register
    Go To Login Page
    Set Username  jussi
    Set Password  jussi12
    Submit Login
    Login Page Should Be Open
    Page Should Contain  Invalid username or password

*** Keywords ***

Submit Register
    Click Button  Register

Submit Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Reset Application Create user And Go To Register Page
    Reset Application
    Create User  ville  ville123
    Go To Register Page