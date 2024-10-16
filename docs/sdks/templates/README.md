# Templates
(*templates*)

### Available Operations

* [list](#list) - List all templates
* [get](#get) - Retrieve a template
* [upsert](#upsert) - Update a template for a given type and slug
* [revert](#revert) - Revert a template
* [preview](#preview) - Preview changes to a template
* [toggle_delivery](#toggle_delivery) - Toggle the delivery by Clerk for a template of a given type and slug

## list

Returns a list of all templates.
The templates are returned sorted by position.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.templates.list(template_type=clerk_backend_api.TemplateType.EMAIL)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_type`                                                     | [models.TemplateType](../../models/templatetype.md)                 | :heavy_check_mark:                                                  | The type of templates to list (email or SMS)                        | email                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[List[models.Template]](../../models/.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## get

Returns the details of a template

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.templates.get(template_type=clerk_backend_api.PathParamTemplateType.EMAIL, slug="welcome-email")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `template_type`                                                       | [models.PathParamTemplateType](../../models/pathparamtemplatetype.md) | :heavy_check_mark:                                                    | The type of templates to retrieve (email or SMS)                      | email                                                                 |
| `slug`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | The slug (i.e. machine-friendly name) of the template to retrieve     | welcome-email                                                         |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |


### Response

**[models.Template](../../models/template.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,404        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## upsert

Updates the existing template of the given type and slug

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.templates.upsert(template_type=clerk_backend_api.UpsertTemplatePathParamTemplateType.SMS, slug="verification-code", request_body={
    "name": "Verification Code",
    "subject": "Your Verification Code",
    "markup": "<p>Your code: {{code}}</p>",
    "body": "Use this code to verify your email: {{code}}",
    "delivered_by_clerk": True,
    "from_email_name": "hello",
    "reply_to_email_name": "support",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `template_type`                                                                                   | [models.UpsertTemplatePathParamTemplateType](../../models/upserttemplatepathparamtemplatetype.md) | :heavy_check_mark:                                                                                | The type of template to update                                                                    | sms                                                                                               |
| `slug`                                                                                            | *str*                                                                                             | :heavy_check_mark:                                                                                | The slug of the template to update                                                                | verification-code                                                                                 |
| `request_body`                                                                                    | [Optional[models.UpsertTemplateRequestBody]](../../models/upserttemplaterequestbody.md)           | :heavy_minus_sign:                                                                                | N/A                                                                                               |                                                                                                   |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |


### Response

**[models.Template](../../models/template.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400,401,402,403,404,422 | application/json        |
| models.SDKError         | 4xx-5xx                 | */*                     |

## revert

Reverts an updated template to its default state

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.templates.revert(template_type=clerk_backend_api.RevertTemplatePathParamTemplateType.EMAIL, slug="welcome-email")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `template_type`                                                                                   | [models.RevertTemplatePathParamTemplateType](../../models/reverttemplatepathparamtemplatetype.md) | :heavy_check_mark:                                                                                | The type of template to revert                                                                    | email                                                                                             |
| `slug`                                                                                            | *str*                                                                                             | :heavy_check_mark:                                                                                | The slug of the template to revert                                                                | welcome-email                                                                                     |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |


### Response

**[models.Template](../../models/template.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,402,404    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## preview

Returns a preview of a template for a given template_type, slug and body

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.templates.preview(template_type="email", slug="welcome-email", request_body={
    "subject": "Welcome to our service!",
    "body": "Hi, thank you for joining our service.",
    "from_email_name": "hello",
    "reply_to_email_name": "support",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `template_type`                                                                           | *str*                                                                                     | :heavy_check_mark:                                                                        | The type of template to preview                                                           | email                                                                                     |
| `slug`                                                                                    | *str*                                                                                     | :heavy_check_mark:                                                                        | The slug of the template to preview                                                       | welcome-email                                                                             |
| `request_body`                                                                            | [Optional[models.PreviewTemplateRequestBody]](../../models/previewtemplaterequestbody.md) | :heavy_minus_sign:                                                                        | Required parameters                                                                       |                                                                                           |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |


### Response

**[models.PreviewTemplateResponseBody](../../models/previewtemplateresponsebody.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,404,422    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## toggle_delivery

Toggles the delivery by Clerk for a template of a given type and slug.
If disabled, Clerk will not deliver the resulting email or SMS.
The app developer will need to listen to the `email.created` or `sms.created` webhooks in order to handle delivery themselves.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.templates.toggle_delivery(template_type=clerk_backend_api.ToggleTemplateDeliveryPathParamTemplateType.EMAIL, slug="welcome-email", request_body={
    "delivered_by_clerk": True,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       | Example                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `template_type`                                                                                                   | [models.ToggleTemplateDeliveryPathParamTemplateType](../../models/toggletemplatedeliverypathparamtemplatetype.md) | :heavy_check_mark:                                                                                                | The type of template to toggle delivery for                                                                       | email                                                                                                             |
| `slug`                                                                                                            | *str*                                                                                                             | :heavy_check_mark:                                                                                                | The slug of the template for which to toggle delivery                                                             | welcome-email                                                                                                     |
| `request_body`                                                                                                    | [Optional[models.ToggleTemplateDeliveryRequestBody]](../../models/toggletemplatedeliveryrequestbody.md)           | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |                                                                                                                   |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |                                                                                                                   |


### Response

**[models.Template](../../models/template.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,404        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
