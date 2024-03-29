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

from openapi_client.models.v2_network_network_id_avm_blockchain_id_address_address_id_transactions_get200_response import V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response

class TestV2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response(unittest.TestCase):
    """V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response:
        """Test V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response`
        """
        model = V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response()
        if include_optional:
            return V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response(
                items = [
                    openapi_client.models._v2_network__network_id__avm__blockchain_id__address__address_id__transactions_get_200_response_items_inner._v2_network__networkId__avm__blockchainId__address__addressId__transactions_get_200_response_items_inner(
                        id = '', 
                        type = 'base', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        inputs_count = 1.337, 
                        outputs_count = 1.337, 
                        inputs_limit = 1.337, 
                        outputs_limit = 1.337, 
                        inputs = [
                            openapi_client.models._v2_network__network_id__avm__blockchain_id__address__address_id__transactions_get_200_response_items_inner_inputs_inner._v2_network__networkId__avm__blockchainId__address__addressId__transactions_get_200_response_items_inner_inputs_inner(
                                id = '', 
                                tx_id = '', 
                                index = 1.337, 
                                amount = '', 
                                src_chain = '', 
                                dst_chain = '', 
                                owner = openapi_client.models._v2_network__network_id__avm__blockchain_id__address__address_id__transactions_get_200_response_items_inner_inputs_inner_owner._v2_network__networkId__avm__blockchainId__address__addressId__transactions_get_200_response_items_inner_inputs_inner_owner(
                                    addresses = [
                                        ''
                                        ], 
                                    threshold = 1.337, ), 
                                locktime = 1.337, 
                                creds = [
                                    openapi_client.models._v2_network__network_id__avm__blockchain_id__address__address_id__transactions_get_200_response_items_inner_inputs_inner_creds_inner._v2_network__networkId__avm__blockchainId__address__addressId__transactions_get_200_response_items_inner_inputs_inner_creds_inner(
                                        address = '', )
                                    ], 
                                asset = openapi_client.models._v2_network__network_id__avm__blockchain_id__address__address_id__transactions_get_200_response_items_inner_inputs_inner_asset._v2_network__networkId__avm__blockchainId__address__addressId__transactions_get_200_response_items_inner_inputs_inner_asset(
                                    id = '', 
                                    name = '', 
                                    symbol = '', 
                                    denomination = 1.337, 
                                    type = 'fixed_cap', ), )
                            ], 
                        outputs = [
                            openapi_client.models._v2_network__network_id__avm__blockchain_id__address__address_id__transactions_get_200_response_items_inner_inputs_inner._v2_network__networkId__avm__blockchainId__address__addressId__transactions_get_200_response_items_inner_inputs_inner(
                                id = '', 
                                tx_id = '', 
                                index = 1.337, 
                                amount = '', 
                                src_chain = '', 
                                dst_chain = '', 
                                owner = openapi_client.models._v2_network__network_id__avm__blockchain_id__address__address_id__transactions_get_200_response_items_inner_inputs_inner_owner._v2_network__networkId__avm__blockchainId__address__addressId__transactions_get_200_response_items_inner_inputs_inner_owner(
                                    addresses = [
                                        ''
                                        ], 
                                    threshold = 1.337, ), 
                                locktime = 1.337, )
                            ], 
                        memo = '', )
                    ],
                link = openapi_client.models._v2_network__network_id__evm_cross_transactions_get_200_response_link._v2_network__networkId__evm_cross_transactions_get_200_response_link(
                    next = '', 
                    next_token = '', )
            )
        else:
            return V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response(
                items = [
                    openapi_client.models._v2_network__network_id__avm__blockchain_id__address__address_id__transactions_get_200_response_items_inner._v2_network__networkId__avm__blockchainId__address__addressId__transactions_get_200_response_items_inner(
                        id = '', 
                        type = 'base', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        inputs_count = 1.337, 
                        outputs_count = 1.337, 
                        inputs_limit = 1.337, 
                        outputs_limit = 1.337, 
                        inputs = [
                            openapi_client.models._v2_network__network_id__avm__blockchain_id__address__address_id__transactions_get_200_response_items_inner_inputs_inner._v2_network__networkId__avm__blockchainId__address__addressId__transactions_get_200_response_items_inner_inputs_inner(
                                id = '', 
                                tx_id = '', 
                                index = 1.337, 
                                amount = '', 
                                src_chain = '', 
                                dst_chain = '', 
                                owner = openapi_client.models._v2_network__network_id__avm__blockchain_id__address__address_id__transactions_get_200_response_items_inner_inputs_inner_owner._v2_network__networkId__avm__blockchainId__address__addressId__transactions_get_200_response_items_inner_inputs_inner_owner(
                                    addresses = [
                                        ''
                                        ], 
                                    threshold = 1.337, ), 
                                locktime = 1.337, 
                                creds = [
                                    openapi_client.models._v2_network__network_id__avm__blockchain_id__address__address_id__transactions_get_200_response_items_inner_inputs_inner_creds_inner._v2_network__networkId__avm__blockchainId__address__addressId__transactions_get_200_response_items_inner_inputs_inner_creds_inner(
                                        address = '', )
                                    ], 
                                asset = openapi_client.models._v2_network__network_id__avm__blockchain_id__address__address_id__transactions_get_200_response_items_inner_inputs_inner_asset._v2_network__networkId__avm__blockchainId__address__addressId__transactions_get_200_response_items_inner_inputs_inner_asset(
                                    id = '', 
                                    name = '', 
                                    symbol = '', 
                                    denomination = 1.337, 
                                    type = 'fixed_cap', ), )
                            ], 
                        outputs = [
                            openapi_client.models._v2_network__network_id__avm__blockchain_id__address__address_id__transactions_get_200_response_items_inner_inputs_inner._v2_network__networkId__avm__blockchainId__address__addressId__transactions_get_200_response_items_inner_inputs_inner(
                                id = '', 
                                tx_id = '', 
                                index = 1.337, 
                                amount = '', 
                                src_chain = '', 
                                dst_chain = '', 
                                owner = openapi_client.models._v2_network__network_id__avm__blockchain_id__address__address_id__transactions_get_200_response_items_inner_inputs_inner_owner._v2_network__networkId__avm__blockchainId__address__addressId__transactions_get_200_response_items_inner_inputs_inner_owner(
                                    addresses = [
                                        ''
                                        ], 
                                    threshold = 1.337, ), 
                                locktime = 1.337, )
                            ], 
                        memo = '', )
                    ],
                link = openapi_client.models._v2_network__network_id__evm_cross_transactions_get_200_response_link._v2_network__networkId__evm_cross_transactions_get_200_response_link(
                    next = '', 
                    next_token = '', ),
        )
        """

    def testV2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response(self):
        """Test V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
