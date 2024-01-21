# openapi_client.EVMApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_network_network_id_evm_chain_id_blocks_get**](EVMApi.md#v2_network_network_id_evm_chain_id_blocks_get) | **GET** /v2/network/{networkId}/evm/{chainId}/blocks | 
[**v2_network_network_id_evm_chain_id_etherscanwildcard_get**](EVMApi.md#v2_network_network_id_evm_chain_id_etherscanwildcard_get) | **GET** /v2/network/{networkId}/evm/{chainId}/etherscan{wildcard} | 
[**v2_network_network_id_evm_chain_id_etherscanwildcard_post**](EVMApi.md#v2_network_network_id_evm_chain_id_etherscanwildcard_post) | **POST** /v2/network/{networkId}/evm/{chainId}/etherscan{wildcard} | 
[**v2_network_network_id_evm_cross_transactions_get**](EVMApi.md#v2_network_network_id_evm_cross_transactions_get) | **GET** /v2/network/{networkId}/evm/cross-transactions | 


# **v2_network_network_id_evm_chain_id_blocks_get**
> V2NetworkNetworkIdEvmChainIdBlocksGet200Response v2_network_network_id_evm_chain_id_blocks_get(network_id, chain_id, count=count, timestamp_from=timestamp_from, timestamp_to=timestamp_to, ecosystem=ecosystem, included_chain_ids=included_chain_ids, excluded_chain_ids=excluded_chain_ids, sort=sort, next=next)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.v2_network_network_id_evm_chain_id_blocks_get200_response import V2NetworkNetworkIdEvmChainIdBlocksGet200Response
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
    api_instance = openapi_client.EVMApi(api_client)
    network_id = 'mainnet' # str | 
    chain_id = '43114' # str | 
    count = True # bool |  (optional)
    timestamp_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    timestamp_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    ecosystem = '' # str |  (optional)
    included_chain_ids = '' # str |  (optional)
    excluded_chain_ids = '' # str |  (optional)
    sort = 'desc' # str |  (optional)
    next = 'next_example' # str |  (optional)

    try:
        api_response = api_instance.v2_network_network_id_evm_chain_id_blocks_get(network_id, chain_id, count=count, timestamp_from=timestamp_from, timestamp_to=timestamp_to, ecosystem=ecosystem, included_chain_ids=included_chain_ids, excluded_chain_ids=excluded_chain_ids, sort=sort, next=next)
        print("The response of EVMApi->v2_network_network_id_evm_chain_id_blocks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EVMApi->v2_network_network_id_evm_chain_id_blocks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**|  | 
 **chain_id** | **str**|  | 
 **count** | **bool**|  | [optional] 
 **timestamp_from** | **datetime**|  | [optional] 
 **timestamp_to** | **datetime**|  | [optional] 
 **ecosystem** | **str**|  | [optional] 
 **included_chain_ids** | **str**|  | [optional] 
 **excluded_chain_ids** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **next** | **str**|  | [optional] 

### Return type

[**V2NetworkNetworkIdEvmChainIdBlocksGet200Response**](V2NetworkNetworkIdEvmChainIdBlocksGet200Response.md)

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

# **v2_network_network_id_evm_chain_id_etherscanwildcard_get**
> v2_network_network_id_evm_chain_id_etherscanwildcard_get(network_id, chain_id)



### Example


```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.EVMApi(api_client)
    network_id = 'mainnet' # str | 
    chain_id = '43114' # str | 

    try:
        api_instance.v2_network_network_id_evm_chain_id_etherscanwildcard_get(network_id, chain_id)
    except Exception as e:
        print("Exception when calling EVMApi->v2_network_network_id_evm_chain_id_etherscanwildcard_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**|  | 
 **chain_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_network_network_id_evm_chain_id_etherscanwildcard_post**
> v2_network_network_id_evm_chain_id_etherscanwildcard_post(network_id, chain_id)



### Example


```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.EVMApi(api_client)
    network_id = 'mainnet' # str | 
    chain_id = '43114' # str | 

    try:
        api_instance.v2_network_network_id_evm_chain_id_etherscanwildcard_post(network_id, chain_id)
    except Exception as e:
        print("Exception when calling EVMApi->v2_network_network_id_evm_chain_id_etherscanwildcard_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**|  | 
 **chain_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_network_network_id_evm_cross_transactions_get**
> V2NetworkNetworkIdEvmCrossTransactionsGet200Response v2_network_network_id_evm_cross_transactions_get(network_id, src_chain_ids=src_chain_ids, dst_chain_ids=dst_chain_ids, src_ecosystem=src_ecosystem, dst_ecosystem=dst_ecosystem, count=count, types=types, ecosystem=ecosystem, included_chain_ids=included_chain_ids, excluded_chain_ids=excluded_chain_ids, next=next, limit=limit)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.v2_network_network_id_evm_cross_transactions_get200_response import V2NetworkNetworkIdEvmCrossTransactionsGet200Response
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
    api_instance = openapi_client.EVMApi(api_client)
    network_id = 'mainnet' # str | 
    src_chain_ids = ['src_chain_ids_example'] # List[str] |  (optional)
    dst_chain_ids = ['dst_chain_ids_example'] # List[str] |  (optional)
    src_ecosystem = 'src_ecosystem_example' # str |  (optional)
    dst_ecosystem = 'dst_ecosystem_example' # str |  (optional)
    count = True # bool |  (optional)
    types = ['types_example'] # List[str] |  (optional)
    ecosystem = '' # str |  (optional)
    included_chain_ids = '' # str |  (optional)
    excluded_chain_ids = '' # str |  (optional)
    next = 'next_example' # str |  (optional)
    limit = 25 # float | Max value: 100 (optional) (default to 25)

    try:
        api_response = api_instance.v2_network_network_id_evm_cross_transactions_get(network_id, src_chain_ids=src_chain_ids, dst_chain_ids=dst_chain_ids, src_ecosystem=src_ecosystem, dst_ecosystem=dst_ecosystem, count=count, types=types, ecosystem=ecosystem, included_chain_ids=included_chain_ids, excluded_chain_ids=excluded_chain_ids, next=next, limit=limit)
        print("The response of EVMApi->v2_network_network_id_evm_cross_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EVMApi->v2_network_network_id_evm_cross_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**|  | 
 **src_chain_ids** | [**List[str]**](str.md)|  | [optional] 
 **dst_chain_ids** | [**List[str]**](str.md)|  | [optional] 
 **src_ecosystem** | **str**|  | [optional] 
 **dst_ecosystem** | **str**|  | [optional] 
 **count** | **bool**|  | [optional] 
 **types** | [**List[str]**](str.md)|  | [optional] 
 **ecosystem** | **str**|  | [optional] 
 **included_chain_ids** | **str**|  | [optional] 
 **excluded_chain_ids** | **str**|  | [optional] 
 **next** | **str**|  | [optional] 
 **limit** | **float**| Max value: 100 | [optional] [default to 25]

### Return type

[**V2NetworkNetworkIdEvmCrossTransactionsGet200Response**](V2NetworkNetworkIdEvmCrossTransactionsGet200Response.md)

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

