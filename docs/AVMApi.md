# openapi_client.AVMApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_network_network_id_avm_blockchain_id_address_address_id_transactions_get**](AVMApi.md#v2_network_network_id_avm_blockchain_id_address_address_id_transactions_get) | **GET** /v2/network/{networkId}/avm/{blockchainId}/address/{addressId}/transactions | 


# **v2_network_network_id_avm_blockchain_id_address_address_id_transactions_get**
> V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response v2_network_network_id_avm_blockchain_id_address_address_id_transactions_get(network_id, blockchain_id, address_id, timestamp_from=timestamp_from, timestamp_to=timestamp_to, next=next, limit=limit)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.v2_network_network_id_avm_blockchain_id_address_address_id_transactions_get200_response import V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AVMApi(api_client)
    network_id = 'mainnet' # str | 
    blockchain_id = '2oYMBNV4eNHyqk2fjjV5nVQLDbtmNJzq5s3qs3Lo6ftnC6FByM' # str | 
    address_id = '' # str | 
    timestamp_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    timestamp_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    next = 'next_example' # str |  (optional)
    limit = 25 # float | Max value: 100 (optional) (default to 25)

    try:
        api_response = api_instance.v2_network_network_id_avm_blockchain_id_address_address_id_transactions_get(network_id, blockchain_id, address_id, timestamp_from=timestamp_from, timestamp_to=timestamp_to, next=next, limit=limit)
        print("The response of AVMApi->v2_network_network_id_avm_blockchain_id_address_address_id_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AVMApi->v2_network_network_id_avm_blockchain_id_address_address_id_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**|  | 
 **blockchain_id** | **str**|  | 
 **address_id** | **str**|  | 
 **timestamp_from** | **datetime**|  | [optional] 
 **timestamp_to** | **datetime**|  | [optional] 
 **next** | **str**|  | [optional] 
 **limit** | **float**| Max value: 100 | [optional] [default to 25]

### Return type

[**V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response**](V2NetworkNetworkIdAvmBlockchainIdAddressAddressIdTransactionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

