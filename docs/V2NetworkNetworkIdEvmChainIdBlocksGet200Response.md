# V2NetworkNetworkIdEvmChainIdBlocksGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[V2NetworkNetworkIdEvmChainIdBlocksGet200ResponseItemsInner]**](V2NetworkNetworkIdEvmChainIdBlocksGet200ResponseItemsInner.md) |  | 
**count** | **float** |  | [optional] 
**count_type** | **str** |  | [optional] 
**link** | [**V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseLink**](V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseLink.md) |  | 

## Example

```python
from openapi_client.models.v2_network_network_id_evm_chain_id_blocks_get200_response import V2NetworkNetworkIdEvmChainIdBlocksGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2NetworkNetworkIdEvmChainIdBlocksGet200Response from a JSON string
v2_network_network_id_evm_chain_id_blocks_get200_response_instance = V2NetworkNetworkIdEvmChainIdBlocksGet200Response.from_json(json)
# print the JSON string representation of the object
print V2NetworkNetworkIdEvmChainIdBlocksGet200Response.to_json()

# convert the object into a dict
v2_network_network_id_evm_chain_id_blocks_get200_response_dict = v2_network_network_id_evm_chain_id_blocks_get200_response_instance.to_dict()
# create an instance of V2NetworkNetworkIdEvmChainIdBlocksGet200Response from a dict
v2_network_network_id_evm_chain_id_blocks_get200_response_form_dict = v2_network_network_id_evm_chain_id_blocks_get200_response.from_dict(v2_network_network_id_evm_chain_id_blocks_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


