import subprocess

if __name__ == "__main__":
    subprocess.run(["behave", "-D", "browser=firefox", "-f", "pretty", "--tags=@positive,@negative"])


"""
to run chrome use only -- "behave",
to run edge use all -- "behave", "-D", "browser=edge",
to run firefox use all -- "behave", "-D", "browser=firefox",

"""
r"""
How to run and get alert report:

cd to the project path = cd C:\Users\tkinf\python_cucumber\python_cucumber
run = allure generate allure-results --clean -o allure-report
Run your tests = python run_tests.py

"""