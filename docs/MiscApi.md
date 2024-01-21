# openapi_client.MiscApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_ping_get**](MiscApi.md#v2_ping_get) | **GET** /v2/ping | 


# **v2_ping_get**
> V2PingGet200Response v2_ping_get()



Ping

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.v2_ping_get200_response import V2PingGet200Response
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
    api_instance = openapi_client.MiscApi(api_client)

    try:
        api_response = api_instance.v2_ping_get()
        print("The response of MiscApi->v2_ping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscApi->v2_ping_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V2PingGet200Response**](V2PingGet200Response.md)

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

