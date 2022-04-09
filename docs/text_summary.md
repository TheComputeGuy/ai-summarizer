# Text Summary

Used to generate summary from text input

**URL**: `/summary`

**Method**: `POST`

**Auth required**: NO

**Input data format - Form data**

Content-Type: application/x-www-form-urlencoded

```
input: [input text to be summarized]
```

**Data example**

```
input: The Great Depression was a severe worldwide economic depression that took place mostly...
```

## Success Response

**Code**: `200 OK`

**Content example**

```json
{
    "input": "The Great Depression was a severe worldwide economic depression that took place mostly...",
    "message": "Request complete",
	"status": "200",
	"summary": "The Great Depression was a severe worldwide economic depression that took place..."
}
```

## Error Responses

**Condition**: If "input" form field is missing from request.

**Code**: `400 BAD REQUEST`

**Content**:

```json
{
    "message": "Input missing in request",
	"status": "400"
}
```

**Condition**: If input text field is empty

**Code** : `400 BAD REQUEST`

**Content**:

```json
{
    "message": "Input text missing in request",
	"status": "400"
}
```

**Condition**: If there's an error in processing the request

**Code**: `500 INTERNAL SERVER ERROR`

**Content**:

```json
{
    "message": "An error occured while processing your request",
	"status": "500"
}
```