from solutions.CHK import checkout_solution


class TestCheckout():

    # Round 4
    def test_volume_discount(self):
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("AAAAAAAAA") == 380

        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("BBB") == 75
        assert checkout_solution.checkout("BBBB") == 90


    # # Round 3
    # def test_multi_buy_F_discount_to_F(self):
    #     assert checkout_solution.checkout("FF") == 20
    #     assert checkout_solution.checkout("FFF") == 20
    #     assert checkout_solution.checkout("FFFF") == 30
    #     assert checkout_solution.checkout("FFFFFF") == 40
    #
    # # Round 2
    # def test_non_linear_combination(self):
    #     assert checkout_solution.checkout("AAAAA") == 200
    #     assert checkout_solution.checkout("AAA") == 130
    #     assert checkout_solution.checkout("AAAAAAAA") == 330
    #     assert checkout_solution.checkout("AAAAAAAAA") == 380
    #
    # def test_multi_buy_E_discount_to_B(self):
    #     assert checkout_solution.checkout("EEB") == 80
    #     assert checkout_solution.checkout("EEEEEEB") == 240
    #     assert checkout_solution.checkout("EEEEEEBB") == 240
    #
    # #Round 1
    # def test_checkout_multi(self):
    #     assert checkout_solution.checkout("A,A,A") == 130
    #     assert checkout_solution.checkout("A,A,A,B,C") == 180
    #     assert checkout_solution.checkout("A,A,A,A,A,A,A,B,B,C") == 365
    #
    # def test_checkout_basic(self):
    #     assert checkout_solution.checkout("A,B,D") == 95
    #
    # def test_checkout_no_delim(self):
    #     assert checkout_solution.checkout("ABD") == 95
    #     assert checkout_solution.checkout("AB D") == 95
    #     assert checkout_solution.checkout("A,BD") == 95
    #
    # def test_checkout_case(self):
    #     assert checkout_solution.checkout("A,b") == -1
    #     assert checkout_solution.checkout("a") == -1
    #     assert checkout_solution.checkout("ABCa") == -1
    #
    # def test_checkout_space(self):
    #     assert checkout_solution.checkout("A, B") == 80
    #
    # def test_checkout_illegal(self):
    #     assert checkout_solution.checkout(123) == -1
    #     # assert checkout_solution.checkout("ABEZ") == -1
    #
    # def test_checkout_empty(self):
    #     assert checkout_solution.checkout("") == 0



