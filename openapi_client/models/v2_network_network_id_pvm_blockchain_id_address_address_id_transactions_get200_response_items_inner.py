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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from openapi_client.models.v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_inputs_inner import V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInner
from openapi_client.models.v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_outputs_inner import V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerOutputsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInner(BaseModel):
    """
    V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInner
    """ # noqa: E501
    id: StrictStr
    type: Optional[StrictStr] = None
    timestamp: datetime
    inputs_count: Union[StrictFloat, StrictInt] = Field(description="Total number of inputs for this transaction", alias="inputsCount")
    outputs_count: Union[StrictFloat, StrictInt] = Field(description="Total number of outputs for this transaction", alias="outputsCount")
    inputs_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="If this field is set, it means we have loaded up to N inputs from the transaction", alias="inputsLimit")
    outputs_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="If this field is set, it means we have loaded up to N outputs from the transaction", alias="outputsLimit")
    inputs: List[V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInner]
    outputs: List[V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerOutputsInner]
    memo: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "type", "timestamp", "inputsCount", "outputsCount", "inputsLimit", "outputsLimit", "inputs", "outputs", "memo"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('add_validator', 'add_subnet_validator', 'add_delegator', 'create_chain', 'create_subnet', 'import', 'export', 'advance_time', 'reward_validator', 'remove_subnet_validator', 'transform_subnet', 'add_permissionsless_validator', 'add_permissionsless_delegator'):
            raise ValueError("must be one of enum values ('add_validator', 'add_subnet_validator', 'add_delegator', 'create_chain', 'create_subnet', 'import', 'export', 'advance_time', 'reward_validator', 'remove_subnet_validator', 'transform_subnet', 'add_permissionsless_validator', 'add_permissionsless_delegator')")
        return value

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
        """Create an instance of V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in inputs (list)
        _items = []
        if self.inputs:
            for _item in self.inputs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['inputs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in outputs (list)
        _items = []
        if self.outputs:
            for _item in self.outputs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['outputs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "timestamp": obj.get("timestamp"),
            "inputsCount": obj.get("inputsCount"),
            "outputsCount": obj.get("outputsCount"),
            "inputsLimit": obj.get("inputsLimit"),
            "outputsLimit": obj.get("outputsLimit"),
            "inputs": [V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInner.from_dict(_item) for _item in obj.get("inputs")] if obj.get("inputs") is not None else None,
            "outputs": [V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerOutputsInner.from_dict(_item) for _item in obj.get("outputs")] if obj.get("outputs") is not None else None,
            "memo": obj.get("memo")
        })
        return _obj


