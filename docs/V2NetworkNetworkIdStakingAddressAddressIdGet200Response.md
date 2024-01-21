# V2NetworkNetworkIdStakingAddressAddressIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staking_rewards** | [**V2NetworkNetworkIdStakingAddressAddressIdGet200ResponseStakingRewards**](V2NetworkNetworkIdStakingAddressAddressIdGet200ResponseStakingRewards.md) |  | 
**from_validations** | [**V2NetworkNetworkIdStakingAddressAddressIdGet200ResponseFromValidations**](V2NetworkNetworkIdStakingAddressAddressIdGet200ResponseFromValidations.md) |  | 
**from_delegations** | [**V2NetworkNetworkIdStakingAddressAddressIdGet200ResponseFromValidations**](V2NetworkNetworkIdStakingAddressAddressIdGet200ResponseFromValidations.md) |  | 

## Example

```python
from openapi_client.models.v2_network_network_id_staking_address_address_id_get200_response import V2NetworkNetworkIdStakingAddressAddressIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2NetworkNetworkIdStakingAddressAddressIdGet200Response from a JSON string
v2_network_network_id_staking_address_address_id_get200_response_instance = V2NetworkNetworkIdStakingAddressAddressIdGet200Response.from_json(json)
# print the JSON string representation of the object
print V2NetworkNetworkIdStakingAddressAddressIdGet200Response.to_json()

# convert the object into a dict
v2_network_network_id_staking_address_address_id_get200_response_dict = v2_network_network_id_staking_address_address_id_get200_response_instance.to_dict()
# create an instance of V2NetworkNetworkIdStakingAddressAddressIdGet200Response from a dict
v2_network_network_id_staking_address_address_id_get200_response_form_dict = v2_network_network_id_staking_address_address_id_get200_response.from_dict(v2_network_network_id_staking_address_address_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


