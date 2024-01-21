# openapi_client.StakingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_network_network_id_staking_address_address_id_get**](StakingApi.md#v2_network_network_id_staking_address_address_id_get) | **GET** /v2/network/{networkId}/staking/address/{addressId} | 
[**v2_network_network_id_staking_address_address_id_overview_get**](StakingApi.md#v2_network_network_id_staking_address_address_id_overview_get) | **GET** /v2/network/{networkId}/staking/address/{addressId}/overview | 


# **v2_network_network_id_staking_address_address_id_get**
> V2NetworkNetworkIdStakingAddressAddressIdGet200Response v2_network_network_id_staking_address_address_id_get(network_id, address_id, with_potential_rewards=with_potential_rewards)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.v2_network_network_id_staking_address_address_id_get200_response import V2NetworkNetworkIdStakingAddressAddressIdGet200Response
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
    api_instance = openapi_client.StakingApi(api_client)
    network_id = 'mainnet' # str | 
    address_id = 'P-avax19zfygxaf59stehzedhxjesads0p5jdvfeedal' # str | 
    with_potential_rewards = 3.4 # float |  (optional)

    try:
        api_response = api_instance.v2_network_network_id_staking_address_address_id_get(network_id, address_id, with_potential_rewards=with_potential_rewards)
        print("The response of StakingApi->v2_network_network_id_staking_address_address_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->v2_network_network_id_staking_address_address_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**|  | 
 **address_id** | **str**|  | 
 **with_potential_rewards** | **float**|  | [optional] 

### Return type

[**V2NetworkNetworkIdStakingAddressAddressIdGet200Response**](V2NetworkNetworkIdStakingAddressAddressIdGet200Response.md)

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

# **v2_network_network_id_staking_address_address_id_overview_get**
> List[V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner] v2_network_network_id_staking_address_address_id_overview_get(network_id, address_id, month_from=month_from, month_to=month_to)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.v2_network_network_id_staking_address_address_id_overview_get200_response_inner import V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner
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
    api_instance = openapi_client.StakingApi(api_client)
    network_id = 'mainnet' # str | 
    address_id = 'P-avax19zfygxaf59stehzedhxjesads0p5jdvfeedal' # str | 
    month_from = '2013-10-20T19:20:30+01:00' # datetime | ISO date string representing the first day of the month (optional)
    month_to = '2013-10-20T19:20:30+01:00' # datetime | ISO date string representing the first day of the month (optional)

    try:
        api_response = api_instance.v2_network_network_id_staking_address_address_id_overview_get(network_id, address_id, month_from=month_from, month_to=month_to)
        print("The response of StakingApi->v2_network_network_id_staking_address_address_id_overview_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->v2_network_network_id_staking_address_address_id_overview_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**|  | 
 **address_id** | **str**|  | 
 **month_from** | **datetime**| ISO date string representing the first day of the month | [optional] 
 **month_to** | **datetime**| ISO date string representing the first day of the month | [optional] 

### Return type

[**List[V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner]**](V2NetworkNetworkIdStakingAddressAddressIdOverviewGet200ResponseInner.md)

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

