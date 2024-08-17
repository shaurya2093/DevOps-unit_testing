from shared import config
import os
import HtmlTestRunner
import unittest
import fnmatch

def main():

    commonPath = config.commonPath
    # Create test suite.
    test_suite = unittest.TestSuite()

    for file in os.listdir(commonPath):
        if fnmatch.fnmatch(file, 'TestSuite*'):
            # Load all test case class in current folder.
            tcFolder = commonPath + "\\" + file

            #To run all test suites
            testSuitesList = ["testsuite2", "testsuite1"]

            if file in testSuitesList:
                all_test_cases = unittest.defaultTestLoader.discover(tcFolder, 'tc*.py', commonPath)
                for test_case in all_test_cases:
                    test_suite.addTest(test_case)
                all_test_cases = 0

    reportDir = "\\htmlReports"

    report_dir = commonPath + reportDir
    if report_dir != "":
       if not os.path.exists(report_dir):
           os.makedirs(report_dir)

    reportFile = report_dir + "\\CodeGym11.Html"
    print("Report file is : " + reportFile)

    if os.path.exists(reportFile) == True:
        try:
            os.remove(reportFile)
        except OSError as e:
            print("Failed with:", e.strerror)

    with open(reportFile, mode="w", encoding="utf-8") as outfile:
        # Create htmlTestRunner object and run the test suite.
        testRunner=HtmlTestRunner.HTMLTestRunner(stream=outfile, title='Codegym - Test Report', verbosity=2)
        testRunner.run(test_suite)


if __name__ == "__main__":
 main()