cd "C:\DEVELOP\python_training\allure-results\"
del *.* /Q
cd "C:\DEVELOP\python_training\"
call venv\Scripts\activate.bat
python -m pytest --alluredir allure-results test\test_add_group.py
call allure.bat generate --clean
call allure.bat open
pause