# openapi_client.PVMApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get**](PVMApi.md#v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get) | **GET** /v2/network/{networkId}/pvm/{blockchainId}/address/{addressId}/transactions | 


# **v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get**
> V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200Response v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get(network_id, blockchain_id, address_id, timestamp_from=timestamp_from, timestamp_to=timestamp_to, categories=categories, next=next, limit=limit)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get200_response import V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200Response
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
    api_instance = openapi_client.PVMApi(api_client)
    network_id = '1' # str | 
    blockchain_id = '11111111111111111111111111111111LpoYY' # str | 
    address_id = 'P-avax1qqx0ng4vkklr5gne6p89dwkmw2u3vl07p8ehlm' # str | 
    timestamp_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    timestamp_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    categories = '' # str |  (optional)
    next = 'next_example' # str |  (optional)
    limit = 25 # float | Max value: 100 (optional) (default to 25)

    try:
        api_response = api_instance.v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get(network_id, blockchain_id, address_id, timestamp_from=timestamp_from, timestamp_to=timestamp_to, categories=categories, next=next, limit=limit)
        print("The response of PVMApi->v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PVMApi->v2_network_network_id_pvm_blockchain_id_address_address_id_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**|  | 
 **blockchain_id** | **str**|  | 
 **address_id** | **str**|  | 
 **timestamp_from** | **datetime**|  | [optional] 
 **timestamp_to** | **datetime**|  | [optional] 
 **categories** | **str**|  | [optional] 
 **next** | **str**|  | [optional] 
 **limit** | **float**| Max value: 100 | [optional] [default to 25]

### Return type

[**V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200Response**](V2NetworkNetworkIdPvmBlockchainIdAddressAddressIdTransactionsGet200Response.md)

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

