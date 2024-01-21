# V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | [optional] 
**timestamp** | **datetime** |  | 
**inputs_count** | **float** | Total number of inputs for this transaction | 
**outputs_count** | **float** | Total number of outputs for this transaction | 
**inputs_limit** | **float** | If this field is set, it means we have loaded up to N inputs from the transaction | [optional] 
**outputs_limit** | **float** | If this field is set, it means we have loaded up to N outputs from the transaction | [optional] 
**inputs** | [**List[V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInner]**](V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerInputsInner.md) |  | 
**outputs** | [**List[V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerOutputsInner]**](V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInnerOutputsInner.md) |  | 
**memo** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner import V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInner from a JSON string
v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_instance = V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInner.from_json(json)
# print the JSON string representation of the object
print V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInner.to_json()

# convert the object into a dict
v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_dict = v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_instance.to_dict()
# create an instance of V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200ResponseItemsInner from a dict
v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_form_dict = v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner.from_dict(v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


