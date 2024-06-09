from solutions.CHK import checkout_solution


class TestCheckout():


    def test_checkout_basic(self):
        assert checkout_solution.checkout("A,B") == 80

    def test_checkout_case(self):
        assert checkout_solution.checkout("A,b") == 80

    def test_checkout_illegal(self):
        assert checkout_solution.checkout(123) == -1

    def test_checkout_empty(self):
        assert checkout_solution.checkout("") == -1


