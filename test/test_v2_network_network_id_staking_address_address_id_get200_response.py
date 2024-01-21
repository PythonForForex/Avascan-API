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

from openapi_client.models.v2_network_network_id_staking_address_address_id_get200_response import V2NetworkNetworkIdStakingAddressAddressIdGet200Response

class TestV2NetworkNetworkIdStakingAddressAddressIdGet200Response(unittest.TestCase):
    """V2NetworkNetworkIdStakingAddressAddressIdGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2NetworkNetworkIdStakingAddressAddressIdGet200Response:
        """Test V2NetworkNetworkIdStakingAddressAddressIdGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2NetworkNetworkIdStakingAddressAddressIdGet200Response`
        """
        model = V2NetworkNetworkIdStakingAddressAddressIdGet200Response()
        if include_optional:
            return V2NetworkNetworkIdStakingAddressAddressIdGet200Response(
                staking_rewards = openapi_client.models._v2_network__network_id__staking_address__address_id__get_200_response_staking_rewards._v2_network__networkId__staking_address__addressId__get_200_response_stakingRewards(
                    value = '', ),
                from_validations = openapi_client.models._v2_network__network_id__staking_address__address_id__get_200_response_from_validations._v2_network__networkId__staking_address__addressId__get_200_response_fromValidations(
                    from_staking = '', 
                    fees = '', 
                    total_rewards = '', ),
                from_delegations = openapi_client.models._v2_network__network_id__staking_address__address_id__get_200_response_from_validations._v2_network__networkId__staking_address__addressId__get_200_response_fromValidations(
                    from_staking = '', 
                    fees = '', 
                    total_rewards = '', )
            )
        else:
            return V2NetworkNetworkIdStakingAddressAddressIdGet200Response(
                staking_rewards = openapi_client.models._v2_network__network_id__staking_address__address_id__get_200_response_staking_rewards._v2_network__networkId__staking_address__addressId__get_200_response_stakingRewards(
                    value = '', ),
                from_validations = openapi_client.models._v2_network__network_id__staking_address__address_id__get_200_response_from_validations._v2_network__networkId__staking_address__addressId__get_200_response_fromValidations(
                    from_staking = '', 
                    fees = '', 
                    total_rewards = '', ),
                from_delegations = openapi_client.models._v2_network__network_id__staking_address__address_id__get_200_response_from_validations._v2_network__networkId__staking_address__addressId__get_200_response_fromValidations(
                    from_staking = '', 
                    fees = '', 
                    total_rewards = '', ),
        )
        """

    def testV2NetworkNetworkIdStakingAddressAddressIdGet200Response(self):
        """Test V2NetworkNetworkIdStakingAddressAddressIdGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()