import unittest
from flight_ticket_upgrader.constants.regex import *


class TestTicketUpgrader(unittest.TestCase):
    def test_mobile_validator(self):
        """
        Tests that given data is a valid mobile number
        :return:
        """

        self.assertRegexpMatches("9876543219", mobile_regex)
        self.assertRegexpMatches("8886543219", mobile_regex)
        self.assertRegexpMatches("6543219000", mobile_regex)

        self.assertNotRegexpMatches("98765432190", mobile_regex)
        self.assertNotRegexpMatches("98765432", mobile_regex)
        self.assertNotRegexpMatches("98765432$%", mobile_regex)
        self.assertNotRegexpMatches("!@#$%98765", mobile_regex)

    def test_email_validator(self):
        """
        Tests that given data is a valid email id
        :return:
        """

        self.assertRegexpMatches("abc.xyz@ppp.com", email_regex)
        self.assertRegexpMatches("abc+xyz@sss.co", email_regex)
        self.assertRegexpMatches("abc-xyz@f.co.in", email_regex)
        self.assertRegexpMatches("abcdx_yz@sd-gf.com", email_regex)

        self.assertNotRegexpMatches("@ggg.com", email_regex)
        self.assertNotRegexpMatches("abcd@", email_regex)
        self.assertNotRegexpMatches("abcd@abcd", email_regex)
        self.assertNotRegexpMatches("123456", email_regex)
        self.assertNotRegexpMatches("", email_regex)

    def test_pnr_validator(self):
        """
        Tests that given data is a valid pnr
        :return:
        """

        self.assertRegexpMatches("AB1234", pnr_regex)
        self.assertRegexpMatches("pqrs12", pnr_regex)
        self.assertRegexpMatches("STHYYY", pnr_regex)
        self.assertRegexpMatches("123456", pnr_regex)

        self.assertNotRegexpMatches("WXE1234", pnr_regex)
        self.assertNotRegexpMatches("WXE12", pnr_regex)
        self.assertNotRegexpMatches("ABC#12", pnr_regex)
        self.assertNotRegexpMatches("ABC#$%", pnr_regex)
        self.assertNotRegexpMatches(":?!@#$", pnr_regex)


if __name__ == '__main__':
    unittest.main()