# coding: utf-8

"""
    Avascan API

    Avalanche multi-chain explorer API docs

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.v2_network_network_id_evm_cross_transactions_get200_response_link import V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseLink

class TestV2NetworkNetworkIdEvmCrossTransactionsGet200ResponseLink(unittest.TestCase):
    """V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseLink unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseLink:
        """Test V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseLink
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseLink`
        """
        model = V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseLink()
        if include_optional:
            return V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseLink(
                next = '',
                next_token = ''
            )
        else:
            return V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseLink(
        )
        """

    def testV2NetworkNetworkIdEvmCrossTransactionsGet200ResponseLink(self):
        """Test V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseLink"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
