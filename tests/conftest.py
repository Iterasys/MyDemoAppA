import pytest
from appium import webdriver

from . import config, credentials


# valores default
def pytest_addoption(parser):
    parser.addoption(
        '--baseurl',
        action='store',
        default='@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        help='local onde está o servidor Appium'
    )
    parser.addoption(
        '--host',
        action='store',
        default='saucelabs',
        help='servidor local ou na nuvem'
    )
    parser.addoption(
        '--platform_name',
        action='store',
        default='Android',
        help='Sistema Operacional do dispositivo ou emulador'
    )
    parser.addoption(
        '--platform_version',
        action='store',
        default='9.0',
        help='Versão do Sistema Operacional do dispositivo ou emulador'
    )


@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption('--baseurl')
    config.host = request.config.getoption('--host')
    config.platform_name = request.config.getoption('--platform_name')
    config.platform_version = request.config.getoption('--platform_version')

    # direciona para a execução no saucelabs ou local
    if config.host == 'saucelabs':
        test_name = request.node.name  # nome do teste
        caps = {
            'platformName': config.platform_name,
            'appium:platformVersion': config.platform_version,
            'appium:deviceName': 'Samsung Galaxy S9 FHD GoogleAPI Emulator',
            'appium:deviceOrientation': 'portrait',
            'appium:app': 'storage:filename=mda-1.0.10-12.apk',
            'appium:appPackage': 'com.saucelabs.mydemoapp.android',
            'appium:appActivity': 'com.saucelabs.mydemoapp.android.view.activities.SplashActivity',
            'sauce:options': {
                'name': test_name  # nome do teste
            }
        }

        # montar a credencial e a url
        _credentials = credentials.SAUCE_USERNAME + ':' + credentials.SAUCE_ACCESS_KEY
        _url = 'https://' + _credentials + config.baseurl

        # instanciar o Saucelabs
        driver_ = webdriver.Remote(_url, caps)

    # execução local
    else:
        caps = {
            'platformName': config.platform_name,
            'appium:platformVersion': config.platform_version,
            "appium:appiumVersion": "1.22.0",
            "appium:automationName": "uiautomator2",
            "appium:deviceName": "emulator5554",
            "appium:deviceOrientation": "portrait",
            "appium:appPackage": "com.saucelabs.mydemoapp.android",
            "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
        }
        driver_ = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # função de finalização
    def quit():
        sauce_result = 'failed' if request.node.rep_call.failed else 'passed'
        driver_.execute_script('sauce:job-result={}'.format(sauce_result))
        driver_.quit()

    request.addfinalizer(quit)
    return driver_


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep_' + rep.when, rep)
