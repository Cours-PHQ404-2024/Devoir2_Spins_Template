import tac
import os


def get_base_grade():
    template_url = r"https://github.com/Cours-PHQ404-2024/Devoir2_Spins_Template"
    report = auto_correct(url=template_url)
    return report.grade


def auto_correct(path_to_root: str = ".", url: str = None):
    code_source = tac.SourceCode(os.path.join(path_to_root, "src"), url=url, logging_func=print)
    tests_source = tac.SourceTests(os.path.join(path_to_root, "tests"), url=url, logging_func=print)
    auto_corrector = tac.Tester(
        code_source, tests_source,
        report_dir="report_dir",
        logging_func=print,
        weights={
            tac.Tester.PEP8_KEY: 10.0,
            tac.Tester.PERCENT_PASSED_KEY: 10.0,
            tac.Tester.CODE_COVERAGE_KEY: 20.0,
            tac.Tester.MASTER_PERCENT_PASSED_KEY: 30.0,
        },
    )
    auto_corrector.run(overwrite=False, clear_pytest_temporary_files=True)
    report = auto_corrector.report
    auto_corrector.rm_report_dir()
    return report


def get_grade_report():
    base_grade = get_base_grade()
    report = auto_correct()
    new_report = tac.Report(
        data=report.data,
        grade_min=base_grade,
        grade_min_value=50.0,
        grade_max=100.0,
        report_filepath=os.path.join(os.path.dirname(__file__), "grade_report.json"),
    )
    print(new_report)
    new_report.save()
    return new_report


if __name__ == "__main__":
    get_grade_report()
