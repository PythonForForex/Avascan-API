# V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tx_id** | **str** |  | 
**index** | **float** |  | 
**amount** | **str** |  | 
**owner** | [**V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerOwner**](V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerOwner.md) |  | [optional] 
**creds** | [**List[V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerCredsInner]**](V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerCredsInner.md) |  | 
**src_chain** | **str** | Populated if this UTXO results from an import | [optional] 
**asset** | [**V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset**](V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInnerAsset.md) |  | [optional] 

## Example

```python
from openapi_client.models.v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_inputs_inner import V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInner from a JSON string
v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_inputs_inner_instance = V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInner.from_json(json)
# print the JSON string representation of the object
print V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInner.to_json()

# convert the object into a dict
v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_inputs_inner_dict = v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_inputs_inner_instance.to_dict()
# create an instance of V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInner from a dict
v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_inputs_inner_form_dict = v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_inputs_inner.from_dict(v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_inputs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


