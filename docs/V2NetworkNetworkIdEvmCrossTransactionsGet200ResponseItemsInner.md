# V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**status** | **str** |  | 
**src_chain_id** | **str** |  | 
**src_timestamp** | **datetime** |  | 
**src_tx_hash** | **str** |  | [optional] 
**src_block_number** | **str** |  | [optional] 
**src_block_hash** | **str** |  | [optional] 
**src_gas_limit** | **str** |  | [optional] 
**dst_chain_id** | **str** |  | 
**dst_timestamp** | **datetime** |  | 
**dst_tx_hash** | **str** |  | [optional] 
**dst_block_number** | **str** |  | [optional] 
**dst_block_hash** | **str** |  | [optional] 
**dst_gas_limit** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 
**data** | [**V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseItemsInnerData**](V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseItemsInnerData.md) |  | [optional] 

## Example

```python
from openapi_client.models.v2_network_network_id_evm_cross_transactions_get200_response_items_inner import V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseItemsInner from a JSON string
v2_network_network_id_evm_cross_transactions_get200_response_items_inner_instance = V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseItemsInner.from_json(json)
# print the JSON string representation of the object
print V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseItemsInner.to_json()

# convert the object into a dict
v2_network_network_id_evm_cross_transactions_get200_response_items_inner_dict = v2_network_network_id_evm_cross_transactions_get200_response_items_inner_instance.to_dict()
# create an instance of V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseItemsInner from a dict
v2_network_network_id_evm_cross_transactions_get200_response_items_inner_form_dict = v2_network_network_id_evm_cross_transactions_get200_response_items_inner.from_dict(v2_network_network_id_evm_cross_transactions_get200_response_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


