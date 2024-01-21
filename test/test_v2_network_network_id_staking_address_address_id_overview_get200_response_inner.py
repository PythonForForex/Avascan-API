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

from openapi_client.models.v2_network_network_id_staking_address_address_id_overview_get200_response_inner import V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner

class TestV2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner(unittest.TestCase):
    """V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner:
        """Test V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner`
        """
        model = V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner()
        if include_optional:
            return V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner(
                month = '',
                stake = openapi_client.models._v2_network__network_id__staking_address__address_id__overview_get_200_response_inner_stake._v2_network__networkId__staking_address__addressId__overview_get_200_response_inner_stake(
                    staked_in_validations = '', 
                    staked_in_delegations = '', 
                    not_staked = '', ),
                rewards = openapi_client.models._v2_network__network_id__staking_address__address_id__overview_get_200_response_inner_rewards._v2_network__networkId__staking_address__addressId__overview_get_200_response_inner_rewards(
                    validation_rewards = '', 
                    delegation_fee_rewards = '', 
                    net_delegation_rewards = '', )
            )
        else:
            return V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner(
                month = '',
                stake = openapi_client.models._v2_network__network_id__staking_address__address_id__overview_get_200_response_inner_stake._v2_network__networkId__staking_address__addressId__overview_get_200_response_inner_stake(
                    staked_in_validations = '', 
                    staked_in_delegations = '', 
                    not_staked = '', ),
                rewards = openapi_client.models._v2_network__network_id__staking_address__address_id__overview_get_200_response_inner_rewards._v2_network__networkId__staking_address__addressId__overview_get_200_response_inner_rewards(
                    validation_rewards = '', 
                    delegation_fee_rewards = '', 
                    net_delegation_rewards = '', ),
        )
        """

    def testV2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner(self):
        """Test V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()