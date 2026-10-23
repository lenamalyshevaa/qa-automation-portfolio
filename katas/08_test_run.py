

class TestRun: 
    def __init__(self):
        self.tests = {}

    def add_result(self, name, status): 
        if status not in ['passed', 'failed', 'skipped']:
            raise ValueError('wrong status')
        self.tests[name] = status

    def summary(self):
        total = {}
        for status in self.tests.values():
            total[status] = total.get(status, 0) +1
            return total

    def failed(self):
        failed_tests = []
        for name, status in self.tests.items():
            if status == 'failed':
                failed_tests.append(name)
        return failed_tests

    def success_rate(self):
        passed = 0
        all_tests  = len(self.tests)
        for status in self.tests.values():
            if status == 'passed': passed += 1
        if passed == 0: return 0 

        else: return round((passed/all_tests) * 100)

run = TestRun()

run.add_result("test_login", "passed")
run.add_result("test_payment", "failed")
run.add_result("test_export", "skipped")

print(run.summary())
print(run.failed())
print(run.success_rate())
try:
    run.add_result("test_x", "broken")
except ValueError as e:
    print("Поймали:", e)