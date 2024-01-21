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

from openapi_client.models.v2_network_network_id_staking_address_address_id_overview_get200_response_inner_rewards import V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerRewards

class TestV2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerRewards(unittest.TestCase):
    """V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerRewards unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerRewards:
        """Test V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerRewards
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerRewards`
        """
        model = V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerRewards()
        if include_optional:
            return V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerRewards(
                validation_rewards = '',
                delegation_fee_rewards = '',
                net_delegation_rewards = ''
            )
        else:
            return V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerRewards(
                validation_rewards = '',
                delegation_fee_rewards = '',
                net_delegation_rewards = '',
        )
        """

    def testV2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerRewards(self):
        """Test V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerRewards"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()