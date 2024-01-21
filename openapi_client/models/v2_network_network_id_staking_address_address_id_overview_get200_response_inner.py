# coding: utf-8

"""
    Avascan API

    Avalanche multi-chain explorer API docs

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from openapi_client.models.v2_network_network_id_staking_address_address_id_overview_get200_response_inner_rewards import V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerRewards
from openapi_client.models.v2_network_network_id_staking_address_address_id_overview_get200_response_inner_stake import V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerStake
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner(BaseModel):
    """
    V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner
    """ # noqa: E501
    month: StrictStr
    stake: V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerStake
    rewards: V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerRewards
    __properties: ClassVar[List[str]] = ["month", "stake", "rewards"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of stake
        if self.stake:
            _dict['stake'] = self.stake.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rewards
        if self.rewards:
            _dict['rewards'] = self.rewards.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "month": obj.get("month"),
            "stake": V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerStake.from_dict(obj.get("stake")) if obj.get("stake") is not None else None,
            "rewards": V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInnerRewards.from_dict(obj.get("rewards")) if obj.get("rewards") is not None else None
        })
        return _obj


