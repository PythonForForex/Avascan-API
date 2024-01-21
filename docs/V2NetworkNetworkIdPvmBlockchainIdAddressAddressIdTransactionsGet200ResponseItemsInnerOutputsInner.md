# V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerOutputsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tx_id** | **str** |  | 
**index** | **float** |  | 
**type** | **str** |  | 
**amount** | **str** |  | 
**owner** | [**V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerOwner**](V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerOwner.md) |  | 
**locktime** | **datetime** |  | [optional] 
**dst_chain** | **str** | Populated if this UTXO results from an export | [optional] 
**asset** | [**V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset**](V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset.md) |  | [optional] 

## Example

```python
from openapi_client.models.v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_outputs_inner import V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerOutputsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerOutputsInner from a JSON string
v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_outputs_inner_instance = V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerOutputsInner.from_json(json)
# print the JSON string representation of the object
print V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerOutputsInner.to_json()

# convert the object into a dict
v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_outputs_inner_dict = v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_outputs_inner_instance.to_dict()
# create an instance of V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerOutputsInner from a dict
v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_outputs_inner_form_dict = v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_outputs_inner.from_dict(v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_outputs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


