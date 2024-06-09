from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("A,B") == 80


    # def test_checkout_illegal(self):
    #     assert checkout_solution.checkout(123) == -1
