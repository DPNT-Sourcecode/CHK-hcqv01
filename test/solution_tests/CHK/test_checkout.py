from solutions.CHK import checkout_solution


class TestCheckout():

    def test_checkout_multi(self):
        assert checkout_solution.checkout("A,A,A") == 130
        assert checkout_solution.checkout("A,A,A,B,C") == 180
        assert checkout_solution.checkout("A,A,A,A,A,A,A,B,B,C") == 375

    def test_checkout_basic(self):
        assert checkout_solution.checkout("A,B,D") == 95

    def test_checkout_no_delim(self):
        assert checkout_solution.checkout("ABD") == 95
        assert checkout_solution.checkout("AB D") == 95
        assert checkout_solution.checkout("A,BD") == 95

    def test_checkout_case(self):
        assert checkout_solution.checkout("A,b") == 80

    def test_checkout_space(self):
        assert checkout_solution.checkout("A, b") == 80

    def test_checkout_illegal(self):
        assert checkout_solution.checkout(123) == -1
        assert checkout_solution.checkout("ABEZ") == -1

    def test_checkout_empty(self):
        assert checkout_solution.checkout("") == -1








