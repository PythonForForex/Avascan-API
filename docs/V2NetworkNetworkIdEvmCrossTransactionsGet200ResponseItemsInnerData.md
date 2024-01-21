# V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseItemsInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queue_index** | **str** |  | [optional] 
**requested_gas_limit** | **str** |  | [optional] 
**l1_tx_origin** | **str** |  | [optional] 
**message_nonce** | **str** |  | [optional] 
**message_hash** | **str** |  | [optional] 
**source_hash** | **str** |  | [optional] 
**withdrawal_hash** | **str** |  | [optional] 
**proof_tx_hash** | **str** |  | [optional] 
**proof_tx_timestamp** | **datetime** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.v2_network_network_id_evm_cross_transactions_get200_response_items_inner_data import V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseItemsInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseItemsInnerData from a JSON string
v2_network_network_id_evm_cross_transactions_get200_response_items_inner_data_instance = V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseItemsInnerData.from_json(json)
# print the JSON string representation of the object
print V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseItemsInnerData.to_json()

# convert the object into a dict
v2_network_network_id_evm_cross_transactions_get200_response_items_inner_data_dict = v2_network_network_id_evm_cross_transactions_get200_response_items_inner_data_instance.to_dict()
# create an instance of V2NetworkNetworkIdEvmCrossTransactionsGet200ResponseItemsInnerData from a dict
v2_network_network_id_evm_cross_transactions_get200_response_items_inner_data_form_dict = v2_network_network_id_evm_cross_transactions_get200_response_items_inner_data.from_dict(v2_network_network_id_evm_cross_transactions_get200_response_items_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


