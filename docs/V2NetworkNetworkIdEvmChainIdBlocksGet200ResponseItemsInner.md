# V2NetworkNetworkIdEvmChainIdBlocksGet200ResponseItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **float** |  | 
**id** | **str** |  | 
**parent** | **str** |  | 
**chain_id** | **str** |  | 
**ecosystems** | **List[str]** |  | [optional] 
**size** | **str** |  | 
**volume** | **str** |  | 
**gas_limit** | **str** |  | 
**gas_used** | **str** |  | 
**atomic** | **bool** |  | 
**transactions** | **List[str]** |  | 
**burned_fees** | **str** |  | 
**timestamp** | **datetime** |  | 
**current_block_number** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.v2_network_network_id_evm_chain_id_blocks_get200_response_items_inner import V2NetworkNetworkIdEvmChainIdBlocksGet200ResponseItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2NetworkNetworkIdEvmChainIdBlocksGet200ResponseItemsInner from a JSON string
v2_network_network_id_evm_chain_id_blocks_get200_response_items_inner_instance = V2NetworkNetworkIdEvmChainIdBlocksGet200ResponseItemsInner.from_json(json)
# print the JSON string representation of the object
print V2NetworkNetworkIdEvmChainIdBlocksGet200ResponseItemsInner.to_json()

# convert the object into a dict
v2_network_network_id_evm_chain_id_blocks_get200_response_items_inner_dict = v2_network_network_id_evm_chain_id_blocks_get200_response_items_inner_instance.to_dict()
# create an instance of V2NetworkNetworkIdEvmChainIdBlocksGet200ResponseItemsInner from a dict
v2_network_network_id_evm_chain_id_blocks_get200_response_items_inner_form_dict = v2_network_network_id_evm_chain_id_blocks_get200_response_items_inner.from_dict(v2_network_network_id_evm_chain_id_blocks_get200_response_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


