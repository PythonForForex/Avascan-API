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

from openapi_client.models.v2_network_network_id_avm_blockchain_id_address_address_id_transactions_get200_response_items_inner_inputs_inner_asset import V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset

class TestV2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset(unittest.TestCase):
    """V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset:
        """Test V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset`
        """
        model = V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset()
        if include_optional:
            return V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset(
                id = '',
                name = '',
                symbol = '',
                denomination = 1.337,
                type = 'fixed_cap'
            )
        else:
            return V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset(
                id = '',
        )
        """

    def testV2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset(self):
        """Test V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()